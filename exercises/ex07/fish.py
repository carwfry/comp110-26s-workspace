"""Exercise 07, Comp 110: Fish class"""

__author__ = "730566916"

class Fish:
    
    def __init__(self) -> None:
        self.age: int = 0
    
    def one_day(self) -> None:
        self.age += 1