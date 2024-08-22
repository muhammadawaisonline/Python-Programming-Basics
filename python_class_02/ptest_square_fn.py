
import pytest
from square_fn import square

""" def test_square():
    assert square(2) == 4
    assert square(-2) == 4
    assert square(3)  == 9
    assert square(-3) ==9
    assert square(0)  ==0
     """
def test_positive_number():
    assert square(2) == 4
    assert square(3) == 9

def test_negative_numbers():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0 

def test_str():
    with pytest.raises(TypeError):
        square("cat")
    