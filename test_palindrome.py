import unittest
from palindrome import *


class test_palindrome(unittest.TestCase):

# Middle case tests
    def test_1(self):
        self.assertTrue(isPalindrome("racecar") is True)
    def test_2(self):
        self.assertTrue(isPalindrome("panama") is False)
    def test_3(self):
        self.assertTrue(isPalindrome("A man, a plan, a canal: Panama") is True)
    def test_4(self):
        self.assertTrue(isPalindrome("Chunky Monkey") is False)

# Edge case tests
    def test_5(self):
        self.assertTrue(isPalindrome("") is True)
    def test_6(self):
        self.assertTrue(isPalindrome("a") is True)
