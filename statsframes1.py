from tkinter import *

# frames for Stats window
def my_statsframes(statscap):

	framestatscap = Frame(statscap, bg='green', relief=RIDGE,bd=5)
	framestatscap.place(x=6, y=6, width=808, height=500)
	
	frame1statscap = Frame(statscap, bg='#31859B', highlightbackground="black", highlightthickness=2)#frame border
	frame1statscap.place(x=10, y=10, width=800, height=490) #frame using x y w h

	frameEC = Frame(statscap, bg='#31859B', highlightbackground="black", highlightthickness=2) # Even Chances
	frameEC.place(x=16, y=60, width=788, height=26) #frame using x y w h

	frameCD = Frame(statscap, bg='#31859B', highlightbackground="black", highlightthickness=2) # Dozens Colmums
	frameCD.place(x=16, y=122, width=788, height=26) #frame using x y w h

	frameLine = Frame(statscap, bg='#31859B', highlightbackground="black", highlightthickness=2) # Lines
	frameLine.place(x=16, y=184, width=676, height=48) #frame using x y w h

	frameCorner = Frame(statscap, bg='#31859B', highlightbackground="black", highlightthickness=2)
	frameCorner.place(x=16, y=274, width=676, height=92) #frame using x y w h

	frameStreet = Frame(statscap, bg='#31859B', highlightbackground="black", highlightthickness=2)
	frameStreet.place(x=16, y=404, width=788, height=48) #frame using x y w h

	return framestatscap,frame1statscap,frameEC,frameCD,frameLine,frameCorner,frameStreet
    #,

# frames for Stats window