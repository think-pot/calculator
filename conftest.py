import os
import pytest

@pytest.fixture(autouse=True)
def setup_subprocess_coverage():
    """Enables coverage tracking across subprocess boundaries."""
    os.environ["COVERAGE_PROCESS_START"] = ".coveragerc"
