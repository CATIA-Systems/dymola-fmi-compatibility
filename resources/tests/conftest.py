from itertools import product
from os import makedirs

import pytest
from pathlib import Path
from shutil import rmtree


@pytest.fixture(scope='session')
def work_dir():
    yield Path(__file__).parent / 'work'

@pytest.fixture(scope='session')
def reference_fmus_dir():
    yield Path(__file__).parent.parent / 'Reference-FMUs-0.0.38'

@pytest.fixture(scope='session')
def resources_dir():
    yield Path(__file__).parent.parent

@pytest.fixture(scope='module')
def dymola(work_dir):

    from pymola import Dymola

    with Dymola(showWindow=True, debug=False) as dymola:

        if work_dir.exists():

            def remove_readonly(func, path, _):
                import os, stat
                os.chmod(path, stat.S_IWRITE)
                func(path)

            rmtree(work_dir, onerror=remove_readonly)

        makedirs(work_dir)

        dymola.cd(work_dir)

        # ensure, that MSL is loaded, as functions like exportSSP do not trigger demand loading
        dymola.openModelFile('Modelica')

        yield dymola
