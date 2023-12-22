# Toms BetVoyager No Zero Roulette Bot BV-Flash V3.2 (Debug Option Added)
# Use FlashBrowser (FlashBrowser.exe)
# to play https://betvoyager.com/ No Zero Roulette Flash Version.

# https://betvoyager.com/equal-odds/?p=E4AO05&lid=17 # Main Page
# https://betvoyager.com/signup/?p=E4AO05&lid=2 # Sign up page
# BetVoyager on winning The House Fee stands at 10%,

##################################### Librarys ###############################
import subprocess
import psutil
import pygetwindow as gw
import cv2

# Calculation libs and possible speed improvment libs.
import numpy as np
import pandas as pd
from numba import jit
import math
# Calculation libs and possible speed improvment libs

import tkinter as tk
from tkinter import * 
from tkinter import scrolledtext

import time #install library
from datetime import datetime

import os #install library
from os import path #install library
import linecache

import random
from random import randint,shuffle #install library

import threading

import ThreadPoolExecutorPlus

import pyautogui #install library

# from PIL import ImageTk,Image,ImageGrab #install library
import PIL.Image

from decimal import Decimal, ROUND_UP, getcontext

import pickle # Save to a file

import pdb # debug tool
# Common commands include:
# n (next): Execute the current line and stop at the first possible occasion.
# c (continue): Continue execution until the next breakpoint.
# q (quit): Quit the debugger and abort the program.
# p variable (print): Print the value of the variable. p variable (p x y etc)
# l (list): Show the source code around the current line.
# pdb.set_trace() place this where you might have issues to move through the code.
# pdb.set_trace()  # n (next), c (continue) q (quit) p variable (print) l (list)

# import .py Library files
# This is where import my python files that are used in the script.
import json # to load in extenal coord files

from folders import * # this makes the empty folders to store data.

from titles import * # Titles for the GUI windows.

# Design of GUI
from myframes import * # Frames for the GUI

from mylabels import * # Labels for the GUI
# Design of GUI

from utils import * # List box and text box

from about import * # My about me window add in BV link

from showcap_bv import * # display the images from the roulette table.

# stats windows
from statswindow1 import *
from statswindow2 import *
from statswindow3 import *
from statswindow4 import *
# stats windows

from start_BV import * # This opens up the flashbrowser and goes to betvoyager.com

from table_functions import *
# import .py Library files
##################################### Librarys ###############################

# Constants (Tried to get the balance to work with Decimal but could not get it to work.)
BASE_STAKE = Decimal('0.05')  # Use Decimal for precise arithmetic

# Function to handle floating-point precision issues
def round_decimal(value, precision=2):
	return Decimal(str(value)).quantize(Decimal('1e-{0}'.format(precision)))

getcontext().prec = 8
# Constants (Tried to get the balance to work with Decimal but could not get it to work.)

##################################### Main Window ############################
root=Tk()
# Setting background color of the root window
#root.configure(background='#11390F')
root.configure(background='black')

# Configure font for the root window
root.option_add('*Font', ('Verdana', 9, 'bold')) # font=('Verdana', 10, 'bold')

# window attributes
root.resizable(width=False, height=False)

# '-topmost', 'true' keeps the window on top of other windows.
root.attributes('-topmost', 'true')
root.geometry('572x221')
# window attributes

# title
root.title(main_title) # from titles import * # Titles for the GUI windows.

#.ico image for window
if os.path.isfile("images\\me.ico"): # Here I see if the file exists.
	root.iconbitmap("images\\me.ico")

# save the x and y position of the window to a file
# Here I save the x and y position of the window to a file "myapp.conf"
if os.path.isfile("data\\myapp.conf"): # Here I see if the file exists.
	#Here I read the X and Y positon of the window from when I last closed it.
	with open("data\\myapp.conf", "r") as conf: 
		root.geometry(conf.read())
		conf.close()
else:
	#Default window position.
	root.geometry('572x221')

# save the x and y position of the window to a file
def on_close_main():
	#Here I write the X Y position of the window to a file "myapp.conf"
	
	# save_settings() # using pickle

	root.geometry('572x221') # This returns the GUI window to its original size before closing.

	root.after(100, real_close) 

def real_close():
	with open("data\\myapp.conf", "w") as conf: 
		conf.write(root.geometry()) # Here I save the x and y position of the window to a file "myapp.conf"
		conf.close()
	root.destroy()	

root.protocol("WM_DELETE_WINDOW",  on_close_main)
# save the x and y position of the window to a file

# window GUI Graphics Frames Labels
# Load in Frames
x = my_frames(root) # Load in frames from myframes import * # Frames for the GUI

# Load in Labels
my_labels(root,x) # Load in frames from mylabels import * # Labels for the GUI
# window GUI Graphics Frames Labels

# window text boxes to display data.
# List box to insert the incoming numbers from RNG or the roulette table.
create_list_box(root)

# Text box to display what is going on in the script. (Instead of print)
text_box = create_text_box(root)
# window text boxes to display data.
##################################### Main Window ############################

##################################### Main Code (defs & class) #####################
# Entry Fields
# Spin Entry frame
spin_var = StringVar()
# Spin Entry frame
def spinxamount(event):
	try:
		spin_amount_str = spin_var.get().strip()
		
		if not spin_amount_str:
			raise ValueError("Please enter a number")
			
		spin_amount_value = int(spin_amount_str)
		
		if spin_amount_value <= 0 or spin_amount_value < 30:
			raise ValueError("Please enter a positive number greater than or equal to 30")
		if spin_amount_value < 30:
			blanklabel_message(root, x, 'The spin amount min should be 30')
			spin_amount_value = 30	# Set a default value of 30
			spinamount.delete(0, "end")	 # Clear the current value in the spinamount entry
			spinamount.insert(0, spin_amount_value)	 # Set the default value in the spinamount entry
			
		append_text(text_box, f'The Roulette Wheel will spin for {spin_amount_value} spins')
		blanklabel_message(root, x, f'The Roulette Wheel will spin for {spin_amount_value} spins')
						
	except ValueError as e:
		error_message = "You did not enter a valid number" if "invalid literal for int() with base 10" in str(e) else str(e)
		append_text(text_box, error_message)
		blanklabel_message(root, x, error_message)
		spinamount.delete(0, 'end')	 # Clear the entry widget
		
frameEntry = Frame(x[5], bg='#31859B', highlightbackground="black", highlightthickness=2)
frameEntry.place(x=73, y=26, width=64, height=25)#entry border

spinamount = Spinbox(frameEntry, textvariable=spin_var, from_=1, to=9999, width=5)
spinamount.bind("<Return>", spinxamount)
spinamount.place(x=0, y=0)	# Adjust placement within the frame

spinamount.delete(0, "end")	 # Clear the current value in the spinamount entry
spinamount.insert(0, 30)
# Spin Entry frame

# Balance Entry frame
balance_var = StringVar()
def balancexamount(event):
	try:
		balance_input_str = balance_var.get().strip()
		
		if not balance_input_str:
			raise ValueError("Please enter a number")
			
		# Convert the input to a float
		balance_input = float(balance_input_str)
		
		if not math.isfinite(balance_input):
			raise ValueError("Invalid number")
			
		append_text(text_box, f"You have entered a balance of {balance_input}")
		append_text(text_box, "Balance is NOT used in the script as I could not get it to work"
					  "\nHowever, I may be able to get the balance to work later on.")
		blanklabel_message(root, x, f'You have entered a balance of {balance_input}')
		
	except ValueError as e:
		error_message = "You did not enter a valid number" if "invalid literal for float()" in str(e) else str(e)
		append_text(text_box, error_message)
		balance_amount.delete(0, 'end')	 # Clear the entry widget
		
def validate_input(event):
	value = balance_var.get()
	# Remove non-numeric and non-decimal characters
	cleaned_value = ''.join(char for char in value if char.isdigit() or char == '.')

	# Update the entry field with cleaned value
	balance_var.set(cleaned_value)

	# Call balancexamount with the cleaned value
	balancexamount(cleaned_value)

BalanceframeEntry = Frame(x[5], bg='#31859B', highlightbackground="black", highlightthickness=2)
BalanceframeEntry.place(x=73, y=60, width=64, height=25)#entry border

balance_amount = Entry(x[5], textvariable=balance_var, width=6)
balance_amount.bind("<Return>",validate_input)
balance_amount.place(x=76, y=63)	# Adjust placement within the frame
# Balance Entry frame  
# Entry Fields

# checkboxs (these are used as an option button to save or not to save data)
var1 = IntVar()
var2 = IntVar()
c1 = Checkbutton(x[5], bg='#31859B', text='Save Data', font=('Verdana', 10, 'bold'),
			variable=var1, onvalue=1, offvalue=0)
c1.place(x=3, y=86)

# Checkbox to save spins
c2 = Checkbutton(x[5], bg='#31859B', text='Save Spins', font=('Verdana', 10, 'bold'),
			variable=var2, onvalue=1, offvalue=0)
c2.place(x=3, y=106)
				
def is_save_data_checked():
	return var1.get()

def is_save_spins_checked():
	return var2.get()
# checkboxs (these are used as an option button to save or not to save data)

# button commands
# ~~~~~~~~~~~~~~~ Stats Windows ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~ Stats 1
def display_stats1_window_button():
	display_stats1(display_stats_window,root,stats_title1,buttons.butstats1)
	
def display_stats1(display_stats_window,root,stats_title1,butstats1):
	display_stats_window(root,stats_title1,butstats1)
	buttons.butstats1["state"] = "disabled"
# ~~~~~~~~~~~~~~~ Stats 1

# ~~~~~~~~~~~~~~~ Stats 2
def display_stats2_window_button():
	display_stats2(display_stats_window2,root,stats_title2,buttons.butstats2)
	
def display_stats2(display_stats_window2,root,stats_title2,butstats2):
	display_stats_window2(root,stats_title2,butstats2)
	buttons.butstats2["state"] = "disabled"
# ~~~~~~~~~~~~~~~ Stats 2

# ~~~~~~~~~~~~~~~ Stats 3
def display_stats3_window_button():
	display_stats3(display_stats_window3,root,stats_title3,buttons.butstats3)
	
def display_stats3(display_stats_window3,root,stats_title3,butstats3):
	display_stats_window3(root,stats_title3,butstats3)
	buttons.butstats3["state"] = "disabled"
# ~~~~~~~~~~~~~~~ Stats 3

# ~~~~~~~~~~~~~~~ Stats 4
def display_stats4_window_button():
	display_stats4(display_stats_window4,root,stats_title4,buttons.butstats4)
	
def display_stats4(display_stats_window4,root,stats_title4,butstats4):
	display_stats_window4(root,stats_title4,butstats4)
	buttons.butstats4["state"] = "disabled"
# ~~~~~~~~~~~~~~~ Stats 4
# ~~~~~~~~~~~~~~~ Stats Windows ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def btnClickFunction(): #defualt command (just prints 'clicked in the output') use this def for testing.
	blanklabel_message(root,x,'button clicked') # use this for error messages

# Chose Mode (RNG or BV) section
def hideimages():
	#The framec is where the chose casino pictures are on.
	my_frames.framec.destroy()
	
def RNGMode():
	hideimages()
	buttons.butRNG["state"] = "normal"
	buttons.spinB["state"] = "disabled"
	root.geometry('572x389') # Tall window
	
def choseNoZeroCasino():
	hideimages()
	append_text(text_box,'Ready to play on BetVoyager')
	buttons.butRNG["state"] = "disabled"
	buttons.spinB["state"] = "normal"
	root.geometry('572x389') # Tall window
	
def showchoice():
	# choice frames
	my_frames.framec = Frame(root, bg='#31859B', highlightbackground="black", highlightthickness=2)#frame border for numbers
	my_frames.framec.place(x=18, y=18, width=533, height=182) #frame using x y w h
	
	rnglab = Label(my_frames.framec, text='Chose the \nNo Zero Table\n to play on\nor try the RNG', 
		height=4,width=14, bg='green', fg='white', borderwidth = 3, relief="sunken", font=('Verdana', 11, 'bold'))
	rnglab.place(x=190, y=3)
	
	# choice Button
	global photo,photo2,photo3
	
	photo = PhotoImage(file = "images\\choice\\nz_flash.png")
	
	photo3 = PhotoImage(file = "images\\choice\\rng.png")
	
	NZButt = Button(my_frames.framec, text = 'Chose Casino!',image =photo ,command=choseNoZeroCasino,
		width=167, height=165)
	NZButt.place(x=3, y=3)

	rngButt = Button(my_frames.framec, text = 'Chose Casino!',image =photo3 ,command=RNGMode,
		width=167, height=165)
	rngButt.place(x=353, y=1)
# Chose Mode (RNG or BV) section

# window size change defs
def normalwin():
	root.geometry('572x221')  # Change the window size as needed
	
def largewin():
	current_geometry = root.geometry()
	if '572x221' in current_geometry:  # Check if the window is in normal state
		root.geometry('572x389')  # Change the window size to be larger
	else:
		root.geometry('572x221')
					
def widewin():
	current_geometry = root.geometry()
	if '572x221' in current_geometry:  # Check if the window is in normal state
		root.geometry('1233x221')  # Change the window size to be larger 737x221
	else:
		root.geometry('572x221')	
# window size change defs

# about window
def showaboutwin(aboutwindow,root,about_title,butcapimg):
	aboutwindow(root,about_title,butcapimg)
	buttons.aboutB["state"] = "disabled"
	
def about_window_show(): # Show the about me window.
	showaboutwin(aboutwindow,root,about_title,buttons.aboutB)
# about window

# showscaptureimages
def get_showscaptureimages():
	showscaptureimages(showscaptureimages_widow_bv_game,root,showcap_title,buttons.butcapimg)
	
def showscaptureimages(showscaptureimages_widow_bc_game,root,showcap_title,butcapimg):
	showscaptureimages_widow_bv_game(root,showcap_title,butcapimg) # see if you can modify this.
	buttons.butcapimg["state"] = "disabled"
# showscaptureimages

