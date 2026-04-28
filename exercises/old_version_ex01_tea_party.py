# Excercise 01, Comp 110

__author__ = "730566916"

def main_planner(guests: int):
    '''This will display the calculated values'''
    print("A Cozy Tea Party for", guests, "People!")
    print("Tea Bags:", tea_bags(guests))
    print("Treats:", treats(guests))
    print("Total Cost: $", cost(guests))

def tea_bags(people:int)-> int:
    '''Calculates the number of tea bags needed given an integer number of people'''
    return (people)*2

def treats(people:int)-> int:
    '''Calculates the number of treats needed given an integer number of people'''
    return int(tea_bags(people)*1.5)


def cost(people: int) -> float: 
    '''Return the total cost of tea bags and treats.'''
    tea_cost = tea_bags(people) * 0.50 
    treat_cost = treats(people) * 0.75 
    return tea_cost + treat_cost

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
