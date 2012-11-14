import random
import sys

selection = ""
rollsLeft = 3

def setup_game():
    print "Let's play Yahtzee!"

def prompt():
    global selection
    global rollsLeft

    print "Choices:"
    print "roll - roll the dice (You have " + str(rollsLeft) + " left)"
    print "quit - quit the game"
    selection = raw_input('Selection: ')

def roll_dice():
    global rollsLeft

    dieOne = random.randint(1,6)
    dieTwo = random.randint(1,6)
    dieThree = random.randint(1,6)
    dieFour = random.randint(1,6)
    dieFive = random.randint(1,6)

    print dieOne
    print dieTwo
    print dieThree
    print dieFour
    print dieFive

    rollsLeft -= 1

setup_game()


while True:
    prompt()

    if selection == "roll" and rollsLeft > 0:
        print "Rolling dice"
        roll_dice()
    elif selection == 'quit':
        print "Thanks for playing."
        sys.exit(0)
