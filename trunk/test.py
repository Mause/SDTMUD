from Tkinter import *

root = Tk()

def callback(event):
    print "clicked at", event.x, event.y 

frame = Frame(root, width=100, height=100)
frame.bind("<Enter>", callback)
frame.pack()

root.mainloop()
