import pytest
from module_calGrade import calGrade

@pytest.mark.parametrize("test_input, expected",\
                         [(25, "D"),(35, "C"),(55, "B"),(75, "A")])
def test_calGrade(test_input, expected):
    assert calGrade(test_input) == expected
    
# def test_calGrade_25():
#     assert calGrade(25) == "D"

# def test_calGrade_35():
#     assert calGrade(35) == "C"

# def test_calGrade_55():
#     assert calGrade(55) == "B"

# def test_calGrade_75():
#     assert calGrade(75) == "A"


# def test_calGrade():
#     assert calGrade(25) == "D"
#     assert calGrade(35) == "C"
#     assert calGrade(55) == "B"
#     assert calGrade(75) == "A"