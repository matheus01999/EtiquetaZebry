from tkinter import *
root = Tk()
root.geometry('250x200+250+200')
Label(root, text="Position 1 : x=0, y=0", bg="#FFFF00", fg="white").place(x=5, y=0)
Label(root, text="Position 2 : x=50, y=40", bg="#3300CC", fg="white").place(x=50, y=40)
Label(root, text="Position 3 : x=100, y=100", bg="#FF0099", fg="white").place(x=10, y=80)
root.mainloop()