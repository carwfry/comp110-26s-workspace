"""Exercise 08, Comp 110: Linked List"""

from __future__ import annotations

__author__ = "730566916"


class Node:
    """Node in a singly-linked list recursive structure."""
    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Construct a Node with the given value and next node."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Produce a string representation of this Node and the ones that follow it."""
        if self.next is None:
            return f"{self.value} -> None"
        else:
            return f"{self.value} -> {self.next}"
       

courses: Node = Node(10, Node(20, Node(30, None)))
items = [10, 20, 30, 40]
    

def value_at(node: Node, index: int) -> int:
    """Returns the value at the given index in the linked list."""
    if node is None:
        raise IndexError("Index out of bounds on the list")
    if index == 0:
        return node.value
    if node.next is None:
        raise IndexError("Index out of bounds on the list")
    if index < 0:
        raise IndexError("Index out of bounds on the list")
    return value_at(node.next, index - 1)


def max(head: Node | None) -> int:
    """Returns the maximum value in the linked list."""
    if head is None:
        raise ValueError("Cannot call max with None")
    if head.next is None:
        return head.value
    else:
        rest_max: int = max(head.next)
        if head.value > rest_max:
            return head.value
        else:
            return rest_max


def linkify(items: list[int]) -> Node | None:
    """Converts a list of integers to a linked list."""
    if len(items) == 0:
        return None
    else:
        first: int = items[0]
        rest: Node | None = linkify(items[1:])
        return Node(first, rest)


def scale(head: Node | None, factor: int) -> Node | None:
    """Returns a new linked list with the values in head scaled by factor."""
    if head is None:
        return None
    else:
        scaled_value: int = head.value * factor
        rest_scaled: Node | None = scale(head.next, factor)
        return Node(scaled_value, rest_scaled)


def recursive_range(start: int, end: int) -> Node | None:
    """Returns a linked list containing the integers from start to end - 1."""
    """edge case"""
    if start > end:
        raise Exception("NO")
    if start == end:
        return None
    else:
        first: int = start
        rest: Node | None = recursive_range(start + 1, end)
        return Node(first, rest)