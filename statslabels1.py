# labels
from tkinter import *
from statsframes1 import *

def statslabels(statscap,x):

	labStats = Label(x[1],text="Stats for Even Chances, Column & Dozen, Lines, Corners and Streets ", 
		height=1,width=60, bg='#31859B', fg='Yellow', anchor='w',font=('Verdana', 12, 'bold'))
	labStats.place(x=6, y=6)
	
	labEvenChances = Label(x[1],text="Even Chances: 1 to 1", 
		height=1,width=18, bg='#31859B', fg='white', anchor='w',font=('Verdana', 12, 'bold'))
	labEvenChances.place(x=6, y=26)
	
	# labECAve = Label(x[1],text="Even Chances Average =", 
		# height=1,width=20, bg='#31859B', fg='white', anchor='w',font=('Verdana', 12, 'bold'))
	# labECAve.place(x=550, y=26)

	labRed = Label(x[2],text="Red", height=1,width=8, bg='black', fg='white').grid(row=0,column=0, padx=1, pady=1)
	labRedR = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=1, padx=1, pady=1)
	labBlack = Label(x[2],text="Black", height=1,width=8, bg='black', fg='white').grid(row=0,column=2, padx=1, pady=1)
	labBlackR = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=3, padx=1, pady=1)
	labOdd = Label(x[2],text="Odd", height=1,width=8, bg='black', fg='white').grid(row=0,column=4, padx=1, pady=1)
	labOddR = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=5, padx=1, pady=1)
	labEven = Label(x[2],text="Even", height=1,width=8, bg='black', fg='white').grid(row=0,column=6, padx=1, pady=1)
	labEvenR = Label(x[2],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=7, padx=1, pady=1)
	labLow = Label(x[2],text="Low", height=1,width=8, bg='black', fg='white').grid(row=0,column=8, padx=1, pady=1)
	labLowR = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=9, padx=1, pady=1)
	labHigh = Label(x[2],text="High", height=1,width=8, bg='black', fg='white').grid(row=0,column=10, padx=1, pady=1)
	labHighR = Label(x[2],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=11, padx=1, pady=1)
	labECA = Label(x[2],text="EC Av", height=1,width=8, bg='black', fg='white').grid(row=0,column=12, padx=1, pady=1)
	labECAR = Label(x[2],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=13, padx=1, pady=1)
	
	labDozCol = Label(x[1],text="Column & Dozen: 2 to 1", 
		height=1,width=20, bg='#31859B', fg='white', anchor='w',font=('Verdana', 12, 'bold'))
	labDozCol.place(x=6, y=88)

	# labDozColAve = Label(x[1],text="Column & Dozen Average = ", 
		# height=1,width=22, bg='#31859B', fg='white', anchor='w',font=('Verdana', 12, 'bold'))
	# labDozColAve.place(x=526, y=88)
	
	labdozen_1 = Label(x[3],text="Dozen 1", height=1,width=8, bg='black', fg='white').grid(row=0,column=0, padx=1, pady=1)
	labdozen_1R = Label(x[3],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=1, padx=1, pady=1)
	labozen_2 = Label(x[3],text="Dozen 2", height=1,width=8, bg='black', fg='white').grid(row=0,column=2, padx=1, pady=1)
	labozen_2R = Label(x[3],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=3, padx=1, pady=1)
	labozen_3 = Label(x[3],text="Dozen 3", height=1,width=8, bg='black', fg='white').grid(row=0,column=4, padx=1, pady=1)
	labozen_3R = Label(x[3],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=5, padx=1, pady=1)
	
	labcolumn_1 = Label(x[3],text="Column 1", height=1,width=8, bg='black', fg='white').grid(row=0,column=6, padx=1, pady=1)
	labcolumn_1R = Label(x[3],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=7, padx=1, pady=1)
	labcolumn_2 = Label(x[3],text="Column 2", height=1,width=8, bg='black', fg='white').grid(row=0,column=8, padx=1, pady=1)
	labcolumn_2R = Label(x[3],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=9, padx=1, pady=1)
	labcolumn_3 = Label(x[3],text="Column 3", height=1,width=8, bg='black', fg='white').grid(row=0,column=10, padx=1, pady=1)
	labcolumn_3R = Label(x[3],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=11, padx=1, pady=1)	
	
	labECA = Label(x[3],text="DC Av", height=1,width=8, bg='black', fg='white').grid(row=0,column=12, padx=1, pady=1)
	labECAR = Label(x[3],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=13, padx=1, pady=1)
	
	labLines = Label(x[1],text="Lines: 5 to 1", 
		height=1,width=18, bg='#31859B', fg='white', anchor='w',font=('Verdana', 12, 'bold'))
	labLines.place(x=6, y=150)
	
	# labLinesAve = Label(x[1],text="Lines: Average = ", 
		# height=1,width=22, bg='#31859B', fg='white', anchor='w',font=('Verdana', 12, 'bold'))
	# labLinesAve.place(x=526, y=150)

	labline_1 = Label(x[4],text="Line 1", height=1,width=8, bg='black', fg='white').grid(row=0,column=0, padx=1, pady=1)
	labline_1R = Label(x[4],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=1, padx=1, pady=1)
	labline_2 = Label(x[4],text="Line 2", height=1,width=8, bg='black', fg='white').grid(row=0,column=2, padx=1, pady=1)
	labline_2R = Label(x[4],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=3, padx=1, pady=1)
	labline_3 = Label(x[4],text="Line 3", height=1,width=8, bg='black', fg='white').grid(row=0,column=4, padx=1, pady=1)
	labline_3R = Label(x[4],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=5, padx=1, pady=1)
	labline_4 = Label(x[4],text="Line 4", height=1,width=8, bg='black', fg='white').grid(row=0,column=6, padx=1, pady=1)
	labline_4R = Label(x[4],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=7, padx=1, pady=1)
	labline_5 = Label(x[4],text="Line 5", height=1,width=8, bg='black', fg='white').grid(row=0,column=8, padx=1, pady=1)
	labline_5R = Label(x[4],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=9, padx=1, pady=1)
	labline_6 = Label(x[4],text="Line 6", height=1,width=8, bg='black', fg='white').grid(row=0,column=10, padx=1, pady=1)
	labline_6R = Label(x[4],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=11, padx=1, pady=1) 
	
	labline_7 = Label(x[4],text="Line 7", height=1,width=8, bg='black', fg='white').grid(row=1,column=0, padx=1, pady=1)
	labline_7R = Label(x[4],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=1, padx=1, pady=1)
	labline_8 = Label(x[4],text="Line 8", height=1,width=8, bg='black', fg='white').grid(row=1,column=2, padx=1, pady=1)
	labline_8R = Label(x[4],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=3, padx=1, pady=1)
	labline_9 = Label(x[4],text="Line 9", height=1,width=8, bg='black', fg='white').grid(row=1,column=4, padx=1, pady=1)
	labline_9R = Label(x[4],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=5, padx=1, pady=1)
	labline_10 = Label(x[4],text="Line 10", height=1,width=8, bg='black', fg='white').grid(row=1,column=6, padx=1, pady=1)
	labline_10R = Label(x[4],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=7, padx=1, pady=1)
	labline_11 = Label(x[4],text="Line 11", height=1,width=8, bg='black', fg='white').grid(row=1,column=8, padx=1, pady=1)
	labline_11R = Label(x[4],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=9, padx=1, pady=1)

	labline_Ave = Label(x[4],text="Line Av", height=1,width=8, bg='black', fg='white').grid(row=1,column=10, padx=1, pady=1)
	labline_AveR = Label(x[4],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=11, padx=1, pady=1)
	
	labCorners = Label(x[1],text="Corners: 8 to 1", 
		height=1,width=18, bg='#31859B', fg='white', anchor='w',font=('Verdana', 12, 'bold'))
	labCorners.place(x=6, y=240)
	
	# CornerAve = Label(x[1],text="Corner: Average = ", 
		# height=1,width=22, bg='#31859B', fg='white', anchor='w',font=('Verdana', 12, 'bold'))
	# CornerAve.place(x=526, y=240)

	labcorner_1 = Label(x[5],text="Corner 1", height=1,width=8, bg='black', fg='white').grid(row=0,column=0, padx=1, pady=1)
	labcorner_1R = Label(x[5],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=1, padx=1, pady=1)
	labcorner_2 = Label(x[5],text="Corner 2", height=1,width=8, bg='black', fg='white').grid(row=0,column=2, padx=1, pady=1)
	labcorner_2R = Label(x[5],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=3, padx=1, pady=1)
	labcorner_3 = Label(x[5],text="Corner 3", height=1,width=8, bg='black', fg='white').grid(row=0,column=4, padx=1, pady=1)
	labcorner_3R = Label(x[5],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=5, padx=1, pady=1)
	labcorner_4 = Label(x[5],text="Corner 4", height=1,width=8, bg='black', fg='white').grid(row=0,column=6, padx=1, pady=1)
	labcorner_4R = Label(x[5],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=7, padx=1, pady=1)
	labcorner_5 = Label(x[5],text="Corner 5", height=1,width=8, bg='black', fg='white').grid(row=0,column=8, padx=1, pady=1)
	labcorner_5R = Label(x[5],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=9, padx=1, pady=1)
	labcorner_6 = Label(x[5],text="Corner 6", height=1,width=8, bg='black', fg='white').grid(row=0,column=10, padx=1, pady=1)
	labcorner_6R = Label(x[5],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=11, padx=1, pady=1)
	
	labcorner_7 = Label(x[5],text="Corner 7", height=1,width=8, bg='black', fg='white').grid(row=1,column=0, padx=1, pady=1)
	labcorner_7R = Label(x[5],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=1, padx=1, pady=1)
	labcorner_8 = Label(x[5],text="Corner 8", height=1,width=8, bg='black', fg='white').grid(row=1,column=2, padx=1, pady=1)
	labcorner_8R = Label(x[5],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=3, padx=1, pady=1)
	labcorner_9 = Label(x[5],text="Corner 9", height=1,width=8, bg='black', fg='white').grid(row=1,column=4, padx=1, pady=1)
	labcorner_9R = Label(x[5],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=5, padx=1, pady=1)
	labcorner_10 = Label(x[5],text="Corner 10", height=1,width=8, bg='black', fg='white').grid(row=1,column=6, padx=1, pady=1)
	labcorner_10R = Label(x[5],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=7, padx=1, pady=1)
	labcorner_11 = Label(x[5],text="Corner 11", height=1,width=8, bg='black', fg='white').grid(row=1,column=8, padx=1, pady=1)
	labcorner_11R = Label(x[5],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=9, padx=1, pady=1)
	labcorner_12 = Label(x[5],text="Corner 12", height=1,width=8, bg='black', fg='white').grid(row=1,column=10, padx=1, pady=1)
	labcorner_12R = Label(x[5],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=11, padx=1, pady=1)
	
	labcorner_13 = Label(x[5],text="Corner 13", height=1,width=8, bg='black', fg='white').grid(row=2,column=0, padx=1, pady=1)
	labcorner_13R = Label(x[5],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=2,column=1, padx=1, pady=1)
	labcorner_14 = Label(x[5],text="Corner 14", height=1,width=8, bg='black', fg='white').grid(row=2,column=2, padx=1, pady=1)
	labcorner_14R = Label(x[5],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=2,column=3, padx=1, pady=1)
	labcorner_15 = Label(x[5],text="Corner 15", height=1,width=8, bg='black', fg='white').grid(row=2,column=4, padx=1, pady=1)
	labcorner_15R = Label(x[5],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=2,column=5, padx=1, pady=1)
	labcorner_16 = Label(x[5],text="Corner 16", height=1,width=8, bg='black', fg='white').grid(row=2,column=6, padx=1, pady=1)
	labcorner_16R = Label(x[5],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=2,column=7, padx=1, pady=1)
	labcorner_17 = Label(x[5],text="Corner 17", height=1,width=8, bg='black', fg='white').grid(row=2,column=8, padx=1, pady=1)
	labcorner_17R = Label(x[5],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=2,column=9, padx=1, pady=1)
	labcorner_18 = Label(x[5],text="Corner 18", height=1,width=8, bg='black', fg='white').grid(row=2,column=10, padx=1, pady=1)
	labcorner_18R = Label(x[5],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=2,column=11, padx=1, pady=1)
	
	labcorner_19 = Label(x[5],text="Corner 19", height=1,width=8, bg='black', fg='white').grid(row=3,column=0, padx=1, pady=1)
	labcorner_19R = Label(x[5],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=3,column=1, padx=1, pady=1)
	labcorner_20 = Label(x[5],text="Corner 20", height=1,width=8, bg='black', fg='white').grid(row=3,column=2, padx=1, pady=1)
	labcorner_20R = Label(x[5],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=3,column=3, padx=1, pady=1)
	labcorner_21 = Label(x[5],text="Corner 21", height=1,width=8, bg='black', fg='white').grid(row=3,column=4, padx=1, pady=1)
	labcorner_21R = Label(x[5],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=3,column=5, padx=1, pady=1)
	labcorner_22 = Label(x[5],text="Corner 22", height=1,width=8, bg='black', fg='white').grid(row=3,column=6, padx=1, pady=1)
	labcorner_22R = Label(x[5],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=3,column=7, padx=1, pady=1)
	
	labcorner_Ave = Label(x[5],text="Corner Av", height=1,width=8, bg='black', fg='white').grid(row=3,column=8, padx=1, pady=1)
	labcorner_AveR = Label(x[5],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=3,column=9, padx=1, pady=1)

	labStreets = Label(x[1],text="Streets: 11 to 1", 
		height=1,width=18, bg='#31859B', fg='white', anchor='w',font=('Verdana', 12, 'bold'))
	labStreets.place(x=6, y=370)

	labstreet_1 = Label(x[6],text="Street_1", height=1,width=8, bg='black', fg='white').grid(row=0,column=0, padx=1, pady=1)
	labstreet_1R = Label(x[6],text="   ", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=1, padx=1, pady=1)
	labstreet_2 = Label(x[6],text="Street_2", height=1,width=8, bg='black', fg='white').grid(row=0,column=2, padx=1, pady=1)
	labstreet_2R = Label(x[6],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=3, padx=1, pady=1)
	labstreet_3 = Label(x[6],text="Street_3", height=1,width=8, bg='black', fg='white').grid(row=0,column=4, padx=1, pady=1)
	labstreet_3R = Label(x[6],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=5, padx=1, pady=1)
	labstreet_4 = Label(x[6],text="Street_4", height=1,width=8, bg='black', fg='white').grid(row=0,column=6, padx=1, pady=1)
	labstreet_4R = Label(x[6],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=7, padx=1, pady=1)
	labstreet_5 = Label(x[6],text="Street_5", height=1,width=8, bg='black', fg='white').grid(row=0,column=8, padx=1, pady=1)
	labstreet_5R = Label(x[6],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=9, padx=1, pady=1)
	labstreet_6 = Label(x[6],text="Street_6", height=1,width=8, bg='black', fg='white').grid(row=0,column=10, padx=1, pady=1)
	labstreet_6R = Label(x[6],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=11, padx=1, pady=1)
	
	labstreet_7 = Label(x[6],text="Street_7", height=1,width=8, bg='black', fg='white').grid(row=1,column=0, padx=1, pady=1)
	labstreet_7R = Label(x[6],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=1, padx=1, pady=1)
	labstreet_8 = Label(x[6],text="Street_8", height=1,width=8, bg='black', fg='white').grid(row=1,column=2, padx=1, pady=1)
	labstreet_8R = Label(x[6],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=3, padx=1, pady=1)
	labstreet_9 = Label(x[6],text="Street_9", height=1,width=8, bg='black', fg='white').grid(row=1,column=4, padx=1, pady=1)
	labstreet_9R = Label(x[6],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=5, padx=1, pady=1)
	labstreet_10 = Label(x[6],text="Street_10", height=1,width=8, bg='black', fg='white').grid(row=1,column=6, padx=1, pady=1)
	labstreet_10R = Label(x[6],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=7, padx=1, pady=1)
	labstreet_11 = Label(x[6],text="Street_11", height=1,width=8, bg='black', fg='white').grid(row=1,column=8, padx=1, pady=1)
	labstreet_11R = Label(x[6],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=9, padx=1, pady=1)
	labstreet_12 = Label(x[6],text="Street_12", height=1,width=8, bg='black', fg='white').grid(row=1,column=10, padx=1, pady=1)
	labstreet_12R = Label(x[6],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=11, padx=1, pady=1)
	labstreet_Ave = Label(x[6],text="Street Av", height=1,width=8, bg='black', fg='white').grid(row=1,column=12, padx=1, pady=1)
	labstreet_AveR = Label(x[6],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=13, padx=1, pady=1)

