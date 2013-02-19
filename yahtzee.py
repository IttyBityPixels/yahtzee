import random
import sys
import curses
import urwid

selection = ""
rollsLeft = 3
rolls = [0, 0, 0, 0, 0]
holds = [0, 0, 0, 0, 0]

# scores
aces = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0
bonus = 0
threeKind = 0
fourKind = 0
fullHouse = 0
smallStraight = 0
largeStraight = 0
yahtzee = 0
chance = 0

# def setup_game():
    # print "Let's play Yahtzee!"

def create_scorecard():
    # stdscr.border(0)
    # stdscr.addstr(1, 2, "  Upper Section")
    # stdscr.addstr(2, 2, "-----------------")
    # stdscr.addstr(3, 2, "Aces:           0")
    # stdscr.addstr(4, 2, "Twos:           0") 
    # stdscr.addstr(5, 2, "Threes:         0")
    # stdscr.addstr(6, 2, "Fours:          0")
    # stdscr.addstr(7, 2, "Fives:          0")
    # stdscr.addstr(8, 2, "Sixes:          0")
    # stdscr.addstr(9, 2, "Bonus:          0")
# 
#     stdscr.addstr(1, 20, "|")
#     stdscr.addstr(2, 20, "|")
#     stdscr.addstr(3, 20, "|")
#     stdscr.addstr(4, 20, "|") 
#     stdscr.addstr(5, 20, "|")
#     stdscr.addstr(6, 20, "|")
#     stdscr.addstr(7, 20, "|")
#     stdscr.addstr(8, 20, "|")
#     stdscr.addstr(9, 20, "|")
# 
#     stdscr.addstr(1, 22, "  Lower Section")
#     stdscr.addstr(2, 22, "-----------------")
#     stdscr.addstr(3, 22, "3 of a kind:    0")
#     stdscr.addstr(4, 22, "4 of a kind:    0") 
#     stdscr.addstr(5, 22, "Full House:     0")
#     stdscr.addstr(6, 22, "Sm. Straight:   0")
#     stdscr.addstr(7, 22, "Lg. Straight:   0")
#     stdscr.addstr(8, 22, "Yahtzee:        0")
#     stdscr.addstr(9, 22, "Chance:         0")
# 
#     stdscr.addstr(1, 43, "Roll:    " + str(rollsLeft))
#     stdscr.addstr(2, 43, "Total:   0")
# 
#     stdscr.refresh()
#     stdscr.getch()
#     stdscr.endwin()

    # upper section
    acesLabel = urwid.Text(u"  Aces:", align='left')
    twosLabel = urwid.Text(u"  Twos:", align='left')
    threesLabel = urwid.Text(u"Threes:", align='left')
    foursLabel = urwid.Text(u" Fours:", align='left')
    fivesLabel = urwid.Text(u" Fives:", align='left')
    sixesLabel = urwid.Text(u" Sixes:", align='left')
    bonusLabel = urwid.Text(u" Bonus:", align='left')

    acesWidget = urwid.Columns([acesLabel, urwid.Text(str(aces), align='right')])
    twosWidget = urwid.Columns([twosLabel, urwid.Text(str(twos), align='right')])
    threesWidget = urwid.Columns([threesLabel, urwid.Text(str(threes), align='right')])
    foursWidget = urwid.Columns([foursLabel, urwid.Text(str(fours), align='right')])
    fivesWidget = urwid.Columns([fivesLabel, urwid.Text(str(fives), align='right')])
    sixesWidget = urwid.Columns([sixesLabel, urwid.Text(str(sixes), align='right')])
    bonusWidget = urwid.Columns([bonusLabel, urwid.Text(str(bonus), align='right')])

    upperSectionWidgets = [acesWidget, twosWidget, threesWidget, foursWidget, fivesWidget, sixesWidget, bonusWidget]

    upperSectionPile = urwid.Pile(upperSectionWidgets)

    # lower section
    threeKindLabel = urwid.Text(u"Three of a Kind:", align='left')
    fourKindLabel = urwid.Text(u" Four of a Kind:", align='left')
    fullHouseLabel = urwid.Text(u"     Full House:", align='left')
    smallStraightLabel = urwid.Text(u" Small Straight:", align='left')
    largeStraightLabel = urwid.Text(u" Large Straight:", align='left')
    yahtzeeLabel = urwid.Text(u"        Yahtzee:", align='left')
    chanceLabel = urwid.Text(u"         Chance:", align='left')
    
    threeKindWidget = urwid.Columns([threeKindLabel, urwid.Text(str(threeKind), align='right')])
    fourKindWidget = urwid.Columns([fourKindLabel, urwid.Text(str(fourKind), align='right')])
    fullHouseWidget = urwid.Columns([fullHouseLabel, urwid.Text(str(fullHouse), align='right')])
    smallStraightWidget = urwid.Columns([smallStraightLabel, urwid.Text(str(smallStraight), align='right')])
    largeStraightWidget = urwid.Columns([largeStraightLabel, urwid.Text(str(largeStraight), align='right')])
    yahtzeeWidget = urwid.Columns([yahtzeeLabel, urwid.Text(str(yahtzee), align='right')])
    chanceWidget = urwid.Columns([chanceLabel, urwid.Text(str(chance), align='right')])
    
    lowerSectionWidgets = [threeKindWidget, fourKindWidget, fullHouseWidget, smallStraightWidget, largeStraightWidget, yahtzeeWidget, chanceWidget]

    lowerSectionPile = urwid.Pile(lowerSectionWidgets)
    
    upperSection = urwid.LineBox(upperSectionPile, title='Upper Section')
    lowerSection = urwid.LineBox(lowerSectionPile, title='Lower Section')

    sections = upperSection, lowerSection
    columns = urwid.Columns(sections)

    fill = urwid.Filler(columns, 'top')
    loop = urwid.MainLoop(fill)
    loop.run()

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
def main(stdscr):
    # setup_game()

    # stdscr.border(0)
    # stdscr.addstr(12, 25, "let's play yagtzee!")
    # stdscr.refresh()
    # stdscr.getch()
    # stdscr.endwin()

    create_scorecard(stdscr)

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

# curses.wrapper(main)

create_scorecard()
