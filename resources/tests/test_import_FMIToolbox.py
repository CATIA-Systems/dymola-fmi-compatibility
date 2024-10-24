import pytest
from itertools import product

tool_name = 'FMIToolbox'
tool_version = '2.15'

@pytest.mark.parametrize('model, interface_type', product([
    'Continuous',
    'Discontinuities',
    'EmbeddedCode',
    'IntegrateSignal',
    'Signal_Attributes'
], ['cs', 'me']))
def test_import_FMIToolbox_fmi2(dymola, resources_dir, model, interface_type):
    filename = resources_dir / f'FMIToolbox/fmus/FMIToolbox_{tool_version}/2.0/{interface_type}/win64/{model}/{model}.fmu'
    model_name = f'{tool_name}_{model}_fmi2_{interface_type}'
    dymola.importFMU(fileName=filename, integrate=interface_type == 'me', modelName=model_name)
    dymola.simulate(model_name)


@pytest.mark.parametrize('model', [
    'Continuous',
    'Discontinuities',
    'EmbeddedCode',
    'IntegrateSignal',
    'Signal_Attributes'
])
def test_import_FMIToolbox_fmi3(dymola, resources_dir, model):
    filename = resources_dir / f'FMIToolbox/fmus/FMIToolbox_{tool_version}/3.0/cs/x86_64-windows/{model}/{model}.fmu'
    model_name = f'{tool_name}_{model}_fmi3_cs'
    dymola.importFMU(fileName=filename, integrate=False, modelName=model_name)
    dymola.simulate(model_name)
