# ---------------------------------------------------------------------------- #
#                         A simulator for the L3D Cube                         #
# ---------------------------------------------------------------------------- #

# importing required libraries
from tkinter import * 
import tkinter.font as font
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

    # Create frame
    frame = Frame()
    
    #add to animation
    anim.append(frame.values)

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

    #update button coloursgu
    h=0
    for i in range(8):
        for j in range(8):
            for k in range(8):
                light_buttons[i][j][k].configure(bg=colour_list[h])
                h+=1



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
    
# Function to change colour of dot
def changeColour(frame, x1,y1,z1):
    global light_buttons
    global plot

    #if button is already desired colour, set to white
    if frame[(x1,y1,z1)] == brush:
        frame[(x1,y1,z1)] = "grey"
        light_buttons[x1][y1][z1].configure(bg="white")
    else:
        frame[(x1,y1,z1)] = brush
        light_buttons[x1][y1][z1].configure(bg=brush)

    refresh()

    print("x: ",x1," y: ",y1," z: ",z1," colour: ",frame[(x1,y1,z1)])

def move_frame(event):
    global current_frame
    global slider
    global plot
    current_frame = slider.get()

    refresh()

def refresh():
    plot.cla()
    draw_frame(anim[current_frame],plot)
    canvas.draw()

# ----------------------------- Global Variables ----------------------------- #
frames = 0
current_frame = 0
brush = "red"
# Create buttons that change the colour of a dot
light_buttons = [[[0 for x in range(8)] for x in range(8)] for x in range(8)]
light_button_colours = [[["white" for x in range(8)] for x in range(8)] for x in range(8)]
anim = []

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
window.geometry("1000x600") 

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

# Create drawing buttons
myFont = font.Font(size=1)
for z in range(8):
    for x in range(8):
        for y in range(8):

            # Create button
            light_buttons[x][y][z] = Button(window,bg="white",height=5,width=3,bd=1)
            
            # Configure button
            light_buttons[x][y][z].configure(command=lambda x1=x, y1=y, z1=z: changeColour(anim[current_frame],x1,y1,z1))

            # Position button
            posx = x+(z*8)+1
            posy = abs(y-7)
            bufx = (0,0)
            bufy = (0,0)
            if x == 0:
                bufx = (8,0)

            if x == 7:
                bufx = (0,8)
            
            if y == 0:
                bufy = (0,8)

            if y == 7:
                bufy = (8,0)
            
            if z>3:
                posx -=32
                posy = abs(y-7)+8


            light_buttons[x][y][z].grid(column=posx,row=posy,padx=bufx,pady=bufy)

            light_buttons[x][y][z]['font'] = myFont

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



# ------------------------------ Start Animation ----------------------------- #

#Start blank animation
add_frame()
draw_frame(anim[0],plot)

# run the gui 
window.mainloop() 