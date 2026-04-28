"""Exercise 05, Comp 110."""

__author__ = "730566916"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Invert the keys and values of a dictionary, and ensure there are no duplicates."""
    result: dict[str, str] = {}
    for key in input:
        if input[key] in result:
            raise KeyError("Error: duplicate key")
        result[input[key]] = key
    return result


def favorite_color(input: dict[str, str]) -> str:
    """Return the color that appears most frequently in the dictionary."""
    color_count: dict[str, int] = {}
    for name in input:
        color = input[name]
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    most_frequent_color: str = ""
    max_count: int = 0
    for color in color_count:
        if color_count[color] > max_count:
            most_frequent_color = color
            max_count = color_count[color]
    return most_frequent_color


def count(input: list[str]) -> dict[str, int]:
    """Count the frequency of each string in a list."""
    result: dict[str, int] = {}
    for item in input:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Group words by their first letter and return a dictionary with keys sorted alphabetically."""
    grouped: dict[str, list[str]] = {}

    for word in words:
        if not isinstance(word, str):
            raise KeyError("Non-string entry found.")
        # Use uppercase first letter as the key so 'a' and 'A' group together
        key = word[0].upper()
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(word)

    """Build a new dict with keys sorted alphabetically"""
    sorted_grouped: dict[str, list[str]] = {}
    for key in sorted(grouped.keys()):
        sorted_grouped[key] = grouped[key]

    return sorted_grouped


    return sorted_dict



def update_attendance(attendance: dict[str, list[str]], day: str, name: str) -> None:
    """ If the day doesn't exist yet, create it"""
    if day not in attendance:
        attendance[day] = []

    """Add the name only if it's not already present"""
    if name not in attendance[day]:
        attendance[day].append(name)
