import random


def guess(z):
    randomnumber = random.randint(1, z)
    x = 0
    y = 1
    q = "Not Found"
    found = False
    while y < 6 and found == False:
        x = int(input("Enter number :"))
        y = y + 1
        if x == randomnumber:
            found = True
        elif x > randomnumber:
            print("Guess lower")
        elif x < randomnumber:
            print("Guess higher")
    if found == True:
        return x
    else:
        return q


guess(20)


