import pytest
from itertools import product


@pytest.mark.parametrize('model, interface_type', product([
    'ControlledTemperature',
    'CoupledClutches',
    'Rectifier'
], ['cs', 'me']))
def test_import_MapleSim_fmi2(dymola, resources_dir, model, interface_type):
    filename = resources_dir / f'MapleSim/MapleSim_2024/FMI_Export/FMI_2/{interface_type.upper()}' / model / f'{model}.fmu'
    model_name = f'MapleSim_{model}_fmi2_{interface_type}'
    dymola.importFMU(fileName=filename, integrate=interface_type == 'me', modelName=model_name)
    dymola.simulate(model_name)


@pytest.mark.parametrize('model, interface_type', product([
    'ControlledTemperature',
    'CoupledClutches',
    'SlidingCrank'
], ['cs', 'me']))
def test_import_MapleSim_fmi3(dymola, resources_dir, model, interface_type):
    filename = resources_dir / f'MapleSim/MapleSim_2024/FMI_Export/FMI_3' / model / f'{model}.fmu'
    model_name = f'MapleSim_{model}_fmi3_{interface_type}'
    dymola.importFMU(fileName=filename, integrate=interface_type == 'me', modelName=model_name)
    dymola.simulate(model_name, algorithm='Euler')
