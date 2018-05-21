import curses
import random
import numpy as np
from math import floor, ceil, sqrt, atan

# grid dimensions
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
    dots = dotGridGradient(findGridSquare(x,y))
    g1 = dots[0]
    g2 = dots[1]
    g3 = dots[2]
    g4 = dots[3]
    u = dots[4]
    v = dots[5]
    p1 = lerp(g1,g2,u)
    p2 = lerp(g3,g4,u)
    avg = lerp(p1,p2,v)
    # return random.choice(["#","."]) # this is actually how noise works don't @ me
    return str(round(avg*10))

def findGridSquare(x,y):
    # corner 0 being top left, 1 being bottom right
    x0 = floor(x/(cWidth/wGrid))
    y0 = floor(y/(cHeight/hGrid))
    x1 = ceil(x/(cWidth/wGrid))
    y1 = ceil(y/(cHeight/hGrid))
    return [x0,y0,x1,y1,x,y]

def dotGridGradient(nodes):
    left = nodes[0]
    top = nodes[1]
    right = nodes[2]
    bottom = nodes[3]   
    cx = nodes[4]
    cy = nodes[5]
    # identifyig the four gradient vectors
    tlv = vMap[top][left]
    trv = vMap[top][right]
    blv = vMap[bottom][left]
    brv = vMap[bottom][right]
    # distance vectors
    tld = [top*hGrid-cy,cx-left*wGrid]
    trd = [top*hGrid-cy,right*wGrid-cx]
    bld = [cy-bottom*hGrid,cx-left*wGrid]
    brd = [cy-bottom*hGrid,right*wGrid-cx]
    # dot products wew
    tldot = tlv[0]*tld[0]+tlv[1]*tld[1]
    trdot = trv[0]*trd[0]+trv[1]*trd[1]
    bldot = blv[0]*bld[0]+blv[1]*bld[1]
    brdot = brv[0]*brd[0]+brv[1]*brd[1]
    return [tldot,trdot,bldot,brdot,cx-left*wGrid,top*hGrid-cy]

def vGen():
    for y in range(hGrid+1):
        vMap.append([0] * (wGrid+1))
    for y in range(hGrid+1):
        for x in range(wGrid+1):
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
