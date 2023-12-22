from tkinter import *

# frames for Stats window
def my_statsframes4(stats4cap):

	framestats4cap = Frame(stats4cap, bg='green', relief=RIDGE,bd=5)
	framestats4cap.place(x=6, y=6, width=906, height=500)
	
	frame1stats4cap = Frame(stats4cap, bg='#31859B', highlightbackground="black", highlightthickness=2)#frame border
	frame1stats4cap.place(x=10, y=10, width=896, height=490) #frame using x y w h

	frameLineCombo = Frame(stats4cap, bg='#31859B', highlightbackground="black", highlightthickness=2)
	frameLineCombo.place(x=16, y=40, width=884, height=70) #frame using x y w h

	frameStreetsCombo = Frame(stats4cap, bg='#31859B', highlightbackground="black", highlightthickness=2)
	frameStreetsCombo.place(x=16, y=154, width=884, height=246) #frame using x y w h

	return framestats4cap,frame1stats4cap,frameLineCombo,frameStreetsCombo