from main import add, subtract, multiply, divide, convert_to_minutes

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(10, 2) == 5
    assert divide(10, 0) is None

def test_convert_to_minutes():
    assert convert_to_minutes(2) == 120