# Settings for the GUI
def save_settings():
	spinamount_value = spinamount.get()
	Balanceamount_value = balance_amount.get()

	if spinamount_value == "":
		spinamount_value = 30
		spinamount.delete(0, 'end')
		spinamount.insert(0,spinamount_value)

	if Balanceamount_value == "":
		Balanceamount_value = 500
		balance_amount.delete(0, 'end')
		balance_amount.insert(0,Balanceamount_value)

	sd_var1 = var1.get()
	sd_var2 = var2.get()

	settings_data = {'spinamount':spinamount_value,
					'Balanceamount':Balanceamount_value,
					'sd_var1':sd_var1,'sd_var2':sd_var2}

	with open('data\\settings_data.pkl', 'wb') as file:
		pickle.dump(settings_data, file)

def load_settings():
	if os.path.isfile("data\\settings_data.pkl"): # Here I see if the file exists.
		with open('data\\settings_data.pkl', 'rb') as file:
			settings_data = pickle.load(file)

			spinamount_value = settings_data['spinamount']
			spinamount.delete(0, 'end')
			spinamount.insert(0,spinamount_value)

			Balanceamount_value = settings_data['Balanceamount']
			balance_amount.delete(0, 'end')
			balance_amount.insert(0,Balanceamount_value)

			sd_var1 = settings_data['sd_var1']
			sd_var2 = settings_data['sd_var2']

			var1.set(sd_var1)
			var2.set(sd_var2)
# Settings for the GUI

# ALL STOP
stop_flag = False  # Initial state of the button

def stop_spins():
	global stop_flag
	stop_flag = True
	enable_buttons()
# ALL STOP

# RNG button
def RNG():
	clear_text()
	append_text(text_box,'RNG Random numbers')
	root.geometry('572x389')
	disable_buttons()
	random_test() # RNG (Random number generator)
# RNG button

# disable & enable buttons
def disable_buttons():
	spinamount.config(state = DISABLED)
	# balance_amount(state = DISABLED)
	
	buttons.butstatsB["state"] = "disabled"
	buttons.butstatsR["state"] = "disabled"
	
	buttons.butcapimg["state"] = "disabled"
	
	buttons.butstats1["state"] = "disabled"
	buttons.butstats2["state"] = "disabled"
	buttons.butstats3["state"] = "disabled"
	buttons.butstats4["state"] = "disabled"
	
	buttons.butRNG["state"] = "disabled"
	buttons.spinB["state"] = "disabled"

def enable_buttons():
	spinamount.config(state = NORMAL)
	# balance_amount(state = normal)
	
	buttons.butstatsB["state"] = "normal"
	buttons.butstatsR["state"] = "normal"
	
	buttons.butcapimg["state"] = "normal"
	
	buttons.butstats1["state"] = "normal"
	buttons.butstats2["state"] = "normal"
	buttons.butstats3["state"] = "normal"
	buttons.butstats4["state"] = "normal"
	
	buttons.butRNG["state"] = "normal"
	buttons.spinB["state"] = "normal"
# disable & enable buttons
# button commands

# ~~~~~~~~~~~~~~~  defs that do stuff ~~~~~~~~~~~~~~~
# row and colm
def array_row_colm(result):
	global colm, rown
	
	if result in RouletteArrays.row2:
		rown = 2
	elif result in RouletteArrays.row1:
		rown = 1
	elif result in RouletteArrays.row0:
		rown = 0  

	# colm
	if result in RouletteArrays.colm1:
		colm = 0
	elif result in RouletteArrays.colm2:
		colm = 1
	elif result in RouletteArrays.colm3:
		colm = 2
	elif result in RouletteArrays.colm4:
		colm = 3
	elif result in RouletteArrays.colm5:
		colm = 4
	elif result in RouletteArrays.colm6:
		colm = 5
	elif result in RouletteArrays.colm7:
		colm = 6
	elif result in RouletteArrays.colm8:
		colm = 7
	elif result in RouletteArrays.colm9:
		colm = 8
	elif result in RouletteArrays.colm10:
		colm = 9
	elif result in RouletteArrays.colm11:
		colm = 10
	elif result in RouletteArrays.colm12:
		colm = 11

def get_row(result): # not sure if I need these now.
	# Assuming labels are arranged in 3 columns
	# Calculate the row based on the result
	return (result - 1) // 3

def get_column(result):
	# Assuming labels are arranged in 3 columns
	# Calculate the column based on the result
	return (result - 1) % 3
# row and colm

# Here I add in what elements I want to track.
def track_elements(): 
	return [
		# Stats 1
		RouletteArrays.red, RouletteArrays.black, # Even Chances
		RouletteArrays.high, RouletteArrays.low,
		RouletteArrays.odd, RouletteArrays.even,
		
		RouletteArrays.doz1, RouletteArrays.doz2, RouletteArrays.doz3, # Doz Col
		RouletteArrays.col1, RouletteArrays.col2, RouletteArrays.col3,
		
		RouletteArrays.line_1,RouletteArrays.line_2,RouletteArrays.line_3, # Lines
		RouletteArrays.line_4,RouletteArrays.line_5,RouletteArrays.line_6,
		RouletteArrays.line_7,RouletteArrays.line_8,RouletteArrays.line_9,
		RouletteArrays.line_10,RouletteArrays.line_11,

		RouletteArrays.corner_1,RouletteArrays.corner_2,RouletteArrays.corner_3, # corners
		RouletteArrays.corner_4,RouletteArrays.corner_5,RouletteArrays.corner_6,
		RouletteArrays.corner_7,RouletteArrays.corner_8,RouletteArrays.corner_9,
		RouletteArrays.corner_10,RouletteArrays.corner_11,RouletteArrays.corner_12,
		RouletteArrays.corner_13,RouletteArrays.corner_14,RouletteArrays.corner_15,
		RouletteArrays.corner_16,RouletteArrays.corner_17,RouletteArrays.corner_18,
		RouletteArrays.corner_19,RouletteArrays.corner_20,RouletteArrays.corner_21,RouletteArrays.corner_22,
		
		RouletteArrays.street_1,RouletteArrays.street_2,RouletteArrays.street_3, # streets
		RouletteArrays.street_4,RouletteArrays.street_5,RouletteArrays.street_6,
		RouletteArrays.street_7,RouletteArrays.street_8,RouletteArrays.street_9,
		RouletteArrays.street_10,RouletteArrays.street_11,RouletteArrays.street_12,
		
		RouletteArrays.split_1,RouletteArrays.split_2,RouletteArrays.split_3, # splits
		RouletteArrays.split_4,RouletteArrays.split_5,RouletteArrays.split_6,
		RouletteArrays.split_7,RouletteArrays.split_8,RouletteArrays.split_9,
		RouletteArrays.split_10,RouletteArrays.split_11,RouletteArrays.split_12,
		RouletteArrays.split_13,RouletteArrays.split_14,RouletteArrays.split_15,
		RouletteArrays.split_16,RouletteArrays.split_17,RouletteArrays.split_18,
		RouletteArrays.split_19,RouletteArrays.split_20,RouletteArrays.split_21,
		RouletteArrays.split_22,RouletteArrays.split_23,RouletteArrays.split_24,
		RouletteArrays.split_25,RouletteArrays.split_26,RouletteArrays.split_27,
		RouletteArrays.split_28,RouletteArrays.split_29,RouletteArrays.split_30,
		RouletteArrays.split_31,RouletteArrays.split_32,RouletteArrays.split_33,
		RouletteArrays.split_34,RouletteArrays.split_35,RouletteArrays.split_36,
		RouletteArrays.split_37,RouletteArrays.split_38,RouletteArrays.split_39,
		RouletteArrays.split_40,RouletteArrays.split_41,RouletteArrays.split_42,
		RouletteArrays.split_43,RouletteArrays.split_44,RouletteArrays.split_45,
		RouletteArrays.split_46,RouletteArrays.split_47,RouletteArrays.split_48,
		RouletteArrays.split_49,RouletteArrays.split_50,RouletteArrays.split_51,
		RouletteArrays.split_52,RouletteArrays.split_53,RouletteArrays.split_54,
		RouletteArrays.split_55,RouletteArrays.split_56,RouletteArrays.split_57,
		
		RouletteArrays.single_1,RouletteArrays.single_2,RouletteArrays.single_3, # singles
		RouletteArrays.single_4,RouletteArrays.single_5,RouletteArrays.single_6,
		RouletteArrays.single_7,RouletteArrays.single_8,RouletteArrays.single_9,
		RouletteArrays.single_10,RouletteArrays.single_11,RouletteArrays.single_12,
		RouletteArrays.single_13,RouletteArrays.single_14,RouletteArrays.single_15,
		RouletteArrays.single_16,RouletteArrays.single_17,RouletteArrays.single_18,
		RouletteArrays.single_19,RouletteArrays.single_20,RouletteArrays.single_21,
		RouletteArrays.single_22,RouletteArrays.single_23,RouletteArrays.single_24,
		RouletteArrays.single_25,RouletteArrays.single_26,RouletteArrays.single_27,
		RouletteArrays.single_28,RouletteArrays.single_29,RouletteArrays.single_30,
		RouletteArrays.single_31,RouletteArrays.single_32,RouletteArrays.single_33,
		RouletteArrays.single_34,RouletteArrays.single_35,RouletteArrays.single_36,
		
		# Stats 2
	]
# Here I add in what elements I want to track.

# Save and Load from Pickle
def save_to_pickle(filename, data):
	with open(filename, 'wb') as file:
		pickle.dump(data, file)

def load_from_pickle(filename):
	with open(filename, 'rb') as file:
		data = pickle.load(file)
	return data
# Save and Load from Pickle
# ~~~~~~~~~~~~~~~  defs that do stuff ~~~~~~~~~~~~~~~

# RNG (Random number generator)
# RNG Mode Test Run
def random_test():
	buttons.butRNG["state"] = "disabled"
	#pdb.set_trace()	 # n (next), c (continue) q (quit) p variable (print) l (list)
	
	global spin_amount_value,stop_flag,spin_count,random_mode
	global elements_to_track,max_missed_counts,current_missed_counts
	
	stop_flag = False
	
	spin_amount_str = spin_var.get().strip()
			
	try:
		# Try converting to an integer
		spin_amount_value = int(spin_amount_str)	
		if spin_amount_value == '':
			spin_amount_value = 30
		elif spin_amount_value == 0:
			spin_amount_value = 30
		elif spin_amount_value <= 30:
			spin_amount_value = 30

	except ValueError as e:
		append_text(text_box, str(e))
		spinamount.delete(0, 'end')	 # Clear the entry widget
		
	append_text(text_box,f'Random will spin for {spin_amount_value}')
		
	spin_count = 0	# Reset spin count before starting a new test
	random_mode = True
	
	elements_to_track = track_elements() # The elements that you want tracked.
		
	max_missed_counts = [0] * len(elements_to_track)
	current_missed_counts = [0] * len(elements_to_track)

	completion_event = threading.Event()
	
	thread = threading.Thread(target=lambda: insert_into_lists(completion_event))
	thread.start()
# RNG Mode Test Run

# landednumcolorchange
def landednumcolorchange(result,row,col):
	if not hasattr(landednumcolorchange, 'lab_change1'):
		# If not, create the label
		landednumcolorchange.lab_change1 = Label(x[2], text='', height=2, width=4, bg='#4BA168', fg='white', font=('Verdana', 9, 'bold'))
		landednumcolorchange.lab_change1.grid(row=row, column=col, padx=1, pady=1)
	else:
		lab_change1 = Label(x[2], text= result, height=2,width=4, bg='#4BA168', fg='white', font=('Verdana', 9, 'bold'))
		lab_change1.grid(row=rown,column=colm, padx=1, pady=1)
# landednumcolorchange

# insert_into_lists
def insert_into_lists(completion_event): # used in random mode.
	global spin_count, all_results	# Add this
	global elements_to_track, max_missed_counts, current_missed_counts
	
	all_results = []
	
	timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M")
	
	# Initialize max_missed_data
	max_missed_data = [{'name': None, 'array': element, 'max_missed': 0} for element in elements_to_track]
		
	if spin_count < spin_amount_value:	# Check if the desired number of spins is reached
	
		if stop_flag:
			append_text(text_box, 'The script will now come to a STOP')
			blanklabel_message(root,x,'All STOP.')
			return	# Stop spinning if the stop flag is set
	
		result = random.randint(1, 36)	# Simulate random result in random mode
		
		color = ''
		txcolor = ''
		
		root.update_idletasks()

		if result in RouletteArrays.red:
			color = str(result)
			txcolor = 'red'
			listBoxInsert(color, '', '')

		elif result in RouletteArrays.black:
			color = str(result)
			txcolor = 'white'
			listBoxInsert('', '', color)
			
		# Check consecutive misses for each element
		for i, element in enumerate(elements_to_track):
			if result not in element:
				current_missed_counts[i] += 1
				max_missed_counts[i] = max(max_missed_counts[i], current_missed_counts[i])
			else:
				current_missed_counts[i] = 0						
				
		if spin_amount_value >100:
			pass
		else:			
			row = get_row(result)
			col = get_column(result)

			labels, labels_data = my_labels(root, x)
			label = labels[row * 3 + col]  # Assuming labels are arranged in 3 columns
			bg_color = label.cget('bg')
			
			array_row_colm(result)
			landednumcolorchange(result, row, col)
			display_label(root, x, result, txcolor)
			
		if spin_count % 10 == 0:
			append_text(text_box,f'Random has spun for {spin_count} so far.')
			
		# Append the result to the list
		all_results.append(result)
		
		spin_count += 1	 # Increment the spin count
		
		# Schedule the next iteration after 500 milliseconds
		root.after(500, lambda: insert_into_lists(completion_event))
		
		if spin_count == spin_amount_value:
			append_text(text_box,'Stats have been updated, view the stats windows')
			
			if var2.get() == 1:
				# Save all_results to a pickle file
				try:
					with open('numdata\\saved_spins\\random\\random_spins_data.pkl', 'wb') as file:
						pickle.dump(result, file)
						append_text(text_box, 'Spin results saved to spin_results.pkl')
					with open('numdata\\saved_spins\\random\\'+filename, "wb") as file:
						filename = f"random_spins_for_{spin_count}_spins_data_{timestamp}.pkl"
						pickle.dump(result, file)
				except Exception as e:
					append_text(text_box, f'Error saving spin results: {e}')
	else:
		completion_event.set()	# Set the completion event to signal that the thread is done
		append_text(text_box, f'The Random numbers have spun for	 = {round(spin_count, 2)} spins.')
		blanklabel_message(root,x,'All STOP.')
		
		if var1.get() == 1:	 # Check if the checkbox is ticked
			save_to_pickle('numdata\\stats_data\\random\\data.pkl',
				{'elements_to_track': elements_to_track, 'max_missed_counts': max_missed_counts})
			filename = f"numdata\\stats_data\\random\\random_stats_for_{spin_count}_spins_data_{timestamp}.pkl"
			save_to_pickle(filename, {'elements_to_track': elements_to_track, 'max_missed_counts': max_missed_counts})
			
		enable_buttons()
