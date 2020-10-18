import unittest

def index(array, n):
    if n >= len(array):
        return -1
    
    return array[n]**n


class TestSolution(unittest.TestCase):
    def test_1(self):
        self.assertEquals(index([1, 2, 3, 4],2),9)

    def test_2(self):
        self.assertEquals(index([1, 3, 10, 100],3),1000000)