from string_search import find, find_index
import unittest


class TestString(unittest.TestCase):
    def test_found_substring(self):
        assert find("Hello", "Hello") == True
        assert find("Hello", "el") == True
        assert find("banana gram", "banana") == True
        assert find("banana gram", " gram") == True

    def test_not_found_substring(self):
        assert find("Hello", "olleH") == False
        assert find("Hello", "Q") == False
        assert find("banana gram", "banana grand") == False
        assert find("banana gram", "grampa") == False

    def test_index_found_for_substring(self):
        assert find_index("Hello", "Hello") == 0
        assert find_index("Hello", "el") == 1
        assert find_index("banana gram", "na") == 2
        assert find_index("banana gram", " gram") == 6

    def test_index_not_found_substring(self):
        assert find_index("Hello", "olleH") == None
        assert find_index("Hello", "Q") == None
        assert find_index("banana gram", "banana grand") == None
        assert find_index("banana gram", "grampa") == None

if __name__ == '__main__':
    unittest.main()
