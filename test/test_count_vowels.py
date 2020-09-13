import pytest

from count_vowels import count_vowels


def test_count_empty() -> None:
    assert count_vowels('') == 0


def test_no_vowel_word() -> None:
    assert count_vowels('rhythm') == 0


def test_simple_word() -> None:
    assert count_vowels('hello') == 2


def test_simple_goodbye() -> None:
    assert count_vowels('GOODBYE') == 3


def test_list() -> None:
    with pytest.raises(AttributeError):
        count_vowels(['abcdefg'])
