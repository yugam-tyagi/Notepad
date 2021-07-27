from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os 

def newfile():
    global file
    root.title("New File")
    file = None
    textarea.delete(1.0,END)

def openfile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file =="":
        file = None
    else:
        root.title(os.path.basename(file) + "- Notepad")
        textarea.delete(1.0,END)
        f = open(file,'r')
        textarea.insert(1.0,f.read())
        file.close()
        
def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file == "":
            file = None
        else:
            f = open(file,'w')
            f.write(textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file) + "- Notepad")
    else:
        f = open(file,'w')
        f.write(textarea.get(1.0,END))
        f.close()

def exitnotepad():
    root.destroy()

def cuttext():
    textarea.event_generate("<<Cut>>")

def copytext():
    textarea.event_generate("<<Copy>>")

def pastetext():
    textarea.event_generate("<<Paste>>")

def aboutus():
    showinfo("Notepad By Yugam Tyagi","Hello! This Notepad Is Created By Yugam Tyagi")

def contactus():
    showinfo("Contact Details","Email Yugam Tyagi At yugamtyagi@gmail.com")

root = Tk()
width= root.winfo_screenwidth() 
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.title("Welcome To Notepad")

scbar = Scrollbar(root)
scbar.pack(side=RIGHT,fill=Y)
textarea = Text(root,font="comicsansms 20",yscrollcommand=scbar.set,bg="pink")
file = None
textarea.pack(expand=True,fill=BOTH)
scbar.config(command=textarea.yview)

menubar = Menu(root)

m1 = Menu(menubar,tearoff=0)
m1.add_command(label="New",command=newfile)
m1.add_command(label="Open",command=openfile)
m1.add_command(label="Save",command=savefile)
m1.add_separator()
m1.add_command(label="Exit",command=exitnotepad)
root.config(menu=menubar)
menubar.add_cascade(label="File",menu=m1)

m2 = Menu(menubar,tearoff=0)
m2.add_command(label="Cut",command=cuttext)
m2.add_command(label="Copy",command=copytext)
m2.add_command(label="Paste",command=pastetext)
root.config(menu=menubar)
menubar.add_cascade(label="Edit",menu=m2)

m3 = Menu(menubar,tearoff=0)
m3.add_command(label="About Us",command=aboutus)
m3.add_command(label="Contact Us",command=contactus)
root.config(menu=menubar)
menubar.add_cascade(label="Help",menu=m3)

root.mainloop()