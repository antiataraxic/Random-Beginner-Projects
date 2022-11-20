import random


def guess(x):
    low = 1
    high = x
    feedback = ""
    y = 0
    guessnumber = 14
    while feedback != "c" and y < 5:
        y = y + 1
        guess = random.randint(low, high)
        if guess == guessnumber:
            feedback = "c"
            print(feedback)
    
guess(30)

