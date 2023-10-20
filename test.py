from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Title")

img = Image.open('Paste the directory path')
bg = ImageTk.PhotoImage(img)

lbl = Label(root, image=bg)
lbl.place(x=0, y=0)

mainloop()