from itertools import product
import pytest


@pytest.mark.parametrize("model, fmi_version", product(
    ["AdaptiveHeadlight", "LunarLanderAutopilot", "SignalGenerator"],
    [2, 3]
))
def test_import_SystemDesk(dymola, resources_dir, model, fmi_version):
    filename = resources_dir / "dSPACE" / "SystemDesk" / f"FMI{fmi_version}-{model}-Win64" / f"{model}.fmu"
    model_name = f"SystemDesk_{model}_fmi{fmi_version}_cs"
    dymola.importFMU(
        fileName=filename, integrate=False, modelName=model_name
    )
    dymola.simulate(model_name)