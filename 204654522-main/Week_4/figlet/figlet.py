from pyfiglet import Figlet
import random, sys

figlet = Figlet()

if len(sys.argv) == 0:
    sys.exit("Invalid input. Try again.")

if len(sys.argv) < 2:
    f = random.choice(figlet.getFonts())
    figlet.setFont(font=f)

elif len(sys.argv) < 4 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    f = sys.argv[2]
    figlet.setFont(font=f)

else:
    sys.exit("Invalid input. Try again.")

if f in figlet.getFonts():
    figlet.setFont(font=sys.argv[2])
    inp = input("Input: ")
    print("Output:", figlet.renderText(inp))
else:
    sys.exit("Invalid input. Try again.")
