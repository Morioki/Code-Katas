import unittest

def warn_the_sheep(queue):
    return 'Pls go away and stop eating my sheep' if queue[::-1].index('wolf') == 0 else f"Oi! Sheep number {queue[::-1].index('wolf')}! You are about to be eaten by a wolf!" 

class TestSolution(unittest.TestCase):
    def test_1(self):
        self.assertEquals(warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep']), 'Oi! Sheep number 2! You are about to be eaten by a wolf!')
        
    def test_2(self):
        self.assertEquals(warn_the_sheep(['sheep', 'wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']), 'Oi! Sheep number 5! You are about to be eaten by a wolf!')
        
    def test_3(self):
        self.assertEquals(warn_the_sheep(['wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']), 'Oi! Sheep number 6! You are about to be eaten by a wolf!')
        
    def test_4(self):
        self.assertEquals(warn_the_sheep(['sheep', 'wolf', 'sheep']), 'Oi! Sheep number 1! You are about to be eaten by a wolf!')
        
    def test_5(self):
        self.assertEquals(warn_the_sheep(['sheep', 'sheep', 'wolf']), 'Pls go away and stop eating my sheep')