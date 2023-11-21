# ---------------------------------------------------------------------------- #
#                         A simulator for the L3D Cube                         #
# ---------------------------------------------------------------------------- #

# importing required libraries
from tkinter import * 
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
x = np.array([])
y = np.array([])
z = np.array([])
for i in range(8):
    for j in range(8):
        for k in range(8):
            x=np.append(x,i)
            y=np.append(y,j)
            z=np.append(z,k)

# Plotting
plot.scatter3D(x, y, z, color='grey', alpha=0.2)

# creating the Tkinter canvas 
# containing the Matplotlib figure 
canvas = FigureCanvasTkAgg(fig, master = window)   
canvas.draw() 

# placing the canvas on the Tkinter window 
canvas.get_tk_widget().pack() 

# placing the toolbar on the Tkinter window 
canvas.get_tk_widget().pack() 

# button that closes the window
close_button = Button(master = window,  
                     command=window.destroy,
                     height = 2,  
                     width = 10, 
                     text = "Close")

close_button.pack()

newWindow = Toplevel(window)
 
# sets the title of the buttons
newWindow.title("Draw")

# sets the geometry of toplevel
newWindow.geometry("1000x200")

# Create buttons that change the colour of a dot
light = [[0 for x in range(8)] for x in range(8)]

def changeColour(x,y,z):
    print(x,y,z)
    plot.scatter3D(x,y,z, color='blue', alpha=0.75)
    canvas.draw() 

for z in range(8):
    for x in range(8):
        for y in range(8):
            light[x][y] = Button(newWindow,bg="black",height=1,width=1)
            light[x][y].configure(command=lambda x1=x, y1=y, z1=z: changeColour(x1,y1,z1))
            if x == 7:
                light[x][y].grid(column=x+(z*8),row=abs(y-7),padx=(0,4),pady=0)
            else:
                light[x][y].grid(column=x+(z*8),row=abs(y-7),padx=0,pady=0)

# run the gui 
window.mainloop() 