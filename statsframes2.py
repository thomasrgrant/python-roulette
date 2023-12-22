from tkinter import *

# frames for Stats window
def my_statsframes2(stats2cap):

	framestats2cap = Frame(stats2cap, bg='green', relief=RIDGE,bd=5)
	framestats2cap.place(x=6, y=6, width=746, height=500)
	
	frame1stats2cap = Frame(stats2cap, bg='#31859B', highlightbackground="black", highlightthickness=2)#frame border
	frame1stats2cap.place(x=10, y=10, width=736, height=490) #frame using x y w h

	frameSplits = Frame(stats2cap, bg='#31859B', highlightbackground="black", highlightthickness=2)
	frameSplits.place(x=16, y=60, width=724, height=224) #frame using x y w h

	frameSingles = Frame(stats2cap, bg='#31859B', highlightbackground="black", highlightthickness=2)
	frameSingles.place(x=16, y=334, width=724, height=136) #frame using x y w h

	return framestats2cap,frame1stats2cap,frameSplits,frameSingles