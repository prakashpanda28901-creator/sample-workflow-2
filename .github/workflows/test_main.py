import unittest
from main import add

class TestMain(unittest.Testcase):
    def test_add(self):
        assert add(2,3) == 5
        assert add(-1,1) == 0


# assert is assertion function which checking

# run this i will use library called pytest