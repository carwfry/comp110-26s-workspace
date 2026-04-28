"""EX09: Data related utility functions."""

__author__ = ["730566916"]

import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

def read_csv_rows(file_path: str) -> list[dict[str, str]]:
    """Read a CSV file into a list of row dictionaries."""
    result: list[dict[str, str]] = []
    with open(file_path, "r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            result.append(row)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Convert a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    if len(row_table) == 0:
        return result
    for key in row_table[0]:
        result[key] = [row[key] for row in row_table]
    return result


def head(column_table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Return the first n rows of a column-oriented table."""
    result: dict[str, list[str]] = {}
    for col in column_table:
        result[col] = column_table[col][:n]
    return result


def select(column_table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Return a subset of columns from a column-oriented table."""
    return {name: column_table[name] for name in names if name in column_table}

rows = read_csv_rows("exercises/ex09/data/survey_izzi.csv")
cols = columnar(rows)
head(cols, 5)

subset = select(cols, ["major", "languages"])
head(subset, 5)

def filter_by_major(column_table: dict[str, list[str]], major: str) -> dict[str, list[str]]:
    """Return only rows where the major matches the given string."""
    result = {col: [] for col in column_table}
    for i in range(len(column_table["major"])):
        if column_table["major"][i] == major:
            for col in column_table:
                result[col].append(column_table[col][i])
    return result

env = filter_by_major(subset, "Environmental Science/Studies")
head(env, 5)

def count_languages(lang_string: str) -> int:
    if lang_string is None:
        return 0
    cleaned = lang_string.replace(";", ",")
    return len([x for x in cleaned.split(",") if x.strip() != ""])

language_counts = [count_languages(x) for x in env["languages"]]
language_counts[:10]

sns.histplot(language_counts, bins=range(0, max(language_counts)+2))
plt.gca().xaxis.set_major_locator(mticker.MaxNLocator(integer=True))
plt.xlabel("Number of Languages")
plt.ylabel("Number of Students")
plt.title("Histogram of Languages Known")
plt.show()
