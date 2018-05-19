import curses
import random
from math import pi
import numpy as np

height = 30
width = 70

# for future seeding, currently does nothing
seed = ""

while not seed.isnumeric():
    # seed = input("Seed input (leave blank for random): ")
    if seed == "":
        seed = str(random.randint(-100000,100000))
        print(seed)
        break

# to fill in with perlin calculations
def noise(nx,ny):
    return random.choice(["#","."]) # this is actually how noise works don't @ me

# defining the vector map?
vMap = []
for y in range(height):
    vMap.append([0] * width)

for y in range(height):
    for x in range(width):
        vMap[y][x]=[random.random(), (random.randint(0,360)*np.pi/180)]

# defining a 2d matrix of scalars, which then gets filled in with randomly either a # or a .
maps = []

for y in range(height):
    maps.append([0] * width)
    for x in range(width):
        nx = x/width - 0.5
        ny = y/height - 0.5
        maps[y][x] = noise(nx,ny)

# just because i need this later and know how to do it...
def lerp(a0, a1, w):
    return (1.0 - w)*a0 + w*a1

# curses + display the scalar map
def main(stdscr):
    stdscr.clear()

    # prints the map
    for h in range(height):
        for w in range (width):
            stdscr.addstr(h, w, maps[h][w])

    stdscr.refresh()
    stdscr.getkey()

curses.wrapper(main)
