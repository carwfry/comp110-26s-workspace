''' Excercise 01, Comp 110 - redo because I got a bad grade on the first one'''

__author__ = "730566916"

def main_planner(guests: int) -> None:
    '''This will display the calculated values'''
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people:int)-> int:
    '''Calculates the number of tea bags needed given an integer number of people'''
    return (people)*2

def treats(people:int)-> int:
    '''Calculates the number of treats needed given an integer number of people'''
    return int(tea_bags(people=people)*1.5)

def cost(tea_count: int, treat_count: int) -> float: 
    '''Return the total cost of tea bags and treats.'''
    return float(tea_count*0.50 + treat_count*0.75)

if __name__ == "__main__":
    '''Main function to run the tea party planner'''
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
