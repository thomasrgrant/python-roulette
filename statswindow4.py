# Libraries
from tkinter import *
import os

from statsframes4 import * # Frames for the GUI # Frames for the GUI
from statslabels4 import * # Frames for the GUI

global statscap4

def display_stats_window4(root,title,btn4):

	statscap4 = Toplevel(root)

	statscap4.title(title)
	#here I put a .ico file as a picture on the window top bar.
	if os.path.isfile("images\\wheel2.ico"):
		statscap4.iconbitmap("images\\wheel2.ico")

	statscap4.resizable(width=False, height=False)
	statscap4.configure(background='black')
	statscap4.attributes('-topmost', 'true')
	statscap4.geometry('918x510')

	#Here I see if the file exists.
	if os.path.isfile("data\\statscap4.conf"):
		#Here I read the X and Y positon of the window from when I last closed it.
		with open("data\\statscap4.conf", "r") as conf: 
			statscap4.geometry(conf.read())
	else:
		#Default window position.
		statscap4.geometry('918x510')

	def on_close(btn4,statscap4):
		#print('closing')
		btn4["state"] = "normal"

		with open("data\\statscap4.conf", "w") as conf:
			conf.write(statscap4.geometry())

		statscap4.destroy()

	statscap4.protocol("WM_DELETE_WINDOW",  lambda arg=btn4,arg2 =statscap4: on_close(arg,arg2))

	x = my_statsframes4(statscap4) # Load in frames
	statslabels4(statscap4,x) # Load in frames