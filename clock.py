from time import time, ctime, sleep
h = (int(ctime(time())[11:13])%12)
m = int(ctime(time())[14:16])
s = int(ctime(time())[17:19])
date = f"{' '.join(ctime(time())[0:10].split())} {ctime(time())[20:24]}"

Numbers = [

    "\n".join([
        " /\"\\ ",
        " | | ",
        " \\_/ "
    ]),

    "\n".join([
        " /|  ",
        "  |  ",
        " _|_ "
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
        "'\"\"| ",
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

print(f"{h}:{m}:{s}")
print("\x1b[2J")
Numbers[int(str(m)[0])].split(nl)[0]
while True:
    print("\x1b[0;0H")
    h = int(ctime(time())[11:13])%12
    m = int(ctime(time())[14:16])
    s = int(ctime(time())[17:19])
    print(f"{Numbers[int(f'{str(h):0>2}'[0])].split(nl)[0]}{Numbers[int(f'{str(h):0>2}'[1])].split(nl)[0]} <> {Numbers[int(f'{str(m):0<2}'[0])].split(nl)[0]}{Numbers[int(f'{str(m):0<2}'[1])].split(nl)[0]}")
    print(f"{Numbers[int(f'{str(h):0>2}'[0])].split(nl)[1]}{Numbers[int(f'{str(h):0>2}'[1])].split(nl)[1]}    {Numbers[int(f'{str(m):0<2}'[0])].split(nl)[1]}{Numbers[int(f'{str(m):0<2}'[1])].split(nl)[1]}")
    print(f"{Numbers[int(f'{str(h):0>2}'[0])].split(nl)[2]}{Numbers[int(f'{str(h):0>2}'[1])].split(nl)[2]} <> {Numbers[int(f'{str(m):0<2}'[0])].split(nl)[2]}{Numbers[int(f'{str(m):0<2}'[1])].split(nl)[2]}.{str(s):0>2}")
    print(f"{str(date):^28}")
    sleep(1)
