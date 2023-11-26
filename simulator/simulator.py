# ---------------------------------------------------------------------------- #
#                         A simulator for the L3D Cube                         #
# ---------------------------------------------------------------------------- #

# importing required libraries
from tkinter import * 
import tkinter.font as font
#from math import *
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
import matplotlib.pyplot as plt
import numpy as np

# --------------------------------- Classes & Functions -------------------------------- #
class Frame:
    def __init__(self,values=None):
        global anim
        global frames
        if values is None:
            values = {}
            for i in range(8):
                for j in range(8):
                    for k in range(8):
                        values[(i,j,k)] = "grey"
        self.values = values

# Add a frame to the animation
def add_frame():
    global anim
    global frames
    global current_frame
    global button_light_anim

    # Create frame
    frame = Frame()
    button_light_frame = Frame()
    
    #add to animation
    anim.append(frame.values)
    button_light_anim.append(button_light_frame.values)

    #Update slider range
    frames +=1
    slider.configure(from_=0, to=frames-1)

    #move to new frame
    current_frame = frames-1
    slider.set(frames-1)

    refresh()

# Draw frame on matplotlib plot
def draw_frame(frame,plot):
    global x_list
    global y_list
    global z_list

    colour_list=[*frame.values()]

    plot.scatter3D(x_list, y_list, z_list, color=colour_list, alpha=0.75)

    #update button colours
    h=0
    for x in range(8):
        for y in range(8):
            for z in range(8):
                button_canvas.itemconfig(light_squares[x][abs(y-7)][z], fill=colour_list[h])
                h+=1

    #print(len(light_squares))

# Change brush colours
def changeBrushRed():
    global brush
    brush = "red"

def changeBrushGreen():
    global brush
    brush = "green"

def changeBrushBlue():
    global brush
    brush = "blue"

def changeBrushErase():
    global brush
    brush = "grey"

def printcoord(event):
    x1 = int(event.x/15)
    y1 = int(event.y/15)
    z1 = int(x1/8) + (4* int(y1/8))

    x1 = x1%8
    y1 = y1%8

    if (x1>0):
        x1-=1 
    print(x1,y1,z1)
    return
    
# Function to change colour of dot
def changeColour(event):
    global anim, current_frame, plot

    frame = anim[current_frame]

    x1 = int(event.x/15)
    y1 = int(event.y/15)

    if 0<=x1<=7:
        if 0<=y1<=7:
            z1 = 0
        else:
            y1-=9
            z1=4

    elif 9<=x1<=16:
        x1-=9
        if 0<=y1<=7:
            z1 = 1

        else:
            y1-=9
            z1=5

    elif 18<=x1<=25:
        x1-=18
        if 0<=y1<=7:
            z1 = 2

        else:
            y1-=9
            z1=6
    
    else:
        x1-=27
        if 0<=y1<=7:
            z1 = 3

        else:
            y1-=9
            z1=7
    
    #if button is already desired colour, ignore
    if frame[(x1,abs(y1-7),z1)] == brush:
        return
    #else set to correct colour
    else:
        frame[(x1,abs(y1-7),z1)] = brush
        if brush=="grey":
            button_canvas.itemconfig(light_squares[x1][abs(y1)][z1], fill="white")
        else:
            button_canvas.itemconfig(light_squares[x1][abs(y1)][z1], fill=brush)

    refresh()

   # print("x: ",x1," y: ",y1," z: ",z1," colour: ",frame[(x1,y1,z1)])
    print("x: ",x1," y: ",y1,"z: ",z1)
    return

def move_frame(event):
    global current_frame
    global slider
    global plot
    current_frame = slider.get()

    refresh()
    refresh_buttons()

def refresh():
    plot.cla()
    draw_frame(anim[current_frame],plot)
    canvas.draw()

def refresh_buttons():
    for x in range(8):
        for y in range(8):
            for z in range(8):
                button_canvas.itemconfig(light_squares[x][abs(y-7)][z], fill=colour_list[h])
                h+=1


