import curses
import random
import numpy as np
from math import floor, ceil

hGrid = 3 
wGrid = 7
cHeight = 10*hGrid
cWidth = 10*wGrid

seed = ""
while True:    
    seed = input("Seed input (leave blank for random): ")
    if seed == "":
        random.seed(random.randint(-100000,100000))
        break
    if seed.isnumeric():
        random.seed(int(seed))
        break

def perlin(x,y):
    # return random.choice(["#","."]) # this is actually how noise works don't @ me
    return str(findGridSquare(x,y)[0])

def findGridSquare(x,y):
    x0 = floor(x/wGrid)
    y0 = floor(y/hGrid)
    x1 = ceil(x/wGrid)
    y1 = ceil(y/hGrid)
    return [x0,y0,x1,y1]

vMap = []
for y in range(hGrid):
    vMap.append([0] * wGrid)

for y in range(hGrid):
    for x in range(wGrid):
        vMap[y][x]=[random.random(), (random.randint(0,360)*np.pi/180)]

# using ASCII chars instead of pixels
maps = []
for y in range(cHeight):
    maps.append([0] * cWidth)
    for x in range(cWidth):
        maps[y][x] = perlin(x,y)

# just because i need this later and know how to do it...
def lerp(a0, a1, w):
    return (1.0 - w)*a0 + w*a1

# curses + display the scalar map
def main(stdscr):
    stdscr.clear()
    # prints the map
    for h in range(cHeight):
        for w in range (cWidth):
            stdscr.addstr(h, w, maps[h][w])

    stdscr.refresh()
    stdscr.getkey()

curses.wrapper(main)
