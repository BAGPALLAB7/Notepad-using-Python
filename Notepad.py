from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def newFile():
    global file
    root.title("Untitled - Notepad (@bagpallab7)")
    file = None
    TextArea.delete(1.0, END)
def openFile():
    global file
    file = askopenfilename(defaultextension=".text", filetypes=[("All files", "*.*"),("Text Documents", "*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"- Notepad")
        TextArea.delete(1.0,END)
        f=open(file,"r")
        try:
            TextArea.insert(1.0,f.read())
            f.close()
        except:
            showinfo("bagpallab7","Open only text file.")
def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            showinfo("bagpallab7","File Saved.")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
    
def cut():
    TextArea.event_generate("<<Cut>>")
def copy():
    TextArea.event_generate("<<Copy>>")
def paste():
    TextArea.event_generate("<<Paste>>")
def about():
    showinfo("bagpallab7","Hii, My name is Pallab, i'm a computer science engineer. I made this Notepad using Tkinter python module(March 2020). In this notepad you can perform many operatoins like inside edit menu you can perform cut, copy, pest operation and from file menu you can create new file, save file, open text file and at least you can exit from this application by clicking on the exit option inside the file menu.")


if __name__ == '__main__':
    #Basic tkinter setup
    root = Tk()
    root.title("Untitled - Notepad (@bagpallab7)")
    root.wm_iconbitmap("newicon.ico")
    
    root.geometry("644x700")

    #Add TextArea
    TextArea = Text(root, font="lucida 13")
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    # Lets create a menubar
    MenuBar = Menu(root)

    #File Menu Starts
    FileMenu = Menu(MenuBar, tearoff=0)
    # To open new file
    FileMenu.add_command(label="New", command=newFile)

    #To Open already existing file
    FileMenu.add_command(label="Open", command = openFile)

    # To save the current file

    FileMenu.add_command(label = "Save", command = saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit", command = quit)
    MenuBar.add_cascade(label = "File", menu=FileMenu)
    # File Menu ends

    # Edit Menu Starts
    EditMenu = Menu(MenuBar, tearoff=0)
    #To give a feature of cut, copy and paste
    EditMenu.add_command(label = "Cut", command=cut)
    EditMenu.add_command(label = "Copy", command=copy)
    EditMenu.add_command(label = "Paste", command=paste)

    MenuBar.add_cascade(label="Edit", menu = EditMenu)
    # Edit Menu Ends

    # Help Menu Starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label = "About Notepad", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    # Help Menu Ends

    root.config(menu=MenuBar)

    #Adding Scrollbar using TKinter
    Scroll=Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)
    
