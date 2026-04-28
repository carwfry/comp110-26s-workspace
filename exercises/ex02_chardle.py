'''Excersize 02 - Chardle - A cute step toward Wordle.'''

__author__ = "730566916"

def main() -> None:
    '''The entrypoint of the program and main game loop.'''
    contains_char(word=input_word(), letter=input_letter())

def input_word() -> str:
    '''Asks for a 5 character word and returns it as a string.'''
    word: str = input("Enter a 5-character word: ")
    # Checking if the word is 5 characters long:
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    else:
        return word

def input_letter() -> str:
    '''Prompts the user for a single character and returns it as a string.'''
    letter: str = input("Enter a single character: ")
    #Checking if the letter is a single character:
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    else:
        return letter

def contains_char(word: str, letter: str) -> None:
    '''Returns True if the single character is found in the 5 character word, False otherwise.'''
    assert len(word) == 5
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    assert len(letter) == 1
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    print("Searching for " + letter + " in " + word)
    #This counts the number of times the letter is found in the word and prints the index of each occurrence:
    letter_count = 0
    if letter == word[0]:
        letter_count += 1
        print(letter + " found at index 0")
    if letter == word[1]:
        letter_count += 1
        print(letter + " found at index 1")
    if letter == word[2]:
        letter_count += 1
        print(letter + " found at index 2")
    if letter == word[3]:
        letter_count += 1
        print(letter + " found at index 3")
    if letter == word[4]:
        letter_count += 1
        print (letter + " found at index 4")

    if letter_count == 0:
        print("No instances of " + letter + " found in " + word)    
    elif letter_count == 1:
        print(str(letter_count) + " instance of " + letter + " found in " + word)
    else:
        print(str(letter_count) + " instances of " + letter + " found in " + word)


if __name__ == "__main__":
    main()