# insert_into_lists
# RNG (Random number generator)

# ~~~~~~~~~~~~~~~  BetVoyager Bet and Table Setttings ~~~~~~~~~~~~~~~
# Red Entry frame
Redvar = IntVar()

R1 = Checkbutton(x[7], bg='#31859B', text='Red', font=('Verdana', 10, 'bold'),
			variable=Redvar, onvalue=1, offvalue=0)
R1.place(x=3, y=46)
Redvar.set(1)

Red_var = StringVar()

def Redxamount(event):
	try:
		Red_amount_str = Red_var.get().strip()
		
		if not Red_amount_str:
			raise ValueError("Please enter a number")
			
		Red_amount_value = int(Red_amount_str)
		
		if Red_amount_value <= 0 or Red_amount_value < 3:
			raise ValueError("Please enter a positive number greater than or equal to 3")
						
	except ValueError as e:
		error_message = "You did not enter a valid number" if "invalid literal for int() with base 10" in str(e) else str(e)
		append_text(text_box, error_message)
		blanklabel_message(root, x, error_message)
		Redamount.delete(0, 'end')	   # Clear the entry widget
		Redamount.insert(0, 3)
		Red_amount_value = 3

frameRedEntry = Frame(x[7], bg='#31859B', highlightbackground="black", highlightthickness=2)
frameRedEntry.place(x=73, y=48, width=66, height=23)  # entry border

# Fix the typo here: Redbox should be Spinbox
Redamount = Spinbox(frameRedEntry, textvariable=Red_var, from_=1, to=9999, width=5)
Redamount.bind("<Return>", Redxamount)
Redamount.place(x=0, y=0)	 # Adjust placement within the frame

Redamount.delete(0, "end")	   # Clear the current value in the Redamount entry
Redamount.insert(0, 3)
# Red Entry frame

# Black Entry frame
Blackvar = IntVar()

B1 = Checkbutton(x[7], bg='#31859B', text='Black', font=('Verdana', 10, 'bold'),
			variable=Blackvar, onvalue=1, offvalue=0)
B1.place(x=3, y=66)
Blackvar.set(1)

Black_var = StringVar()

def Blackxamount(event):
	try:
		Black_amount_str = Black_var.get().strip()
		
		if not Black_amount_str:
			raise ValueError("Please enter a number")
			
		Black_amount_value = int(Black_amount_str)
		
		if Black_amount_value <= 0 or Black_amount_value < 3:
			raise ValueError("Please enter a positive number greater than or equal to 3")
						
	except ValueError as e:
		error_message = "You did not enter a valid number" if "invalid literal for int() with base 10" in str(e) else str(e)
		append_text(text_box, error_message)
		blanklabel_message(root, x, error_message)
		Blackamount.delete(0, 'end')	   # Clear the entry widget
		Blackamount.insert(0, 3)
		Black_amount_value = 3

frameBlackEntry = Frame(x[7], bg='#31859B', highlightbackground="black", highlightthickness=2)
frameBlackEntry.place(x=73, y=68, width=66, height=23)	# entry border

# Fix the typo here: Blackbox should be Spinbox
Blackamount = Spinbox(frameBlackEntry, textvariable=Black_var, from_=1, to=9999, width=5)
Blackamount.bind("<Return>", Blackxamount)
Blackamount.place(x=0, y=0)	 # Adjust placement within the frame

Blackamount.delete(0, "end")	   # Clear the current value in the Blackamount entry
Blackamount.insert(0, 3)
# Black Entry frame.

# high Entry frame
Highvar = IntVar()

H1 = Checkbutton(x[7], bg='#31859B', text='High', font=('Verdana', 10, 'bold'),
			variable=Highvar, onvalue=1, offvalue=0)
H1.place(x=3, y=86)
Highvar.set(1)

High_var = StringVar()

def Highxamount(event):
	try:
		High_amount_str = High_var.get().strip()
		
		if not High_amount_str:
			raise ValueError("Please enter a number")
			
		High_amount_value = int(High_amount_str)
		
		if High_amount_value <= 0 or High_amount_value < 3:
			raise ValueError("Please enter a positive number greater than or equal to 3")
						
	except ValueError as e:
		error_message = "You did not enter a valid number" if "invalid literal for int() with base 10" in str(e) else str(e)
		append_text(text_box, error_message)
		blanklabel_message(root, x, error_message)
		Highamount.delete(0, 'end')	   # Clear the entry widget
		Highamount.insert(0, 3)
		High_amount_value = 3

frameHighEntry = Frame(x[7], bg='#31859B', highlightbackground="black", highlightthickness=2)
frameHighEntry.place(x=73, y=88, width=66, height=23)  # entry border

# Fix the typo here: highbox should be Spinbox
Highamount = Spinbox(frameHighEntry, textvariable=High_var, from_=1, to=9999, width=5)
Highamount.bind("<Return>", Highxamount)
Highamount.place(x=0, y=0)	 # Adjust placement within the frame

Highamount.delete(0, "end")	   # Clear the current value in the highamount entry
Highamount.insert(0, 3)
# high Entry frame

# Low Entry frame
Lowvar = IntVar()

Low1 = Checkbutton(x[7], bg='#31859B', text='Low', font=('Verdana', 10, 'bold'),
			variable=Lowvar, onvalue=1, offvalue=0)
Low1.place(x=3, y=106)
Lowvar.set(1)

Low_var = StringVar()

def Lowxamount(event):
	try:
		Low_amount_str = Low_var.get().strip()
		
		if not Low_amount_str:
			raise ValueError("Please enter a number")
			
		Low_amount_value = int(Low_amount_str)
		
		if Low_amount_value <= 0 or Low_amount_value < 3:
			raise ValueError("Please enter a positive number greater than or equal to 3")
						
	except ValueError as e:
		error_message = "You did not enter a valid number" if "invalid literal for int() with base 10" in str(e) else str(e)
		append_text(text_box, error_message)
		blanklabel_message(root, x, error_message)
		Lowamount.delete(0, 'end')	   # Clear the entry widget
		Lowamount.insert(0, 3)
		Low_amount_value = 3

frameLowEntry = Frame(x[7], bg='#31859B', highlightbackground="black", highlightthickness=2)
frameLowEntry.place(x=73, y=108, width=66, height=23)  # entry border

# Fix the typo here: Lowbox should be Spinbox
Lowamount = Spinbox(frameLowEntry, textvariable=Low_var, from_=1, to=9999, width=5)
Lowamount.bind("<Return>", Lowxamount)
Lowamount.place(x=0, y=0)	 # Adjust placement within the frame

Lowamount.delete(0, "end")	   # Clear the current value in the Lowamount entry
Lowamount.insert(0, 3)
# Low Entry frame

# Even Entry frame
Evenvar = IntVar()

Ev1 = Checkbutton(x[7], bg='#31859B', text='Even', font=('Verdana', 10, 'bold'),
			variable=Evenvar, onvalue=1, offvalue=0)
Ev1.place(x=3, y=126)
Evenvar.set(1)

Even_var = StringVar()

def Evenxamount(Event):
	try:
		Even_amount_str = Even_var.get().strip()
		
		if not Even_amount_str:
			raise ValueError("Please enter a number")
			
		Even_amount_value = int(Even_amount_str)
		
		if Even_amount_value <= 0 or Even_amount_value < 3:
			raise ValueError("Please enter a positive number greater than or equal to 3")
						
	except ValueError as e:
		error_message = "You did not enter a valid number" if "invalid literal for int() with base 10" in str(e) else str(e)
		append_text(text_box, error_message)
		blanklabel_message(root, x, error_message)
		Evenamount.delete(0, 'end')	   # Clear the entry widget
		Evenamount.insert(0, 3)
		Even_amount_value = 3

frameEvenEntry = Frame(x[7], bg='#31859B', highlightbackground="black", highlightthickness=2)
frameEvenEntry.place(x=73, y=128, width=66, height=23)	# entry border

# Fix the typo here: Evenbox should be Spinbox
Evenamount = Spinbox(frameEvenEntry, textvariable=Even_var, from_=1, to=9999, width=5)
Evenamount.bind("<Return>", Evenxamount)
Evenamount.place(x=0, y=0)	 # Adjust placement within the frame

Evenamount.delete(0, "end")	   # Clear the current value in the Evenamount entry
Evenamount.insert(0, 3)
# Even Entry frame

# Odd Entry frame
Oddvar = IntVar()

Ov1 = Checkbutton(x[7], bg='#31859B', text='Odd', font=('Verdana', 10, 'bold'),
			variable=Oddvar, onvalue=1, offvalue=0)
Ov1.place(x=3, y=146)
Oddvar.set(1)

Odd_var = StringVar()

def Oddxamount(Oddt):
	try:
		Odd_amount_str = Odd_var.get().strip()
		
		if not Odd_amount_str:
			raise ValueError("Please enter a number")
			
		Odd_amount_value = int(Odd_amount_str)
		
		if Odd_amount_value <= 0 or Odd_amount_value < 3:
			raise ValueError("Please enter a positive number greater than or equal to 3")
						
	except ValueError as e:
		error_message = "You did not enter a valid number" if "invalid literal for int() with base 10" in str(e) else str(e)
		append_text(text_box, error_message)
		blanklabel_message(root, x, error_message)
		Oddamount.delete(0, 'end')	   # Clear the entry widget
		Oddamount.insert(0, 3)
		Odd_amount_value = 3

frameOddEntry = Frame(x[7], bg='#31859B', highlightbackground="black", highlightthickness=2)
frameOddEntry.place(x=73, y=148, width=66, height=23)	# entry border

# Fix the typo here: Oddbox should be Spinbox
Oddamount = Spinbox(frameOddEntry, textvariable=Odd_var, from_=1, to=9999, width=5)
Oddamount.bind("<Return>", Oddxamount)
Oddamount.place(x=0, y=0)	 # Adjust placement within the frame

Oddamount.delete(0, "end")	   # Clear the current value in the Oddamount entry
Oddamount.insert(0, 3)
# Odd Entry frame

# Doz Entry frame
Dozvar = IntVar()

Dz1 = Checkbutton(x[7], bg='#31859B', text='Doz', font=('Verdana', 10, 'bold'),
			variable=Dozvar, onvalue=1, offvalue=0)
Dz1.place(x=153, y=46)
Dozvar.set(1)

Doz_var = StringVar()

def Dozxamount(event):
	try:
		Doz_amount_str = Doz_var.get().strip()
		
		if not Doz_amount_str:
			raise ValueError("Please enter a number")
			
		Doz_amount_value = int(Doz_amount_str)
		
		if Doz_amount_value <= 0 or Doz_amount_value < 5:
			raise ValueError("Please enter a positive number greater than or equal to 5")
						
	except ValueError as e:
		error_message = "You did not enter a valid number" if "invalid literal for int() with base 10" in str(e) else str(e)
		append_text(text_box, error_message)
		blanklabel_message(root, x, error_message)
		Dozamount.delete(0, 'end')	   # Clear the entry widget
		Dozamount.insert(0, 5)
		Doz_amount_value = 5

frameDozEntry = Frame(x[7], bg='#31859B', highlightbackground="black", highlightthickness=2)
frameDozEntry.place(x=238, y=48, width=66, height=23)  # entry border

# Fix the typo here: Dozbox should be Spinbox
Dozamount = Spinbox(frameDozEntry, textvariable=Doz_var, from_=1, to=9999, width=5)
Dozamount.bind("<Return>", Dozxamount)
Dozamount.place(x=0, y=0)	 # Adjust placement within the frame

Dozamount.delete(0, "end")	   # Clear the current value in the Dozamount entry
Dozamount.insert(0, 5)
# Doz Entry frame

# Colm Entry frame
Colmvar = IntVar()

Clm1 = Checkbutton(x[7], bg='#31859B', text='Colmm', font=('Verdana', 10, 'bold'),
			variable=Colmvar, onvalue=1, offvalue=0)
Clm1.place(x=153, y=66)
Colmvar.set(1)

Colm_var = StringVar()

def Colmxamount(event):
	try:
		Colm_amount_str = Colm_var.get().strip()
		
		if not Colm_amount_str:
			raise ValueError("Please enter a number")
			
		Colm_amount_value = int(Colm_amount_str)
		
		if Colm_amount_value <= 0 or Colm_amount_value < 5:
			raise ValueError("Please enter a positive number greater than or equal to 5")
						
	except ValueError as e:
		error_message = "You did not enter a valid number" if "invalid literal for int() with base 10" in str(e) else str(e)
		append_text(text_box, error_message)
		blanklabel_message(root, x, error_message)
		Colmamount.delete(0, 'end')	   # Clear the entry widget
		Colmamount.insert(0, 5)
		Colm_amount_value = 5

frameColmEntry = Frame(x[7], bg='#31859B', highlightbackground="black", highlightthickness=2)
frameColmEntry.place(x=238, y=68, width=66, height=23)	# entry border

# Fix the typo here: Colmbox should be Spinbox
Colmamount = Spinbox(frameColmEntry, textvariable=Colm_var, from_=1, to=9999, width=5)
Colmamount.bind("<Return>", Colmxamount)
Colmamount.place(x=0, y=0)	 # Adjust placement within the frame

Colmamount.delete(0, "end")	   # Clear the current value in the Colmamount entry
Colmamount.insert(0, 5)
# Colm Entry frame

# Line Entry frame
Linevar = IntVar()

Line1 = Checkbutton(x[7], bg='#31859B', text='Lines', font=('Verdana', 10, 'bold'),
			variable=Linevar, onvalue=1, offvalue=0)
Line1.place(x=153, y=106)
Linevar.set(1)

Line_var = StringVar()

def Linexamount(event):
	try:
		Line_amount_str = Line_var.get().strip()
		
		if not Line_amount_str:
			raise ValueError("Please enter a number")
			
		Line_amount_value = int(Line_amount_str)
		
		if Line_amount_value <= 0 or Line_amount_value < 18:
			raise ValueError("Please enter a positive number greater than or equal to 18")
						
	except ValueError as e:
		error_message = "You did not enter a valid number" if "invalid literal for int() with base 10" in str(e) else str(e)
		append_text(text_box, error_message)
		blanklabel_message(root, x, error_message)
		Lineamount.delete(0, 'end')	   # Clear the entry widget
		Lineamount.insert(0, 18)
		Line_amount_value = 18

