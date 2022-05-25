from tkinter import *
import tkinter.font as tkfont

from regex import P

root = Tk()

# Configure Window
root.title("ToDoList")
SizeWindow = "400x500"

root.geometry(SizeWindow)
root.iconbitmap("todolisticon.ico")

root.configure(
    bg = "#ffffff"
)

#Label Judul
JudulFrame = Frame(root)
JudulFrame.configure(

)
JudulFrame.pack()

TextJudul = StringVar()
TextJudul.set("TO DO LIST")
Judul = Label(JudulFrame, 
    textvariable= TextJudul
)

Judul.configure(
    bg="#ffffff",
    font =tkfont.Font(
        family = "Bahnschrift SemiBold Condensed",
        size= 30,
        weight = "bold"
    )
)
Judul.pack()

Input = Frame(root)
#Entry Text Box
InputToDo = Entry(Input,
    relief = "flat",
    bd = 5,
    bg= "#c8d4e8",
    width = 50,
    justify= "center",
    borderwidth=10
)

InputToDo.pack()
Input.pack(pady=20)


#to do list

ListFrame = Frame(root)

data = [
    "satu","dua","tiga", "empat"
    ]

todo = Listbox(ListFrame)
for do in data:
    todo.insert(END,do)
todo.configure(
    width = 50
)
todo.pack()
ListFrame.pack()

root.mainloop()
