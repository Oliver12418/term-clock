# Imports
from time import time, ctime, sleep
import os
import argparse
parser = argparse.ArgumentParser(description="A clock for your terminal")
parser.add_argument("-b", "--blinking", action="store_true", help="Makes the colon blink")
parser.add_argument("-c", "--center", action="store_true", help="Centers the clock")
args = parser.parse_args()
h = (int(ctime(time())[11:13])%12)
m = int(ctime(time())[14:16])
s = int(ctime(time())[17:19])
date = f"{' '.join(ctime(time())[0:10].split())} {ctime(time())[20:24]}"
centerd = args.center # Check if centering is enabled
blinking = args.blinking
Numbers = [

    # ASCII art for numbers 0 to 9

    "\n".join([
        " /\"\\ ",
        " | | ",
        " \\_/ "
    ]),

    "\n".join([
        " /|  ",
        "  |  ",
        "  |  "
    ]),

    "\n".join([
        " /\"\\ ",
        "   / ",
        " /__ "
    ]),

    "\n".join([
        " /\"\\ ",
        "  -< ",
        " \\_/ "
    ]),

    "\n".join([
        " /\"| ",
        "'--|-",
        "   | "
    ]),

    "\n".join([
        " |\"\" ",
        " '\"\\ ",
        " \\_/ "
    ]),

    "\n".join([
        " /\"\\ ",
        " |/\\ ",
        " \\_/ "
    ]),

    "\n".join([
        " \"\"/ ",
        "  /  ",
        " /   "
    ]),

    "\n".join([
        " /\"\\ ",
        " >-< ",
        " \\_/ "
    ]),

    "\n".join([
        " /\"\\ ",
        " \\/| ",
        "  _/ "
    ])

]

nl="\n"
n=1

print(f"{h}:{m}:{s}")
print("\x1b[2J")
Numbers[int(str(m)[0])].split(nl)[0]
while True:
    if blinking:
        n+=1
    print("\x1b[0;0H")
    h = int(ctime(time())[11:13]) % 12                                       # Hours
    m = int(ctime(time())[14:16])                                            # Minutes
    s = int(ctime(time())[17:19])                                            # Seconds
    date = f"{' '.join(ctime(time())[0:10].split())} {ctime(time())[20:24]}" # The date

    terminal_width, terminal_height = os.get_terminal_size()
    vertical_center = (terminal_height - 4) // 2  # Adjust for 4 lines of output
    if centerd:
        print(f"{nl*(vertical_center-4)}")  # Move cursor to vertical center

    output_lines = [
        # Magical shit only god understands
        f"{Numbers[int(f'{str(h):0>2}'[0])].split(nl)[0]}{Numbers[int(f'{str(h):0>2}'[1])].split(nl)[0]} {'<>'*(n%2)+'  '*((n+1)%2)} {Numbers[int(f'{str(m):0<2}'[0])].split(nl)[0]}{Numbers[int(f'{str(m):0<2}'[1])].split(nl)[0]}   ",
        f"{Numbers[int(f'{str(h):0>2}'[0])].split(nl)[1]}{Numbers[int(f'{str(h):0>2}'[1])].split(nl)[1]}    {Numbers[int(f'{str(m):0<2}'[0])].split(nl)[1]}{Numbers[int(f'{str(m):0<2}'[1])].split(nl)[1]}   ",
        f"{Numbers[int(f'{str(h):0>2}'[0])].split(nl)[2]}{Numbers[int(f'{str(h):0>2}'[1])].split(nl)[2]} {'<>'*(n%2)+'  '*((n+1)%2)} {Numbers[int(f'{str(m):0<2}'[0])].split(nl)[2]}{Numbers[int(f'{str(m):0<2}'[1])].split(nl)[2]}.{str(s):0>2}",
        f"{str(date):^28}   "
    ]

    for line in output_lines:
        if centerd:
            padding = (terminal_width - len(line)) // 2
        else:
            padding=0
        print(f"\033[1m{' ' * padding + line}\033[0m")  # Center horizontally

    sleep(1)
