# Betplay Roulette Bot GUI V14.0 by Thomas Grant (stats_window.py)

# Libraries
from tkinter import *
import os
from tkinter import Tk, filedialog

import pickle # Save to a file

from statsframes1 import * # Frames for the GUI # Frames for the GUI
from statslabels1 import * # Frames for the GUI

from cas_arrays import * # Cas arrays

global statscap1

def display_stats_window(root,title,btn):

	statscap1 = Toplevel(root)

	statscap1.title(title)
	#here I put a .ico file as a picture on the window top bar.
	if os.path.isfile("images\\wheel2.ico"):
		statscap1.iconbitmap("images\\wheel2.ico")

	statscap1.resizable(width=False, height=False)
	statscap1.configure(background='black')
	statscap1.attributes('-topmost', 'true')
	statscap1.geometry('918x510')

	#Here I see if the file exists.
	if os.path.isfile("data\\statscap1.conf"):
		#Here I read the X and Y positon of the window from when I last closed it.
		with open("data\\statscap1.conf", "r") as conf: 
			statscap1.geometry(conf.read())
	else:
		#Default window position.
		statscap1.geometry('818x510')

	def on_close(btn,statscap1):
		#print('closing')
		btn["state"] = "normal"

		with open("data\\statscap1.conf", "w") as conf:
			conf.write(statscap1.geometry())

		statscap1.destroy()

	statscap1.protocol("WM_DELETE_WINDOW",	lambda arg=btn,arg2 =statscap1: on_close(arg,arg2))

	x = my_statsframes(statscap1) # Load in frames
	statslabels(statscap1,x) # Load in labels

	def display_data(data):
		if 'elements_to_track' in data and 'max_missed_counts' in data:
			elements_to_track = data['elements_to_track']
			max_missed_counts = data['max_missed_counts']

			for i, element in enumerate(elements_to_track):
				bet_name = next(name for name, value in RouletteArrays.__dict__.items() if value == element)
				
				# Even chances
				if bet_name.lower() == 'red':
					change_label_value(statscap1,x,'red',max_missed_counts[i])
				if bet_name.lower() == 'black':
					change_label_value(statscap1,x,'black',max_missed_counts[i])
				if bet_name.lower() == 'high':
					change_label_value(statscap1,x,'high',max_missed_counts[i])
				if bet_name.lower() == 'low':
					change_label_value(statscap1,x,'low',max_missed_counts[i])
				if bet_name.lower() == 'odd':
					change_label_value(statscap1,x,'odd',max_missed_counts[i])
				if bet_name.lower() == 'even':
					change_label_value(statscap1,x,'even',max_missed_counts[i])
				# Even chances
				
				# Dozens / Colums
				if bet_name.lower() == 'doz1':
					change_label_value(statscap1,x,'doz1',max_missed_counts[i])
				if bet_name.lower() == 'doz2':
					change_label_value(statscap1,x,'doz2',max_missed_counts[i])
				if bet_name.lower() == 'doz3':
					change_label_value(statscap1,x,'doz3',max_missed_counts[i])
					
				if bet_name.lower() == 'col1':
					change_label_value(statscap1,x,'col1',max_missed_counts[i])
				if bet_name.lower() == 'col2':
					change_label_value(statscap1,x,'col2',max_missed_counts[i])
				if bet_name.lower() == 'col3':
					change_label_value(statscap1,x,'col3',max_missed_counts[i])
				# Dozens / Colums
				
				# Lines
				if bet_name.lower() == 'line_1':
					change_label_value(statscap1,x,'line_1',max_missed_counts[i])
				if bet_name.lower() == 'line_2':
					change_label_value(statscap1,x,'line_2',max_missed_counts[i])
				if bet_name.lower() == 'line_3':
					change_label_value(statscap1,x,'line_3',max_missed_counts[i])
				if bet_name.lower() == 'line_4':
					change_label_value(statscap1,x,'line_4',max_missed_counts[i])
				if bet_name.lower() == 'line_5':
					change_label_value(statscap1,x,'line_5',max_missed_counts[i])
				if bet_name.lower() == 'line_6':
					change_label_value(statscap1,x,'line_6',max_missed_counts[i])
				if bet_name.lower() == 'line_7':
					change_label_value(statscap1,x,'line_7',max_missed_counts[i])
				if bet_name.lower() == 'line_8':
					change_label_value(statscap1,x,'line_8',max_missed_counts[i])
				if bet_name.lower() == 'line_9':
					change_label_value(statscap1,x,'line_9',max_missed_counts[i])
				if bet_name.lower() == 'line_10':
					change_label_value(statscap1,x,'line_10',max_missed_counts[i])
				if bet_name.lower() == 'line_11':
					change_label_value(statscap1,x,'line_11',max_missed_counts[i])
				# Lines
				
				# Corners
				if bet_name.lower() == 'corner_1':
					change_label_value(statscap1,x,'corner_1',max_missed_counts[i])
				if bet_name.lower() == 'corner_2':
					change_label_value(statscap1,x,'corner_2',max_missed_counts[i])
				if bet_name.lower() == 'corner_3':
					change_label_value(statscap1,x,'corner_3',max_missed_counts[i])
				if bet_name.lower() == 'corner_4':
					change_label_value(statscap1,x,'corner_4',max_missed_counts[i])
				if bet_name.lower() == 'corner_5':
					change_label_value(statscap1,x,'corner_5',max_missed_counts[i])
				if bet_name.lower() == 'corner_6':
					change_label_value(statscap1,x,'corner_6',max_missed_counts[i])
				if bet_name.lower() == 'corner_7':
					change_label_value(statscap1,x,'corner_7',max_missed_counts[i])
				if bet_name.lower() == 'corner_8':
					change_label_value(statscap1,x,'corner_8',max_missed_counts[i])
				if bet_name.lower() == 'corner_9':
					change_label_value(statscap1,x,'corner_9',max_missed_counts[i])
				if bet_name.lower() == 'corner_10':
					change_label_value(statscap1,x,'corner_10',max_missed_counts[i])
				if bet_name.lower() == 'corner_11':
					change_label_value(statscap1,x,'corner_11',max_missed_counts[i])
				if bet_name.lower() == 'corner_12':
					change_label_value(statscap1,x,'corner_12',max_missed_counts[i])
				if bet_name.lower() == 'corner_13':
					change_label_value(statscap1,x,'corner_13',max_missed_counts[i])
				if bet_name.lower() == 'corner_14':
					change_label_value(statscap1,x,'corner_14',max_missed_counts[i])
				if bet_name.lower() == 'corner_15':
					change_label_value(statscap1,x,'corner_15',max_missed_counts[i])
				if bet_name.lower() == 'corner_16':
					change_label_value(statscap1,x,'corner_16',max_missed_counts[i])
				if bet_name.lower() == 'corner_17':
					change_label_value(statscap1,x,'corner_17',max_missed_counts[i])
				if bet_name.lower() == 'corner_18':
					change_label_value(statscap1,x,'corner_18',max_missed_counts[i])
				if bet_name.lower() == 'corner_19':
					change_label_value(statscap1,x,'corner_19',max_missed_counts[i])
				if bet_name.lower() == 'corner_20':
					change_label_value(statscap1,x,'corner_20',max_missed_counts[i])
				if bet_name.lower() == 'corner_21':
					change_label_value(statscap1,x,'corner_21',max_missed_counts[i])
				if bet_name.lower() == 'corner_22':
					change_label_value(statscap1,x,'corner_22',max_missed_counts[i])
				# Corners
				
				# Streets				
				if bet_name.lower() == 'street_1':
					change_label_value(statscap1,x,'street_1',max_missed_counts[i])
				if bet_name.lower() == 'street_2':
					change_label_value(statscap1,x,'street_2',max_missed_counts[i])
				if bet_name.lower() == 'street_3':
					change_label_value(statscap1,x,'street_3',max_missed_counts[i])
				if bet_name.lower() == 'street_4':
					change_label_value(statscap1,x,'street_4',max_missed_counts[i])
				if bet_name.lower() == 'street_5':
					change_label_value(statscap1,x,'street_5',max_missed_counts[i])
				if bet_name.lower() == 'street_6':
					change_label_value(statscap1,x,'street_6',max_missed_counts[i])
				if bet_name.lower() == 'street_7':
					change_label_value(statscap1,x,'street_7',max_missed_counts[i])
				if bet_name.lower() == 'street_8':
					change_label_value(statscap1,x,'street_8',max_missed_counts[i])
				if bet_name.lower() == 'street_9':
					change_label_value(statscap1,x,'street_9',max_missed_counts[i])
				if bet_name.lower() == 'street_10':
					change_label_value(statscap1,x,'street_10',max_missed_counts[i])
				if bet_name.lower() == 'street_11':
					change_label_value(statscap1,x,'street_11',max_missed_counts[i])
				if bet_name.lower() == 'street_12':
					change_label_value(statscap1,x,'street_12',max_missed_counts[i])
				# Streets

		else:
			print("Invalid or missing data keys.")

	def load_data():
		global data
		dataload["state"] = "disabled"
		current_directory = os.getcwd()
		# Open a file dialog for the user to select a pickle file
		file_path = filedialog.askopenfilename(initialdir=current_directory, filetypes=[("Pickle Files", "*.pkl")])

		dataload["state"] = "normal"

		if file_path:
			# Load the data from the pickle file
			with open(file_path, "rb") as file:
				data = pickle.load(file)
				display_data(data)
		else:
			print("No file selected.")

	dataload = Button(x[1], text='Load Data', width=12, bg='#00FFFF', font=('Verdana', 9, 'bold'), 
		command=load_data) # 
	dataload.place(x=680, y=6)

	# Load in data file to set labels.
	if os.path.isfile('numdata\\stats_data\\random\\data.pkl'):
		with open('numdata\\stats_data\\random\\data.pkl', 'rb') as file:
			data = pickle.load(file)
			display_data(data)

		