import curses
import random
import numpy as np

hGrid = 3 
wGrid = 8 
height = 10*hGrid
width = 10*wGrid

# for future seeding, currently does nothing
seed = ""

while not seed.isnumeric():
    seed = input("Seed input (leave blank for random): ")
    if seed == "":
        seed = str(random.randint(-100000,100000))
        print(seed)
        break

def perlin(x,y):
    return random.choice(["#","."]) # this is actually how noise works don't @ me

vMap = []
for y in range(hGrid):
    vMap.append([0] * wGrid)

for y in range(hGrid):
    for x in range(wGrid):
        vMap[y][x]=[random.random(), (random.randint(0,360)*np.pi/180)]

# using ASCII chars instead of pixels
maps = []
for y in range(height):
    maps.append([0] * width)
    for x in range(width):
        nx = x/width - 0.5
        ny = y/height - 0.5
        maps[y][x] = perlin(nx,ny)

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
