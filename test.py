
# Python program to demonstrate 
# scale widget 
  
from tkinter import * 
  
  
root = Tk()   
root.geometry("400x300")  
  
v1 = DoubleVar() 
  
def show1():   
      
    sel = "Horizontal Scale Value = " + str(v1.get()) 
    l1.config(text = sel, font =("Courier", 14))   

def test(event):
    print(s1.get())
  
  
s1 = Scale( root, variable = v1,  
           from_ = 1, to = 100,  
           orient = HORIZONTAL,command = test)    
  
l3 = Label(root, text = "Horizontal Scaler") 
  
b1 = Button(root, text ="Display Horizontal",  
            command = show1,  
            bg = "yellow")   
  
l1 = Label(root) 
  
  
s1.pack(anchor = CENTER)  
l3.pack() 
b1.pack(anchor = CENTER) 
l1.pack()  
  
root.mainloop() 