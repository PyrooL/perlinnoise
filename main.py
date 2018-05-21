import curses
import random
import numpy as np
from math import floor, ceil, sqrt, atan

# perlin grid dimensions
hGrid = 3 
wGrid = 7
# character grid to display
cHeight = 10*hGrid
cWidth = 10*wGrid
vMap = []
cMap = []

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
    # dotGridGradient(findGridSquare(x,y))
    return random.choice(["#","."]) # this is actually how noise works don't @ me
    # return str(findGridSquare(x,y)[0])

def findGridSquare(x,y):
    # corner 0 being top left, 1 being bottom right
    x0 = floor(x/wGrid)
    y0 = floor(y/hGrid)
    x1 = ceil(x/wGrid)
    y1 = ceil(y/hGrid)
    return [x0,y0,x1,y1,x,y]

def dotGridGradient(nodes):
    top = nodes[1]
    bottom = nodes[3]
    left = nodes[0]
    right = nodes[2]
    cx = nodes[4]
    cy = nodes[5]
    # identifyig the four gradient vectors
    tlv = vMap[top][left]
    trv = vMap[top][right]
    blv = vMap[bottom][left]
    rv = vMap[bottom][right]
    # distance vectors, using pythagorean from each node to the point
    tld = [top*hGrid-cy,cx-left*wGrid]
    trd = [top*hGrid-cy,right*wGrid-cx]
    bld = [cy-bottom*hGrid,cx-left*wGrid]
    brd = [cy-bottom*hGrid,right*wGrid-cx]

def vGen():
    for y in range(hGrid):
        vMap.append([0] * wGrid)
    for y in range(hGrid):
        for x in range(wGrid):
            vMap[y][x]=[random.random(),random.random()]

def pCalc():
    for y in range(cHeight):
        cMap.append([0] * cWidth)
        for x in range(cWidth):
            cMap[y][x] = perlin(x,y)

def lerp(a0, a1, w):
    return (1.0 - w)*a0 + w*a1

vGen()
pCalc()

def main(stdscr):
    stdscr.clear()
    for h in range(cHeight):
        for w in range (cWidth):
            stdscr.addstr(h, w, cMap[h][w])
    stdscr.refresh()
    stdscr.getkey()

curses.wrapper(main)
