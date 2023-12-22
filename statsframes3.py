from tkinter import *

# frames for Stats window
def my_statsframes3(stats3cap):

	framestats3cap = Frame(stats3cap, bg='green', relief=RIDGE,bd=5)
	framestats3cap.place(x=6, y=6, width=746, height=500)
	
	frame1stats3cap = Frame(stats3cap, bg='#31859B', highlightbackground="black", highlightthickness=2)#frame border
	frame1stats3cap.place(x=10, y=10, width=736, height=490) #frame using x y w h

	frameVoisins = Frame(stats3cap, bg='#31859B', highlightbackground="black", highlightthickness=2)
	frameVoisins.place(x=16, y=60, width=724, height=26) #frame using x y w h

	frameNeighbors = Frame(stats3cap, bg='#31859B', highlightbackground="black", highlightthickness=2)
	frameNeighbors.place(x=16, y=116, width=724, height=136) #frame using x y w h

	frameFinalbet = Frame(stats3cap, bg='#31859B', highlightbackground="black", highlightthickness=2)
	frameFinalbet.place(x=16, y=284, width=724, height=48) #frame using x y w h

	frameCombo = Frame(stats3cap, bg='#31859B', highlightbackground="black", highlightthickness=2)
	frameCombo.place(x=16, y=370, width=724, height=26) #frame using x y w h	

	frameMagic_9 = Frame(stats3cap, bg='#31859B', highlightbackground="black", highlightthickness=2)
	frameMagic_9.place(x=16, y=430, width=724, height=48) #frame using x y w h

	return framestats3cap,frame1stats3cap,frameVoisins,frameNeighbors,frameFinalbet,frameCombo,frameMagic_9
    #