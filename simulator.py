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

# the main Tkinter window 
window = Tk() 
  
# setting the title  
window.title('Plotting in Tkinter') 
  
# dimensions of the main window 
window.geometry("600x600") 

# Setting up plot
fig = Figure(figsize=(5,5),dpi=100)

plot = fig.add_subplot(111, projection='3d')
plot.set_box_aspect([1,1,1])
plot.set_title("Matrix", pad=25, size=15)
plot.set_xlabel("X") 
plot.set_ylabel("Y") 
plot.set_zlabel("Z")

# Create dot matrix
x_list = np.array([])
y_list = np.array([])
z_list = np.array([])
col = {}
for i in range(8):
    for j in range(8):
        for k in range(8):
            x_list=np.append(x_list,i)
            y_list=np.append(y_list,j)
            z_list=np.append(z_list,k)
            col[(i,j,k)] = "grey"

# Plotting
plot.scatter3D(x_list, y_list, z_list, color=[*col.values()], alpha=0.75)

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

# Create buttons that change the colour of a dot
light = [[[0 for x in range(8)] for x in range(8)] for x in range(8)]

# Function to change colour of dot
def changeColour(x1,y1,z1):
    if col[(x1,y1,z1)] == "red":
        col[(x1,y1,z1)] = "grey"
        light[x1][y1][z1].configure(bg="grey")
    else:
        col[(x1,y1,z1)] = "red"
        light[x1][y1][z1].configure(bg="red")

    plot.cla()
    plot.scatter3D(x_list, y_list, z_list, color=[*col.values()], alpha=0.75)
    canvas.draw()

    print("x: ",x1," y: ",y1," z: ",z1," colour: ",col[(x1,y1,z1)])

# Create drawing buttons
myFont = font.Font(size=1)
for z in range(8):
    for x in range(8):
        for y in range(8):

            # Create button
            light[x][y][z] = Button(window,bg="grey",height=5,width=3)

            # Configure button
            light[x][y][z].configure(command=lambda x1=x, y1=y, z1=z: changeColour(x1,y1,z1))

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


            light[x][y][z].grid(column=posx,row=posy,padx=bufx,pady=bufy)

            light[x][y][z]['font'] = myFont

# run the gui 
window.mainloop() 