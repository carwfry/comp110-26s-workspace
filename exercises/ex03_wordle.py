'''Excersize 03 - Wordle'''

__author__ = "730566916"

def input_guess(secret_word: int) -> str:
    '''Asks the user for a word and returns whether it is the correct length''' 
    guess: str = input(f"Enter a {secret_word} character word: ")
    # Checking if the guess is the correct length:
    while (len(guess) != secret_word):
        print(f"That wasn't {secret_word} chars! Try again: ")
        guess =input()
    return(guess)

def contains_char(secret_word: str, char_guess: str) -> bool:
    '''Checks each character to see if it is in the secret word and returns True if it is, False otherwise.'''
    assert len(char_guess) == 1
    for char in secret_word:
        if char == char_guess:
            return True
    return False
    
def emojified(guess: str, secret_word: str) -> str:
    '''Returns a string of emojis that indicate which characters in the guess are correct and in the correct position (green), which characters are correct but in the wrong position (yellow), and which characters are not in the secret word at all (white).'''
    assert len(guess) == len(secret_word)
    emoji_string: str = ""
    i:int=0
    while i<len(secret_word):
        if guess[i] == secret_word[i]:
            emoji_string += "\U0001F7E9"
            #green box
        elif contains_char(secret_word, guess[i]):
            emoji_string += "\U0001F7E8"
            #yellow box
        else:
            emoji_string += "\U00002B1C"
            #white box
        i += 1
    return emoji_string

def main(secret_word: str) -> None:
    '''Main game loop'''
    turns: int = 0
    max_turns: int = 6
    guess: str = ""
    #This allows for 6 turns and ends the game if the user guesses the word correctly or runs out of turns.
    while (turns < max_turns and guess != secret_word):
        print(f"=== Turn {turns + 1}/{max_turns} ===")
        guess = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        turns += 1
    if (guess == secret_word):
        print(f"You won in {turns}/{max_turns} turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":    main(secret_word="codes")
