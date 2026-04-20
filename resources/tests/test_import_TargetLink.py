from itertools import product
import pytest


@pytest.mark.parametrize(
    "model",
    ["Fmucontroller", "Fmufuelratecontroller", "FmuTL_VelocityController"]
)
def test_import_TargetLink_fmi2(dymola, resources_dir, model):
    filename = resources_dir / "dSPACE" / "TargetLink" / f"TL-24_1-FMI2-{model}-With_Binaries" / f"{model}.fmu"
    model_name = f"TargetLink_{model}_fmi2_cs"
    dymola.importFMU(
        fileName=filename, integrate=False, modelName=model_name
    )
    dymola.simulate(model_name)


@pytest.mark.parametrize(
    "model",
    ["controller", "fuelratecontroller", "TL_VelocityController"]
)
def test_import_TargetLink_fmi3(dymola, resources_dir, model):
    filename = resources_dir / "dSPACE" / "TargetLink" / f"TL-24_1-FMI3-{model}-With_Binaries" / f"{model}.fmu"
    model_name = f"TargetLink_{model}_fmi3_cs"
    dymola.importFMU(
        fileName=filename, integrate=False, modelName=model_name
    )
    dymola.simulate(model_name)