frameLineEntry = Frame(x[7], bg='#31859B', highlightbackground="black", highlightthickness=2)
frameLineEntry.place(x=238, y=108, width=66, height=23)	# entry border

# Fix the typo here: Linebox should be Spinbox
Lineamount = Spinbox(frameLineEntry, textvariable=Line_var, from_=1, to=9999, width=5)
Lineamount.bind("<Return>", Linexamount)
Lineamount.place(x=0, y=0)	 # Adjust placement within the frame

Lineamount.delete(0, "end")	   # Clear the current value in the Lineamount entry
Lineamount.insert(0, 18)
# Line Entry frame

# Corner Entry frame
Cornervar = IntVar()

Corner1 = Checkbutton(x[7], bg='#31859B', text='Corners', font=('Verdana', 10, 'bold'),
			variable=Cornervar, onvalue=1, offvalue=0)
Corner1.place(x=153, y=146)
Cornervar.set(1)

Corner_var = StringVar()

def Cornerxamount(event):
	try:
		Corner_amount_str = Corner_var.get().strip()
		
		if not Corner_amount_str:
			raise ValueError("Please enter a number")
			
		Corner_amount_value = int(Corner_amount_str)
		
		if Corner_amount_value <= 0 or Corner_amount_value < 28:
			raise ValueError("Please enter a positive number greater than or equal to 28")
						
	except ValueError as e:
		error_message = "You did not enter a valid number" if "invalid literal for int() with base 10" in str(e) else str(e)
		append_text(text_box, error_message)
		blanklabel_message(root, x, error_message)
		Corneramount.delete(0, 'end')	   # Clear the entry widget
		Corneramount.insert(0, 28)
		Corner_amount_value = 28

frameCornerEntry = Frame(x[7], bg='#31859B', highlightbackground="black", highlightthickness=2)
frameCornerEntry.place(x=238, y=148, width=66, height=23)  # entry border

# Fix the typo here: Cornerbox should be Spinbox
Corneramount = Spinbox(frameCornerEntry, textvariable=Corner_var, from_=1, to=9999, width=5)
Corneramount.bind("<Return>", Cornerxamount)
Corneramount.place(x=0, y=0)	 # Adjust placement within the frame

Corneramount.delete(0, "end")	   # Clear the current value in the Corneramount entry
Corneramount.insert(0, 28)
# Corner Entry frame

# Street Entry frame
Streetvar = IntVar()

Street1 = Checkbutton(x[7], bg='#31859B', text='Streets', font=('Verdana', 10, 'bold'),
			variable=Streetvar, onvalue=1, offvalue=0)
Street1.place(x=316, y=46)
Streetvar.set(1)

Street_var = StringVar()

def Streetxamount(event):
	try:
		Street_amount_str = Street_var.get().strip()
		
		if not Street_amount_str:
			raise ValueError("Please enter a number")
			
		Street_amount_value = int(Street_amount_str)
		
		if Street_amount_value <= 0 or Street_amount_value < 12:
			raise ValueError("Please enter a positive number greater than or equal to 12")
						
	except ValueError as e:
		error_message = "You did not enter a valid number" if "invalid literal for int() with base 10" in str(e) else str(e)
		append_text(text_box, error_message)
		blanklabel_message(root, x, error_message)
		Streetamount.delete(0, 'end')	   # Clear the entry widget
		Streetamount.insert(0, 12)
		Street_amount_value = 12

frameStreetEntry = Frame(x[7], bg='#31859B', highlightbackground="black", highlightthickness=2)
frameStreetEntry.place(x=413, y=48, width=66, height=23)  # entry border

# Fix the typo here: Streetbox should be Spinbox
Streetamount = Spinbox(frameStreetEntry, textvariable=Street_var, from_=1, to=9999, width=5)
Streetamount.bind("<Return>", Streetxamount)
Streetamount.place(x=0, y=0)	 # Adjust placement within the frame

Streetamount.delete(0, "end")	   # Clear the current value in the Streetamount entry
Streetamount.insert(0, 12)
# Street Entry frame

# Number Entry frame
Numbervar = IntVar()

Number1 = Checkbutton(x[7], bg='#31859B', text='Numbers', font=('Verdana', 10, 'bold'),
			variable=Numbervar, onvalue=1, offvalue=0)
Number1.place(x=316, y=88)
Numbervar.set(1)

Number_var = StringVar()

def Numberxamount(event):
	try:
		Number_amount_str = Number_var.get().strip()
		
		if not Number_amount_str:
			raise ValueError("Please enter a Number")
			
		Number_amount_value = int(Number_amount_str)
		
		if Number_amount_value <= 0 or Number_amount_value < 18:
			raise ValueError("Please enter a positive Number greater than or equal to 18")
						
	except ValueError as e:
		error_message = "You did not enter a valid Number" if "invalid literal for int() with base 10" in str(e) else str(e)
		append_text(text_box, error_message)
		blanklabel_message(root, x, error_message)
		Numberamount.delete(0, 'end')	   # Clear the entry widget
		Numberamount.insert(0, 18)
		Numberamount = 18

frameNumberEntry = Frame(x[7], bg='#31859B', highlightbackground="black", highlightthickness=2)
frameNumberEntry.place(x=413, y=88, width=66, height=23)  # entry border

# Fix the typo here: Numberbox should be Spinbox
Numberamount = Spinbox(frameNumberEntry, textvariable=Number_var, from_=1, to=9999, width=5)
Numberamount.bind("<Return>", Numberxamount)
Numberamount.place(x=0, y=0)	 # Adjust placement within the frame

Numberamount.delete(0, "end")	   # Clear the current value in the Numberamount entry
Numberamount.insert(0, 18)
# Number Entry frame

# Split Entry frame
Splitvar = IntVar()

Split1 = Checkbutton(x[7], bg='#31859B', text='Splits', font=('Verdana', 10, 'bold'),
			variable=Splitvar, onvalue=1, offvalue=0)
Split1.place(x=316, y=128)
Splitvar.set(1)

Split_var = StringVar()

def Splitxamount(event):
	try:
		Split_amount_str = Split_var.get().strip()
		
		if not Split_amount_str:
			raise ValueError("Please enter a Split")
			
		Split_amount_value = int(Split_amount_str)
		
		if Split_amount_value <= 0 or Split_amount_value < 77:
			raise ValueError("Please enter a positive Split greater than or equal to 77")
						
	except ValueError as e:
		error_message = "You did not enter a valid Split" if "invalid literal for int() with base 10" in str(e) else str(e)
		append_text(text_box, error_message)
		blanklabel_message(root, x, error_message)
		Splitamount.delete(0, 'end')	   # Clear the entry widget
		Splitamount.insert(0, 77)
		Splitamount = 77

frameSplitEntry = Frame(x[7], bg='#31859B', highlightbackground="black", highlightthickness=2)
frameSplitEntry.place(x=413, y=128, width=66, height=23)  # entry border

# Fix the typo here: Splitbox should be Spinbox
Splitamount = Spinbox(frameSplitEntry, textvariable=Split_var, from_=1, to=9999, width=5)
Splitamount.bind("<Return>", Splitxamount)
Splitamount.place(x=0, y=0)	 # Adjust placement within the frame

Splitamount.delete(0, "end")	   # Clear the current value in the Splitamount entry
Splitamount.insert(0, 77)
# Split Entry frame

# Save and Load BV settings
def BVsave_settings():
	# Even Chances
	Red_var1 = Redvar.get()
	Red_amount_str = Red_var.get().strip()
	Red_amount_value = int(Red_amount_str)
	
	Black_var1 = Blackvar.get()
	Black_amount_str = Black_var.get().strip()
	Black_amount_value = int(Black_amount_str)
	
	High_var1 = Highvar.get()
	High_amount_str = High_var.get().strip()
	High_amount_value = int(High_amount_str)
	
	Low_var1 = Lowvar.get()
	Low_amount_str = Low_var.get().strip()
	Low_amount_value = int(Low_amount_str)
	
	Even_var1 = Evenvar.get()
	Even_amount_str = Even_var.get().strip()
	Even_amount_value = int(Even_amount_str)
	
	Odd_var1 = Oddvar.get()
	Odd_amount_str = Odd_var.get().strip()
	Odd_amount_value = int(Odd_amount_str)
	# Even Chances
	
	# Doz Colm
	Doz_var1 = Dozvar.get()
	Doz_amount_str = Doz_var.get().strip()
	Doz_amount_value = int(Doz_amount_str)
	
	Colm_var1 = Colmvar.get()
	Colm_amount_str = Colm_var.get().strip()
	Colm_amount_value = int(Colm_amount_str)
	# Doz Colm
	
	# Lines
	Line_var1 = Linevar.get()
	Line_amount_str = Line_var.get().strip()
	Line_amount_value = int(Line_amount_str)
	# Lines
	
	# Corner
	Corner_var1 = Cornervar.get()
	Corner_amount_str = Corner_var.get().strip()
	Corner_amount_value = int(Corner_amount_str)
	# Corner
	
	# Street
	Street_var1 = Streetvar.get()
	Street_amount_str = Street_var.get().strip()
	Street_amount_value = int(Street_amount_str)
	# Street
	
	# Number
	Number_var1 = Numbervar.get()
	Number_amount_str = Number_var.get().strip()
	Number_amount_value = int(Number_amount_str)
	# Number
	
	# Split
	Split_var1 = Splitvar.get()
	Split_amount_str = Split_var.get().strip()
	Split_amount_value = int(Split_amount_str)
	# Split
	
	BVsettings_data = {'Redvar':Red_var1,'Red_amount_value':Red_amount_value,
									'Blackvar':Black_var1,'Black_amount_value':Black_amount_value,
									'Highvar':High_var1,'High_amount_value':High_amount_value,
									'Lowvar':Low_var1,'Low_amount_value':Low_amount_value,
									'Evenvar':Even_var1,'Even_amount_value':Even_amount_value,
									'Oddvar':Odd_var1,'Odd_amount_value':Odd_amount_value,
									'Dozvar':Doz_var1,'Doz_amount_value':Doz_amount_value,
									'Colmvar':Colm_var1,'Colm_amount_value':Colm_amount_value,
									'Linevar':Line_var1,'Line_amount_value':Line_amount_value,
									'Cornervar':Corner_var1,'Corner_amount_value':Corner_amount_value,
									'Streetvar':Street_var1,'Street_amount_value':Street_amount_value,
									'Numbervar':Number_var1,'Number_amount_value':Number_amount_value,
									'Splitvar':Split_var1,'Split_amount_value':Split_amount_value}
									
	timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M")
	filename = f"data\\BVsettings_data_{timestamp}.pkl"
	
	save_to_pickle('data\\BVsettings_data.pkl',BVsettings_data)
	save_to_pickle(filename,BVsettings_data)
		
def load_BV_data(BVsettings_data):

	# Even Chances
	sRed_var1 = BVsettings_data['Redvar']
	Redvar.set(sRed_var1)
	
	Red_amount_value = BVsettings_data['Red_amount_value']
	Redamount.delete(0, "end")
	Redamount.insert(0, Red_amount_value)
	
	sBlack_var1 = BVsettings_data['Blackvar']
	Blackvar.set(sBlack_var1)
	
	Black_amount_value = BVsettings_data['Black_amount_value']
	Blackamount.delete(0, "end")
	Blackamount.insert(0, Black_amount_value)
	
	sHigh_var1 = BVsettings_data['Highvar']
	Highvar.set(sHigh_var1)
	
	High_amount_value = BVsettings_data['High_amount_value']
	Highamount.delete(0, "end")
	Highamount.insert(0, High_amount_value)
	
	sLow_var1 = BVsettings_data['Lowvar']
	Lowvar.set(sLow_var1)
	
	Low_amount_value = BVsettings_data['Low_amount_value']
	Lowamount.delete(0, "end")
	Lowamount.insert(0, Low_amount_value)
	
	sEven_var1 = BVsettings_data['Evenvar']
	Evenvar.set(sEven_var1)
	
	Even_amount_value = BVsettings_data['Even_amount_value']
	Evenamount.delete(0, "end")
	Evenamount.insert(0, Even_amount_value)
	
	sOdd_var1 = BVsettings_data['Oddvar']
	Oddvar.set(sOdd_var1)
	
	Odd_amount_value = BVsettings_data['Odd_amount_value']
	Oddamount.delete(0, "end")
	Oddamount.insert(0, Odd_amount_value)
	# Even Chances
	
	# Doz Col
	sDoz_var1 = BVsettings_data['Dozvar']
	Dozvar.set(sDoz_var1)
	
	Doz_amount_value = BVsettings_data['Doz_amount_value']
	Dozamount.delete(0, "end")
	Dozamount.insert(0, Doz_amount_value)
	
	sColm_var1 = BVsettings_data['Colmvar']
	Colmvar.set(sColm_var1)
	
	Colm_amount_value = BVsettings_data['Colm_amount_value']
	Colmamount.delete(0, "end")
	Colmamount.insert(0, Colm_amount_value)
	# Doz Col
	
	# Lines
	sLine_var1 = BVsettings_data['Linevar']
	Linevar.set(sLine_var1)
	
	Line_amount_value = BVsettings_data['Line_amount_value']
	Lineamount.delete(0, "end")
	Lineamount.insert(0, Line_amount_value)
	# Lines
	
	# Corners
	sCorner_var1 = BVsettings_data['Cornervar']
	Cornervar.set(sCorner_var1)
	
	Corner_amount_value = BVsettings_data['Corner_amount_value']
	Corneramount.delete(0, "end")
	Corneramount.insert(0, Corner_amount_value)
	# Corners
	
	# Streets
	sStreet_var1 = BVsettings_data['Streetvar']
	Streetvar.set(sStreet_var1)
	
	Street_amount_value = BVsettings_data['Street_amount_value']
	Streetamount.delete(0, "end")
	Streetamount.insert(0, Street_amount_value)
	# Streets
	
	# Number
	sNumber_var1 = BVsettings_data['Numbervar']
	Numbervar.set(sNumber_var1)
	
	Number_amount_value = BVsettings_data['Number_amount_value']
	Numberamount.delete(0, "end")
	Numberamount.insert(0, Number_amount_value)
	# Number
	
	# Split
	sSplit_var1 = BVsettings_data['Splitvar']
	Splitvar.set(sSplit_var1)
	
	Split_amount_value = BVsettings_data['Split_amount_value']
	Splitamount.delete(0, "end")
	Splitamount.insert(0, Split_amount_value)
	
