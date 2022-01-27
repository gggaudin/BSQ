import tkinter
from tkinter import *
from PIL import Image, ImageTk
import random

fenetre = Tk()
fenetre.configure(background='black')
fenetre.title('BSQ')
circle = Image.open("src/CircleW.png")
circleGreen = Image.open("src/CircleG.png")
circleRed = Image.open("src/CircleR.png")
square = Image.open("src/SquareW.png")
squareGreen = Image.open("src/SquareG.png")
squareRed = Image.open("src/SquareR.png")
xRed = Image.open("src/CrossR.png")
xGreen = Image.open("src/CrossG.png")
circleW = ImageTk.PhotoImage(circle)
squareW = ImageTk.PhotoImage(square)
squareG = ImageTk.PhotoImage(squareGreen)
circleG = ImageTk.PhotoImage(circleGreen)
circleR = ImageTk.PhotoImage(circleRed)
squareR = ImageTk.PhotoImage(squareRed)
xR = ImageTk.PhotoImage(xRed)
xG = ImageTk.PhotoImage(xGreen)

def putPic(pic, pixX, pixY):
    label = tkinter.Label(image=pic, borderwidth=0, highlightthickness=0)
    label.image = pic
    label.place(x=(pixX*20), y=(pixY*20))

def main():
    numFile = random.randint(1, 40)
    def resolve(x, y, new):
        new_pic = circleR if (new[y][x] == 'o') else (xG if (new[y][x] == 'X') else squareR)
        putPic(new_pic, x, y)
        x += 1
        if x >= len(new[y]):
            x = 0
            y += 1
        if (y < len(new) and x < len(new[y])):
            fenetre.after(1, resolve, x, y, puzzle)

    def buildMap(puzzle, maxLen):
        line = 0 
        while line < maxLen["len"]:
            col = 0
            while col < maxLen["len"]:
                puzzle[maxLen["startY"]+line][maxLen["startX"]+col] = 'X'
                col += 1
            line += 1
        return puzzle

    def checkSqr(puzzle, lenSqr, start, h, w):
        x = start[1]
        y = start[0]
        round = 0
        while round <= lenSqr:
            if ((x + lenSqr) < w) and y < h:
                if (puzzle[y][x+lenSqr] != 'o'):
                    y += 1
                else:
                    return False
            else:
                return False
            round += 1
        y -= 1
        round = 0
        while (round <= lenSqr):
            if (x + round) < w:
                if (puzzle[y][x+round] != 'o'):
                    round += 1
                else:
                    return False
            else:
                return False
        return True
    f = open("maps/map_"+str(numFile), "r")
    i = 0
    height = 0
    width = 0
    puzzle = []
    for x in f:
        if i > 0:
            curr = list(x)
            curr.pop()
            puzzle.append(curr)
        i += 1
    height = i -1
    width = len(puzzle[0])
    fenetre.geometry(str((width*20)+200)+"x"+str(height*20))
    px = 0
    py = 0
    labelTab = []
    for line in puzzle:
        px = 0
        for col in line:
            if col == 'o':
                curr = circleW
            else:
                curr = squareW
            label1 = tkinter.Label(image=curr, borderwidth=0, highlightthickness=0)
            label1.image = curr
            label1.place(x=px, y=py)
            labelTab.append(label1)
            px += 20
        py += 20
    start = [0 ,0]
    lenSqr = 0
    finalSqr = []
    while (start[0] < height) and (start[1]< width):
        while checkSqr(puzzle, lenSqr, start, height, width):
            lenSqr += 1
        if lenSqr > 0:
            finalSqr.append({"startX":start[1],"startY":start[0], "len":lenSqr, "fact": (start[0]+start[1])})
        lenSqr = 0
        start[1] += 1
        if start[1] >= width:
            start[0] += 1
            start[1] = 0
    maxLen = max(finalSqr, key=lambda x:x['len'])
    puzzle = buildMap(puzzle, maxLen)
    btnResolve = Button(fenetre, text = 'Resolve', bg='black', borderwidth=0, highlightthickness=0, highlightbackground='black', command= lambda: resolve(0,0,puzzle))
    btnResolve.place(x=(((width*20)+200)-135), y=20)
    btnChangeMap = Button(fenetre, text = 'ChangeMap', bg='black', borderwidth=0, highlightthickness=0, highlightbackground='black', command= lambda: main())
    btnChangeMap.place(x=(((width*20)+200)-147), y=60)
    btnQuit = Button(fenetre, text = 'Quit', bg='black', borderwidth=0, highlightthickness=0, highlightbackground='black', command=fenetre.destroy)
    btnQuit.place(x=(((width*20)+200)-125), y=100)
    fenetre.mainloop()

main()