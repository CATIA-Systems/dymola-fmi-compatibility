import pytest
from itertools import product


@pytest.mark.parametrize('model, interface_type', product([
    'ActivateRC',
    'Arenstorf',
    'Boocwen',
    'CVloop',
    'DiscreteController',
    'Pendulum'
], ['cs', 'me']))
def test_import_Activate_fmi2(dymola, resources_dir, model, interface_type):
    filename = resources_dir / f'Activate/Altair-Activate/2.0/export/{interface_type}/win64/{model}/{model}.fmu'
    model_name = f'Activate_{model}_fmi2_{interface_type}'
    dymola.importFMU(fileName=filename, integrate=interface_type == 'me', modelName=model_name)
    dymola.simulate(model_name, algorithm='Euler')


@pytest.mark.parametrize('model, interface_type', product([
    'periodic_clock',
    'sinewave_array',
    'triggered_and_periodic_clock'
], ['cs', 'me']))
def test_import_Activate_fmi3(dymola, resources_dir, model, interface_type):
    filename = resources_dir / f'Activate/Altair-Activate/3.0/export/{interface_type}/x86_64-windows/{model}/{model}.fmu'
    model_name = f'Activate_{model}_fmi3_{interface_type}'
    dymola.importFMU(fileName=filename, integrate=interface_type == 'me', modelName=model_name)
    dymola.simulate(model_name, algorithm='Euler')
