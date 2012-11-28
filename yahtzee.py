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
    print "(1) Roll - roll the dice (You have " + str(rollsLeft) + " left)"
    print "(2) Quit - quit the game"
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

    if selection == '1':
        if rollsLeft > 0:
            print "Rolling dice"
            roll_dice()
        else:
            print "You can not roll anymore"
    elif selection == '2':
        print "Thanks for playing."
        sys.exit(0)
