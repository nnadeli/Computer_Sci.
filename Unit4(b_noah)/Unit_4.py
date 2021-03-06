''' Day 1       November 14'''

#To find a file and use it somewhere
#Type 'ls' in terminal
#Type the folder by typing 'cd' then folder
#When you find the file, type    python3 'name of file'
#Must be .py file
#'r' means read, 'w' means write, 'a' means append a str to end of .txt file

f = open('sampletext.txt', 'r')
x = f.readlines()
for line in x:
    print('Line! :',line)
    print(line.replace(',no','ABSOLUTELY NOT'))
    print(line.split(' ')[1].split(':'))



'''Day 2       November 15'''

print('Script Starting')
f = open('sampletext.txt', 'r+w+a')
f.readlines()
f.write('This line is added to the file')
f.append(str(x))
print('Script Ending')

#to remove files from os permanently
import os
try:
    os.remove('sampletext.txt')
except OSError:
    print('Can not find file')

#Deleting folders
import os
try:
    os.remove('Faketext.txt')
except OSError:
    print('Can not find file')
for x in os.listdir('Folder to remove'):
    os.remove('Folder to remove'+g)
os.rmdir('Folder to remove')

f = open('sampletext.txt', 'w')
for x in range(0,10):
    f.write(str(x))
    f.write('\n')


'''Day 3        November 19'''

#To make a new text file:                           x = open('name of new file.txt', 'w')
#To open a text file in the following modes:        x = open('already exiting file.txt', 'r+a+w')
#Read a text file and make string manipulations:    text = x.read()
#Convert things in a text file:                     x = text.upper()    x = text.upper()    x = text.count('a') x = text.replace('a','$')
#Write in a newly created text file:                x.write('The file will contain this')   In 'w' mode
#Append the end of a text text file:                x.write('this is added to the end')     In 'a' mode
#Close the document                                 x.close()
#This line is a comment

f = open('surprisedpikachu.txt', 'w')
f.close()
f = open('surprisedpikachu.txt', 'a')
f.write('this aint it chief')
f.close()
f = open('surprisedpikachu.txt', 'r')
text = f.read()
f.close()
f = open('text999.txt', 'w')
newtext = text.replace('s', '$')
f.write(newtext)
f.close()


'''Day 4        November 22'''
import matplotlib
import matplotlib.pyplot
matplotlib.pyplot.plot([1,2,3,4])
matplotlib.pyplot.ylabel('some numbers')
matplotlib.pyplot.show()

import matplotlib
import numpy
import matplotlib.pyplot
x = numpy.arange(0, 5, 0.1)
y = numpy.sin(x)
matplotlib.pyplot.plot(x, y)
matplotlib.pyplot.show()

import matplotlib
import matplotlib.pyplot
import numpy                                        # similar to the math module
def f(t):
    s1 = numpy.cos(2 * numpy.pi * t)
    e1 = numpy.exp(-t)
    return s1 * e1
t1 = numpy.arange(0.0, 5.0, .2)
l = matplotlib.pyplot.plot(t1, f(t1), 'ro')
matplotlib.pyplot.setp(l, markersize=10)
matplotlib.pyplot.setp(l, markerfacecolor='red')
matplotlib.pyplot.show()

import matplotlib.pyplot
import math
x=[]
y=[]
for i in range(360):
    x.append(i)
for j in range(360):
    y.append(math.cos(j*3.1415/180))
matplotlib.pyplot.plot(x,y, label='y=cos(x)')
matplotlib.pyplot.title('Cosine graph')
matplotlib.pyplot.ylabel('y value')
matplotlib.pyplot.xlabel('x value')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
# same example below, but with bar instead of plot and range to 45 degrees
import matplotlib
import pyplot
import math
x=[]
y=[]
for i in range(45):
    x.append(i)
for j in range(45):
    y.append(math.cos(j*3.1415/180))
matplotlib.pyplot.bar(x,y, label='y=cos(x)')
matplotlib.pyplot.title('Cosine graph')
matplotlib.pyplot.ylabel('y value')
matplotlib.pyplot.xlabel('x value')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()

import matplotlib.pyplot
import numpy
t = numpy.arange(0., 5., 0.2)   # evenly sampled time at 200ms intervals
matplotlib.pyplot.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, ‘g^')
# straight line red dash
# quadratic blue square
# cubic green triangles
matplotlib.pyplot.show()

#extra
import matplotlib
import matplotlib.pyplot
import numpy

t1 = numpy.arange(0.0, 5.0, .2)
l = matplotlib.pyplot.plot(t1, t1**2)
#x formula for y
matplotlib.pyplot.show()


#.plot is scatter or line graph
#.bar is a bar graph

'''Day 5        Nov 26'''

import matplotlib
import matplotlib.pyplot
import numpy

t1 = numpy.arange(0.0, 10.0, .2)
l = matplotlib.pyplot.plot(t1, t1**-2, label = 'LABEL GOES HERE')
matplotlib.pyplot.title('THIS IS THE TITLE')
matplotlib.pyplot.ylabel('Y AXIS LABEL')
matplotlib.pyplot.xlabel('X AXIS LABEL')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()

'''
Bar/Column Charts

Comparison between items or individual data at specific times
Stacked bar chart shows relationship of individual items to a whole picture.


Pie Charts

Place emphasis on an item.
General rule: For 7 or less portions.


Line Charts

Show trends


Scatter Charts

Show uneven intervals or data clusters.
'''


'''Day 6        Dec 3'''

from tkinter import *
import tkinter
root = Tk() # initialize base window
root.geometry('300x300') # dimensions of window
root.title('My first Tkinter project')
#adds a title to the root window
l=Label(root, text = 'Hello World') # create label
l.pack(side = TOP) # places label object in root window
root.mainloop() # holds view in place

from tkinter import *
import tkinter
root = Tk() # initialize base window
root.geometry('300x300') # dimensions of window
def buttonFunction():
    print('Hello World!')
b1 = Button(root, text = 'Click me!', command = buttonFunction)
# create button
b1.pack(side = LEFT) # places button object in root window
b2 = Button(root, text = 'Click me!', command = buttonFunction)
# create button
b2.pack(side = RIGHT) # places button object in root window
root.mainloop() # holds view in place

from tkinter import *
import tkinter
def hello():
    print('Hello!')
def goodbye():
    print('Goodbye!')
root = Tk() # initialize base window
root.geometry('300x300') # dimensions of window
menubutton = Menubutton(root, text = 'this is a menu') #create
menubutton.menu = Menu(menubutton) #initialize menu
menubutton['Menu'] = menubutton.menu #associates menubutton with
menubutton.menu.add_command(label = 'option1', command = hello)
menubutton.menu.add_command(label = 'option2', command = goodbye)
menubutton.pack()
root.mainloop() # holds view in place

from tkinter import *
import tkinter
root = Tk() # initialize base window
root.geometry('300x300') # dimensions of window
v=tkinter.IntVar()
radioButton1 = Radiobutton(root, variable = v, value = 0, text = 'It is good', command = lambda : print(v.get()))
radioButton2 = Radiobutton(root, variable = v, value = 1, text = 'It is good', command = lambda : print(v.get()))
radioButton1.pack()
radioButton2.pack()
root.mainloop() # holds view in place


'''Day 7        Dec 6'''
sudo install pygame
import pygame
pygame.init()
(6, 0)
pygame.mixer.music.load('1114.wav')
pygame.mixer.music.play(0)
pygame.mixer.music.play(10)
pygame.mixer.music.load('0999.wav')
pygame.mixer.music.play(0)
