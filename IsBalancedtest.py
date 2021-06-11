import IsBalanced
import unittest


class TestStringMethods(unittest.TestCase):
    def test_IsBalanced(self):
        self.assertTrue(IsBalanced.check('({()})'))
    
    def test_IsBalancedToo(self):
        self.assertTrue(IsBalanced.check('{[]{()}}'))

    def test_IsNotBalanced(self):
        self.assertFalse(IsBalanced.check('[{{})(]'))
    
    def test_IsNotBalancedComplex(self):
        self.assertFalse(IsBalanced.check('(){])}'))




