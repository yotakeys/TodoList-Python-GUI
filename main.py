from tkinter import *
import tkinter.font as tkfont

root = Tk()

# Configure Window
root.title("ToDoList")
SizeWindow = "400x500"

root.geometry(SizeWindow)
root.resizable(False,False)
root.iconbitmap("todolisticon.ico")

root.configure(
    bg = "#1b2330"
)

#Label Judul
JudulFrame = Frame(root)
JudulFrame.pack()

TextJudul = StringVar()
TextJudul.set("TO DO LIST")
Judul = Label(JudulFrame, 
    textvariable= TextJudul
)

Judul.configure(
    bg="#1b2330",
    fg = "#ffffff",
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
    relief = "ridge",
    bd = 5,
    bg= "#c8d4e8",
    width = 50,
    justify= "center",
    borderwidth=10,
    font =tkfont.Font(
        family = "courier")
)

InputToDo.pack()
Input.pack(pady=10, padx=20)

#Button
BtnFrame = Frame(root)

def add_task():
    todo.insert(END, "> " + InputToDo.get())
    InputToDo.delete(0,END)
def delete_task():
    todo.delete(ANCHOR)
def done_task():
    todo.itemconfig(
        todo.curselection(),
        fg = "#747e8f"
    )

add = Button(BtnFrame,text = "Add",command=add_task)
delete = Button(BtnFrame,text = "Delete",command=delete_task)
done = Button(BtnFrame,text = "Done",command=done_task)

add.configure(bg = "#3279a8",relief = "ridge", width = 7, height =1,font =tkfont.Font(
        family = "Bahnschrift SemiBold Condensed", size =12))
delete.configure(bg = "#3279a8",relief = "ridge", width = 7, height =1,font =tkfont.Font(
        family = "Bahnschrift SemiBold Condensed", size =12))
done.configure(bg = "#3279a8",relief = "ridge", width = 7, height =1,font =tkfont.Font(
        family = "Bahnschrift SemiBold Condensed", size =12))

add.grid(row = 0, column = 0, padx = 15)
delete.grid(row = 0, column = 1, padx = 15)
done.grid(row = 0, column = 2, padx = 15)

BtnFrame.configure(bg = "#1b2330")
BtnFrame.pack(pady = 10)

#to do list

ListFrame = Frame(root)

data = [
    "Makan bareng ayang",
    "Minum bareng ayang",
    "Kelas Matematika",
    "UAS FISIKA",
    "as mdsa jnjk njsanjksn an sanjnd kanjn snjksa jdnna kajs asj ",
    "Welcome Party","a","b","c","d","e","f","g","h","i","j"
,"k","l","m","o"]

todo = Listbox(ListFrame)
for do in data:
    x = "> " + do
    todo.insert(END,x)
todo.configure(
    width = 32,
    height = 100,
    font = tkfont.Font(
        family = "courier",
        size = 12,
        weight = "bold"
    )
)
scroll = Scrollbar(ListFrame)

todo.configure(yscrollcommand=scroll.set,
    bg= "#c8d4e8",
    highlightthickness=0,
    selectbackground= "#ffffff",
    selectforeground= "#1b2330",
    activestyle= "none"
)
todo.pack(side=LEFT, fill=BOTH)
scroll.configure(command = todo.yview)
scroll.pack(side=RIGHT,fill = BOTH)

ListFrame.configure(
    pady = 20,
    padx = 20,
    bg = "#1b2330"
)
ListFrame.pack()

root.mainloop()