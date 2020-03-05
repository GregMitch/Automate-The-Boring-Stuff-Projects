"""
My solution does not use 'H' or 'T' values in the list
Instead it just uses int value 1s and 0s to represent heads and tails
Also made program a function so it is easy to call from shell
"""
import random

def coin_flips():
    numberOfStreaks = 0

    for experimentNumber in range(10000):
        # Code that creates a list of 100 'heads' or 'tails' values.
        flips = []
        for i in range(100):
            flips.append(random.randint(0,1))
    
        """
        Code that checks if there is a streak of 6 heads or tails in a row.
        Since we are only counting streaks in general, my program just checks
        to see if future values are the same as the present value.
        (Basically it does not keep track of heads streaks vs tail streaks)
        """
        consecutiveValues = 0
        for j in range(len(flips) - 1):
            if(flips[j] == flips[j + 1]):
                consecutiveValues += 1
            else:
                consecutiveValues = 0

            if(consecutiveValues == 6):
                numberOfStreaks += 1

    return('Chance of streak: %s%%' % (numberOfStreaks / 100))
