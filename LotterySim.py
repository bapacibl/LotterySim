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
def player_input():
    ticket_nums = []
    num_left = num_balls
    while len(ticket_nums) < num_balls:
        selected = input("Pick a number from 1-45: ")
        if (int(selected) not in ticket_nums) and (1 <= int(selected) <= 45):
            ticket_nums.append(int(selected))
            num_left -= 1
        elif (int(selected) in ticket_nums):
            print("You have already selected this number, try again")
        elif not((1 <= int(selected) <= 45)):
            print("This number is not between 1 and 45")
        print(str(num_left) + " Balls left to choose.")
    return ticket_nums


# Draws the winning numbers out of the pool
def draw_winners():
    winning_nums = []
    while len(winning_nums) < num_selected:
        ball_draw = randint(1, ball_pool)
        if ball_draw not in winning_nums:
            winning_nums.append(ball_draw)

    return winning_nums


# Draws the supplementary numbers from the pool
def draw_supps():
    supps = []
    while len(supps) < num_supp:
        ball_draw = randint(1, ball_pool)
        if (ball_draw not in winning_nums) and (ball_draw not in supps):
            supps.append(ball_draw)
    return supps


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

def check_ticket():
    counter = 0
    winner_ticker = 0
    supp_catch = False
    while counter < len(ticket_nums):
        if ticket_nums[counter] in winning_nums:
            winner_ticker += 1
        elif ticket_nums[counter] in supp_nums:
            supp_catch = True
        counter += 1


    if winner_ticker == 7:
        return 1
    elif (winner_ticker == 6) and (supp_catch):
        return 2
    elif (winner_ticker == 6):
        return 3
    elif (winner_ticker == 5) and (supp_catch):
        return 4
    elif (winner_ticker == 5):
        return 5
    elif (winner_ticker == 4):
        return 6
    elif (winner_ticker == 3) and (supp_catch):
        return 7
    else:
        # Every game that doesn't reach at least div 7
        #  is put into 0, the losers
        return 0

ball_pool = 45
num_balls = 7
num_selected = 7
num_supp = 2
week_num = 1
num_divisions = 7
victories = []
divisionWon = 0

victories += num_divisions * [0]

ticket_nums = player_input()

while divisionWon != 1:
    winning_nums = draw_winners()
    supp_nums = draw_supps()
    division_won = check_ticket()
    if division_won > 0:
        victories[division_won - 1] += 1
    week_num += 1

    print 'Week {0:7} | {1:28} | {2:8} | {3:25}'.format(week_num, winning_nums, supp_nums, victories)

print("You finally won Div 1!")
print("It only took " + str(week_num) + " weeks!")
print("That's equal to " + str(week_num * 7 / 365.25) + "  years!")
print(victories)
