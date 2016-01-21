# Simple OzLotto Sim
# Ben Apacible

# This is a much more simple version of my OzLotto Sim

from random import *

chance_of_winning = 45379620
week_num = 1

while (randint(1, chance_of_winning) != 1):
    print("Week " + str(week_num))
    week_num += 1


print ("You won Div 1 after " + str(week_num) + " weeks")
