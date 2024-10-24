import pytest
from itertools import product


@pytest.mark.parametrize('model, interface_type', product([
    'BouncingBall',
    'CoupledClutches',
    'DFFREG'
], ['me']))
def test_import_Sysplorer_fmi2(dymola, resources_dir, model, interface_type):
    filename = resources_dir / f'Sysplorer/MWORKS.Sysplorer2024a/2.0/{interface_type}/win64/{model}/{model}.fmu'
    model_name = f'Sysplorer_{model}_fmi2_{interface_type}'
    dymola.importFMU(fileName=filename, integrate=interface_type == 'me', modelName=model_name)
    dymola.simulate(model_name)

@pytest.mark.parametrize('model, interface_type', product([
    'BouncingBall',
    'CoupledClutches',
    'DFFREG'
], ['me']))
def test_import_Sysplorer_fmi3(dymola, resources_dir, model, interface_type):
    filename = resources_dir / f'Sysplorer/MWORKS.Sysplorer2024a/3.0/{interface_type}/x86_64-windows/{model}/{model}.fmu'
    model_name = f'Sysplorer_{model}_fmi3_{interface_type}'
    dymola.importFMU(fileName=filename, integrate=interface_type == 'me', modelName=model_name)
    dymola.simulate(model_name)
