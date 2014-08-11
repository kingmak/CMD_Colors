# bad variable names, yea i know
from os import system

x = ['0', '1', '2', '3' ,'4', '5', '6', '7']
y = ['8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

while True:
    for _ in x:
        for __ in y:
            color = _ + __
            system('color ' + color)
            raw_input('Color is: ' + color + ' ')
            system('cls')
