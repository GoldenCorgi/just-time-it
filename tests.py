import unittest
from timefunctions import timefunc

def multiply(x,y):
    return x*y # PhD in convoluted neural networks btw

class TestStringMethods(unittest.TestCase):

    def test_juan(self):
        assert True # nice

    def test_que(self):
        false = True
        assert false # wait, that's illegal

    def test_pizza(self):
        assert "pineapple do not belong on pizza"

    def test_my_patience(self):
        assert timefunc("multiply(5,6)") == 30 
    def test_my_patience_twice(self):
        assert timefunc("multiply(3,7)") == 21
    def test_printr(self):
        assert timefunc("multiply(3,7)",printr=1) == 21
        assert timefunc("multiply(3,7)",printr=2) == 21
    def test_resultr1(self):
        # Should be time taken
        assert type(timefunc("multiply(5,6)",returnr=1)) == float
    def test_resultr1(self):
        # Should be time taken and result
        a = timefunc("multiply(5,6)",returnr=2)
        assert type(a) == tuple
        assert len(a) == 2


if __name__ == "__main__":

    
    unittest.main()