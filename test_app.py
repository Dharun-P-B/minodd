from app import is_odd

def test_is_odd_with_odd_number():
    assert is_odd(3) is True
    assert is_odd(-5) is True

def test_is_odd_with_even_number():
    assert is_odd(4) is False
    assert is_odd(0) is False
