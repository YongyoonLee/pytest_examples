from functools import partial
import pytest

@pytest.fixture
def fix_w_finalizers(request):
    request.addfinalizer(partial(print, "finalizer_2"))
    request.addfinalizer(partial(print, "finalizer_1"))

def test_bar(fix_w_finalizers):
    print("test_bar")
