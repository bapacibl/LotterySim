# OzLotto Sim
# Ben Apacible
# This program simulates playing OzLotto once each week with the same numbers


# Oz Lotto numbers are drawn from a machine containing balls from 1 to 45
# For a standard game, you choose 7 numbers from this range.
# In total, 9 balls are drawn of which the first 7 are the winning numbers.
# The last 2 balls are the supplementary numbers.
# Supplementary balls are used to determine prizes in Divisions 2, 4 and 7.
# The chance of winning a Division One prize in Oz Lotto is 1 in 45,379,620


from random import *



# Player inputs the numbers they want to play the lottery with
def PlayerInput():
    TicketNums = []
    NumLeft = NumBalls
    while len(TicketNums) < NumBalls:
        Selected = input("Pick a number from 1-45: ")
        if (int(Selected) not in TicketNums) and (1 <= int(Selected) <= 45):
            TicketNums.append(int(Selected))
            NumLeft -= 1
        elif (int(Selected) in TicketNums):
            print("You have already selected this number, try again")
        elif not((1 <= int(Selected) <= 45)):
            print("This number is not between 1 and 45")
        print(str(NumLeft) + " Balls left to choose.")
    return TicketNums


# Draws the winning numbers out of the pool
def DrawWinners():
    WinningNums = []
    print("Week " + str(WeekNum))
    while len(WinningNums) < NumSelected:
        BallDraw = randint(1, BallPool)
        if BallDraw not in WinningNums:
            WinningNums.append(BallDraw)

    return WinningNums


# Draws the supplementary numbers from the pool
def DrawSupps(Drawn):
    Supps = []
    while len(Supps) < NumSupp:
        BallDraw = randint (1, BallPool)
        if (BallDraw not in Drawn) and (BallDraw not in Supps):
            Supps.append(BallDraw)
    return Supps


# Checks the player ticket against the winning numbers
# Oz Lotto offers 7 'divisions' or levels of prizes.
#
# Here is what you need to match in one game to win a prize:
#
# Division 1: All 7 main winning numbers
# Division 2: Any 6 main winning numbers and either supplementary number
# Division 3: Any 6 main winning numbers
# Division 4: Any 5 main winning numbers and either supplementary number
# Division 5: Any 5 main winning numbers
# Division 6: Any 4 main winning numbers
# Division 7: Any 3 main winning numbers and either supplementary number

def CheckTicket():
    WinnerTicker = 0
    SuppCatch = False
    for i in TicketNums:
        if TicketNums[i-1] in WinningNums:
            WinnerTicker += 1
        elif TicketNums[i-1] in SuppNums:
            SuppCatch = True
    if WinnerTicker == 7:
        return 1
    elif (WinnerTicker == 6) and (SuppCatch):
        return 2
    elif (WinnerTicker == 6):
        return 3
    elif (WinnerTicker == 5) and (SuppCatch):
        return 4
    elif (WinnerTicker == 5):
        return 5
    elif (WinnerTicker == 4):
        return 6
    elif (WinnerTicker == 3) and (SuppCatch):
        return 7
    else:
        # Every game that doesn't reach at least div 7
        #  is put into 0, the losers
        return 0

BallPool = 45
NumBalls = 7
NumSelected = 7
NumSupp = 2
WeekNum = 1
NumDivisions = 7
Victories = []
DivisionWon = 0

Victories += NumDivisions * [0]

TicketNums = PlayerInput()

while DivisionWon != 1:
    WinningNums = DrawWinners()
    SuppNums = DrawSupps(WinningNums)
    DivisionWon = CheckTicket()
    if DivisionWon > 0:
        Victories[DivisionWon - 1] += 1
    WeekNum += 1

print("You finally won Div 1!")
print("It only took " + str(WeekNum) + " weeks!")
print("That's equal to " + str(WeekNum * 7 / 365.25) + "  years!")
# Victories counts how many wins you've had in all the divisions.
print(Victories)
