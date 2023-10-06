import unittest

from palindrome import *

#test 1
class test_palindrome(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(isvalid(400), 798)
