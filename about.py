from tkinter import *
import os
from time import sleep

import webbrowser

# selenium
import threading

import warnings

def fb_about():
	global url
	url = "https://www.facebook.com/thomasrgrant/"
	t1 = threading.Thread(target = look_me_up).start()

def yt_about():
	global url
	url = "https://www.youtube.com/channel/UCzcSdBRZu4XDK5I43KHJEVQ"
	t1 = threading.Thread(target = look_me_up).start()

def tel_about():
	global url
	url = "https://t.me/thomasgrant"
	t1 = threading.Thread(target = look_me_up).start()

def ezy_about():
	global url
	url = "https://my.eazybot.com/134984"
	t1 = threading.Thread(target = look_me_up).start()
	
def bv_join():
	global url
	url = "https://betvoyager.com/equal-odds/?p=E4AO05&lid=17"
	t1 = threading.Thread(target = look_me_up).start()
	
def look_me_up():

	look_me_up_url(url)		   

def look_me_up_url(url):

	webbrowser.open(url)

def aboutwindow(root,title,btn):
	aboutwin = Toplevel(root)
	#Title of the window
	aboutwin.title("About Me!")
	#here I put a .ico file as a picture on the window top bar.
	if os.path.isfile("images\\me.ico"):
		aboutwin.iconbitmap("images\\me.ico")
	aboutwin.resizable(width=False, height=False)
	aboutwin.configure(background='black')
	aboutwin.attributes('-topmost', 'true')
	aboutwin.geometry('285x330+681+0')

	frame = Frame(aboutwin, bg='green',relief=RIDGE, borderwidth=5, bd=5).place(x=6, y=6, 
		width=272, height=320)
	frame1 = Frame(aboutwin, bg='#31859B', relief=RIDGE, borderwidth=5,highlightbackground="black", highlightthickness=2)#frame border
	frame1.place(x=10, y=10, width=264, height=310) #frame using x y w h

	global photo5,photo6,photo7,photo8,photo9,photo10
	photo5 = PhotoImage(file = "images\\profile\\me_profile_100.png")
	photo6 = PhotoImage(file = "images\\profile\\fb_small.png")
	photo7 = PhotoImage(file = "images\\profile\\yt.png")
	photo8 = PhotoImage(file = "images\\profile\\tel.png")
	photo9 = PhotoImage(file = "images\\profile\\eazy-s.png")
	photo10 = PhotoImage(file = "images\\profile\\bv_logo.png")

	meButt = Button(frame1, text = 'Me!',image =photo5 ,command=fb_about)
	meButt.place(x=75, y=1)

	fbButt = Button(frame1, text = 'Me!',image =photo6 ,command=fb_about)
	fbButt.place(x=4, y=236)

	ytButt = Button(frame1, text = 'Me!',image =photo7 ,command=yt_about)
	ytButt.place(x=64, y=236)

	telButt = Button(frame1, text = 'Me!',image =photo8 ,command=tel_about)
	telButt.place(x=124, y=236)

	ezyButt = Button(frame1, text = 'Me!',image =photo9 ,command=ezy_about)
	ezyButt.place(x=182, y=236)
	
	BVButt = Button(frame1, text = 'Me!',image =photo10 ,command=bv_join)
	BVButt.place(x=4, y=156)

	mylab = Label(frame1, 
		# text = 'My name is Thomas Grant\nOnline entrepreneur\nOnline educator\nCrypto enthusiast\nPython intermediate coder', 
		text = 'My name is Thomas Grant\nCrypto enthusiast\nPython intermediate coder', 
		height=3,width=22, bg='green', fg='white', borderwidth = 3, relief="sunken", font=('Verdana', 9, 'bold'))
	mylab.place(x=35, y=108)

	def on_close(btn,aboutwin):
		btn["state"] = "normal"
		aboutwin.destroy()

	aboutwin.protocol("WM_DELETE_WINDOW",  lambda arg=btn,arg2 =aboutwin: on_close(arg,arg2))