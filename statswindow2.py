# Betplay Roulette Bot GUI V15.0 by Thomas Grant (stats_window2.py)

# Libraries
from tkinter import *
import os
from tkinter import Tk, filedialog
from statsframes2 import * # Frames for the GUI # Frames for the GUI
from statslabels2 import * # Frames for the GUI

import pickle # Save to a file

from cas_arrays import * # Cas arrays

global statscap2

def display_stats_window2(root,title,btn2):

	statscap2 = Toplevel(root)

	statscap2.title(title)
	#here I put a .ico file as a picture on the window top bar.
	if os.path.isfile("images\\wheel2.ico"):
		statscap2.iconbitmap("images\\wheel2.ico")

	statscap2.resizable(width=False, height=False)
	statscap2.configure(background='black')
	statscap2.attributes('-topmost', 'true')
	statscap2.geometry('756x510')

	#Here I see if the file exists.
	if os.path.isfile("data\\statscap2.conf"):
		#Here I read the X and Y positon of the window from when I last closed it.
		with open("data\\statscap2.conf", "r") as conf: 
			statscap2.geometry(conf.read())
	else:
		#Default window position.
		statscap2.geometry('756x510')

	def on_close(btn2,statscap2):
		#print('closing')
		btn2["state"] = "normal"

		with open("data\\statscap2.conf", "w") as conf:
			conf.write(statscap2.geometry())

		statscap2.destroy()

	statscap2.protocol("WM_DELETE_WINDOW",	lambda arg=btn2,arg2 =statscap2: on_close(arg,arg2))

	x = my_statsframes2(statscap2) # Load in frames
	statslabels2(statscap2,x) # Load in frames
	
	def display_data(data):
		if 'elements_to_track' in data and 'max_missed_counts' in data:
			elements_to_track = data['elements_to_track']
			max_missed_counts = data['max_missed_counts']

			for i, element in enumerate(elements_to_track):
				bet_name = next(name for name, value in RouletteArrays.__dict__.items() if value == element)
				
				for i in range(1, 58):
					split_name = f'split_{i}'
					if bet_name.lower() == split_name:
						change_label_value(statscap2, x, split_name, max_missed_counts[i])
					
				for i in range(1, 37):
					single_name = f'single_{i}'
					if bet_name.lower() == single_name:
						change_label_value(statscap2, x, single_name, max_missed_counts[i])
	
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
	dataload.place(x=580, y=6)
	
	# Load in data file to set labels.
	if os.path.isfile('numdata\\stats_data\\random\\data.pkl'):
		with open('numdata\\stats_data\\random\\data.pkl', 'rb') as file:
			data = pickle.load(file)
			display_data(data)