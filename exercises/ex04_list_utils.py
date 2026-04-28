''' Excercise 04: List Utils, Comp 110 - redo because I got a bad grade on the first one'''

__author__ = "730566916"

def all(list1: list[int], value: int) -> bool:
    if not list1:
        return False
    for item in list1:
        if item != value:
            return False
    return True

def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max_value = input[0]
    for item in input:
        if item > max_value:
            max_value = item
    return max_value

def is_equal(list1: list[int], list2: list[int]) -> bool:
    if list1 == list2:
        return True
    else:
        return False

def extend(list1: list[int], list2: list[int]) -> None:
    for item in list2:
        list1.append(item)
    return None
