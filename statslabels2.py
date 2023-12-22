# labels
from tkinter import *
from statsframes2 import *

def statslabels2(stats2cap,x):
	labSplits = Label(x[1],text="Splits: 17 to 1", height=1,width=18, 
		bg='#31859B', fg='white', anchor='w',font=('Verdana', 12, 'bold'))
	labSplits.place(x=6, y=26)

	labStats = Label(x[1],text="Stats for Splits and Single Numbers", height=1,
		width=48, bg='#31859B', fg='Yellow', anchor='w',font=('Verdana', 12, 'bold'))
	labStats.place(x=60, y=6)

	labSplit_1_2 = Label(x[2],text="Split 1 2", height=1,width=9, bg='black', fg='white').grid(row=0,column=0, padx=1, pady=1)
	labSplit_1_2R = Label(x[2],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=1, padx=1, pady=1)
	labSplit_1_4 = Label(x[2],text="Split 1 4", height=1,width=9, bg='black', fg='white').grid(row=0,column=2, padx=1, pady=1)
	labSplit_1_4R = Label(x[2],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=3, padx=1, pady=1)
	labSplit_2_3 = Label(x[2],text="Split 2 3", height=1,width=9, bg='black', fg='white').grid(row=0,column=4, padx=1, pady=1)
	labSplit_2_3R = Label(x[2],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=5, padx=1, pady=1)
	labSplit_2_5 = Label(x[2],text="Split 2 5", height=1,width=9, bg='black', fg='white').grid(row=0,column=6, padx=1, pady=1)
	labSplit_2_5R = Label(x[2],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=7, padx=1, pady=1)
	labSplit_3_6 = Label(x[2],text="Split 3 6", height=1,width=9, bg='black', fg='white').grid(row=0,column=8, padx=1, pady=1)
	labSplit_3_6R = Label(x[2],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=9, padx=1, pady=1)
	labSplit_4_5 = Label(x[2],text="Split 4 5", height=1,width=9, bg='black', fg='white').grid(row=0,column=10, padx=1, pady=1)
	labSplit_4_5R = Label(x[2],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=11, padx=1, pady=1)
	
	labSplit_3_6 = Label(x[2],text="Split 3 6", height=1,width=9, bg='black', fg='white').grid(row=1,column=0, padx=1, pady=1)
	labSplit_3_6R = Label(x[2],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=1, padx=1, pady=1)
	labSplit_5_6 = Label(x[2],text="Split 5 6", height=1,width=9, bg='black', fg='white').grid(row=1,column=2, padx=1, pady=1)
	labSplit_5_6R = Label(x[2],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=3, padx=1, pady=1)
	labSplit_5_8 = Label(x[2],text="Split 5 8", height=1,width=9, bg='black', fg='white').grid(row=1,column=4, padx=1, pady=1)
	labSplit_5_8R = Label(x[2],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=5, padx=1, pady=1)
	labSplit_6_9 = Label(x[2],text="Split 6 9", height=1,width=9, bg='black', fg='white').grid(row=1,column=6, padx=1, pady=1)
	labSplit_6_9R = Label(x[2],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=7, padx=1, pady=1)
	labSplit_7_8 = Label(x[2],text="Split 7 8", height=1,width=9, bg='black', fg='white').grid(row=1,column=8, padx=1, pady=1)
	labSplit_7_8R = Label(x[2],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=9, padx=1, pady=1)
	labSplit_7_10 = Label(x[2],text="Split 7 10", height=1,width=9, bg='black', fg='white').grid(row=1,column=10, padx=1, pady=1)
	labSplit_7_10R = Label(x[2],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=11, padx=1, pady=1)
	
	labSplit_8_9 = Label(x[2],text="Split 8 9", height=1,width=9, bg='black', fg='white').grid(row=2,column=0, padx=1, pady=1)
	labSplit_8_9R = Label(x[2],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=2,column=1, padx=1, pady=1)
	labSplit_8_11 = Label(x[2],text="Split 8 11", height=1,width=9, bg='black', fg='white').grid(row=2,column=2, padx=1, pady=1)
	labSplit_8_11R = Label(x[2],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=2,column=3, padx=1, pady=1)
	labSplit_9_12 = Label(x[2],text="Split 9 12", height=1,width=9, bg='black', fg='white').grid(row=2,column=4, padx=1, pady=1)
	labSplit_9_12R = Label(x[2],text="	", height=1,width=4, bg='#11390F', fg='white').grid(row=2,column=5, padx=1, pady=1)
	labSplit_10_11 = Label(x[2],text="Split 10 11", height=1,width=9, bg='black', fg='white').grid(row=2,column=6, padx=1, pady=1)
	labSplit_10_11R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=2,column=7, padx=1, pady=1)
	labSplit_10_13 = Label(x[2],text="Split 10 13", height=1,width=9, bg='black', fg='white').grid(row=2,column=8, padx=1, pady=1)
	labSplit_10_13R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=2,column=9, padx=1, pady=1)
	labSplit_11_12 = Label(x[2],text="Split 11 12", height=1,width=9, bg='black', fg='white').grid(row=2,column=10, padx=1, pady=1)
	labSplit_11_12R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=2,column=11, padx=1, pady=1)

	labSplit_11_14 = Label(x[2],text="Split 11 14", height=1,width=9, bg='black', fg='white').grid(row=3,column=0, padx=1, pady=1)
	labSplit_11_14R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=3,column=1, padx=1, pady=1)
	labSplit_12_15 = Label(x[2],text="Split 12 15", height=1,width=9, bg='black', fg='white').grid(row=3,column=2, padx=1, pady=1)
	labSplit_12_15R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=3,column=3, padx=1, pady=1)
	labSplit_13_14 = Label(x[2],text="Split 13 14", height=1,width=9, bg='black', fg='white').grid(row=3,column=4, padx=1, pady=1)
	labSplit_13_14R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=3,column=5, padx=1, pady=1)
	labSplit_13_16 = Label(x[2],text="Split 13 16", height=1,width=9, bg='black', fg='white').grid(row=3,column=6, padx=1, pady=1)
	labSplit_13_16R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=3,column=7, padx=1, pady=1)
	labSplit_14_15 = Label(x[2],text="Split 14 15", height=1,width=9, bg='black', fg='white').grid(row=3,column=8, padx=1, pady=1)
	labSplit_14_15R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=3,column=9, padx=1, pady=1)
	labSplit_14_17 = Label(x[2],text="Split 14 17", height=1,width=9, bg='black', fg='white').grid(row=3,column=10, padx=1, pady=1)
	labSplit_14_17R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=3,column=11, padx=1, pady=1)

	labSplit_15_18 = Label(x[2],text="Split 15 18", height=1,width=9, bg='black', fg='white').grid(row=4,column=0, padx=1, pady=1)
	labSplit_15_18R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=4,column=1, padx=1, pady=1)
	labSplit_16_17 = Label(x[2],text="Split 16 17", height=1,width=9, bg='black', fg='white').grid(row=4,column=2, padx=1, pady=1)
	labSplit_16_17R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=4,column=3, padx=1, pady=1)
	labSplit_16_19 = Label(x[2],text="Split 16 19", height=1,width=9, bg='black', fg='white').grid(row=4,column=4, padx=1, pady=1)
	labSplit_16_19R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=4,column=5, padx=1, pady=1)
	labSplit_17_18 = Label(x[2],text="Split 17 18", height=1,width=9, bg='black', fg='white').grid(row=4,column=6, padx=1, pady=1)
	labSplit_17_18R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=4,column=7, padx=1, pady=1)
	labSplit_17_20 = Label(x[2],text="Split 17 20", height=1,width=9, bg='black', fg='white').grid(row=4,column=8, padx=1, pady=1)
	labSplit_17_20R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=4,column=9, padx=1, pady=1)
	labSplit_18_21 = Label(x[2],text="Split 18 21", height=1,width=9, bg='black', fg='white').grid(row=4,column=10, padx=1, pady=1)
	labSplit_18_21R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=4,column=11, padx=1, pady=1)

	labSplit_19_20 = Label(x[2],text="Split 19 20", height=1,width=9, bg='black', fg='white').grid(row=5,column=0, padx=1, pady=1)
	labSplit_19_20R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=5,column=1, padx=1, pady=1)
	labSplit_19_22 = Label(x[2],text="Split 19 22", height=1,width=9, bg='black', fg='white').grid(row=5,column=2, padx=1, pady=1)
	labSplit_19_22R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=5,column=3, padx=1, pady=1)
	labSplit_20_21 = Label(x[2],text="Split 20 21", height=1,width=9, bg='black', fg='white').grid(row=5,column=4, padx=1, pady=1)
	labSplit_20_21R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=5,column=5, padx=1, pady=1)
	labSplit_20_23 = Label(x[2],text="Split 20 23", height=1,width=9, bg='black', fg='white').grid(row=5,column=6, padx=1, pady=1)
	labSplit_20_23R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=5,column=7, padx=1, pady=1)
	labSplit_21_24 = Label(x[2],text="Split 21 24", height=1,width=9, bg='black', fg='white').grid(row=5,column=8, padx=1, pady=1)
	labSplit_21_24R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=5,column=9, padx=1, pady=1)
	labSplit_22_23 = Label(x[2],text="Split 22 23", height=1,width=9, bg='black', fg='white').grid(row=5,column=10, padx=1, pady=1)
	labSplit_22_23R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=5,column=11, padx=1, pady=1)

	labSplit_22_25 = Label(x[2],text="Split 22 25", height=1,width=9, bg='black', fg='white').grid(row=6,column=0, padx=1, pady=1)
	labSplit_22_25R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=6,column=1, padx=1, pady=1)
	labSplit_23_24 = Label(x[2],text="Split 23 24", height=1,width=9, bg='black', fg='white').grid(row=6,column=2, padx=1, pady=1)
	labSplit_23_24R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=6,column=3, padx=1, pady=1)
	labSplit_23_26 = Label(x[2],text="Split 23 26", height=1,width=9, bg='black', fg='white').grid(row=6,column=4, padx=1, pady=1)
	labSplit_23_26R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=6,column=5, padx=1, pady=1)
	labSplit_24_27 = Label(x[2],text="Split 24 27", height=1,width=9, bg='black', fg='white').grid(row=6,column=6, padx=1, pady=1)
	labSplit_24_27R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=6,column=7, padx=1, pady=1)
	labSplit_25_26 = Label(x[2],text="Split 25 26", height=1,width=9, bg='black', fg='white').grid(row=6,column=8, padx=1, pady=1)
	labSplit_25_26R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=6,column=9, padx=1, pady=1)
	labSplit_25_28 = Label(x[2],text="Split 25 28", height=1,width=9, bg='black', fg='white').grid(row=6,column=10, padx=1, pady=1)
	labSplit_25_28R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=6,column=11, padx=1, pady=1)

	labSplit_26_27 = Label(x[2],text="Split 26 27", height=1,width=9, bg='black', fg='white').grid(row=7,column=0, padx=1, pady=1)
	labSplit_26_27R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=7,column=1, padx=1, pady=1)
	labSplit_26_29 = Label(x[2],text="Split 26 29", height=1,width=9, bg='black', fg='white').grid(row=7,column=2, padx=1, pady=1)
	labSplit_26_29R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=7,column=3, padx=1, pady=1)
	labSplit_27_30 = Label(x[2],text="Split 27 30", height=1,width=9, bg='black', fg='white').grid(row=7,column=4, padx=1, pady=1)
	labSplit_27_30R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=7,column=5, padx=1, pady=1)
	labSplit_28_29 = Label(x[2],text="Split 28 29", height=1,width=9, bg='black', fg='white').grid(row=7,column=6, padx=1, pady=1)
	labSplit_28_29R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=7,column=7, padx=1, pady=1)
	labSplit_28_31 = Label(x[2],text="Split 28 31", height=1,width=9, bg='black', fg='white').grid(row=7,column=8, padx=1, pady=1)
	labSplit_28_31R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=7,column=9, padx=1, pady=1)
	labSplit_29_30 = Label(x[2],text="Split 29 30", height=1,width=9, bg='black', fg='white').grid(row=7,column=10, padx=1, pady=1)
	labSplit_29_30R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=7,column=11, padx=1, pady=1)

	labSplit_29_32 = Label(x[2],text="Split 29 32", height=1,width=9, bg='black', fg='white').grid(row=8,column=0, padx=1, pady=1)
	labSplit_29_32R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=8,column=1, padx=1, pady=1)
	labSplit_30_33 = Label(x[2],text="Split 30 33", height=1,width=9, bg='black', fg='white').grid(row=8,column=2, padx=1, pady=1)
	labSplit_30_33R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=8,column=3, padx=1, pady=1)
	labSplit_31_32 = Label(x[2],text="Split 31 32", height=1,width=9, bg='black', fg='white').grid(row=8,column=4, padx=1, pady=1)
	labSplit_31_32R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=8,column=5, padx=1, pady=1)
	labSplit_31_34 = Label(x[2],text="Split 31 34", height=1,width=9, bg='black', fg='white').grid(row=8,column=6, padx=1, pady=1)
	labSplit_31_34R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=8,column=7, padx=1, pady=1)
	labSplit_32_33 = Label(x[2],text="Split 32 33", height=1,width=9, bg='black', fg='white').grid(row=8,column=8, padx=1, pady=1)
	labSplit_32_33R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=8,column=9, padx=1, pady=1)
	labSplit_32_35 = Label(x[2],text="Split 32 35", height=1,width=9, bg='black', fg='white').grid(row=8,column=10, padx=1, pady=1)
	labSplit_32_35R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=8,column=11, padx=1, pady=1)

	labSplit_33_36 = Label(x[2],text="Split 33 36", height=1,width=9, bg='black', fg='white').grid(row=9,column=0, padx=1, pady=1)
	labSplit_33_36R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=9,column=1, padx=1, pady=1)
	labSplit_34_35 = Label(x[2],text="Split 34 35", height=1,width=9, bg='black', fg='white').grid(row=9,column=2, padx=1, pady=1)
	labSplit_34_35R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=9,column=3, padx=1, pady=1)
	labSplit_35_36 = Label(x[2],text="Split 35 36", height=1,width=9, bg='black', fg='white').grid(row=9,column=4, padx=1, pady=1)
	labSplit_35_36R = Label(x[2],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=9,column=5, padx=1, pady=1)

	labSingles = Label(x[1],text="Single Numbers: 35 to 1", height=1,width=24, bg='#31859B', fg='white', anchor='w',font=('Verdana', 12, 'bold')).place(x=6, y=300)

	labSingle1 = Label(x[3],text="Single 1", height=1,width=9, bg='black', fg='white').grid(row=0,column=0, padx=1, pady=1)
	labSingle1R = Label(x[3],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=1, padx=1, pady=1)
	labSingle2 = Label(x[3],text="Single 2", height=1,width=9, bg='black', fg='white').grid(row=0,column=2, padx=1, pady=1)
	labSingle2R = Label(x[3],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=3, padx=1, pady=1)
	labSingle3 = Label(x[3],text="Single 3", height=1,width=9, bg='black', fg='white').grid(row=0,column=4, padx=1, pady=1)
	labSingle3R = Label(x[3],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=5, padx=1, pady=1)
	labSingle4 = Label(x[3],text="Single 4", height=1,width=9, bg='black', fg='white').grid(row=0,column=6, padx=1, pady=1)
	labSingle4R = Label(x[3],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=7, padx=1, pady=1)
	labSingl5 = Label(x[3],text="Single 5", height=1,width=9, bg='black', fg='white').grid(row=0,column=8, padx=1, pady=1)
	labSingle5R = Label(x[3],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=9, padx=1, pady=1)
	labSingle6 = Label(x[3],text="Single 6", height=1,width=9, bg='black', fg='white').grid(row=0,column=10, padx=1, pady=1)
	labSingle6R = Label(x[3],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=11, padx=1, pady=1)

	labSingle7 = Label(x[3],text="Single 7", height=1,width=9, bg='black', fg='white').grid(row=1,column=0, padx=1, pady=1)
	labSingle7R = Label(x[3],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=1, padx=1, pady=1)
	labSingle8 = Label(x[3],text="Single 8", height=1,width=9, bg='black', fg='white').grid(row=1,column=2, padx=1, pady=1)
	labSingle8R = Label(x[3],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=3, padx=1, pady=1)
	labSingle9 = Label(x[3],text="Single 9", height=1,width=9, bg='black', fg='white').grid(row=1,column=4, padx=1, pady=1)
	labSingle9R = Label(x[3],text="	 ", height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=5, padx=1, pady=1)
	labSingle10 = Label(x[3],text="Single 10", height=1,width=9, bg='black', fg='white').grid(row=1,column=6, padx=1, pady=1)
	labSingle10R = Label(x[3],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=7, padx=1, pady=1)
	labSingl11 = Label(x[3],text="Single 11", height=1,width=9, bg='black', fg='white').grid(row=1,column=8, padx=1, pady=1)
	labSingle11R = Label(x[3],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=9, padx=1, pady=1)
	labSingle12 = Label(x[3],text="Single 12", height=1,width=9, bg='black', fg='white').grid(row=1,column=10, padx=1, pady=1)
	labSingle12R = Label(x[3],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=11, padx=1, pady=1)

	labSingle13 = Label(x[3],text="Single 13", height=1,width=9, bg='black', fg='white').grid(row=2,column=0, padx=1, pady=1)
	labSingle13R = Label(x[3],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=2,column=1, padx=1, pady=1)
	labSingl14 = Label(x[3],text="Single 14", height=1,width=9, bg='black', fg='white').grid(row=2,column=2, padx=1, pady=1)
	labSingle14R = Label(x[3],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=2,column=3, padx=1, pady=1)
	labSingle15 = Label(x[3],text="Single 15", height=1,width=9, bg='black', fg='white').grid(row=2,column=4, padx=1, pady=1)
	labSingle15R = Label(x[3],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=2,column=5, padx=1, pady=1)
	labSingle16 = Label(x[3],text="Single 16", height=1,width=9, bg='black', fg='white').grid(row=2,column=6, padx=1, pady=1)
	labSingle16R = Label(x[3],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=2,column=7, padx=1, pady=1)
	labSingl17 = Label(x[3],text="Single 17", height=1,width=9, bg='black', fg='white').grid(row=2,column=8, padx=1, pady=1)
	labSingle17R = Label(x[3],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=2,column=9, padx=1, pady=1)
	labSingle18 = Label(x[3],text="Single 18", height=1,width=9, bg='black', fg='white').grid(row=2,column=10, padx=1, pady=1)
	labSingle18R = Label(x[3],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=2,column=11, padx=1, pady=1)

	labSingle19 = Label(x[3],text="Single 19", height=1,width=9, bg='black', fg='white').grid(row=3,column=0, padx=1, pady=1)
	labSingle19R = Label(x[3],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=3,column=1, padx=1, pady=1)
	labSingl20 = Label(x[3],text="Single 20", height=1,width=9, bg='black', fg='white').grid(row=3,column=2, padx=1, pady=1)
	labSingle20R = Label(x[3],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=3,column=3, padx=1, pady=1)
	labSingle21 = Label(x[3],text="Single 21", height=1,width=9, bg='black', fg='white').grid(row=3,column=4, padx=1, pady=1)
	labSingle21R = Label(x[3],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=3,column=5, padx=1, pady=1)
	labSingle22 = Label(x[3],text="Single 22", height=1,width=9, bg='black', fg='white').grid(row=3,column=6, padx=1, pady=1)
	labSingle22R = Label(x[3],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=3,column=7, padx=1, pady=1)
	labSingl23 = Label(x[3],text="Single 23", height=1,width=9, bg='black', fg='white').grid(row=3,column=8, padx=1, pady=1)
	labSingle23R = Label(x[3],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=3,column=9, padx=1, pady=1)
	labSingle24 = Label(x[3],text="Single 24", height=1,width=9, bg='black', fg='white').grid(row=3,column=10, padx=1, pady=1)
	labSingle24R = Label(x[3],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=3,column=11, padx=1, pady=1)

	labSingle25 = Label(x[3],text="Single 25", height=1,width=9, bg='black', fg='white').grid(row=4,column=0, padx=1, pady=1)
	labSingle25R = Label(x[3],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=4,column=1, padx=1, pady=1)
	labSingl26 = Label(x[3],text="Single 26", height=1,width=9, bg='black', fg='white').grid(row=4,column=2, padx=1, pady=1)
	labSingle26R = Label(x[3],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=4,column=3, padx=1, pady=1)
	labSingle27 = Label(x[3],text="Single 27", height=1,width=9, bg='black', fg='white').grid(row=4,column=4, padx=1, pady=1)
	labSingle27R = Label(x[3],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=4,column=5, padx=1, pady=1)
	labSingle28 = Label(x[3],text="Single 28", height=1,width=9, bg='black', fg='white').grid(row=4,column=6, padx=1, pady=1)
	labSingle28R = Label(x[3],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=4,column=7, padx=1, pady=1)
	labSingl29 = Label(x[3],text="Single 29", height=1,width=9, bg='black', fg='white').grid(row=4,column=8, padx=1, pady=1)
	labSingle29R = Label(x[3],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=4,column=9, padx=1, pady=1)
	labSingle30 = Label(x[3],text="Single 30", height=1,width=9, bg='black', fg='white').grid(row=4,column=10, padx=1, pady=1)
	labSingle30R = Label(x[3],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=4,column=11, padx=1, pady=1)

	labSingle31= Label(x[3],text="Single 31", height=1,width=9, bg='black', fg='white').grid(row=5,column=0, padx=1, pady=1)
	labSingle31R = Label(x[3],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=5,column=1, padx=1, pady=1)
	labSingl32 = Label(x[3],text="Single 32", height=1,width=9, bg='black', fg='white').grid(row=5,column=2, padx=1, pady=1)
	labSingle32R = Label(x[3],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=5,column=3, padx=1, pady=1)
	labSingle33 = Label(x[3],text="Single 33", height=1,width=9, bg='black', fg='white').grid(row=5,column=4, padx=1, pady=1)
	labSingle33R = Label(x[3],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=5,column=5, padx=1, pady=1)
	labSingle34 = Label(x[3],text="Single 34", height=1,width=9, bg='black', fg='white').grid(row=5,column=6, padx=1, pady=1)
	labSingle34R = Label(x[3],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=5,column=7, padx=1, pady=1)
	labSingl35 = Label(x[3],text="Single 35", height=1,width=9, bg='black', fg='white').grid(row=5,column=8, padx=1, pady=1)
	labSingle35R = Label(x[3],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=5,column=9, padx=1, pady=1)
	labSingle36 = Label(x[3],text="Single 36", height=1,width=9, bg='black', fg='white').grid(row=5,column=10, padx=1, pady=1)
	labSingle36R = Label(x[3],text="  ", height=1,width=4, bg='#11390F', fg='white').grid(row=5,column=11, padx=1, pady=1)

