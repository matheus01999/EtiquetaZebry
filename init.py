# Import Module
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("Welcome to GeekForGeeks")
# Set geometry (widthxheight)
root.geometry('500x500')

#adding a label to the root window
lbl = Label(root, text = "Selecione um Zebra")
lbl.grid()

# adding Entry Field
txt = Entry(root, width=10)
txt.grid(column =2, row =0)

# button widget with red color text
# inside
btn = Button(root, text = "IMPRIMIR")
# set Button grid
btn.grid(column=3, row=0)

# all widgets will be here
# Execute Tkinter
root.mainloop()