def BVload_settings():
	global BVsettings_data
	current_directory = os.getcwd()
	
	file_path = filedialog.askopenfilename(initialdir=current_directory, filetypes=[("Pickle Files", "*.pkl")])
	
	if file_path:
			# Load the data from the pickle file
			with open(file_path, "rb") as file:
				BVsettings_data = pickle.load(file)
				load_BV_data(BVsettings_data)
	else:
		blanklabel_message(root,x,'No file selected.')		
# Save and Load BV settings

# Load BV settings from data
def display_data(data):
	if 'elements_to_track' in data and 'max_missed_counts' in data:
		elements_to_track = data['elements_to_track']
		max_missed_counts = data['max_missed_counts']
		
		for i, element in enumerate(elements_to_track):
			bet_name = next(name for name, value in RouletteArrays.__dict__.items() if value == element)
			
			# Even chances
			if bet_name.lower() == 'red':
				Redamount.delete(0, "end")
				Redamount.insert(0, max_missed_counts[i])
				
			if bet_name.lower() == 'black':
				Blackamount.delete(0, "end")
				Blackamount.insert(0, max_missed_counts[i])
				
			if bet_name.lower() == 'high':
				Highamount.delete(0, "end")
				Highamount.insert(0, max_missed_counts[i])
				
			if bet_name.lower() == 'low':
				Lowamount.delete(0, "end")
				Lowamount.insert(0, max_missed_counts[i])
				
			if bet_name.lower() == 'odd':
				Oddamount.delete(0, "end")
				Oddamount.insert(0, max_missed_counts[i])
				
			if bet_name.lower() == 'even':
				Evenamount.delete(0, "end")
				Evenamount.insert(0, max_missed_counts[i])
			# Even chances
			
			# Dozens / Colums
			if bet_name.lower() == 'doz1':
				Dozamount.delete(0, "end")
				Dozamount.insert(0, max_missed_counts[i])
				
			if bet_name.lower() == 'col1':
				Colmamount.delete(0, "end")
				Colmamount.insert(0, max_missed_counts[i])
			# Dozens / Colums
			
			# Lines
			if bet_name.lower() == 'line_1':
				Lineamount.delete(0, "end")
				Lineamount.insert(0, max_missed_counts[i])
			# Lines
			
			# Corners
			if bet_name.lower() == 'corner_1':
				Corneramount.delete(0, "end")
				Corneramount.insert(0, max_missed_counts[i])
			# Corners
			
			# Streets
			if bet_name.lower() == 'street_1':
				Streetamount.delete(0, "end")
				Streetamount.insert(0, max_missed_counts[i])
			# Streets
			
			# Single Numbers
			if bet_name.lower() == 'single_1':
				Numberamount.delete(0, "end")
				Numberamount.insert(0, max_missed_counts[i])
			# Single Numbers
			
			# Single Numbers
			if bet_name.lower() == 'split_1':
				Splitamount.delete(0, "end")
				Splitamount.insert(0, max_missed_counts[i])
			# Single Numbers
		
def LoadBVSettingsFromData():
	if os.path.isfile('numdata\\stats_data\\random\\data.pkl'):
		with open('numdata\\stats_data\\random\\data.pkl', 'rb') as file:
			data = pickle.load(file)
			display_data(data)
# Load BV settings from data
# ~~~~~~~~~~~~~~~  BetVoyager Bet and Table Setttings ~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~  Real Mode Test Area ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def PlayBV(): # This loads the BetVoyager browers and goes to the website.
	global spin_amount_value,stop_flag,spin_count,random_mode
	global elements_to_track,max_missed_counts,current_missed_counts
	
	stop_flag = False
	
	disable_buttons()
	#buttons.spinB["state"] = "normal"
	clear_text()
	
	root.geometry('572x389+18+270')
	
	completion_event = threading.Event()
	pause_event = threading.Event()
	
	image_to_find1 = "images\\search\\fullscreen.png"
	image_to_find2 = "images\\search\\go_fullscreen.png"
	
	fullscreen = pyautogui.locateOnScreen(image_to_find1)
	
	if fullscreen:
		append_text(text_box, 'Ready to play')
		bvruntest()
	else:
		go_fullscreen_pic = pyautogui.locateOnScreen(image_to_find2)
		if go_fullscreen_pic:
			append_text(text_box, 'Go full screen')
			go_fullscreen()
			time.sleep(2)
			buttons.spinB["state"] = "normal"
			bvruntest()
		else:
			thread = threading.Thread(target=lambda: find_image_on_screen(text_box, root))
			thread.start()
			buttons.spinB["state"] = "normal"

def bvruntest():
	global stop_flag
	stop_flag = False
	root.geometry('572x389') # '610x862+0+0'
	clear_text()
	disable_buttons()
	thread = threading.Thread(target=BVRunTestRealPlay)
	thread.start()
	
