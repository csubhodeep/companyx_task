import pytest

def test_import():

    # assert that the main function can be imported and that it does not throw an error
    try:
        from booking_forecaster import main
    except (ImportError, ModuleNotFoundError):
        pytest.fail("Could not import main function")