def change_label_value(statscap,x,arg1,arg2):
	if arg1 == 'split_1':
		labSplit_1_2R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=1, padx=1, pady=1)
	if arg1 == 'split_2':
		labSplit_1_4R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=3, padx=1, pady=1)
	if arg1 == 'split_3':
		labSplit_2_3R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=5, padx=1, pady=1)
	if arg1 == 'split_4':
		labSplit_2_5R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=7, padx=1, pady=1)
	if arg1 == 'split_5':
		labSplit_3_6R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=9, padx=1, pady=1)
	if arg1 == 'split_6':
		labSplit_4_5R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=11, padx=1, pady=1)
	if arg1 == 'split_7':
		labSplit_3_6R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=1, padx=1, pady=1)
	if arg1 == 'split_8':
		labSplit_5_6R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=3, padx=1, pady=1)
	if arg1 == 'split_9':
		labSplit_5_8R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=5, padx=1, pady=1)
	if arg1 == 'split_10':
		labSplit_6_9R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=7, padx=1, pady=1)
	if arg1 == 'split_11':
		labSplit_7_8R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=9, padx=1, pady=1)
	if arg1 == 'split_12':
		labSplit_7_10R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=11, padx=1, pady=1)
	if arg1 == 'split_13':
		labSplit_8_9R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=2,column=1, padx=1, pady=1)
	if arg1 == 'split_14':
		labSplit_8_11R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=2,column=3, padx=1, pady=1)
	if arg1 == 'split_15':
		labSplit_9_12R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=2,column=5, padx=1, pady=1)
	if arg1 == 'split_16':
		labSplit_10_11R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=2,column=7, padx=1, pady=1)
	if arg1 == 'split_17':
		labSplit_10_13R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=2,column=9, padx=1, pady=1)
	if arg1 == 'split_18':
		labSplit_11_12R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=2,column=11, padx=1, pady=1)
	if arg1 == 'split_19':
		labSplit_11_14R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=3,column=1, padx=1, pady=1)
	if arg1 == 'split_20':
		labSplit_12_15R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=3,column=3, padx=1, pady=1)
	if arg1 == 'split_21':
		labSplit_13_14R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=3,column=5, padx=1, pady=1)
	if arg1 == 'split_22':
		labSplit_13_16R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=3,column=7, padx=1, pady=1)
	if arg1 == 'split_23':
		labSplit_14_15R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=3,column=9, padx=1, pady=1)
	if arg1 == 'split_24':
		labSplit_14_17R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=3,column=11, padx=1, pady=1)
	if arg1 == 'split_25':
		labSplit_15_18R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=4,column=1, padx=1, pady=1)
	if arg1 == 'split_26':
		labSplit_16_17R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=4,column=3, padx=1, pady=1)
	if arg1 == 'split_27':
		labSplit_16_19R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=4,column=5, padx=1, pady=1)
	if arg1 == 'split_28':
		labSplit_17_18R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=4,column=7, padx=1, pady=1)
	if arg1 == 'split_29':
		labSplit_17_20R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=4,column=9, padx=1, pady=1)
	if arg1 == 'split_30':
		labSplit_18_21R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=4,column=11, padx=1, pady=1)
	if arg1 == 'split_31':
		labSplit_19_20R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=5,column=1, padx=1, pady=1)
	if arg1 == 'split_32':
		labSplit_19_22R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=5,column=3, padx=1, pady=1)
	if arg1 == 'split_33':
		labSplit_20_21R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=5,column=5, padx=1, pady=1)
	if arg1 == 'split_34':
		labSplit_20_23R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=5,column=7, padx=1, pady=1)
	if arg1 == 'split_35':
		labSplit_21_24R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=5,column=9, padx=1, pady=1)
	if arg1 == 'split_36':
		labSplit_22_23R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=5,column=11, padx=1, pady=1)
	if arg1 == 'split_37':
		labSplit_22_25R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=6,column=1, padx=1, pady=1)
	if arg1 == 'split_38':
		labSplit_23_24R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=6,column=3, padx=1, pady=1)
	if arg1 == 'split_39':
		labSplit_23_26R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=6,column=5, padx=1, pady=1)
	if arg1 == 'split_40':
		labSplit_24_27R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=6,column=7, padx=1, pady=1)
	if arg1 == 'split_41':
		labSplit_25_26R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=6,column=9, padx=1, pady=1)
	if arg1 == 'split_42':
		labSplit_25_28R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=6,column=11, padx=1, pady=1)
	if arg1 == 'split_43':
		labSplit_26_27R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=7,column=1, padx=1, pady=1)
	if arg1 == 'split_44':
		labSplit_26_29R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=7,column=3, padx=1, pady=1)
	if arg1 == 'split_45':
		labSplit_27_30R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=7,column=5, padx=1, pady=1)
	if arg1 == 'split_46':
		labSplit_28_29R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=7,column=7, padx=1, pady=1)
	if arg1 == 'split_47':
		labSplit_28_31R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=7,column=9, padx=1, pady=1)
	if arg1 == 'split_48':
		labSplit_29_30R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=7,column=11, padx=1, pady=1)
	if arg1 == 'split_49':
		labSplit_29_32R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=8,column=1, padx=1, pady=1)
	if arg1 == 'split_50':
		labSplit_30_33R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=8,column=3, padx=1, pady=1)
	if arg1 == 'split_51':
		labSplit_31_32R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=8,column=5, padx=1, pady=1)
	if arg1 == 'split_52':
		labSplit_31_34R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=8,column=7, padx=1, pady=1)
	if arg1 == 'split_53':
		labSplit_32_33R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=8,column=9, padx=1, pady=1)
	if arg1 == 'split_54':
		labSplit_32_35R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=8,column=11, padx=1, pady=1)
	if arg1 == 'split_55':
		labSplit_33_36R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=9,column=1, padx=1, pady=1)
	if arg1 == 'split_56':
		labSplit_34_35R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=9,column=3, padx=1, pady=1)
	if arg1 == 'split_57':
		labSplit_35_36R = Label(x[2],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=9,column=5, padx=1, pady=1)	
		
	if arg1 == 'single_1':
		labSingle1R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=1, padx=1, pady=1)
	if arg1 == 'single_2':
		labSingle2R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=3, padx=1, pady=1)
	if arg1 == 'single_3':
		labSingle3R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=5, padx=1, pady=1)
	if arg1 == 'single_4':
		labSingle4R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=7, padx=1, pady=1)
	if arg1 == 'single_5':
		labSingle5R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=9, padx=1, pady=1)
	if arg1 == 'single_6':
		labSingle6R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=0,column=11, padx=1, pady=1)
	if arg1 == 'single_7':
		labSingle7R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=1, padx=1, pady=1)
	if arg1 == 'single_8':
		labSingle8R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=3, padx=1, pady=1)
	if arg1 == 'single_9':
		labSingle9R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=5, padx=1, pady=1)
	if arg1 == 'single_10':
		labSingle10R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=7, padx=1, pady=1)
	if arg1 == 'single_11':
		labSingle11R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=9, padx=1, pady=1)
	if arg1 == 'single_12':
		labSingle12R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=1,column=11, padx=1, pady=1)
	if arg1 == 'single_13':
		labSingle13R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=2,column=1, padx=1, pady=1)
	if arg1 == 'single_14':
		labSingle14R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=2,column=3, padx=1, pady=1)
	if arg1 == 'single_15':
		labSingle15R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=2,column=5, padx=1, pady=1)
	if arg1 == 'single_16':
		labSingle16R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=2,column=7, padx=1, pady=1)
	if arg1 == 'single_17':
		labSingle17R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=2,column=9, padx=1, pady=1)
	if arg1 == 'single_18':
		labSingle18R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=2,column=11, padx=1, pady=1)
	if arg1 == 'single_19':
		labSingle19R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=3,column=1, padx=1, pady=1)
	if arg1 == 'single_20':
		labSingle20R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=3,column=3, padx=1, pady=1)
	if arg1 == 'single_21':
		labSingle21R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=3,column=5, padx=1, pady=1)
	if arg1 == 'single_22':
		labSingle22R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=3,column=7, padx=1, pady=1)
	if arg1 == 'single_23':
		labSingle23R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=3,column=9, padx=1, pady=1)
	if arg1 == 'single_24':
		labSingle24R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=3,column=11, padx=1, pady=1)
	if arg1 == 'single_25':
		labSingle25R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=4,column=1, padx=1, pady=1)
	if arg1 == 'single_26':
		labSingle26R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=4,column=3, padx=1, pady=1)
	if arg1 == 'single_27':
		labSingle27R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=4,column=5, padx=1, pady=1)
	if arg1 == 'single_28':
		labSingle28R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=4,column=7, padx=1, pady=1)
	if arg1 == 'single_29':
		labSingle29R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=4,column=9, padx=1, pady=1)
	if arg1 == 'single_30':
		labSingle30R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=4,column=11, padx=1, pady=1)
	if arg1 == 'single_31':
		labSingle31R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=5,column=1, padx=1, pady=1)
	if arg1 == 'single_32':
		labSingle32R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=5,column=3, padx=1, pady=1)
	if arg1 == 'single_33':
		labSingle33R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=5,column=5, padx=1, pady=1)
	if arg1 == 'single_34':
		labSingle34R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=5,column=7, padx=1, pady=1)
	if arg1 == 'single_35':
		labSingle35R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=5,column=9, padx=1, pady=1)
	if arg1 == 'single_36':
		labSingle36R = Label(x[3],text=arg2, height=1,width=4, bg='#11390F', fg='white').grid(row=5,column=11, padx=1, pady=1)
	