# BVRunTestRealPlay this is where I test out playing on the Table.
def BVRunTestRealPlay(): # One that works so far.
	global result,color,colm,row,txcolor,number,stop_flag
	global elements_to_track, max_missed_counts, current_missed_counts
	
	root.update_idletasks()
	
	append_text(text_box,'Make sure to keep the table at Full Screen Mode.')
	pyautogui.PAUSE = 0.08 # pyautogui click speed. 0.05 0.08was where I set it.
	
	go_fullscreen()
	
	# Table Variables
	stop_flag = False 
	
	# table spins amount
	spin_amount_str = spin_var.get().strip()
			
	try:
		# Try converting to an integer
		tblspin = int(spin_amount_str)	
		if tblspin == '':
			tblspin = 30
		elif tblspin == 0:
			tblspin = 30
		elif tblspin <= 30:
			tblspin = 30

	except ValueError as e:
		append_text(text_box, str(e))
		spinamount.delete(0, 'end')	 # Clear the entry widget  
	# table spins amount
		
	append_text(text_box, 'Ready to play on BetVoyager No Zero Table')
	append_text(text_box, 'No Balance Calculations as I could not get it to work') 
	append_text(text_box,' ')
	append_text(text_box, 'A Free Spin to capture the first Number')
	freespin()
	pyautogui.click(1565, 970) #click on the spin button
	
	spin = 1
	time.sleep(5)
	clear_text()
	
	append_text(text_box,f'BetVoyager will spin for {tblspin} spins.')
	append_text(text_box,' ')
	append_text(text_box,'Table Bet Settings')
	
	# ~~~~~~~~~~~~~~ Initialize all variables ~~~~~~~~~~~~
	timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M")
	 
	elements_to_track = track_elements()
	
	max_missed_counts = [0] * len(elements_to_track)
	current_missed_counts = [0] * len(elements_to_track)
	
	max_missed_data = [{'name': None, 'array': element, 'max_missed': 0} for element in elements_to_track]
	
	# Even Chances
	ecr, ecb, ech, ecl, ece, eco  = 0, 0, 0, 0, 0, 0 # Initialize counters for Even Chances
	r_bet, b_bet, h_bet, l_bet, e_bet, o_bet = False, False, False, False, False, False
	
	Red_amount_str = Red_var.get().strip()
	Red_amount_value = int(Red_amount_str)
	if Redvar.get() == 1: 
		max_consecutive_misses_red = Red_amount_value
		append_text(text_box, f'max_consecutive_misses_Red set to {max_consecutive_misses_red}')
	consecutive_misses_red = 0	
	
	Black_amount_str = Black_var.get().strip()
	Black_amount_value = int(Black_amount_str)
	if Blackvar.get() == 1: 
		max_consecutive_misses_black = Black_amount_value
		append_text(text_box, f'max_consecutive_misses_Black set to {max_consecutive_misses_black}')
	consecutive_misses_black = 0 
	
	High_amount_str = High_var.get().strip()
	High_amount_value = int(High_amount_str)
	if Highvar.get() == 1: 
		max_consecutive_misses_high = int(High_amount_str)
		append_text(text_box, f'max_consecutive_misses_high set to {max_consecutive_misses_high}')
	consecutive_misses_high = 0 
	
	Low_amount_str = Low_var.get().strip()
	Low_amount_value = int(Low_amount_str)
	if Lowvar.get() == 1: 
		max_consecutive_misses_low = int(Low_amount_str)
		append_text(text_box, f'max_consecutive_misses_Low set to {max_consecutive_misses_low}')
	consecutive_misses_low = 0
	
	Even_amount_str = Even_var.get().strip()
	Even_amount_value = int(Even_amount_str)
	if Evenvar.get() == 1: 
		max_consecutive_misses_even = int(Even_amount_str)
		append_text(text_box, f'max_consecutive_misses_Even set to {max_consecutive_misses_even}')
	consecutive_misses_even = 0 
	
	Odd_amount_str = Odd_var.get().strip()
	Odd_amount_value = int(Odd_amount_str)
	if Oddvar.get() == 1: 
		max_consecutive_misses_odd = int(Odd_amount_str)
		append_text(text_box, f'max_consecutive_misses_Odd set to {max_consecutive_misses_odd}')
	consecutive_misses_odd = 0
	
	# Even Chances can go up to 22
	# max_consecutive_misses = 13 # 2 for testing and fast play. Dangerous.
	# max_consecutive_misses_red = 6 
	# max_consecutive_misses_black = 6
	# max_consecutive_misses_high = 6
	# max_consecutive_misses_low = 6
	# max_consecutive_misses_even = 6
	# max_consecutive_misses_odd = 6
	# Even Chances
	
	# Dozens and Columns
	Doz_amount_str = Doz_var.get().strip()
	Doz_amount_value = int(Doz_amount_str)
	if Dozvar.get() == 1: 
		max_consecutive_misses_doz = int(Doz_amount_str)
		append_text(text_box, f'max_consecutive_misses_Doz set to {max_consecutive_misses_doz}')
		
	Colm_amount_str = Colm_var.get().strip()
	Colm_amount_value = int(Colm_amount_str)
	if Colmvar.get() == 1: 
		max_consecutive_misses_colm = int(Colm_amount_str)
		append_text(text_box, f'max_consecutive_misses_Colm set to {max_consecutive_misses_colm}')
		
	doz1_bet, doz2_bet, doz3_bet = False, False, False
	col1_bet, col2_bet, col3_bet = False, False, False
	d1p, d2p, d3p, cl1, cl2, cl3 = 0, 0, 0, 0, 0, 0	 # Initialize counters for Dozens and Columns

	consecutive_misses_doz1 = 0
	consecutive_misses_doz2 = 0
	consecutive_misses_doz3 = 0

	consecutive_misses_col1 = 0
	consecutive_misses_col2 = 0
	consecutive_misses_col3 = 0

	# max_consecutive_misses_doz = 16 # 8 b4 for fast play. dangerous.
	# max_consecutive_misses_colm = 16
	# Dozens and Columns
	
	# Lines
	line_1_bet, line_2_bet, line_3_bet, line_4_bet, line_5_bet = False, False, False, False, False
	line_6_bet, line_7_bet, line_8_bet, line_9_bet, line_10_bet, line_11_bet = False, False, False, False, False, False
	
	lines = [
		'Line_1', 'Line_2', 'Line_3', 'Line_4', 'Line_5', 
		'Line_6', 'Line_7', 'Line_8', 'Line_9', 'Line_10', 'Line_11'
		]
		
	Line_bets = [False] * 11	
	Line_counters = [0] * 11
	Line_variables = [(f'Line_{i}_bet', f'l{i}p') for i in range(1, 12)]
	consecutive_misses_lines = [0 for _ in range(11)]
	
	Line_amount_str = Line_var.get().strip()
	Line_amount_value = int(Line_amount_str)
	if Linevar.get() == 1: 
		max_consecutive_misses_lines = int(Line_amount_str)
		append_text(text_box, f'max_consecutive_misses_Lines set to {max_consecutive_misses_lines}')
		
	# max_consecutive_misses_lines = 52 # 46 16 for testing.   
	bet_on_lines = False
	# Lines
	
	# Corners
	corner_variables = [
		("corner_1_bet", "c1p"),
		("corner_2_bet", "c2p"),
		("corner_3_bet", "c3p"),
		("corner_4_bet", "c4p"),
		("corner_5_bet", "c5p"),
		("corner_6_bet", "c6p"),
		("corner_7_bet", "c7p"),
		("corner_8_bet", "c8p"),
		("corner_9_bet", "c9p"),
		("corner_10_bet", "c10p"),
		("corner_11_bet", "c11p"),
		("corner_12_bet", "c12p"),
		("corner_13_bet", "c13p"),
		("corner_14_bet", "c14p"),
		("corner_15_bet", "c15p"),
		("corner_16_bet", "c16p"),
		("corner_17_bet", "c17p"),
		("corner_18_bet", "c18p"),
		("corner_19_bet", "c19p"),
		("corner_20_bet", "c20p"),
		("corner_21_bet", "c21p"),
		("corner_22_bet", "c21p")
		]
		
	Corner_amount_str = Corner_var.get().strip()
	Corner_amount_value = int(Corner_amount_str)
	if Cornervar.get() == 1: 
		max_consecutive_misses_corners = int(Corner_amount_str)
		append_text(text_box, f'max_consecutive_misses_Corner set to {max_consecutive_misses_corners}')
		
	consecutive_misses_corners = [0 for _ in range(22)]
	# max_consecutive_misses_corners = 88 # 70 28 for testing.
	bet_on_corners = False
	# Corners
	
	# Streets
	street_variables = [
		("street_1_bet", "st1p"),
		("street_2_bet", "st2p"),
		("street_3_bet", "st3p"),
		("street_4_bet", "st4p"),
		("street_5_bet", "st5p"),
		("street_6_bet", "st6p"),
		("street_7_bet", "st7p"),
		("street_8_bet", "st8p"),
		("street_9_bet", "st9p"),
		("street_10_bet", "st10p"),
		("street_11_bet", "st11p"),
		("street_12_bet", "st12p")
		] 
	
	Street_amount_str = Street_var.get().strip()
	Street_amount_value = int(Street_amount_str)
	if Streetvar.get() == 1: 
		max_consecutive_misses_streets = int(Street_amount_str)
		append_text(text_box, f'max_consecutive_misses_Streets set to {max_consecutive_misses_streets}')
	
	# max_consecutive_misses_streets = 58 # 8 for testing.		
	
	consecutive_misses_streets = [0 for _ in range(12)]
	bet_on_streets = False
	# Streets
	
	# Numbers
	number_variables = [
		("single_1_bet", "sgn1p"),
		("single_2_bet", "sgn2p"),
		("single_3_bet", "sgn3p"),
		("single_4_bet", "sgn4p"),
		("single_5_bet", "sgn5p"),
		("single_6_bet", "sgn6p"),
		("single_7_bet", "sgn7p"),
		("single_8_bet", "sgn8p"),
		("single_9_bet", "sgn9p"),
		("single_10_bet", "sgn10p"),
		("single_11_bet", "sgn11p"),
		("single_12_bet", "sgn12p"),
		("single_13_bet", "sgn13p"),
		("single_14_bet", "sgn14p"),
		("single_15_bet", "sgn15p"),
		("single_16_bet", "sgn16p"),
		("single_17_bet", "sgn17p"),
		("single_18_bet", "sgn18p"),
		("single_19_bet", "sgn19p"),
		("single_20_bet", "sgn20p"),
		("single_21_bet", "sgn21p"),
		("single_22_bet", "sgn22p"),
		("single_23_bet", "sgn23p"),
		("single_24_bet", "sgn24p"),
		("single_25_bet", "sgn25p"),
		("single_26_bet", "sgn26p"),
		("single_27_bet", "sgn27p"),
		("single_28_bet", "sgn28p"),
		("single_29_bet", "sgn29p"),
		("single_30_bet", "sgn30p"),
		("single_31_bet", "sgn31p"),
		("single_32_bet", "sgn32p"),
		("single_33_bet", "sgn33p"),
		("single_34_bet", "sgn34p"),
		("single_35_bet", "sgn35p"),
		("single_36_bet", "sgn36p")
		] 
	
	Number_amount_str = Number_var.get().strip()
	Number_amount_value = int(Number_amount_str)
	if Numbervar.get() == 1: 
		max_consecutive_misses_number = int(Number_amount_str)
		append_text(text_box, f'max_consecutive_misses_Number set to {max_consecutive_misses_number}')	
		
	# max_consecutive_misses_numbers = 58 # 28 for testing, short play around 100 18	
	
	consecutive_misses_numbers = [0 for _ in range(37)]	 # Assuming 1-36 numbers
	bet_on_number = False
	# Numbers
	
	# Splits
	split_bets = [False] * 57
	split_counters = [0] * 57
	split_variables = [(f'split_{i+1}_bet', f's{i+1}p') for i in range(57)]
	consecutive_misses_splits = [0] * 57
	
	Split_amount_str = Split_var.get().strip()
	Split_amount_value = int(Split_amount_str)
	if Splitvar.get() == 1: 
		max_consecutive_misses_splits = int(Split_amount_str)
		append_text(text_box, f'max_consecutive_misses_Split set to {max_consecutive_misses_splits}')
		
	# max_consecutive_misses_splits = 137 # Adjust the value as needed
	
	bet_on_splits = False
	# Splits
	# ~~~~~~~~~~~~~~ Initialize all variables ~~~~~~~~~~~~
	
	append_text(text_box,' ')
	
	# ~~~~~~~~~~ This is where all the bets and calculations are done. ~~~~~~~~~~
	while spin < tblspin:
	
		go_fullscreen()
		
		if stop_flag:
			# clear_text()
			append_text(text_box, 'The script will now come to a STOP')
			return	# Stop spinning if the stop flag is set
			
		# Wait for a maximum of 120 seconds for "no more spins.png" to disappear
		timeout = time.time() + 120
		while time.time() < timeout:
			if not pyautogui.locateCenterOnScreen("images\\table\\b_small.png"	):
				break
			time.sleep(1)
			
		findnum()
		
		try:
		
			root.update_idletasks()
			result = (number)
			
			# ~~~~~~~~~~~~~ Even Chances ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			# Red Black max_consecutive_misses EC 3 6
			if result in RouletteArrays.red:
				color = str(result)
				txcolor = 'red'
				bg_color = 'red'
				listBoxInsert(color, '', '')
				
				consecutive_misses_black += 1
				consecutive_misses_red = 0
				
				if r_bet == True:
					r_bet = False
					ecr = 0
					
			elif result in RouletteArrays.black:
				color = str(result)
				txcolor = 'white'
				bg_color = 'black'
				listBoxInsert('', '', color)
				
				consecutive_misses_red += 1
				consecutive_misses_black = 0
				
				if b_bet == True:
					b_bet = False
					ecb = 0
					
			if Redvar.get() == 1: 
				#print('red on')
				max_consecutive_misses_red = Red_amount_value
				#print(f'consecutive_misses_red = {consecutive_misses_red}')
				#print(f'max_consecutive_misses_red = {max_consecutive_misses_red}')
				if consecutive_misses_red >= max_consecutive_misses_red:
					#print('bet on red')
					# Start betting on red
					r_bet = True
					append_text(text_box, f'consecutive_misses_red {consecutive_misses_red}')
					if ecr < len(progression_1):
						value_to_bet = progression_1[ecr]
						append_text(text_box, f'Betting on Red with {value_to_bet}')
						calculate_and_simulate_betting(value_to_bet, 'Red', chips, chip_coordinates, element_coordinates)
						ecr += 1
					
			if Blackvar.get() == 1: 
				#print('black on')
				max_consecutive_misses_Black = Black_amount_value
				#print(f'consecutive_misses_black = {consecutive_misses_black}')
				#print(f'max_consecutive_misses_Black = {max_consecutive_misses_Black}')
				if consecutive_misses_black >= max_consecutive_misses_black:
					#print('bet on Black')
					# Start betting on black
					b_bet = True
					append_text(text_box, f'consecutive_misses_black {consecutive_misses_black}')
					if ecb < len(progression_1):					
						value_to_bet = progression_1[ecb]
						append_text(text_box, f'Betting on Black with {value_to_bet}')
						calculate_and_simulate_betting(value_to_bet, 'Black', chips, chip_coordinates, element_coordinates)
						ecb += 1
			# Red Black
			
			# High Low
			if result in RouletteArrays.high:
				consecutive_misses_low += 1
				consecutive_misses_high = 0

				if h_bet == True:
					h_bet = False
					ech = 0

			elif result in RouletteArrays.low:
				consecutive_misses_high += 1
				consecutive_misses_low = 0

				if l_bet == True:
					l_bet = False
					ecl = 0

			if Highvar.get() == 1: 
				max_consecutive_misses_high = int(High_amount_str)
				if consecutive_misses_high >= max_consecutive_misses_high:
					# Start betting on high
					h_bet = True
					append_text(text_box, f'consecutive_misses_High {consecutive_misses_high}')
					if ech < len(progression_1):
						value_to_bet = progression_1[ech]
						append_text(text_box, f'Betting on High with {value_to_bet}')
						calculate_and_simulate_betting(value_to_bet, 'High', chips, chip_coordinates, element_coordinates)
						ech += 1

			if Lowvar.get() == 1: 
				max_consecutive_misses_low = int(Low_amount_str)
				if consecutive_misses_low >= max_consecutive_misses_low:
					# Start betting on low
					l_bet = True
					if ecl < len(progression_1):
						append_text(text_box, f'consecutive_misses_Low {consecutive_misses_low}')
						value_to_bet = progression_1[ecl]
						append_text(text_box, f'Betting on Low with {value_to_bet}')
						calculate_and_simulate_betting(value_to_bet, 'Low', chips, chip_coordinates, element_coordinates)
						ecl += 1 
			# High Low
			
			# Even Odd
			if result in RouletteArrays.even:
				consecutive_misses_odd += 1
				consecutive_misses_even = 0

				if e_bet == True:
					e_bet = False
					ece = 0 

			elif result in RouletteArrays.odd:
				consecutive_misses_even += 1
				consecutive_misses_odd = 0

				if o_bet == True:
					o_bet = False
					eco = 0

			if Evenvar.get() == 1: 
				max_consecutive_misses_even = int(Even_amount_str)
				if consecutive_misses_even >= max_consecutive_misses_even:
					# Start betting on even
					e_bet = True
					#print(f'consecutive_misses_even ',{consecutive_misses_even})
					append_text(text_box, f'consecutive_misses_Even {consecutive_misses_even}')
					if ece < len(progression_1):
						value_to_bet = progression_1[ece]
						append_text(text_box, f'Betting on Even with {value_to_bet}')
						calculate_and_simulate_betting(value_to_bet, 'Even', chips, chip_coordinates, element_coordinates)
						ece += 1

			if Oddvar.get() == 1: 
				max_consecutive_misses_odd = int(Odd_amount_str)
				if consecutive_misses_odd >= max_consecutive_misses_odd:
					# Start betting on odd
					o_bet = True
					if eco < len(progression_1):
						append_text(text_box, f'consecutive_misses_Odd {consecutive_misses_odd}')
						value_to_bet = progression_1[eco]
						append_text(text_box, f'Betting on Odd with {value_to_bet}')
						calculate_and_simulate_betting(value_to_bet, 'Odd', chips, chip_coordinates, element_coordinates)
						eco += 1 
			# Even Odd
			# ~~~~~~~~~~~~~ Even Chances ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			
			# ~~~~~~~~~~~~~ Dozens Colums ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			# max_consecutive_misses_ doz colm 5 8 16 dozens betting not that good for profit
			# Check for Dozens
			if result in RouletteArrays.doz1:
				consecutive_misses_doz1 = 0
				consecutive_misses_doz2 += 1
				consecutive_misses_doz3 += 1
				doz2_bet = False
				doz3_bet = False

				if doz1_bet:
					doz1_bet = False
					d1p = 0

			elif result in RouletteArrays.doz2:
				consecutive_misses_doz1 += 1
				consecutive_misses_doz2 = 0
				consecutive_misses_doz3 += 1
				doz1_bet = False
				doz3_bet = False

				if doz2_bet:
					doz2_bet = False
					d2p = 0

			elif result in RouletteArrays.doz3:
				consecutive_misses_doz1 += 1
				consecutive_misses_doz2 += 1
				consecutive_misses_doz3 = 0
				doz1_bet = False
				doz2_bet = False

				if doz3_bet:
					doz3_bet = False
					d3p = 0
					
			if Dozvar.get() == 1: 
				max_consecutive_misses_doz = int(Doz_amount_str)
				
				# append_text(text_box, f'consecutive_misses_Doz1 {consecutive_misses_doz1}')
				# append_text(text_box, f'consecutive_misses_Doz2 {consecutive_misses_doz2}')
				# append_text(text_box, f'consecutive_misses_Doz3 {consecutive_misses_doz3}')
				
				if consecutive_misses_doz1 >= max_consecutive_misses_doz:
					doz1_bet = True
					doz2_bet = False
					doz3_bet = False
					append_text(text_box, f'consecutive_misses_Doz1 {consecutive_misses_doz1}')
					if d1p < len(progression_2):
						value_to_bet = progression_2[d1p]
						append_text(text_box, f'Betting on Doz1 with {value_to_bet}')
						calculate_and_simulate_betting(value_to_bet, 'Doz1', chips, chip_coordinates, element_coordinates)
						d1p += 1						
				
				elif consecutive_misses_doz2 >= max_consecutive_misses_doz:
					doz1_bet = False
					doz2_bet = True
					doz3_bet = False
					append_text(text_box, f'consecutive_misses_Doz2 {consecutive_misses_doz2}')
					if d2p < len(progression_2):
						value_to_bet = progression_2[d2p]
						append_text(text_box, f'Betting on Doz2 with {value_to_bet}')
						calculate_and_simulate_betting(value_to_bet, 'Doz2', chips, chip_coordinates, element_coordinates)
						d2p += 1
						
				elif consecutive_misses_doz3 >= max_consecutive_misses_doz:
					doz1_bet = False
					doz2_bet = False
					doz3_bet = True
					append_text(text_box, f'consecutive_misses_doz3 {consecutive_misses_doz3}')
					if d3p < len(progression_2):
						value_to_bet = progression_2[d3p]
						append_text(text_box, f'Betting on Doz3 with {value_to_bet}')
						calculate_and_simulate_betting(value_to_bet, 'Doz3', chips, chip_coordinates, element_coordinates)
						d3p += 1 
			# Check for Dozens
			
			# Check for Colums
			if result in RouletteArrays.col1:
				consecutive_misses_col1 = 0
				consecutive_misses_col2 += 1
				consecutive_misses_col3 += 1
				col2_bet = False
				col3_bet = False

				if col1_bet == True:
					col1_bet = False
					cl1 = 0

			elif result in RouletteArrays.col2:
				consecutive_misses_col2 = 0
				consecutive_misses_col1 += 1
				consecutive_misses_col3 += 1
				col1_bet = False
				col3_bet = False

				if col2_bet:
					col2_bet = False
					cl2 = 0

			elif result in RouletteArrays.col3:
				consecutive_misses_col3 = 0
				consecutive_misses_col1 += 1
				consecutive_misses_col2 += 1
				col1_bet = False
				col2_bet = False

				if col3_bet:
					col3_bet = False				
					cl3 = 0
			
			if Colmvar.get() == 1:
				max_consecutive_misses_colm = int(Colm_amount_str)
				
				# append_text(text_box, f'consecutive_misses_Col1 {consecutive_misses_col1}')
				# append_text(text_box, f'consecutive_misses_Col2 {consecutive_misses_col2}')
				# append_text(text_box, f'consecutive_misses_Col3 {consecutive_misses_col3}')
				
				if consecutive_misses_col1 >= max_consecutive_misses_colm:
					col1_bet = True
					col2_bet = False
					col3_bet = False
					append_text(text_box, f'consecutive_misses_Col1 {consecutive_misses_col1}')
					if cl1 < len(progression_2):
						value_to_bet = progression_2[cl1]
						append_text(text_box, f'Betting on Col1 with {value_to_bet}')
						calculate_and_simulate_betting(value_to_bet, 'Col1', chips, chip_coordinates, element_coordinates)
						cl1 += 1
				
				elif consecutive_misses_col2 >= max_consecutive_misses_colm:
					col2_bet = True
					col1_bet = False
					col3_bet = False
					append_text(text_box, f'consecutive_misses_Col2 {consecutive_misses_col2}')
					if cl2 < len(progression_2):
						value_to_bet = progression_2[cl2]
						append_text(text_box, f'Betting on Col2 with {value_to_bet}')
						calculate_and_simulate_betting(value_to_bet, 'Col2', chips, chip_coordinates, element_coordinates)
						cl2 += 1
				
				elif consecutive_misses_col3 >= max_consecutive_misses_colm:
					col3_bet = True
					col2_bet = False
					col1_bet = False
					append_text(text_box, f'consecutive_misses_Col3 {consecutive_misses_col3}')
					if cl3 < len(progression_2):
						value_to_bet = progression_2[cl3]
						append_text(text_box, f'Betting on Col3 with {value_to_bet}')
						calculate_and_simulate_betting(value_to_bet, 'Col3', chips, chip_coordinates, element_coordinates)
						cl3 += 1
			# ~~~~~~~~~~~~~ Dozens Colums ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			
			# ~~~~~~~~~~~~~ Iterate over Lines ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			# max_consecutive_misses_lines 52 46 16 for testing.
			if Linevar.get() == 1:
				max_consecutive_misses_lines = int(Line_amount_str)
				
				for i, line in enumerate(lines):
					if result in getattr(RouletteArrays, f'line_{i+1}', []):
						# print(f"Betting on line {i+1}")
						for j in range(0, 11):
							consecutive_misses_lines[j] += 1
						# Remove the following line
						consecutive_misses_lines[i] = 0	 # Reset consecutive misses for the current line

						# Reset other lines
						for k, v in Line_variables:
							if k != f'line_{i}_bet':
								globals()[k] = False

						# Set the current line and counter variables
						current_line_bet, current_counter = Line_variables[i]
						globals()[current_line_bet] = True
						globals()[current_counter] = 0

					# Print and simulate betting if needed
					if consecutive_misses_lines[i] >= max_consecutive_misses_lines:
						current_p = globals()[current_counter]
						if current_p < len(progression_5):
							bet_on_lines = True
							value_to_bet = progression_5[current_p]
							append_text(text_box, f'Betting on Line_{i+1} with {value_to_bet}')
							# print(f'Betting on {line} with {value_to_bet}')
							calculate_and_simulate_betting(value_to_bet, f'Line_{i+1}', chips, chip_coordinates, element_coordinates)
							globals()[current_counter] += 1
			# ~~~~~~~~~~~~~ Iterate over Lines ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			
			# ~~~~~~~~~~~~~ Iterate over corners ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			# max_consecutive_misses_corners = 88 70 28 for testing.
			if Cornervar.get() == 1:
				for i, corner in enumerate(corners):
					if result in getattr(RouletteArrays, f'corner_{i+1}', []):
						for j in range(0, 22):
							consecutive_misses_corners[j] += 1

						consecutive_misses_corners[i] = 0  # Reset consecutive misses for the current corner

						# Reset other corners
						for k, v in corner_variables:
							globals()[k] = False
						# Set the current corner and counter variables
						current_corner_bet, current_counter = corner_variables[i]
						globals()[current_corner_bet] = True
						globals()[current_counter] = 0

					# Print and simulate betting if needed
					if consecutive_misses_corners[i] >= max_consecutive_misses_corners:
						current_p = globals()[current_counter]
						if current_p < len(progression_8):
							bet_on_corners = True
							value_to_bet = progression_8[current_p]
							append_text(text_box, f'Betting on Corner_{i+1} with {value_to_bet}')
							calculate_and_simulate_betting(value_to_bet, f'Corner_{i+1}', chips, chip_coordinates, element_coordinates)
							globals()[current_counter] += 1
			# ~~~~~~~~~~~~~ Iterate over corners ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			
			# ~~~~~~~~~~~~~ Iterate over streets ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			# max_consecutive_misses_streets = 12 24 58 for testing.
			if Streetvar.get() == 1:
				for i, street in enumerate(streets):
					if result in getattr(RouletteArrays, f'street_{i+1}', []):
						for j in range(0, 12):
							consecutive_misses_streets[j] += 1

						consecutive_misses_streets[i] = 0  # Reset consecutive misses for the current street

						# Reset other streets
						for k, v in street_variables:
							globals()[k] = False
						# Set the current street and counter variables
						current_street_bet, current_counter_street = street_variables[i]
						globals()[current_street_bet] = True
						globals()[current_counter_street] = 0

					# Print and simulate betting if needed
					if consecutive_misses_streets[i] >= max_consecutive_misses_streets:
						current_p = globals()[current_counter_street]
						if current_p < len(progression_11):
							bet_on_streets = True
							value_to_bet = progression_11[current_p]
							append_text(text_box, f'Betting on Street_{i+1} with {value_to_bet}')
							calculate_and_simulate_betting(value_to_bet, f'Street_{i+1}', chips, chip_coordinates, element_coordinates)
							globals()[current_counter_street] += 1
			# ~~~~~~~~~~~~~ Iterate over streets ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			
			# ~~~~~~~~~~~~~ Iterate over Numbers ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			# max_consecutive_misses_numbers = 18 28 58	 for testing, short play around 100 
			if Numbervar.get() == 1:
				for i, number_bet in enumerate(number_variables):
					current_number_bet, current_counter_number = number_bet
					if result == i + 1:	 # Assuming 1-36 numbers
						for j in range(1, 37):	# Assuming 1-36 numbers
							consecutive_misses_numbers[j] += 1
						consecutive_misses_numbers[i] = 0  # Reset consecutive misses for the current number

						# Reset other numbers
						for k, v in number_variables:
							globals()[k] = False
						# Set the current number and counter variables
						globals()[current_number_bet] = True
						globals()[current_counter_number] = 0

					if consecutive_misses_numbers[i] >= max_consecutive_misses_number:
						current_p = globals().get(current_counter_number, 0)
						if current_p < len(progression_35):
							bet_on_number = True
							value_to_bet = progression_35[current_p]
							if stop_flag:
								# clear_text()
								append_text(text_box, 'The script will now come to a STOP')
								return	# Stop spinning if the stop flag is set
							append_text(text_box, f'Betting on Number {i+1} with {value_to_bet}')
							calculate_and_simulate_betting(value_to_bet, f'Single_{i+1}', chips, chip_coordinates, element_coordinates)
							globals()[current_counter_number] = current_p + 1
			# ~~~~~~~~~~~~~ Iterate over Numbers ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			
			# ~~~~~~~~~~~~~ Iterate over Splits ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			# max_consecutive_misses_streets = 77 (2 3 x single numbers) for testing.
			if Splitvar.get() == 1:
				for i, split in enumerate(split_variables):
					if result in getattr(RouletteArrays, f'split_{i+1}', []):
						for j in range(57):
							consecutive_misses_splits[j] += 1
						consecutive_misses_splits[i] = 0  # Reset consecutive misses for the current split

						for k, v in split_variables:
							if k != f'split_{i+1}_bet':
								globals()[k] = False

						current_split_bet, current_counter_split = split_variables[i]
						globals()[current_split_bet] = True
						globals()[current_counter_split] = 0
						split_bets[i] = True  # Set the corresponding split_bet to True

					if consecutive_misses_splits[i] >= max_consecutive_misses_splits:
						current_p = globals()[current_counter_split]
						if current_p < len(progression_17):
							bet_on_splits = True
							value_to_bet = progression_17[current_p]
							append_text(text_box, f'Betting on Split_{i+1} with {value_to_bet}')
							calculate_and_simulate_betting(value_to_bet, f'Split_{i+1}', chips, chip_coordinates, element_coordinates)
							globals()[current_counter_split] += 1
			# ~~~~~~~~~~~~~ Iterate over Splits ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			
			# Check consecutive misses for each element
			for i, element in enumerate(elements_to_track):
				if result not in element:
					current_missed_counts[i] += 1
					max_missed_counts[i] = max(max_missed_counts[i], current_missed_counts[i])
				else:
					current_missed_counts[i] = 0
			# Check consecutive misses for each element
		
			if any([
				r_bet, b_bet , l_bet, h_bet, o_bet, e_bet, # even chances
				doz1_bet, doz2_bet, doz3_bet, col1_bet, col2_bet, col3_bet, # doz/colm
				bet_on_lines , bet_on_corners , bet_on_streets , bet_on_number , bet_on_splits
			]):
				pass
			else:
				freespin()
				
			if bet_on_lines:
				bet_on_lines = False
				
			if bet_on_corners:
				bet_on_corners = False
				
			if bet_on_streets:
				bet_on_streets = False
				
			if bet_on_number:
				bet_on_number = False
				
			if bet_on_splits:
				bet_on_splits = False
			
			pyautogui.click(1565, 970) #click on the spin button
			append_text(text_box, f'Spin = {spin}, Number = {number}, {bg_color}')
			
			array_row_colm(result)
			
			landednumcolorchange.lab_change1 = Label(x[2], text=result, 
				height=2, width=4, bg='#4BA168', fg='white', font=('Verdana', 9, 'bold'))
			landednumcolorchange.lab_change1.grid(row=rown, column=colm, padx=1, pady=1)
			time.sleep(2)
			landednumcolorchange.lab_change1 = Label(x[2], text=result, 
				height=2, width=4, bg=bg_color, fg='white', font=('Verdana', 9, 'bold'))
			landednumcolorchange.lab_change1.grid(row=rown, column=colm, padx=1, pady=1)
			
			display_label(root, x, result, txcolor)
			
		except UnboundLocalError:
			# Handle the case when the variables are not associated with a value
			clear_text()
			append_text('Something went wrong.')
			blanklabel_message(root,x,'Something went wrong.')
			append_text('Error: Variables not associated with a value')
	
		spin += 1
		
		if spin == tblspin:
			append_text(text_box,'Stats have been updated, view the stats windows')
			if var1.get() == 1:	 # Check if the checkbox is ticked
				save_to_pickle('numdata\\stats_data\\bv\\data.pkl',
					{'elements_to_track': elements_to_track, 'max_missed_counts': max_missed_counts})
				filename = f"numdata\\stats_data\\bv\\bv_stats_for_{spin}_spins_data_{timestamp}.pkl"
				save_to_pickle(filename, {'elements_to_track': elements_to_track, 'max_missed_counts': max_missed_counts})
	# ~~~~~~~~~~ This is where all the bets and calculations are done. ~~~~~~~~~~
	blanklabel_message(root,x,'Play on BetVoyager has completed')
	enable_buttons()
