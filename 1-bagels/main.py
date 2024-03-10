import random

def main():
    print('''
    Bagels, a deductive logic game.
    I am thinking of a 3-digit number. Try to guess what it is.
    Here are some clues:
    When I say:         It means:
        Pico              One digit is correct but in the wrong position.
        Fermi             One digit is correct and in the correct position.
        Bagels            No digit is correct.
    I have thought up a number.''')
    randomInt = random.randrange(100,999)
    guessInt = 1
    print("You have 10 guesses to get it.")
    while guessInt != 11:
        print(f'Guess #{guessInt}: \n')
        guessInt += 1

    print("Do you want to play again? (yes or no)")
    playAgain = input();

if __name__ == "__main__":
    main()