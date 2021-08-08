import pytest

MOCK_DICTIONARY = {
    "first_name": "Jake",
    "last_name": "Basel",
    "active": 1,
    "age": 100
}

def test_dictionary_has_integer_valid_age():
    assert isinstance(MOCK_DICTIONARY["age"], int)

def test_dictionary_has_valid_username():
    assert MOCK_DICTIONARY.get("first_name") == "Jake"

