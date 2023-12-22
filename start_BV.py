import tkinter as tk
from tkinter import messagebox
import subprocess
import psutil
import pygetwindow as gw
import pyautogui
import time
from utils import *

import os #install library

import linecache

import threading

import ThreadPoolExecutorPlus

executable_path = "C:\Program Files (x86)\FlashBrowser\FlashBrowser.exe"  # Replace with the actual path to your executable

def is_process_running(process_name):
	for process in psutil.process_iter(['pid', 'name']):
		if process.info['name'] == process_name:
			return True
	return False
	
def load_data_from_secret_file(root):
	global mUsername,mPasswrd

	if os.path.isfile("secret"):
		# print('secret file found')
		global mUsername,mPasswrd
		linecache.clearcache()
		mUsername = linecache.getline(r"secret", 1)
		mUsername = mUsername.strip()
		mPasswrd = linecache.getline(r"secret", 2)
		mPasswrd = mPasswrd.strip()
	else:
		print('no secret file found')
		messagebox.showerror("Error", "No username or password found. Closing down the program.")
		root.destroy()

def get_flash_browser_window():
	# Search for the window with the title "Flash Browser"
	flash_browser_window = gw.getWindowsWithTitle("Flash Browser")

	# Check if the window was found
	if flash_browser_window:
		return flash_browser_window[0]
	else:
		return None
		
def open_ex(text_box, root):
	# If none of the images are found, open the executable
	append_text(text_box, "None of the images found. Opening the executable FlashBrowser.exe.")
	# Check if the process is already running
	if is_process_running(executable_path):
		append_text(text_box, f"{executable_path} is already running.")
	else:
		try:
			process = subprocess.Popen([executable_path])
			
			# Allow some time for the window to open
			time.sleep(2)
			
			# Get the active window
			active_window = gw.getActiveWindow()
			# Maximize the active window
			active_window.maximize()
			
			find_image_on_screen(text_box, root)
				
		except FileNotFoundError:
				append_text(text_box, f"Error: {executable_path} not found.")
		# except Exception as e:
		#	append_text(text_box, f"An error occurred: {e}")