# ----------------------------- Global Variables ----------------------------- #
frames = 0
current_frame = 0
brush = "red"
# Create buttons that change the colour of a dot
light_buttons = [[[0 for x in range(8)] for x in range(8)] for x in range(8)]
light_button_colours = [[["white" for x in range(8)] for x in range(8)] for x in range(8)]
anim = []
button_light_anim = []

x_list = np.array([])
y_list = np.array([])
z_list = np.array([])
for i in range(8):
    for j in range(8):
        for k in range(8):
            x_list=np.append(x_list,i)
            y_list=np.append(y_list,j)
            z_list=np.append(z_list,k)

# ----------------------------------- Build UI ---------------------------------- #
# The main Tkinter window 
window = Tk() 
  
# setting the title  
window.title('L3D Cube Simulator') 
  
# dimensions of the main window 
window.geometry("1080x600") 

# Setting up plot
fig = Figure(figsize=(5,5),dpi=100)
plot = fig.add_subplot(111, projection='3d')
plot.set_box_aspect([1,1,1])
plot.set_title("Matrix", pad=25, size=15)
plot.set_xlabel("X") 
plot.set_ylabel("Y") 
plot.set_zlabel("Z")

# creating the Tkinter canvas 
# containing the Matplotlib figure 
canvas = FigureCanvasTkAgg(fig, master = window)   
canvas.draw() 

# placing the canvas on the Tkinter window 
canvas.get_tk_widget().grid(row=0,rowspan=128,column=0,padx=10,pady=10) 

# button that closes the window
close_button = Button(master = window,  
                     command=window.destroy,
                     height = 2,  
                     width = 10, 
                     text = "Close")

close_button.grid(row=128,column=0,padx=10,pady=10)

# draw frames slider
slider = Scale(window, from_=0, to=frames-1, orient=HORIZONTAL,command = move_frame)
slider.grid(row=18,column=2,columnspan=10)

#draw add frames button
add_frame_font = font.Font(size=5)
add_frame_button = Button(window, height = 10, width = 10, text = "Add Frame")
add_frame_button.configure(command=add_frame)
add_frame_button.grid(row=18,column=11,columnspan=6)

add_frame_button['font'] = add_frame_font

#canvas for all light squares
button_canvas = Canvas(window, height=255, width=525, bd=0,bg="white")
button_canvas.grid(row=0,column=1,columnspan=128,pady=(15,0))
button_canvas.bind("<B1-Motion>",changeColour)
button_canvas.bind("<Button-1>",changeColour)

#draw squares for all painting buttons
light_squares = [[[None for x in range(8)] for y in range(8)] for z in range(8)]
for x in range(8):
    for y in range(8):
        for z in range(8):
            light_squares[x][y][z] = button_canvas.create_rectangle(x*15+((z%4)*9*15),y*15+(int(z/4)*9*15),x*15+15+((z%4)*9*15),y*15+15+(int(z/4)*9*15))



# brush colour buttons
brush_button_red = Button(master = window, height = 10, width = 10, text = "Red", bg ="red")
brush_button_red.configure(command=changeBrushRed)
brush_button_red.grid(row=17,column=1,columnspan=8,padx=10,pady=10)

brush_button_green = Button(master = window, height = 10, width = 10, text = "Green", bg ="green")
brush_button_green.configure(command=changeBrushGreen)
brush_button_green.grid(row=17,column=9,columnspan=8,padx=10,pady=10)

brush_button_blue = Button(master = window, height = 10, width = 10, text = "Blue", bg ="blue")
brush_button_blue.configure(command=changeBrushBlue)
brush_button_blue.grid(row=17,column=17,columnspan=8,padx=10,pady=10)

brush_button_erase = Button(master = window, height = 10, width = 10, text = "Erase", bg ="grey")
brush_button_erase.configure(command=changeBrushErase)
brush_button_erase.grid(row=17,column=25,columnspan=8,padx=10,pady=10)

# ------------------------------ Start ----------------------------- #
#Start blank animation
add_frame()
draw_frame(anim[0],plot)

# run the gui 
window.mainloop() 