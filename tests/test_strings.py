from src import string_manipulation as str
import pytest


def test_is_equal():
    assert str.is_equal("hello","hello") == True
    assert str.is_equal("Hello","hello") == False
    assert str.is_equal("abc","abc") == True
    assert str.is_equal("abc","abcd") == False
    assert str.is_equal("","") == True

def test_is_capitalized():
    assert str.is_capitalized("Hello") == True
    assert str.is_capitalized("hello") == False
    assert str.is_capitalized("HELLO") == True

@pytest.mark.April_Release
def test_is_palindrome():
    assert str.is_palindrome("madam") == True
    assert str.is_palindrome("level") == True
    assert str.is_palindrome("racecar") == True
    assert str.is_palindrome("hello") == False

@pytest.mark.April_Release
def test_is_uppercase():
    assert str.is_uppercase("HELLO") == True
    assert str.is_uppercase("Hello") == False
    assert str.is_uppercase("hello") == False

def test_is_lowercase():
    assert str.is_lowercase("hello") == True
    assert str.is_lowercase("Hello") == False
    assert str.is_lowercase("HELLO") == False
