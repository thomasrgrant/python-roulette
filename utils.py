import tkinter as tk
from tkinter import scrolledtext
from myframes import * # Frames for the GUI

def create_text_box(root):
    #x = my_frames(root)  # Load in frames
    global text_box
    frametallTBF2 = Frame(root, bg='#31859B', highlightbackground="black", highlightthickness=2)#frame border for numbers
    frametallTBF2.place(x=11, y=225, width=550, height=153) #frame using x y w h
    text_box = scrolledtext.ScrolledText(frametallTBF2, width=58, height=10,bg='#00FFFF')
    text_box.place(x=2, y=2)
    return text_box  # Return the created text_box

def append_text(text_box, arg1):
    text_box.configure(state="normal")
    text_box.insert(tk.END, arg1 + "\n")
    text_box.yview_moveto(1.0)
    text_box.configure(state="disabled")

def clear_text():
	text_box.configure(state="normal")
	text_box.delete("1.0", tk.END)
	text_box.configure(state="disabled")

# listbox
def create_list_box(root):
    global listBoxOne,listBoxTwo
    frameNL = Frame(root, bg='#31859B', highlightbackground="black", highlightthickness=2)
    frameNL.place(x=505, y=18, width=46, height=112) #frame using x y w h
    
    listBoxOne=Listbox(frameNL, bg='black', fg='red', relief=SUNKEN, borderwidth=1, highlightthickness=0, width=2, height=7)
    listBoxOne.place(x=1, y=1)

    listBoxTwo=Listbox(frameNL, bg='black', fg='white', relief=SUNKEN, borderwidth=1, highlightthickness=0,width=2, height=7)
    listBoxTwo.place(x=21, y=1)

def listBoxInsert(red,green,black):
    listBoxOne.insert(0, red) #red
    listBoxTwo.insert(0, black) #Black
# listbox
