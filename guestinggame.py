import random


def get_integer(prompt):
    """
    Gets an integer from Standard Input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.
    :param prompt: The String that the user will see, when
    they're prompted to enter the value.
    :return: The integer that the user enters
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else:
        print("{0} is not a valid number".format(temp))


highest = 1000
answer = random.randint(1, highest)

print("Please guess number between 1 and {}: ".format(highest))
guess = get_integer(": ")

if guess == answer:
    print("You got it first time")

while guess != answer:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = get_integer(": ")
    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it!")
