from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("500x600")

def save_file():
    open_file=filedialog.askopenfile(mode='w',defaulttextensions=".txt")
    if open_file is None:
        return
    text=str(entry.get(1.0,END))
    open_file.write(text)
    open_file.close()

def clear_file():
    entry.delete(1.0,END)

def open_file():
    file=filedialog.askopenfile(mode='root',filetypes=[{'text files', '*.txt'}])

    if file is not None:
        content=file.read()
    entry.insert(INSERT,content)



b1=Button(root,text="Save File", command=save_file)
b1.place(x=10,y=10)

b2 = Button(root, text="Clear", command=clear_file)
b2.place(x=70,y=10)

b3 = Button(root, text="Open File", command=open_file)
b3.place(x=130,y=10)

entry = Text(root,height=150, width=150,wrap=WORD)
entry.place(x=15,y=50)
root.mainloop()