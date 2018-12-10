# Connect 4 Game

from tkinter import *
from tkinter import font

class Info(Frame):
    def __init__(self, master = None):
        Frame.__init__(self)
        self.configure(width = 500, height = 100)
        police = font.Font(self, size = 20, family = 'Helvetica')
        self.t = Label(self, text = 'Blue Player Turn', font = police)
        self.t.grid(sticky = NSEW, pady = 20)

class Piont(object):
    def __init__(self, x, y, can, colour = 'white', bg = 'green'):
        self.can = can
        self.x = x
        self.y = y
        self.colour = colour
        self.tour = 1
        self.r = 60
        self.piont = self.can.create_oval(self.x + 10, self.y + 10, self.x + 61, self.y + 61, fill = colour, outline = 'orange')

    def changeColour(self, colour):
        self.can.itemconfigure(self.piont, fill = colour)
        self.colour = colour

class Terrain(Canvas):
    def __init__(self, master = None):
        Canvas.__init__(self)
        self.configure(width = 500, height = 400, bg = 'orange')
        self.player = 1
        self.colour = 'blue'
        self.p = []
        self.perm = True
        for i in range(0, 340, int(400/6)):
            liste_rangee = []
            for j in range(0, 440, int(500/7)):
                liste_rangee.append(Piont(j, i ,self))
            self.p.append(liste_rangee)
        self.bind('<Button-1>', self.detCol)

    def detCol(self, event):
        if self.perm:
            col = int(event.x/71)
            lig = 0
            lig = 0
            while lig < len(self.p):
                if self.p[0][col].colour == 'green' or self.p[0][0].colour == 'blue':
                    break
                if self.p[lig][col].colour == 'green' or self.p[lig][col].colour == 'blue':
                    self.p[lig-1][col].changeColour(self.colour)
                    break
                elif lig == len(self.p)-1:
                    self.p[lig][col].changeColour(self.colour)
                    break
                if self.p[lig][col].colour != 'green' and self.p[lig][col].colour != 'blue':
                    lig+=1
            if self.player == 1:
                self.player = 2
                info.t.config(text = 'Green Player Turn')
                self.colour = 'green'
            elif self.player == 2:
                self.player = 1
                info.t.config(text = 'Blue Player Turn')
                self.colour = 'blue'
            self.Horizontal()
            self.Vertical()
            self.Diagonal1()
            self.Diagonal2()

    def Horizontal(self):
        i = 0
        while(i < len(self.p)):
            j = 0
            while(j < 3):
                if(self.p[i][j].colour == self.p[i][j+1].colour == self.p[i][j+2].colour == self.p[i][j+3].colour == 'green'):
                    info.t.config(text = 'Green Player Wins!')
                    self.perm = False
                    break
                elif(self.p[i][j].colour == self.p[i][j+1].colour == self.p[i][j+2].colour == self.p[i][j+3].colour == 'blue'):
                    info.t.config(text = 'Blue Player Wins!')
                    self.perm = False
                    break
                j +=1
            i += 1

    def Vertical(self):
        i = 0
        while(i < 3):
            j = 0
            while(j < len(self.p[i])):
                if(self.p[i][j].colour == self.p[i+1][j].colour == self.p[i+2][j].colour == self.p[i+3][j].colour == 'green'):
                    info.t.config(text = 'Green Player Wins!')
                    self.perm = False
                    break
                elif(self.p[i][j].colour == self.p[i+1][j].colour == self.p[i+2][j].colour == self.p[i+3][j].colour == 'blue'):
                    info.t.config(text = 'Blue Player Wins!')
                    self.perm = False
                    break
                j+=1
            i+=1

    def Diagonal1(self):
        i = 0
        while(i < 3):
            j = 0
            while(j < 3):
                if(self.p[i][j].colour == self.p[i+1][j+1].colour == self.p[i+2][j+2].colour == self.p[i+3][j+3].colour == 'green'):
                    info.t.config(text = 'Green Player Wins!')
                    self.perm = False
                    break
                elif(self.p[i][j].colour == self.p[i+1][j+1].colour == self.p[i+2][j+2].colour == self.p[i+3][j+3].colour == 'blue'):
                    info.t.config(text = 'Blue Player Wins!')
                    self.perm = False
                    break
                j += 1
            i += 1

    def Diagonal2(self):
        i = 0
        while(i < 3):
            j = len(self.p[i])-1
            while(j > len(self.p)-4):
                if(self.p[i][j].colour == self.p[i+1][j-1].colour == self.p[i+2][j-2].colour == self.p[i+3][j-3].colour == 'green'):
                    info.t.config(text = 'Green Player Wins!')
                    self.perm = False
                    break
                elif(self.p[i][j].colour == self.p[i+1][j-1].colour == self.p[i+2][j-2].colour == self.p[i+3][j-3].colour == 'blue'):
                    info.t.config(text = 'Blue Player Wins!')
                    self.perm = False
                    break
                j -= 1
            i += 1



root = Tk()
root.geometry('500x550')
root.title('Connect Four Game')

info = Info(root)
info.grid(row = 0, column = 0)


t = Terrain(root)
t.grid(row = 1, column = 0)

def rein():
    global info
    info.t.config(text = '')

    info = Info(root)
    info.grid(row = 0, column = 0)

    t = Terrain(root)
    t.grid(row = 1, column = 0)

Button(root, text = 'Reinitialize', command = rein).grid(row = 2, column = 0, pady = 30)

root.mainloop()
#https://stackoverflow.com/questions/16256010/python-connect-4-with-tkinter?answertab=oldest#tab-top
#https://github.com/romainvause/Connect4/blob/master/connect4_Tk.py