# BVRunTestRealPlay this is where I test out playing on the Table.

# load coords from external file so that people can change the x y coords.
def load_coordinates(filename):
	with open(filename, 'r') as file:
		coordinates = json.load(file)
	return coordinates
	
# Load chip coordinates and element coordinates
chip_coordinates = load_coordinates('chip_coords.json')
element_coordinates = load_coordinates('element_coords.json')

# calculate_and_simulate_betting works out how to place on the table
def calculate_and_simulate_betting(value, element, chips, chip_coords, element_coords):
	remaining_value = value
	bet_formula = []

	# Calculate the betting formula
	for chip in sorted(chips, reverse=True):
		if remaining_value >= chip:
			num_chips = int(remaining_value / chip)
			remaining_value -= num_chips * chip
			bet_formula.append((chip, num_chips))

	# Simulate the betting clicks
	for chip_value, num_chips in bet_formula:
		pyautogui.click(chip_coords[str(chip_value)][0], chip_coords[str(chip_value)][1])
		
		for _ in range(num_chips):
			pyautogui.click(element_coords[element][0], element_coords[element][1])
			#time.sleep(0.5)	 # Introducing a small delay between clicks for demonstration purposes
# calculate_and_simulate_betting works out how to place on the table

# go_fullscreen
def go_fullscreen():
	#pdb.set_trace()  # n (next), c (continue) q (quit) p variable (print) l (list)
	fs = pyautogui.locateOnScreen("images\\search\\go_fullscreen.png")
	if fs:
		try:
		  x1, y1 = pyautogui.locateCenterOnScreen("images\\search\\go_fullscreen.png")
		  pyautogui.click(x1, y1)
		except TypeError:
		  blanklabel_message(root,x,'go_fullscreen.png not found on screen')
# go_fullscreen
  
# findnum,numberfoundonscreen and locatenumberonscreen are the key components of Table PLAY
def findnum():
	locatenumberonscreen(1360,70,100,100)
	numberfoundonscreen()
	
