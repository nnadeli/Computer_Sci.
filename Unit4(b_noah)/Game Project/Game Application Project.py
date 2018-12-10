# Snake
import random
import string
import tkinter
from tkinter import *

HEAD_CHARACTER = 'Ô'                        #Determines what the head of the snake is
FOOD_CHARACTERS = string.ascii_letters      #Font of writing in game

class Application:
    TITLE = 'Snake Game'                    #Title
    SIZE = 750, 500                         #Size of window

    def __init__(self, master):
        self.master = master
        self.head = None
        self.head_position = None
        self.segments = []
        self.segment_positions = []
        self.food = None
        self.food_position = None
        self.direction = None
        self.moved = True
        self.running = False
        self.init()

    def init(self):
        self.master.title(self.TITLE)
        self.canvas = tkinter.Canvas(self.master)
        self.canvas.grid(sticky = tkinter.NSEW)
        self.start_button = tkinter.Button(self.master, text = 'Start', command = self.on_start)
        self.start_button.grid(sticky = tkinter.EW)
        self.master.bind('<Up>', self.on_up)                    #Lines 33-36 determine controls
        self.master.bind('<Left>', self.on_left)
        self.master.bind('<Down>', self.on_down)
        self.master.bind('<Right>', self.on_right)
        self.master.columnconfigure(0, weight = 1)
        self.master.rowconfigure(0, weight = 1)
        self.master.resizable(width = False, height = False)
        self.master.geometry('%dx%d' % self.SIZE)

    def on_start(self):                                     #Determines start and stop button
        self.reset()
        if self.running:
            self.running = False
            self.start_button.configure(text = 'Start')
        else:
            self.running = True
            self.start_button.configure(text = 'Stop')
            self.start()

    def reset(self):
        self.segments.clear()
        self.segment_positions.clear()
        self.canvas.delete(tkinter.ALL)

    def start(self):
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        self.canvas.create_rectangle(10, 10, width-10, height-10, outline = 'red') #outline = 'red' added changes outline of box.
        self.direction = random.choice('<Up><Left><Down><Right>')
        head_position = [round(width // 2, -1), round(height // 2, -1)]
        self.head = self.canvas.create_text(tuple(head_position), text = HEAD_CHARACTER)
        self.head_position = head_position
        self.spawn_food()
        self.tick()

    def spawn_food(self):
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        positions = [tuple(self.head_position), self.food_position] + self.segment_positions
        position = (round(random.randint(20, width-20), -1), round(random.randint(20, height-20), -1))
        while position in positions:
            position = (round(random.randint(20, width-20), -1), round(random.randint(20, height-20), -1))
        character = '8'     #Determines what the snakes food is
        self.food = self.canvas.create_text(position, text = character)
        self.food_position = position
        self.food_character = character

    def tick(self):
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        previous_head_position = tuple(self.head_position)
        if self.direction == '<Up>':
            self.head_position[1] -= 10
        elif self.direction == '<Left>':
            self.head_position[0] -= 10
        elif self.direction == '<Down>':
            self.head_position[1] += 10
        elif self.direction == '<Right>':
            self.head_position[0] += 10
        head_position = tuple(self.head_position)
        if (self.head_position[0] < 10 or self.head_position[0] >= width-10 or
            self.head_position[1] < 10 or self.head_position[1] >= height-10 or
            any(segment_position == head_position for segment_position in self.segment_positions)):
            self.game_over()
            return
        if head_position == self.food_position:
            self.canvas.coords(self.food, previous_head_position)
            self.segments.append(self.food)
            self.segment_positions.append(previous_head_position)
            self.spawn_food()
        if self.segments:
            previous_position = previous_head_position
            for index, (segment, position) in enumerate(zip(self.segments, self.segment_positions)):
                self.canvas.coords(segment, previous_position)
                self.segment_positions[index] = previous_position
                previous_position = position
        self.canvas.coords(self.head, head_position)
        self.moved = True
        if self.running:
            self.canvas.after(100, self.tick)      #Determines the speed of the game. The higher the number, the slower it is.

    def game_over(self):
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        self.running = False
        self.start_button.configure(text = 'Start')
        score = len(self.segments) * 10
        self.canvas.create_text((round(width // 2, -1), round(height // 2, -1)), text = 'Game Over! Git gud for next time because your score was: %d' % score)
#Lines 122-140 make sure that you cannot move backwards.
    def on_up(self, event):
        if self.moved and not self.direction == '<Down>':
            self.direction = '<Up>'
            self.moved = False

    def on_down(self, event):
        if self.moved and not self.direction == '<Up>':
            self.direction = '<Down>'
            self.moved = False

    def on_left(self, event):
        if self.moved and not self.direction == '<Right>':
            self.direction = '<Left>'
            self.moved = False

    def on_right(self, event):
        if self.moved and not self.direction == '<Left>':
            self.direction = '<Right>'
            self.moved = False

def main():
    root = tkinter.Tk()
    Application(root)
    root.mainloop()

if __name__ == '__main__':
    main()
