"""Exercise 07, Comp 110: Bear class"""

__author__ = "730566916"

class Bear:
    
    def __init__(self)-> None:
        self.age: int = 0
        self.hunger_score: int = 0
    
    def one_day(self) -> None:
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int) -> None:
        self.hunger_score += num_fish