def numberfoundonscreen():
	global number
	if Num01:
		#print('Located Number 9 on the screen')
		blanklabel_message(root,x,'Located Number 1 on the screen')
		number = 1
		
	if Num02:
		#print('Located Number 9 on the screen')
		blanklabel_message(root,x,'Located Number 2 on the screen')
		number = 2
	
	if Num03:
		#print('Located Number 9 on the screen')
		blanklabel_message(root,x,'Located Number 3 on the screen')
		number = 3
		
	if Num04:
		#print('Located Number 9 on the screen')
		blanklabel_message(root,x,'Located Number 4 on the screen')
		number = 4
		
	if Num05:
		#print('Located Number 9 on the screen')
		blanklabel_message(root,x,'Located Number 5 on the screen')
		number = 5
		
	if Num06:
		#print('Located Number 9 on the screen')
		blanklabel_message(root,x,'Located Number 6 on the screen')
		number = 6
		
	if Num07:
		#print('Located Number 9 on the screen')
		blanklabel_message(root,x,'Located Number 7 on the screen')
		number = 7
		
	if Num08:
		#print('Located Number 9 on the screen')
		blanklabel_message(root,x,'Located Number 8 on the screen')
		number = 8
			
	if Num09:
		#print('Located Number 9 on the screen')
		blanklabel_message(root,x,'Located Number 9 on the screen')
		number = 9
	
	if Num10:
		#print('Located Number 9 on the screen')
		blanklabel_message(root,x,'Located Number 10 on the screen')
		number = 10
		
	if Num11:
		#print('Located Number 9 on the screen')
		blanklabel_message(root,x,'Located Number 11 on the screen')
		number = 11
		
	if Num12:
		#print('Located Number 9 on the screen')
		blanklabel_message(root,x,'Located Number 12 on the screen')
		number = 12
	
	if Num13:
		#print('Located Number 9 on the screen')
		blanklabel_message(root,x,'Located Number 13 on the screen')
		number = 13
		
	if Num14:
		#print('Located Number 9 on the screen')
		blanklabel_message(root,x,'Located Number 14 on the screen')
		number = 14
		
	if Num15:
		#print('Located Number 9 on the screen')
		blanklabel_message(root,x,'Located Number 15 on the screen')
		number = 15
		
	if Num16:
		#print('Located Number 9 on the screen')
		blanklabel_message(root,x,'Located Number 16 on the screen')
		number = 16
		
	if Num17:
		#print('Located Number 9 on the screen')
		blanklabel_message(root,x,'Located Number 17 on the screen')
		number = 17
		
	if Num18:
		#print('Located Number 9 on the screen')
		blanklabel_message(root,x,'Located Number 18 on the screen')
		number = 18
			
	if Num19:
		#print('Located Number 9 on the screen')
		blanklabel_message(root,x,'Located Number 19 on the screen')
		number = 19
	
	if Num20:
		#print('Located Number 9 on the screen')
		blanklabel_message(root,x,'Located Number 20 on the screen')
		number = 20
		
	if Num21:
		#print('Located Number 9 on the screen')
		blanklabel_message(root,x,'Located Number 21 on the screen')
		number = 21
		
	if Num22:
		#print('Located Number 9 on the screen')
		blanklabel_message(root,x,'Located Number 22 on the screen')
		number = 22
	
	if Num23:
		#print('Located Number 9 on the screen')
		blanklabel_message(root,x,'Located Number 23 on the screen')
		number = 23
		
	if Num24:
		#print('Located Number 9 on the screen')
		blanklabel_message(root,x,'Located Number 24 on the screen')
		number = 24
		
	if Num25:
		#print('Located Number 9 on the screen')
		blanklabel_message(root,x,'Located Number 25 on the screen')
		number = 25
		
	if Num26:
		#print('Located Number 9 on the screen')
		blanklabel_message(root,x,'Located Number 26 on the screen')
		number = 26
		
	if Num27:
		#print('Located Number 9 on the screen')
		blanklabel_message(root,x,'Located Number 27 on the screen')
		number = 27
		
	if Num28:
		#print('Located Number 9 on the screen')
		blanklabel_message(root,x,'Located Number 28 on the screen')
		number = 28
			
	if Num29:
		#print('Located Number 9 on the screen')
		blanklabel_message(root,x,'Located Number 29 on the screen')
		number = 29
		
	if Num30:
		#print('Located Number 9 on the screen')
		blanklabel_message(root,x,'Located Number 30 on the screen')
		number = 30
		
	if Num31:
		#print('Located Number 9 on the screen')
		blanklabel_message(root,x,'Located Number 31 on the screen')
		number = 31
		
	if Num32:
		#print('Located Number 9 on the screen')
		blanklabel_message(root,x,'Located Number 32 on the screen')
		number = 32
	
	if Num33:
		#print('Located Number 9 on the screen')
		blanklabel_message(root,x,'Located Number 33 on the screen')
		number = 33
		
	if Num34:
		#print('Located Number 9 on the screen')
		blanklabel_message(root,x,'Located Number 34 on the screen')
		number = 34
		
	if Num35:
		#print('Located Number 9 on the screen')
		blanklabel_message(root,x,'Located Number 35 on the screen')
		number = 35
		
	if Num36:
		#print('Located Number 9 on the screen')
		blanklabel_message(root,x,'Located Number 36 on the screen')
		number = 36
		
def locatenumberonscreen(regx,regy,regw,regh):
	global Num01,Num02,Num03,Num04,Num05,Num06
	global Num07,Num08,Num09,Num10,Num11,Num12
	global Num13,Num14,Num15,Num16,Num17,Num18
	global Num19,Num20,Num21,Num22,Num23,Num24
	global Num25,Num26,Num27,Num28,Num29,Num30
	global Num31,Num32,Num33,Num34,Num35,Num36
	
	Num01 = pyautogui.locateCenterOnScreen("images\\numbers\\1.png",  region = (regx,regy,regw,regh)) #grayscale=True locateOnScreen
	Num02 = pyautogui.locateCenterOnScreen("images\\numbers\\2.png",  region = (regx,regy,regw,regh))
	Num03 = pyautogui.locateCenterOnScreen("images\\numbers\\3.png",  region = (regx,regy,regw,regh))
	Num04 = pyautogui.locateCenterOnScreen("images\\numbers\\4.png",  region = (regx,regy,regw,regh))
	Num05 = pyautogui.locateCenterOnScreen("images\\numbers\\5.png",  region = (regx,regy,regw,regh))
	Num06 = pyautogui.locateCenterOnScreen("images\\numbers\\6.png",  region = (regx,regy,regw,regh))
	Num07 = pyautogui.locateCenterOnScreen("images\\numbers\\7.png",  region = (regx,regy,regw,regh))
	Num08 = pyautogui.locateCenterOnScreen("images\\numbers\\8.png",  region = (regx,regy,regw,regh))
	Num09 = pyautogui.locateCenterOnScreen("images\\numbers\\9.png",  region = (regx,regy,regw,regh))
	Num10 = pyautogui.locateCenterOnScreen("images\\numbers\\10.png",  region = (regx,regy,regw,regh))
	Num11 = pyautogui.locateCenterOnScreen("images\\numbers\\11.png",  region = (regx,regy,regw,regh))
	Num12 = pyautogui.locateCenterOnScreen("images\\numbers\\12.png",  region = (regx,regy,regw,regh))
	Num13 = pyautogui.locateCenterOnScreen("images\\numbers\\13.png",  region = (regx,regy,regw,regh))
	Num14 = pyautogui.locateCenterOnScreen("images\\numbers\\14.png",  region = (regx,regy,regw,regh))
	Num15 = pyautogui.locateCenterOnScreen("images\\numbers\\15.png",  region = (regx,regy,regw,regh))
	Num16 = pyautogui.locateCenterOnScreen("images\\numbers\\16.png",  region = (regx,regy,regw,regh))
	Num17 = pyautogui.locateCenterOnScreen("images\\numbers\\17.png",  region = (regx,regy,regw,regh))
	Num18 = pyautogui.locateCenterOnScreen("images\\numbers\\18.png",  region = (regx,regy,regw,regh))
	Num19 = pyautogui.locateCenterOnScreen("images\\numbers\\19.png",  region = (regx,regy,regw,regh))
	Num20 = pyautogui.locateCenterOnScreen("images\\numbers\\20.png",  region = (regx,regy,regw,regh))
	Num21 = pyautogui.locateCenterOnScreen("images\\numbers\\21.png",  region = (regx,regy,regw,regh)) # keep a look out for this one
	Num22 = pyautogui.locateCenterOnScreen("images\\numbers\\22.png",  region = (regx,regy,regw,regh))
	Num23 = pyautogui.locateCenterOnScreen("images\\numbers\\23.png",  region = (regx,regy,regw,regh))
	Num24 = pyautogui.locateCenterOnScreen("images\\numbers\\24.png",  region = (regx,regy,regw,regh))
	Num25 = pyautogui.locateCenterOnScreen("images\\numbers\\25.png",  region = (regx,regy,regw,regh))
	Num26 = pyautogui.locateCenterOnScreen("images\\numbers\\26.png",  region = (regx,regy,regw,regh))
	Num27 = pyautogui.locateCenterOnScreen("images\\numbers\\27.png",  region = (regx,regy,regw,regh))
	Num28 = pyautogui.locateCenterOnScreen("images\\numbers\\28.png",  region = (regx,regy,regw,regh))
	Num29 = pyautogui.locateCenterOnScreen("images\\numbers\\29.png",  region = (regx,regy,regw,regh)) # keep a look out for this one
	Num30 = pyautogui.locateCenterOnScreen("images\\numbers\\30.png",  region = (regx,regy,regw,regh))
	Num31 = pyautogui.locateCenterOnScreen("images\\numbers\\31.png",  region = (regx,regy,regw,regh))
	Num32 = pyautogui.locateCenterOnScreen("images\\numbers\\32.png",  region = (regx,regy,regw,regh))
	Num33 = pyautogui.locateCenterOnScreen("images\\numbers\\33.png",  region = (regx,regy,regw,regh))
	Num34 = pyautogui.locateCenterOnScreen("images\\numbers\\34.png",  region = (regx,regy,regw,regh))
	Num35 = pyautogui.locateCenterOnScreen("images\\numbers\\35.png",  region = (regx,regy,regw,regh))
	Num36 = pyautogui.locateCenterOnScreen("images\\numbers\\36.png",  region = (regx,regy,regw,regh))
# findnum,numberfoundonscreen and locatenumberonscreen are the key components of Table PLAY
# ~~~~~~~~~~~~~~~  Real Mode Test Area ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# buttons
class buttons():
	# butRNG run RNG mode
	butRNG = Button(x[3], text='RNG', width=3, bg='#00FFFF', font=('Verdana', 9, 'bold'),state=NORMAL,
		command=RNG) # RNG btnClickFunction
	butRNG.place(x=368, y=0)
	
	# testing button commands here
	spinB = Button(x[3], text='Play', width=4, bg='#00FFFF', font=('Verdana', 9, 'bold'), 
		command=PlayBV) # PlayBV btnClickFunction
	spinB.place(x=324, y=0)
	
	# ~~~~~~~~~~~~~~~ Expanded Window ~~~~~~~~~
	butstatsB = Button(x[3], text='Text B', width=5, bg='#00FFFF', font=('Verdana', 9, 'bold'),state=NORMAL,
		command=largewin) # largewin 
	butstatsB.place(x=472, y=0)
	
	# butstatsR Stats and Settings
	butstatsR = Button(x[3], text='Settings', width=7, bg='#00FFFF', font=('Verdana', 9, 'bold'), 
		command=widewin) # widewin
	butstatsR.place(x=404, y=0)
	# ~~~~~~~~~~~~~~~ Expanded Window ~~~~~~~~~
	
		# about me window
	aboutB = Button(x[5],text='About', width=5, bg='#00FFFF', font=('Verdana', 9, 'bold'), 
		command=about_window_show) # btnClickFunction about_window_show
	aboutB.place(x=9, y=160)
	
	# ~~~~~~~~~~~~~~~ Settings commands ~~~~~~~~~
	Savesettings = Button(x[5], text='Save', width=5, bg='#00FFFF', font=('Verdana', 9, 'bold'), 
		command=save_settings) # save_settings btnClickFunction
	Savesettings.place(x=9, y=132)

	loadsettings = Button(x[5], text='Load', width=5, bg='#00FFFF', font=('Verdana', 9, 'bold'), 
		command=load_settings) # load_settings btnClickFunction
	loadsettings.place(x=69, y=132)
	# ~~~~~~~~~~~~~~~ Settings commands ~~~~~~~~~
	
	# ~~~~~~~~~~~~~~~ Stats Windows ~~~~~~~~~~~~~~~~~
	butstats1 = Button(x[3], text='Stats1', width=5, bg='#00FFFF', font=('Verdana', 9, 'bold'),
		command=display_stats1_window_button) # display_stats1_window_button)
	butstats1.place(x=1, y=0)

	butstats2 = Button(x[3], text='Stats2', width=5, bg='#00FFFF', font=('Verdana', 9, 'bold'), 
		command=display_stats2_window_button) # display_stats2_window_button
	butstats2.place(x=54, y=0)

	butstats3 = Button(x[3], text='Stats3', width=5, bg='#00FFFF', font=('Verdana', 9, 'bold'), 
		command=display_stats3_window_button) # display_stats3_window_button
	butstats3.place(x=107, y=0)

	butstats4 = Button(x[3], text='Stats4', width=5, bg='#00FFFF', font=('Verdana', 9, 'bold'), 
		command=display_stats4_window_button) # display_stats4_window_button
	butstats4.place(x=159, y=0)
	# ~~~~~~~~~~~~~~~ Stats Windows ~~~~~~~~~~~~~~~~~
	
	# showscaptureimages
	butcapimg = Button(x[3], text='Images', width=6, bg='#00FFFF', font=('Verdana', 9, 'bold'),state=NORMAL, 
		command=get_showscaptureimages) # get_showscaptureimages
	butcapimg.place(x=264, y=0)
	
	# ~~~~~~~~~~~~~~ STOP ~~~~~~~~~~~~~~~~~~~~
	stopB = Button(x[3], text='STOP', width=5, bg='RED',fg='Yellow', font=('Verdana', 9, 'bold'), 
		command=stop_spins) # stop_spins
	stopB.place(x=212, y=0)
	# ~~~~~~~~~~~~~~ STOP ~~~~~~~~~~~~~~~~~~~~
	
	# ~~~~~~~~~~~~~~~ BetVoyager Bet Settings ~~~~~~~~~
	BVSavesettings = Button(x[7], text='Save', width=5, bg='#00FFFF', font=('Verdana', 9, 'bold'), 
		command=BVsave_settings) # BVsave_settings btnClickFunction
	BVSavesettings.place(x=322, y=160) 
	
	BVloadsettings = Button(x[7], text='Load', width=5, bg='#00FFFF', font=('Verdana', 9, 'bold'), 
		command=BVload_settings) # BVload_settings btnClickFunction
	BVloadsettings.place(x=381, y=160)
	
	BVloadsettings2 = Button(x[7], text='Load Settings from Data', width=22, bg='#00FFFF', font=('Verdana', 7, 'bold'), 
		command=LoadBVSettingsFromData) # LoadBVSettingsFromData btnClickFunction
	BVloadsettings2.place(x=6, y=170)
	# ~~~~~~~~~~~~~~~ BetVoyager Bet Settings ~~~~~~~~~
	
	# test script defs
	testB = Button(x[5],text='Test', width=5, bg='#00FFFF', font=('Verdana', 9, 'bold'), 
		command=btnClickFunction) # btnClickFunction  bvruntest
	testB.place(x=69, y=160) 
# buttons
##################################### Main Code (defs & class) #####################

# main start

showchoice()

append_text(text_box,main_title)
blanklabel_message(root,x,'Important Messages will be displayed here') # use this for error messages

display_label(root,x,7,'red')

root.mainloop()

# Notes
# run threads on things that need to run independently.
# check the code so it makes sense and keep up to date to what is happening.

# Notes of scripts that have info in them.
# BV-Flash-Elemental-V0.4 main.py main-09-working.py
# BVNoZero V16-Flash OldScripts V5 BVNoZeroNoFlash-GUI-V5.0.py 
# BVNoZero V-Flash V24-Flash