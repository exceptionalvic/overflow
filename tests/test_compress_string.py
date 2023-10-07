"""Test cases for compress_string."""
import pytest
from challenge1.compress_string import compress


# Test cases for the compress function
def test_compress():
    """Test compress functiom."""
    # Test when the input string is 'bbcceeee'
    assert compress("bbcceeee") == "b2c2e4"

    # Test when the input string is 'aaabbbcccaaa'
    assert compress("aaabbbcccaaa") == "a3b3c3a3"

    # Test when the input string is 'a'
    assert compress("a") == "a"

    # Test when the input string is empty
    assert compress("") == ""

    # Test when the input string is 'abcd'
    # it should return the original string.
    assert compress("abcd") == "abcd"

    # Test when the input string is 'aAaAAa'
    # return input string since format is
    # not right
    assert compress("aAaAAa") == "aAaAAa"

    # Test when the input string contains digits
    assert compress("1122334455") == "1122334455"

    # Test when the input string contains special characters
    assert compress("!@#$%^&*") == "!@#$%^&*"


if __name__ == "__main__":
    pytest.main()
