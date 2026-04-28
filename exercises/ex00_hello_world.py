# Excercise 00, Comp 110
__author__ = "730566916"

print("Hello, world!")


def greet(name: str) -> str:
    """A welcoming first function definition."""
    return "Hello, " + name + "!"


greet(name="Caroline")

if __name__ == "__main__":
    print(greet(name=input("What is your name?")))
