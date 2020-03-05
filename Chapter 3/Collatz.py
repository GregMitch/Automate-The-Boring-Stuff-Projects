import sys

def collatz(number):
    if (number % 2 == 0):
        return(number // 2)
    else:
        return(3 * number + 1)
    
try:
    numPicked = int(input('Please enter a number: '))
except ValueError:
    print('Please use an integer value next time')
    sys.exit()

equalsOne = False
while(equalsOne != True):
    numPicked = collatz(numPicked)
    if(numPicked == 1):
        print(numPicked)
        equalsOne = True
    else:
        print(numPicked)
