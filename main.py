import curses
import random

seed = ""

while not seed.isnumeric():
    # seed = input("Seed input (leave blank for random): ")
    if seed == "":
        seed = str(random.randint(-100000,100000))
        print(seed)
        break

def noise(nx,ny):
    # lol figure perlin out
    return "#"

height = 20
width = 40

maps = []

for y in range(height):
    maps.append([0] * width)
    for x in range(width):
        nx = x/width - 0.5
        ny = y/height - 0.5
        maps[y][x] = noise(nx,ny)

def main(stdscr):
    stdscr.clear()
    for h in range(height):
        for w in range (width):
            stdscr.addstr(h, w, maps[h][w])
    stdscr.refresh()
    stdscr.getkey()

curses.wrapper(main)
