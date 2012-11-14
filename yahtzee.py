import random
import sys

selection = ""

def setup_game():
    print "Let's play Yahtzee!"
    print "Choices:"
    print "roll - roll the dice"
    print "quit - quit the game"

def prompt():
    global selection
    selection = raw_input('Selection: ')

def roll_dice():
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

setup_game()


while True:
    prompt()

    if selection == "roll":
        print "Rolling dice"
        roll_dice()
    elif selection == 'quit':
        print "Thanks for playing."
        sys.exit(0)
