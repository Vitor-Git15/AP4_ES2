def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def reverse_string(text):
    return text[::-1]

def is_palindrome(text):
    text = ''.join(char.lower() for char in text if char.isalnum())
    return text == text[::-1]

def count_words(text):
    return len(text.split())

def capitalize_words(text):
    return ' '.join(word.capitalize() for word in text.split())

def find_longest_word(text):
    words = text.split()
    return max(words, key=len) if words else None

def remove_whitespace(text):
    return ''.join(text.split())

def count_occurrences(text, substring):
    return text.count(substring)