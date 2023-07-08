## setup
from pyfiglet import Figlet
figlet = Figlet()
from sys import argv
import random
from sys import exit

## get fonts
fonts = figlet.getFonts()

## set font from terminal (smshadow, odel_lak, fireing)
if len(argv) == 1:
    figlet.setFont(font = random.choice(fonts))

elif len(argv) == 3 and argv[1] == '-f' or '-- font':
    figlet.setFont(font = argv[2])

else:
    exit

## get input
n = input("Input: ")
print("Output:")
print(figlet.renderText(n))