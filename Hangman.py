import random
from Words import words
import string

def get_valid_word(word):
    word = random.choice(words)
    while '-' in word or '' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word((words))
    letterwords = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6
    while lives > 0 and len(letterwords) > 0:
        user_input_letter = input("Please enter a letter :").upper()

        print("You have used these letters: ", ''.join(used_letters))
        print("You have", lives, "lives left")
        letterused = [letter if letter in letterwords else '-' for letter in word ]
        print("Currently guessed word is :",''.join(letterused))

        if user_input_letter in alphabet:
            used_letters.add(user_input_letter)
            if user_input_letter in letterwords:
                letterwords.remove(user_input_letter)
            else:
                lives = lives - 1
        elif user_input_letter in used_letters:
            print("You have already used this letter")
        else:
            print("Invalid Character")
    if lives == 0:
        return print("You lost, Try again.")
    else:
        return print("You won. The word was :", word)
print(hangman())