def change_label_value(statscap,x,arg1,arg2):
	if arg1 == 'red':
		labRedR = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=1, padx=1, pady=1)
	if arg1 == 'black':
		labBlackR = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=3, padx=1, pady=1)

	if arg1 == 'odd':
		labOddR = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=5, padx=1, pady=1)
	if arg1 == 'even':
		labEvenR = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=7, padx=1, pady=1)
	
	if arg1 == 'low':
		labLowR = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=9, padx=1, pady=1)
	if arg1 == 'high':
		labHighR = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=11, padx=1, pady=1)
	
	if arg1 == 'doz1':
		labdozen_1R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=1, padx=1, pady=1)
	if arg1 == 'doz2':
		labozen_2R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=3, padx=1, pady=1)
	if arg1 == 'doz3':
		labozen_3R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=5, padx=1, pady=1)
	
	if arg1 == 'col1':
		labcolumn_1R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=7, padx=1, pady=1)
	if arg1 == 'col2':
		labcolumn_2R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=9, padx=1, pady=1)
	if arg1 == 'col3':
		labcolumn_3R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=11, padx=1, pady=1)

	if arg1 == 'line_1':
		labline_1R = Label(x[4],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=1, padx=1, pady=1)
	if arg1 == 'line_2':
		labline_2R = Label(x[4],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=3, padx=1, pady=1)
	if arg1 == 'line_3':
		labline_3R = Label(x[4],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=5, padx=1, pady=1)
	if arg1 == 'line_4':
		labline_4R = Label(x[4],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=7, padx=1, pady=1)
	if arg1 == 'line_5':
		labline_5R = Label(x[4],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=9, padx=1, pady=1)
	if arg1 == 'line_6':
		labline_6R = Label(x[4],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=11, padx=1, pady=1) 
	if arg1 == 'line_7':
		labline_7R = Label(x[4],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=1, padx=1, pady=1)
	if arg1 == 'line_8':
		labline_8R = Label(x[4],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=3, padx=1, pady=1)
	if arg1 == 'line_9':
		labline_9R = Label(x[4],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=5, padx=1, pady=1)
	if arg1 == 'line_10':
		labline_10R = Label(x[4],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=7, padx=1, pady=1)
	if arg1 == 'line_11':
		labline_11R = Label(x[4],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=9, padx=1, pady=1)

	if arg1 == 'corner_1':
		labcorner_1R = Label(x[5],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=1, padx=1, pady=1)
	if arg1 == 'corner_2':
		labcorner_2R = Label(x[5],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=3, padx=1, pady=1)
	if arg1 == 'corner_3':
		labcorner_3R = Label(x[5],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=5, padx=1, pady=1)
	if arg1 == 'corner_4':
		labcorner_4R = Label(x[5],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=7, padx=1, pady=1)
	if arg1 == 'corner_5':
		labcorner_5R = Label(x[5],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=9, padx=1, pady=1)
	if arg1 == 'corner_6':
		labcorner_6R = Label(x[5],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=11, padx=1, pady=1)
	if arg1 == 'corner_7':
		labcorner_7R = Label(x[5],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=1, padx=1, pady=1)
	if arg1 == 'corner_8':
		labcorner_8R = Label(x[5],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=3, padx=1, pady=1)
	if arg1 == 'corner_9':
		labcorner_9R = Label(x[5],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=5, padx=1, pady=1)
	if arg1 == 'corner_10':
		labcorner_10R = Label(x[5],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=7, padx=1, pady=1)
	if arg1 == 'corner_11':
		labcorner_11R = Label(x[5],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=9, padx=1, pady=1)
	if arg1 == 'corner_12':
		labcorner_12R = Label(x[5],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=11, padx=1, pady=1)
	if arg1 == 'corner_13':
		labcorner_13R = Label(x[5],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=2,column=1, padx=1, pady=1)
	if arg1 == 'corner_14':
		labcorner_14R = Label(x[5],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=2,column=3, padx=1, pady=1)
	if arg1 == 'corner_15':
		labcorner_15R = Label(x[5],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=2,column=5, padx=1, pady=1)
	if arg1 == 'corner_16':
		labcorner_16R = Label(x[5],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=2,column=7, padx=1, pady=1)
	if arg1 == 'corner_17':
		labcorner_17R = Label(x[5],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=2,column=9, padx=1, pady=1)
	if arg1 == 'corner_18':
		labcorner_18R = Label(x[5],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=2,column=11, padx=1, pady=1)
	if arg1 == 'corner_19':
		labcorner_19R = Label(x[5],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=3,column=1, padx=1, pady=1)
	if arg1 == 'corner_20':
		labcorner_20R = Label(x[5],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=3,column=3, padx=1, pady=1)
	if arg1 == 'corner_21':
		labcorner_21R = Label(x[5],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=3,column=5, padx=1, pady=1)
	if arg1 == 'corner_22':
		labcorner_22R = Label(x[5],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=3,column=7, padx=1, pady=1)

	if arg1 == 'street_1':
		# labstreet_1R = Label(x[6],text="99", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=1, padx=1, pady=1)
		labstreet_1R = Label(x[6],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=1, padx=1, pady=1)
	if arg1 == 'street_2':
		labstreet_2R = Label(x[6],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=3, padx=1, pady=1)
	if arg1 == 'street_3':
		labstreet_3R = Label(x[6],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=5, padx=1, pady=1)
	if arg1 == 'street_4':
		labstreet_4R = Label(x[6],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=7, padx=1, pady=1)
	if arg1 == 'street_5':
		labstreet_5R = Label(x[6],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=9, padx=1, pady=1)
	if arg1 == 'street_6':
		labstreet_6R = Label(x[6],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=11, padx=1, pady=1)
	if arg1 == 'street_7':
		labstreet_7R = Label(x[6],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=1, padx=1, pady=1)
	if arg1 == 'street_8':
		labstreet_8R = Label(x[6],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=3, padx=1, pady=1)
	if arg1 == 'street_9':
		labstreet_9R = Label(x[6],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=5, padx=1, pady=1)
	if arg1 == 'street_10':
		labstreet_10R = Label(x[6],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=7, padx=1, pady=1)
	if arg1 == 'street_11':
		labstreet_11R = Label(x[6],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=9, padx=1, pady=1)
	if arg1 == 'street_12':
		labstreet_12R = Label(x[6],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=11, padx=1, pady=1)