# content of test_module.py
 
def setup_function(function):
    print("setting up", function)
 
def test_func1():
    assert True
 
def test_func2():
    assert False
