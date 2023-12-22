# Libraries
from tkinter import *
import os

from statsframes3 import * # Frames for the GUI # Frames for the GUI
from statslabels3 import * # Frames for the GUI

global statscap3

def display_stats_window3(root,title,btn3):

	statscap3 = Toplevel(root)

	statscap3.title(title)
	#here I put a .ico file as a picture on the window top bar.
	if os.path.isfile("images\\wheel2.ico"):
		statscap3.iconbitmap("images\\wheel2.ico")

	statscap3.resizable(width=False, height=False)
	statscap3.configure(background='black')
	statscap3.attributes('-topmost', 'true')
	statscap3.geometry('756x510')

	#Here I see if the file exists.
	if os.path.isfile("data\\statscap3.conf"):
		#Here I read the X and Y positon of the window from when I last closed it.
		with open("data\\statscap3.conf", "r") as conf: 
			statscap3.geometry(conf.read())
	else:
		#Default window position.
		statscap3.geometry('756x510')

	def on_close(btn3,statscap3):
		#print('closing')
		btn3["state"] = "normal"

		with open("data\\statscap3.conf", "w") as conf:
			conf.write(statscap3.geometry())

		statscap3.destroy()

	statscap3.protocol("WM_DELETE_WINDOW",  lambda arg=btn3,arg2 =statscap3: on_close(arg,arg2))

	x = my_statsframes3(statscap3) # Load in frames
	statslabels3(statscap3,x) # Load in frames