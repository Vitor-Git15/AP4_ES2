import unittest
from StringUtils import (
    count_vowels,
    reverse_string,
    is_palindrome,
    count_words,
    capitalize_words,
    find_longest_word,
    remove_whitespace,
    count_occurrences,
)

class TestStringUtils(unittest.TestCase):
    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("HELLO"), 2)
        self.assertEqual(count_vowels("xyz"), 0)

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("world"), "dlrow")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racear"))
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama"))
        self.assertFalse(is_palindrome("hello"))

    def test_count_words(self):
        self.assertEqual(count_words("hello world"), 2)
        self.assertEqual(count_words(""), 0)

    def test_capitalize_words(self):
        self.assertEqual(capitalize_words("hello world"), "Hello World")
        self.assertEqual(capitalize_words("PYTHON is fun"), "Python Is Fun")

    def test_find_longest_word(self):
        self.assertEqual(find_longest_word("hello world"), "hello")
        self.assertEqual(find_longest_word(""), None)

    def test_remove_whitespace(self):
        self.assertEqual(remove_whitespace("hello world"), "helloworld")
        self.assertEqual(remove_whitespace("  python   programming  "), "pythonprogramming")

    def test_count_occurrences(self):
        self.assertEqual(count_occurrences("hello world hello", "hello"), 2)
        self.assertEqual(count_occurrences("hello world", "Python"), 0)

if __name__ == "__main__":
    unittest.main()
