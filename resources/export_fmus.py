""" Export and test Dymola FMUs for the FMI Compatibility repository """

import shutil
from itertools import product
from os import makedirs
from pathlib import Path
from subprocess import check_call

from fmpy import read_model_description, supported_platforms, simulate_fmu
from fmpy.util import compile_platform_binary
from pymola import Dymola


algorithms = [
    ('Dassl', 'csSolver', False, 0),
    ('Cvode', 'all', True, 0),
    ('Inline', 'cs', True, 1),
]

fmi_versions = ['1', '2', '3']

dymola_version = '2024x Refresh 1'

root = Path(__file__).parent.parent

fmusim = root / 'resources/Reference-FMUs-0.0.29/fmusim-x86_64-windows/fmusim.exe'

output_dir = Path(root / dymola_version)
temp_dir = Path(root / 'temp')

for path in [temp_dir, output_dir]:

    if path.exists():
        shutil.rmtree(path)

    makedirs(path)

mo_path = Path(root / 'resources' / 'CoupledClutches.mo')


with Dymola(showWindow=True) as dymola:

    dymola.cd(temp_dir)

    dymola.setVariable('Advanced.FMI.CrossExport', True)
    dymola.setVariable('Advanced.FMI3.EventModeCoSim', True)

    dymola.openModel(mo_path, changeDirectory=False)

    for fmi_version, (algorithm, fmi_type, include_source, inline_method) in product(fmi_versions, algorithms):

        model_name = f'CoupledClutches_fmi{fmi_version}_{algorithm}'

        print(model_name)

        dymola.setVariable('Advanced.InlineMethod', inline_method)

        dymola.translateModelFMU(
            modelToOpen=f'CoupledClutches annotation(experiment(StopTime=1.5, Interval=0.001, __Dymola_fixedstepsize=0.001, __Dymola_Algorithm="{algorithm}"))',
            modelName=model_name,
            fmiVersion=fmi_version,
            fmiType=fmi_type,
            includeSource=include_source
        )

        fmu_path = temp_dir / f'{model_name}.fmu'

        model_description = read_model_description(fmu_path)
        platforms = supported_platforms(fmu_path)

        assert model_description.fmiVersion.startswith(fmi_version)
        assert model_description.generationTool.startswith(f"Dymola Version {dymola_version}")

        if fmi_version == '3':
            assert model_description.coSimulation.hasEventMode

        assert 'linux64' in platforms
        assert 'win64' in platforms

        if algorithm in {'Cvode', 'Inline'}:
            assert 'c-code' in platforms

        shutil.copyfile(fmu_path, output_dir / f'{model_name}.fmu')

        # simulate FMU in FMPy
        simulate_fmu(output_dir / f'{model_name}.fmu')

        # compile platform binary from source
        if 'c-code' in platforms and model_description.fmiVersion != '1.0':
            temp_file = temp_dir / f'temp_{model_name}.fmu'
            shutil.copyfile(fmu_path, temp_file)
            compile_platform_binary(temp_file)

        # run FMU in fmusim
        check_call([fmusim, output_dir / f'{model_name}.fmu'])
