"""Exercise 06, Comp 110."""

__author__ = "730566916"

import pytest
from exercises.ex05.dictionary import (
    alphabetizer,
    count,
    favorite_color,
    invert,
    update_attendance,
)

# -------------------------
# Invert tests
# -------------------------


def test_invert_names() -> None:
    """Use case: names."""
    name_dictionary = {'Caleb': 'Wilson', 'Henri': 'Veesaar', 'Seth': 'Trimble'}
    assert invert(name_dictionary) == {'Wilson': 'Caleb', 'Veesaar': 'Henri', 'Trimble': 'Seth'}


def test_invert_numbers() -> None:
    """Use case: numeric strings."""
    number_dictionary = {'1': 'one', '2': 'two', '3': 'three'}
    assert invert(number_dictionary) == {'one': '1', 'two': '2', 'three': '3'}


def test_invert_empty() -> None:
    """Edge case: empty dictionary."""
    assert invert({}) == {}


def test_invert_duplicate_values() -> None:
    """Edge case: duplicate values should raise KeyError."""
    with pytest.raises(KeyError):
        invert({'a': 'x', 'b': 'x'})


# -------------------------
# Favorite color tests
# -------------------------

def test_favorite_color_names() -> None:
    """Use case: names."""
    name_dictionary = {'Caleb': 'Red', 'Henri': 'Blue', 'Seth': 'Green'}
    assert favorite_color(name_dictionary) == 'Red'


def test_favorite_color_repeated() -> None:
    """Repeated colors should return the most frequent."""
    edge_dictionary = {'Caleb': 'Red', 'Henri': 'Red', 'Seth': 'Blue'}
    assert favorite_color(edge_dictionary) == 'Red'
    

def test_favorite_color_empty() -> None:
    """Empty dictionary should raise KeyError."""
    with pytest.raises(KeyError):
        favorite_color({})


# -------------------------
# Count tests
# -------------------------

def test_count_names() -> None:
    """Use case: names."""
    name_list = ['Alice', 'Bob', 'Alice', 'Charlie']
    assert count(name_list) == {'Alice': 2, 'Bob': 1, 'Charlie': 1}


def test_count_numbers() -> None:
    """Use case: numeric strings."""
    number_list = ['1', '2', '1', '3']
    assert count(number_list) == {'1': 2, '2': 1, '3': 1}


def test_count_empty() -> None:
    """Empty list should return empty dictionary."""
    assert count([]) == {}


# -------------------------
# Alphabetizer tests
# -------------------------

def test_alphabetizer_basic() -> None:
    """Basic alphabetical grouping."""
    names = ['Alice', 'Bob', 'Charlie']
    assert alphabetizer(names) == {'A': ['Alice'], 'B': ['Bob'], 'C': ['Charlie']}


def test_alphabetizer_duplicates() -> None:
    """Multiple names with same starting letter."""
    names = ['Alice', 'Adam', 'Bob']
    assert alphabetizer(names) == {'A': ['Alice', 'Adam'], 'B': ['Bob']}


def test_alphabetizer_case_insensitive() -> None:
    """Case-insensitive grouping."""
    names = ['Alice', 'alice', 'Bob']
    assert alphabetizer(names) == {'A': ['Alice', 'alice'], 'B': ['Bob']}


def test_alphabetizer_empty() -> None:
    """Empty list should return empty dictionary."""
    assert alphabetizer([]) == {}


# -------------------------
# Update attendance tests
# -------------------------

def test_update_attendance_adds_name() -> None:
    """Adding a new name to an existing day."""
    attendance = {'Monday': ['Alice', 'Bob']}
    update_attendance(attendance, 'Monday', 'David')
    assert attendance == {'Monday': ['Alice', 'Bob', 'David']}


def test_update_attendance_new_day() -> None:
    """Adding a name to a new day creates the key."""
    attendance = {'Monday': ['Alice']}
    update_attendance(attendance, 'Tuesday', 'Bob')
    assert attendance == {'Monday': ['Alice'], 'Tuesday': ['Bob']}


def test_update_attendance_empty_dict() -> None:
    """Empty dictionary should create the new day."""
    attendance = {}
    update_attendance(attendance, 'Monday', 'Alice')
    assert attendance == {'Monday': ['Alice']}


def test_update_attendance_no_duplicates() -> None:
    """Name should not be added twice."""
    attendance = {'Tuesday': ['Anna']}
    update_attendance(attendance, 'Tuesday', 'Anna')
    assert attendance == {'Tuesday': ['Anna']}