def find_image_on_screen(text_box, root):
	global mUsername,mPasswrd
	
	load_data_from_secret_file(root)
	
	completion_event = threading.Event()
	pause_event = threading.Event() 
	try:
		image_to_find1 = "images\\search\\fullscreen.png"
		image_to_find2 = "images\\search\\go_fullscreen.png"
		
		image_to_find3 = "images\\search\\bv_logo.png"
		text_to_find1 = "images\\search\\login.png"
		text_to_find2 = "images\\search\\password.png"
		image_to_find4 = "images\\search\\bv_proflie.png"
		
		image_to_find5 = "images\\search\\no_zero_roulette.png"
		
		image_to_find6 = "images\\search\\demo_mode.png"
		
		text_to_find = "images\\search\\google.png"
		
		# Step 1: Look for fullscreen.png
		fullscreen = pyautogui.locateOnScreen(image_to_find1)
		if fullscreen:
			#append_text(text_box, f"Image '{image_to_find1}' found at position {fullscreen}.")
			append_text(text_box, 'Ready to play')
			#completion_event.set()
			# The rest of your logic for handling the found image
		else:
			# Step 2: Look for go_fullscreen.png
			go_fullscreen = pyautogui.locateOnScreen(image_to_find2)
			if go_fullscreen:
				#append_text(text_box, f"Image '{image_to_find2}' found at position {go_fullscreen}.")
				# Click on the 'go_fullscreen' button
				pyautogui.click(go_fullscreen)
				time.sleep(2)
			else:
				# Step 3: Look for bv_logo.png
				bv_logo = pyautogui.locateOnScreen(image_to_find3)
				if bv_logo:
					#append_text(text_box, f"Image '{image_to_find3}' found at position {bv_logo}.")
					
					# Search for the Flash Browser window
					flash_browser_window = get_flash_browser_window()
					# Check if the Flash Browser window was found
					if flash_browser_window:
						# Maximize the Flash Browser window
						flash_browser_window.maximize()
						append_text(text_box, "Flash Browser window maximized.")
						
						time.sleep(2)
						
						profile_pic = pyautogui.locateOnScreen(image_to_find4)
						if profile_pic:
							#append_text(text_box, f"Image '{image_to_find4}' found at position {profile_pic}.")
							
							no_zero_open = pyautogui.locateOnScreen(image_to_find5)
							if no_zero_open:
								#append_text(text_box, f"Image '{image_to_find5}' found at position {no_zero_open}.")
								
								center_x = no_zero_open.left + no_zero_open.width // 2
								center_y = no_zero_open.top + no_zero_open.height // 2
								pyautogui.moveTo(center_x, center_y)
								
								time.sleep(2)
								
								demo_mode = pyautogui.locateOnScreen(image_to_find6) 
								if demo_mode:
									#append_text(text_box, f"Image '{image_to_find6}' found at position {demo_mode}.") 
									center_x = demo_mode.left + demo_mode.width // 2
									center_y = demo_mode.top + demo_mode.height // 2
									pyautogui.click(center_x, center_y)
									clear_text()
									append_text(text_box, "Wait until the No Zero Roulette table is open.")
									append_text(text_box, "Then Press Play Again to play in fullscreen mode")
							
						else:
						
							login = pyautogui.locateOnScreen(text_to_find1)
							if login:
								#append_text(text_box, f"Image '{text_to_find1}' found at position {login}.")
								
								center_x = login.left + login.width // 2
								center_y = login.top + login.height // 2
								
								# Simulate a mouse click at the center of the found location
								pyautogui.click(center_x, center_y)
								
								# Type some text
								text_to_type = mUsername # grantdownunder
								pyautogui.typewrite(text_to_type)
								
							password = pyautogui.locateOnScreen(text_to_find2)
							if password:
								#append_text(text_box, f"Image '{text_to_find2}' found at position {password}.")
								
								center_x = password.left + password.width // 2
								center_y = password.top + password.height // 2
								
								# Simulate a mouse click at the center of the found location
								pyautogui.click(center_x, center_y)
								
								# Type some text
								append_text(text_box, "Loggin In with username and password")
								text_to_type = mPasswrd # "Nicola02!"
								pyautogui.typewrite(text_to_type)
								# Press the "Enter" key
								pyautogui.press("enter")								
								
								append_text(text_box, "You are now logged into betvoyager.com")
								append_text(text_box, "Press Play Again to load No Zero Roulette Demo")
								pause_event.wait()
								clear_text()
					else:
						append_text(text_box, "Something went wrong.")
				else:
					# Check for the existence of the google image
					location = pyautogui.locateOnScreen(text_to_find)
					if location:
						#append_text(text_box, f"Image '{text_to_find}' found at position {location}.")
						flash_browser_window = get_flash_browser_window()
						flash_browser_window.maximize()
						
						# Wait for a moment to ensure the window has fully loaded
						time.sleep(2)
						
						# Calculate the center of the found location
						center_x = location.left + location.width // 2
						center_y = location.top + location.height // 2
						
						# Simulate a mouse click at the center of the found location
						pyautogui.click(center_x, center_y)
						
						# Type some text
						append_text(text_box, "Opening betvoyager.com with my referral link.")
						text_to_type = "https://betvoyager.com/equal-odds/?p=E4AO05&lid=17"
						pyautogui.typewrite(text_to_type)
						append_text(text_box, "This is my reffal link to BetVoyager \n "
							"https://betvoyager.com/equal-odds/?p=E4AO05&lid=17")
							
						pyautogui.press("enter")
						
						# Simulate pressing the backspace key to clear the text
						for _ in range(len(text_to_type)):
							pyautogui.press('backspace')							
						
						append_text(text_box, "Opening betvoyager.com Games.")
						text_to_type = "https://betvoyager.com/"
						pyautogui.typewrite(text_to_type)
						time.sleep(5)
						
						# Press the "Enter" key
						pyautogui.press("enter")
						clear_text()
						append_text(text_box, "Wait until betvoyager.com is open, and then Press Play Again")
						pause_event.wait()
					else:
						open_ex(text_box, root) # open the executable
						append_text(text_box, "Press Play Again")
						pause_event.wait()					
		
	except Exception as e:
		append_text(text_box, f"An error occurred: {e}")