##################################### Main Labels ##################################################
# labels
from tkinter import *
from myframes import * # Frames for the GUI

#from myframes import frame_
def my_labels(root,x):
	# This section of labels is for the Roulette Table Squares with Numbers.
	#slice the tuple to get each frame eg. x[0] is the first frame, x[1] is the second frame
	
	Settingslab = Label(x[5], text='Settings', height=1,width=16, bg='black', fg='white')
	Settingslab.place(x=3, y=3)
	
	SpinsLab =Label(x[5], text='Spins', height=1,width=8, bg='#31859B',fg='white', anchor='w')
	SpinsLab.place(x=3, y=28)
	
	BalanceLab =Label(x[5], text='Balance', height=1,width=8, bg='#31859B',fg='white', anchor='w')
	BalanceLab.place(x=3, y=62)

	OverallSettings = Label(x[7], text='BetVoyager Bet Settings', height=1,width=59, bg='black', fg='white')
	OverallSettings.place(x=3, y=3)
	
	EClab = Label(x[7],text="Even Chances", 
		height=1,width=15, bg='#31859B', fg='Yellow', anchor='w',font=('Verdana', 12, 'bold'))
	EClab.place(x=6, y=24)
	
	DozCollab = Label(x[7],text="Doz & Col", 
		height=1,width=15, bg='#31859B', fg='Yellow', anchor='w',font=('Verdana', 12, 'bold'))
	DozCollab.place(x=156, y=24)
	
	Lineslab = Label(x[7],text="Lines", 
		height=1,width=15, bg='#31859B', fg='Yellow', anchor='w',font=('Verdana', 12, 'bold'))
	Lineslab.place(x=156, y=86)
	
	Cornerslab = Label(x[7],text="Corners", 
		height=1,width=15, bg='#31859B', fg='Yellow', anchor='w',font=('Verdana', 12, 'bold'))
	Cornerslab.place(x=156, y=128)
	
	Streetlab = Label(x[7],text="Streets", 
		height=1,width=10, bg='#31859B', fg='Yellow', anchor='w',font=('Verdana', 12, 'bold'))
	Streetlab.place(x=316, y=24)
	
	Numberlab = Label(x[7],text="Numbers", 
		height=1,width=10, bg='#31859B', fg='Yellow', anchor='w',font=('Verdana', 12, 'bold'))
	Numberlab.place(x=316, y=68)
	
	Splitlab = Label(x[7],text="Splits", 
		height=1,width=10, bg='#31859B', fg='Yellow', anchor='w',font=('Verdana', 12, 'bold'))
	Splitlab.place(x=316, y=108)

	labels = []
	labels_data = {}
	
	# x[2] = frame2 frame for number labels x[2] is the 3rd frame in frames
	lab01=Label(x[2], text='1', height=2,width=4, bg='red', fg='white')
	lab01.grid(row=2,column=0, padx=1, pady=1)
	labels_data['1'] = 'red'  # Store original color in the dictionary

	lab02=Label(x[2], text='2', height=2,width=4, bg='black', fg='white')
	lab02.grid(row=1,column=0, padx=1, pady=1)
	labels_data['2'] = 'black'	# Store original color in the dictionary

	lab03=Label(x[2], text='3', height=2,width=4, bg='red', fg='white')
	lab03.grid(row=0,column=0, padx=1, pady=1)
	labels_data['3'] = 'red'  # Store original color in the dictionary

	lab04=Label(x[2], text='4', height=2,width=4, bg='black', fg='white')
	lab04.grid(row=2,column=1, padx=1, pady=1)
	labels_data['4'] = 'black'	# Store original color in the dictionary

	lab05=Label(x[2], text='5', height=2,width=4, bg='red', fg='white')
	lab05.grid(row=1,column=1, padx=1, pady=1)
	labels_data['5'] = 'red'  # Store original color in the dictionary

	lab06=Label(x[2], text='6', height=2,width=4, bg='black', fg='white')
	lab06.grid(row=0,column=1, padx=1, pady=1)
	labels_data['6'] = 'black'	# Store original color in the dictionary

	lab07=Label(x[2], text='7', height=2,width=4, bg='red', fg='white')
	lab07.grid(row=2,column=2, padx=1, pady=1)
	labels_data['7'] = 'red'  # Store original color in the dictionary

	lab08=Label(x[2], text='8', height=2,width=4, bg='black', fg='white')
	lab08.grid(row=1,column=2, padx=1, pady=1)
	labels_data['8'] = 'black'	# Store original color in the dictionary

	lab09=Label(x[2], text='9', height=2,width=4, bg='red', fg='white')
	lab09.grid(row=0,column=2, padx=1, pady=1)
	labels_data['9'] = 'red'  # Store original color in the dictionary

	lab10=Label(x[2], text='10', height=2,width=4, bg='black', fg='white')
	lab10.grid(row=2,column=3, padx=1, pady=1)
	labels_data['10'] = 'black'	 # Store original color in the dictionary

	lab11=Label(x[2], text='11', height=2,width=4, bg='black', fg='white')
	lab11.grid(row=1,column=3, padx=1, pady=1)
	labels_data['11'] = 'black'	 # Store original color in the dictionary

	lab12=Label(x[2], text='12', height=2,width=4, bg='red', fg='white')
	lab12.grid(row=0,column=3, padx=1, pady=1)
	labels_data['12'] = 'red'  # Store original color in the dictionary

	lab13=Label(x[2], text='13', height=2,width=4, bg='black', fg='white')
	lab13.grid(row=2,column=4, padx=1, pady=1)
	labels_data['13'] = 'black'	 # Store original color in the dictionary

	lab14=Label(x[2], text='14', height=2,width=4, bg='red', fg='white')
	lab14.grid(row=1,column=4, padx=1, pady=1)
	labels_data['14'] = 'red'  # Store original color in the dictionary

	lab15=Label(x[2], text='15', height=2,width=4, bg='black', fg='white')
	lab15.grid(row=0,column=4, padx=1, pady=1)
	labels_data['15'] = 'black'	 # Store original color in the dictionary

	lab16=Label(x[2], text='16', height=2,width=4, bg='red', fg='white')
	lab16.grid(row=2,column=5, padx=1, pady=1)
	labels_data['16'] = 'red'  # Store original color in the dictionary

	lab17=Label(x[2], text='17', height=2,width=4, bg='black', fg='white')
	lab17.grid(row=1,column=5, padx=1, pady=1)
	labels_data['17'] = 'black'	 # Store original color in the dictionary

	lab18=Label(x[2], text='18', height=2,width=4, bg='red', fg='white')
	lab18.grid(row=0,column=5, padx=1, pady=1)
	labels_data['18'] = 'red'  # Store original color in the dictionary

	lab19=Label(x[2], text='19', height=2,width=4, bg='red', fg='white')
	lab19.grid(row=2,column=6, padx=1, pady=1)
	labels_data['19'] = 'red'  # Store original color in the dictionary

	lab20=Label(x[2], text='20', height=2,width=4, bg='black', fg='white')
	lab20.grid(row=1,column=6, padx=1, pady=1)
	labels_data['20'] = 'black'	 # Store original color in the dictionary

	lab21=Label(x[2], text='21', height=2,width=4, bg='red', fg='white')
	lab21.grid(row=0,column=6, padx=1, pady=1)
	labels_data['21'] = 'red'  # Store original color in the dictionary

	lab22=Label(x[2], text='22', height=2,width=4, bg='black', fg='white')
	lab22.grid(row=2,column=7, padx=1, pady=1)
	labels_data['22'] = 'black'	 # Store original color in the dictionary

	lab23=Label(x[2], text='23', height=2,width=4, bg='red', fg='white')
	lab23.grid(row=1,column=7, padx=1, pady=1)
	labels_data['23'] = 'red'  # Store original color in the dictionary

	lab24=Label(x[2], text='24', height=2,width=4, bg='black', fg='white')
	lab24.grid(row=0,column=7, padx=1, pady=1)
	labels_data['24'] = 'black'	 # Store original color in the dictionary

	lab25=Label(x[2], text='25', height=2,width=4, bg='red', fg='white')
	lab25.grid(row=2,column=8, padx=1, pady=1)
	labels_data['25'] = 'red'  # Store original color in the dictionary

	lab26=Label(x[2], text='26', height=2,width=4, bg='black', fg='white')
	lab26.grid(row=1,column=8, padx=1, pady=1)
	labels_data['26'] = 'black'	 # Store original color in the dictionary

	lab27=Label(x[2], text='27', height=2,width=4, bg='red', fg='white')
	lab27.grid(row=0,column=8, padx=1, pady=1)
	labels_data['27'] = 'red'  # Store original color in the dictionary

	lab28=Label(x[2], text='28', height=2,width=4, bg='black', fg='white')
	lab28.grid(row=2,column=9, padx=1, pady=1)
	labels_data['28'] = 'black'	 # Store original color in the dictionary

	lab29=Label(x[2], text='29', height=2,width=4, bg='black', fg='white')
	lab29.grid(row=1,column=9, padx=1, pady=1)
	labels_data['29'] = 'black'	 # Store original color in the dictionary

	lab30=Label(x[2], text='30', height=2,width=4, bg='red', fg='white')
	lab30.grid(row=0,column=9, padx=1, pady=1)
	labels_data['30'] = 'red'  # Store original color in the dictionary

	lab31=Label(x[2], text='31', height=2,width=4, bg='black', fg='white')
	lab31.grid(row=2,column=10, padx=1, pady=1)
	labels_data['31'] = 'black'	 # Store original color in the dictionary

	lab32=Label(x[2], text='32', height=2,width=4, bg='red', fg='white')
	lab32.grid(row=1,column=10, padx=1, pady=1)
	labels_data['32'] = 'red'  # Store original color in the dictionary

	lab33=Label(x[2], text='33', height=2,width=4, bg='black', fg='white')
	lab33.grid(row=0,column=10, padx=1, pady=1)
	labels_data['33'] = 'black'	 # Store original color in the dictionary

	lab34=Label(x[2], text='34', height=2,width=4, bg='red', fg='white')
	lab34.grid(row=2,column=11, padx=1, pady=1)
	labels_data['34'] = 'red'  # Store original color in the dictionary

	lab35=Label(x[2], text='35', height=2,width=4, bg='black', fg='white')
	lab35.grid(row=1,column=11, padx=1, pady=1)
	labels_data['35'] = 'black'	 # Store original color in the dictionary

	lab36=Label(x[2], text='36', height=2,width=4, bg='red', fg='white')
	lab36.grid(row=0,column=11, padx=1, pady=1)
	labels_data['36'] = 'red'  # Store original color in the dictionary

	return [
	lab01, lab02, lab03, lab04, lab05, lab06,
	lab07, lab08, lab09, lab10, lab11, lab12,
	lab13, lab14, lab15, lab16, lab17, lab18,
	lab19, lab20, lab21, lab22, lab23, lab24,
	lab25, lab26, lab27, lab28, lab29, lab30,
	lab31, lab32, lab33, lab34, lab35, lab36
	], labels_data	# Return the list of labels	 
	
def display_label(root,x,num,col):
	# lab_display=Label(x[1], text=num, height=2,width=4, bg='black', fg=col, font=('Verdana', 14, 'bold'))
	# lab_display.place(x=490, y=120, height=50,width=46)

	if hasattr(root, 'lab_display'):
		root.lab_display.config(text=num, fg=col, bg='black')
	else:
		root.lab_display = Label(x[1], text=num, height=2, width=4, bg='black', fg=col)
		root.lab_display.place(x=490, y=120, height=20, width=46)

def blanklabel_message(root,x,message):
	messagelab = Label(x[1], text=message, height=1,width=59, bg='black', fg='white', anchor='w')
	messagelab.place(x=3, y=120)

	# root.lab_display = Label(x[1], text=7, height=2, width=4, bg='black', fg='white')
	# root.lab_display.place(x=488, y=120, height=20, width=46)
##################################### Main Labels ################################################## 