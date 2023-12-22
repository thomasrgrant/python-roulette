from tkinter import *

# frames
def my_frames(root):
    #Here I design the layout of the GUI (Graphic User Interface). Well... I got it to look good.
    
    # border relief 
    # relief=GROOVE, borderwidth=5
    # relief=RAISED, borderwidth=5
    # relief=RIDGE, borderwidth=5

    # Main frame green background with dard green border
    frame = Frame(root, bg='green', 
        relief=RIDGE, borderwidth=5)
    frame.place(x=6, y=6, width=560, height=209) #frame using x y w h

    # frame black boarder with blue background width=660
    # frame border for numbers
    frame1 = Frame(root, bg='#31859B', 
        relief=RAISED, borderwidth=5)
    frame1.place(x=10, y=10, width=551, height=200) #frame using x y w h

    # frame for number labels
    frame2 = Frame(root, bg='#31859B', highlightbackground="black", highlightthickness=2)
    frame2.place(x=18, y=18, width=484, height=112) #frame using x y w h

    # # bottom frame for the buttons.
    framebase = Frame(root, bg='#31859B',
        relief=RIDGE, borderwidth=5) # bottom frame for the buttons.
    framebase.place(x=18, y=164, width=533, height=36) #frame using x y w h

    # framewide for the right side for settings etc
    framewide = Frame(root, bg='green', bd=5,
        relief=RIDGE, borderwidth=5)#Main frame green background with dard green border
    framewide.place(x=572, y=6, width=656, height=209) #frame using x y w h  framewide.place(x=572, y=6, width=160, height=209)

    frameSettings = Frame(root, bg='#31859B',
        relief=RAISED, borderwidth=5)#frame border for numbers
    frameSettings.place(x=576, y=10, width=152, height=201) #frame using x y w h

    frametallTBF = Frame(root, bg='green', bd=5,
        relief=RIDGE, borderwidth=5)#Main frame green background with dard green border
    frametallTBF.place(x=6, y=221, width=560, height=162) #frame using x y w h
    
    frameStats = Frame(root, bg='#31859B',
        relief=RAISED, borderwidth=5)#frame border for numbers
    frameStats.place(x=728, y=10, width=494, height=201) #frame using x y w h  frameStats.place(x=752, y=10, width=715, height=201)

    return frame,frame1,frame2,framebase,framewide,frameSettings,frametallTBF,frameStats

