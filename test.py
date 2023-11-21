# import all classes/methods 
# from the tkinter module 
from tkinter import *
  
# The main tkinter window 
window = Tk() 
  
# setting the title and  
window.title('Plotting in Tkinter') 
  
# setting the dimensions of  
# the main window 
window.geometry("500x500") 

light = [[0 for x in range(8)] for x in range(8)]

def printcord(x,y,z):
    print(x,y,z)

for z in range(8):
    for x in range(8):
        for y in range(8):
            light[x][y] = Button(window,bg="black")
            light[x][y].configure(command=lambda x1=x, y1=y, z1=z: printcord(x1,y1,z1))
            if x == 7:
                light[x][y].grid(column=x+(z*8),row=abs(y-7),padx=(1,4),pady=1)
            else:
                light[x][y].grid(column=x+(z*8),row=abs(y-7),padx=1,pady=1)



# run the gui 

window.mainloop()