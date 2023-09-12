import pytest

@pytest.fixture
def fixt(request):
    marker = request.node.get_closest_marker("fixt_data")
    if marker is None:
        # Handle missing marker in some way...
        data = None
    else:
        data = marker.args[0]

    # Do something with the data
    return data

@pytest.mark.fixt_data(42)
def test_fixt(fixt):
    assert fixt == 42
