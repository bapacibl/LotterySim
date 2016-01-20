# Simple OzLotto Sim
# Ben Apacible

# This is a much more simple version of my OzLotto Sim

from random import *

chanceOfWinning = 45379620
weekNum = 1

while (randint(1, chanceOfWinning) != 1):
    print("Week " + str(weekNum))
    weekNum += 1


print ("You won Div 1 after " + str(weekNum) + " weeks")
