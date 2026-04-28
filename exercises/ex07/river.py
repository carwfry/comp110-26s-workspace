from __future__ import annotations
"""Exercise 07, Comp 110: River class"""

__author__ = "730566916"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        # Remove fish older than 3
        self.fish = [fish for fish in self.fish if fish.age <= 3]

        # Remove bears older than 5
        self.bears = [bear for bear in self.bears if bear.age <= 5]

    def bears_eating(self) -> None:
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

    def check_hunger(self) -> None:
        self.bears = [bear for bear in self.bears if bear.hunger_score >= 0]

    def repopulate_fish(self) -> None:
        num_new_fish = (len(self.fish) // 2) * 4
        for _ in range(num_new_fish):
            self.fish.append(Fish())

    def repopulate_bears(self) -> None:
        num_new_bears = len(self.bears) // 2
        for _ in range(num_new_bears):
            self.bears.append(Bear())

    def __str__(self) -> str:
        return (
            f"~~~ Day {self.day}: ~~~\n"
            f"Fish population: {len(self.fish)}\n"
            f"Bear population: {len(self.bears)}"
        )
    
    def __add__(self, r: "River") -> "River":
        total_fish = len(self.fish) + len(r.fish)
        total_bears = len(self.bears) + len(r.bears)
        return River(total_fish, total_bears)

    def __mul__(self, factor: int) -> "River":
        new_fish = len(self.fish) * factor
        new_bears = len(self.bears) * factor
        return River(new_fish, new_bears)

    def one_river_day(self) -> None:
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()

    def one_river_week(self) -> None:
        for _ in range(7):
            self.one_river_day()

    def remove_fish(self, amount: int) -> None:
        for _ in range(amount):
            if len(self.fish) > 0:
                self.fish.pop(0)