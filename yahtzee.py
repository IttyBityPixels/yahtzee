import random
import sys

selection = ""
rollsLeft = 3
rolls = [0, 0, 0, 0, 0]
holds = [0, 0, 0, 0, 0]

def setup_game():
    print "Let's play Yahtzee!"

def prompt():
    global selection
    global rollsLeft

    print "Choices:"
    print "(1) Roll - roll the dice (You have " + str(rollsLeft) + " left)"
    print "(2) Hold/Release - hold or release dice"
    print "(3) Quit - quit the game"
    selection = raw_input('Selection: ')

def roll_dice():
    global rollsLeft
    global rolls
    global holds

    # dieOne = random.randint(1,6)
    # dieTwo = random.randint(1,6)
    # dieThree = random.randint(1,6)
    # dieFour = random.randint(1,6)
    # dieFive = random.randint(1,6)

    for i in range(5):
        if holds[i] == 0:
            rolls[i] = random.randint(1,6)

    print rolls

    rollsLeft -= 1

def hold_prompt():
    print "HOLD STATUS"

    for index, item in enumerate(holds):
        if item == 0:
            print str(index + 1) + ": released"
        else:
            print str(index + 1) + ": held"

    print "Specify which dice you would like to hold or release"

    dice = raw_input('> ').split(' ')

    for i in dice:
        index = int(i) - 1

        if holds[index] == 0:
            holds[index] = 1
        else:
            holds[index] = 0

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
        hold_prompt()
    elif selection == '3':
        print "Thanks for playing."
        sys.exit(0)
