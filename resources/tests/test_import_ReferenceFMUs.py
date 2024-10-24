import pytest
from itertools import product


models = [
    'BouncingBall',
    'Dahlquist',
    # 'Feedthrough', # inputs must be connected
    'Resource',
    'Stair',
    'StateSpace',
    'VanDerPol'
]

@pytest.mark.parametrize('model, fmi_version, interface_type', product(models, [1, 2, 3], ['cs', 'me']))
def test_fmu_import(dymola, reference_fmus_dir, model, fmi_version, interface_type):

    if model == 'StateSpace' and fmi_version < 3:
        return

    if model == 'Resource' and fmi_version == 1 and interface_type == 'me':
        return

    if fmi_version == 1:
        filename = reference_fmus_dir / '1.0' / interface_type / f'{model}.fmu'
    else:
        filename = reference_fmus_dir / f'{fmi_version}.0' / f'{model}.fmu'

    model_name = f'{model}_fmi{fmi_version}_{interface_type}'

    dymola.importFMU(fileName=filename, integrate=interface_type == 'me', modelName=model_name)

    dymola.simulate(model_name)
