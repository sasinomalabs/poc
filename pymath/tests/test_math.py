import unittest
from pymath.lib.math import is_palindrome

class TestIsPalindrome(unittest.TestCase):

    def test_string_palindromes(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(is_palindrome("No lemon, no melon."))

    def test_integer_palindromes(self):
        self.assertTrue(is_palindrome(121))
        self.assertTrue(is_palindrome(12321))
        self.assertTrue(is_palindrome(1001))

    def test_string_non_palindromes(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))

    def test_integer_non_palindromes(self):
        self.assertFalse(is_palindrome(123))
        self.assertFalse(is_palindrome(4567))

    def test_mixed_case_palindromes(self):
        self.assertTrue(is_palindrome("RaceCar"))
        self.assertTrue(is_palindrome("Madam"))

    def test_palindromes_with_non_alphanumeric(self):
        self.assertTrue(is_palindrome("Able was I, ere I saw Elba."))
        self.assertTrue(is_palindrome("Step on no pets."))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_single_character_string(self):
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("7"))

    def test_input_type_validation(self):
        with self.assertRaises(TypeError):
            is_palindrome([1, 2, 1])
        with self.assertRaises(TypeError):
            is_palindrome({"a": 1})
        with self.assertRaises(TypeError):
            is_palindrome(12.321)

if __name__ == '__main__':
    unittest.main()
