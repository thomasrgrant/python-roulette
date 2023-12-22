# Libraries
from tkinter import *
import os

import threading

from PIL import ImageTk,Image #install library

global showcap

def showscaptureimages_widow_bv_game(root,title,btn):

    showcap = Toplevel(root)

    showcap.title(title)
    #here I put a .ico file as a picture on the window top bar.
    if os.path.isfile("images\\wheel2.ico"):
        showcap.iconbitmap("images\\wheel2.ico")

    showcap.resizable(width=False, height=False)
    showcap.configure(background='black')
    showcap.attributes('-topmost', 'true')
    showcap.geometry('834x254') # '834x454+681+0'

    #Here I see if the file exists.
    if os.path.isfile("data\\showcap.conf"):
        #Here I read the X and Y positon of the window from when I last closed it.
        with open("data\\showcap.conf", "r") as conf: 
            showcap.geometry(conf.read())
    else:
        #Default window position.
        showcap.geometry('834x254') # '834x454+645+80'

    def on_close(btn,showcap):
        btn["state"] = "normal"

        with open("data\\showcap.conf", "w") as conf:
            conf.write(showcap.geometry())

        showcap.destroy()

    showcap.protocol("WM_DELETE_WINDOW",  lambda arg=btn,arg2 =showcap: on_close(arg,arg2))

    def btnClickFunction(): #defualt command (just prints 'clicked in the output') use this def for testing.
        print('clicked')

    def locate_image():
        t1 = threading.Thread(target = locate_image_on_numbers_table).start()

    # display window
    #Here I display the show capture window.
    def displaywindow():
        global xpos,ypos,my_box,entry

        # showcap frames
        frameshowcap = Frame(showcap, bg='green', relief=RIDGE, bd=5).place(x=6, y=6, width=822, height=246)
        
        frame1showcap = Frame(showcap, bg='#31859B', highlightbackground="black", highlightthickness=2)#frame border
        frame1showcap.place(x=10, y=10, width=814, height=238) #frame using x y w h
        # showcap frames

        # showcap labels
        my_label = Label(showcap,text="Roulette numbers used in BetVoyager are displayed here.", height=1,width=73, bg='black', fg='white', font=('Verdana', 12, 'bold'))
        my_label.place(x=12, y=12)        
        # showcap Entry
    # display window

    # frame2showcap image area
    #The frame2showcap is used to hide(destroy) and then show images again (Updates the window).
    def showcapimagesframe():
        global frame2showcap
        frame2showcap = Frame(showcap, bg='#31859B', highlightbackground="black", highlightthickness=2)#frame for numbers use picture of labels
        frame2showcap.place(x=16, y=40, width=802, height=202) #frame using x y w h
    # frame2showcap image area

    # numbers Images
    def numberarea_numbers():
        # variables
        global img0,img1,img2,img3,img4,img5,img6,img7,img8,img9,img10,img11,img12
        global img13,img14,img15,img16,img17,img18,img19,img20,img21,img22,img23,img24
        global img25,img26,img27,img28,img29,img30,img31,img32,img33,img34,img35,img36
        # variables

        # numbers.png
        if os.path.isfile("images\\numbers\\0.png"):
            img0 = Image.open("images\\numbers\\0.png")
            img0 = img0.resize((60, 60), Image.ANTIALIAS)            
            img0 = ImageTk.PhotoImage(img0)
            sclab00 = Label(frame2showcap, image=img0,height=60,width=60).grid(row=3,column=0, padx=1, pady=1)

        if os.path.isfile("images\\numbers\\1.png"):
            img1 = Image.open("images\\numbers\\1.png")
            img1 = img1.resize((60, 60), Image.ANTIALIAS)            
            img1 = ImageTk.PhotoImage(img1)
            sclab01 = Label(frame2showcap, image=img1,height=60,width=60).grid(row=2,column=0, padx=1, pady=1)

        if os.path.isfile("images\\numbers\\2.png"):
            img2 = Image.open("images\\numbers\\2.png")
            img2 = img2.resize((60, 60), Image.ANTIALIAS)            
            img2 = ImageTk.PhotoImage(img2)
            sclab02 = Label(frame2showcap, image=img2,height=60,width=60).grid(row=1,column=0, padx=1, pady=1)

        if os.path.isfile("images\\numbers\\3.png"):
            img3 = Image.open("images\\numbers\\3.png")
            img3 = img3.resize((60, 60), Image.ANTIALIAS)            
            img3 = ImageTk.PhotoImage(img3)
            sclab03 = Label(frame2showcap, image=img3,height=60,width=60).grid(row=0,column=0, padx=1, pady=1)

        if os.path.isfile("images\\numbers\\4.png"):
            img4 = Image.open("images\\numbers\\4.png")
            img4 = img4.resize((60, 60), Image.ANTIALIAS)            
            img4 = ImageTk.PhotoImage(img4)
            sclab04 = Label(frame2showcap, image=img4,height=60,width=60).grid(row=2,column=1, padx=1, pady=1)

        if os.path.isfile("images\\numbers\\5.png"):
            img5 = Image.open("images\\numbers\\5.png")
            img5 = img5.resize((60, 60), Image.ANTIALIAS)            
            img5 = ImageTk.PhotoImage(img5)
            sclab05 = Label(frame2showcap, image=img5,height=60,width=60).grid(row=1,column=1, padx=1, pady=1)

        if os.path.isfile("images\\numbers\\6.png"):
            img6 = Image.open("images\\numbers\\6.png")
            img6 = img6.resize((60, 60), Image.ANTIALIAS)            
            img6 = ImageTk.PhotoImage(img6)
            sclab06 = Label(frame2showcap, image=img6,height=60,width=60).grid(row=0,column=1, padx=1, pady=1)

        if os.path.isfile("images\\numbers\\7.png"):
            img7 = Image.open("images\\numbers\\7.png")
            img7 = img7.resize((60, 60), Image.ANTIALIAS)            
            img7 = ImageTk.PhotoImage(img7)
            sclab07 = Label(frame2showcap, image=img7,height=60,width=60).grid(row=2,column=2, padx=1, pady=1)

        if os.path.isfile("images\\numbers\\8.png"):
            img8 = Image.open("images\\numbers\\8.png")
            img8 = img8.resize((60, 60), Image.ANTIALIAS)            
            img8 = ImageTk.PhotoImage(img8)
            sclab08 = Label(frame2showcap, image=img8,height=60,width=60).grid(row=1,column=2, padx=1, pady=1)

        if os.path.isfile("images\\numbers\\9.png"):
            img9 = Image.open("images\\numbers\\9.png")
            img9 = img9.resize((60, 60), Image.ANTIALIAS)            
            img9 = ImageTk.PhotoImage(img9)
            sclab09 = Label(frame2showcap, image=img9,height=60,width=60).grid(row=0,column=2, padx=1, pady=1)

        if os.path.isfile("images\\numbers\\10.png"):
            img10 = Image.open("images\\numbers\\10.png")
            img10 = img10.resize((60, 60), Image.ANTIALIAS)            
            img10 = ImageTk.PhotoImage(img10)
            sclab10 = Label(frame2showcap, image=img10,height=60,width=60).grid(row=2,column=3, padx=1, pady=1)

        if os.path.isfile("images\\numbers\\11.png"):
            img11 = Image.open("images\\numbers\\11.png")
            img11 = img11.resize((60, 60), Image.ANTIALIAS)            
            img11 = ImageTk.PhotoImage(img11)
            sclab11 = Label(frame2showcap, image=img11,height=60,width=60).grid(row=1,column=3, padx=1, pady=1)

        if os.path.isfile("images\\numbers\\12.png"):
            img12 = Image.open("images\\numbers\\12.png")
            img12 = img12.resize((60, 60), Image.ANTIALIAS)            
            img12 = ImageTk.PhotoImage(img12)
            sclab12 = Label(frame2showcap, image=img12,height=60,width=60).grid(row=0,column=3, padx=1, pady=1)

        if os.path.isfile("images\\numbers\\13.png"):
            img13 = Image.open("images\\numbers\\13.png")
            img13 = img13.resize((60, 60), Image.ANTIALIAS)            
            img13 = ImageTk.PhotoImage(img13)
            sclab13 = Label(frame2showcap, image=img13,height=60,width=60).grid(row=2,column=4, padx=1, pady=1)

        if os.path.isfile("images\\numbers\\14.png"):        
            img14 = Image.open("images\\numbers\\14.png")
            img14 = img14.resize((60, 60), Image.ANTIALIAS)            
            img14 = ImageTk.PhotoImage(img14)
            sclab14 = Label(frame2showcap, image=img14,height=60,width=60).grid(row=1,column=4, padx=1, pady=1)

        if os.path.isfile("images\\numbers\\15.png"):
            img15 = Image.open("images\\numbers\\15.png")
            img15 = img15.resize((60, 60), Image.ANTIALIAS)            
            img15 = ImageTk.PhotoImage(img15)       
            sclab15 = Label(frame2showcap, image=img15,height=60,width=60).grid(row=0,column=4, padx=1, pady=1)

        if os.path.isfile("images\\numbers\\16.png"):
            img16 = Image.open("images\\numbers\\16.png")
            img16 = img16.resize((60, 60), Image.ANTIALIAS)            
            img16 = ImageTk.PhotoImage(img16)
            sclab16 = Label(frame2showcap, image=img16,height=60,width=60).grid(row=2,column=5, padx=1, pady=1)

        if os.path.isfile("images\\numbers\\17.png"):    
            img17 = Image.open("images\\numbers\\17.png")
            img17 = img17.resize((60, 60), Image.ANTIALIAS)            
            img17 = ImageTk.PhotoImage(img17)
            sclab17 = Label(frame2showcap, image=img17,height=60,width=60).grid(row=1,column=5, padx=1, pady=1)

        if os.path.isfile("images\\numbers\\18.png"):    
            img18 = Image.open("images\\numbers\\18.png")
            img18 = img18.resize((60, 60), Image.ANTIALIAS)            
            img18 = ImageTk.PhotoImage(img18)        
            sclab18 = Label(frame2showcap, image=img18,height=60,width=60).grid(row=0,column=5, padx=1, pady=1)

        if os.path.isfile("images\\numbers\\19.png"):
            img19 = Image.open("images\\numbers\\19.png")
            img19 = img19.resize((60, 60), Image.ANTIALIAS)            
            img19 = ImageTk.PhotoImage(img19)
            sclab19 = Label(frame2showcap, image=img19,height=60,width=60).grid(row=2,column=6, padx=1, pady=1)

        if os.path.isfile("images\\numbers\\20.png"):    
            img20 = Image.open("images\\numbers\\20.png")
            img20 = img20.resize((60, 60), Image.ANTIALIAS)            
            img20 = ImageTk.PhotoImage(img20)
            sclab20 = Label(frame2showcap, image=img20,height=60,width=60).grid(row=1,column=6, padx=1, pady=1)

        if os.path.isfile("images\\numbers\\21.png"):
            img21 = Image.open("images\\numbers\\21.png")
            img21 = img21.resize((60, 60), Image.ANTIALIAS)            
            img21 = ImageTk.PhotoImage(img21)
            sclab21 = Label(frame2showcap, image=img21,height=60,width=60).grid(row=0,column=6, padx=1, pady=1)        

        if os.path.isfile("images\\numbers\\22.png"):
            img22 = Image.open("images\\numbers\\22.png")
            img22 = img22.resize((60, 60), Image.ANTIALIAS)            
            img22 = ImageTk.PhotoImage(img22)
            sclab22 = Label(frame2showcap, image=img22,height=60,width=60).grid(row=2,column=7, padx=1, pady=1)

        if os.path.isfile("images\\numbers\\23.png"):
            img23 = Image.open("images\\numbers\\23.png")
            img23 = img23.resize((60, 60), Image.ANTIALIAS)            
            img23 = ImageTk.PhotoImage(img23)
            sclab23 = Label(frame2showcap, image=img23,height=60,width=60).grid(row=1,column=7, padx=1, pady=1)

        if os.path.isfile("images\\numbers\\24.png"):
            img24 = Image.open("images\\numbers\\24.png")
            img24 = img24.resize((60, 60), Image.ANTIALIAS)            
            img24 = ImageTk.PhotoImage(img24)
            sclab24 = Label(frame2showcap, image=img24,height=60,width=60).grid(row=0,column=7, padx=1, pady=1)

        if os.path.isfile("images\\numbers\\25.png"):
            img25 = Image.open("images\\numbers\\25.png")
            img25 = img25.resize((60, 60), Image.ANTIALIAS)            
            img25 = ImageTk.PhotoImage(img25)
            sclab25 = Label(frame2showcap, image=img25,height=60,width=60).grid(row=2,column=8, padx=1, pady=1)

        if os.path.isfile("images\\numbers\\26.png"):
            img26 = Image.open("images\\numbers\\26.png")
            img26 = img26.resize((60, 60), Image.ANTIALIAS)            
            img26 = ImageTk.PhotoImage(img26)
            sclab26 = Label(frame2showcap, image=img26,height=60,width=60).grid(row=1,column=8, padx=1, pady=1)

        if os.path.isfile("images\\numbers\\27.png"):
            img27 = Image.open("images\\numbers\\27.png")
            img27 = img27.resize((60, 60), Image.ANTIALIAS)            
            img27 = ImageTk.PhotoImage(img27)
            sclab27 = Label(frame2showcap, image=img27,height=60,width=60).grid(row=0,column=8, padx=1, pady=1)

        if os.path.isfile("images\\numbers\\28.png"):
            img28 = Image.open("images\\numbers\\28.png")
            img28 = img28.resize((60, 60), Image.ANTIALIAS)            
            img28 = ImageTk.PhotoImage(img28)
            sclab28 = Label(frame2showcap, image=img28,height=60,width=60).grid(row=2,column=9, padx=1, pady=1)

        if os.path.isfile("images\\numbers\\29.png"):
            img29 = Image.open("images\\numbers\\29.png")
            img29 = img29.resize((60, 60), Image.ANTIALIAS)            
            img29 = ImageTk.PhotoImage(img29)
            sclab29 = Label(frame2showcap, image=img29,height=60,width=60).grid(row=1,column=9, padx=1, pady=1)

        if os.path.isfile("images\\numbers\\30.png"):
            img30 = Image.open("images\\numbers\\30.png")
            img30 = img30.resize((60, 60), Image.ANTIALIAS)            
            img30 = ImageTk.PhotoImage(img30)
            sclab30 = Label(frame2showcap, image=img30,height=60,width=60).grid(row=0,column=9, padx=1, pady=1)

        if os.path.isfile("images\\numbers\\31.png"):
            img31 = Image.open("images\\numbers\\31.png")
            img31 = img31.resize((60, 60), Image.ANTIALIAS)            
            img31 = ImageTk.PhotoImage(img31)
            sclab31 = Label(frame2showcap, image=img31,height=60,width=60).grid(row=2,column=10, padx=1, pady=1)

        if os.path.isfile("images\\numbers\\32.png"):
            img32 = Image.open("images\\numbers\\32.png")
            img32 = img32.resize((60, 60), Image.ANTIALIAS)            
            img32 = ImageTk.PhotoImage(img32)
            sclab32 = Label(frame2showcap, image=img32,height=60,width=60).grid(row=1,column=10, padx=1, pady=1)

        if os.path.isfile("images\\numbers\\33.png"):
            img33 = Image.open("images\\numbers\\33.png")
            img33 = img33.resize((60, 60), Image.ANTIALIAS)            
            img33 = ImageTk.PhotoImage(img33)
            sclab32 = Label(frame2showcap, image=img33,height=60,width=60).grid(row=0,column=10, padx=1, pady=1)

        if os.path.isfile("images\\numbers\\34.png"):
            img34 = Image.open("images\\numbers\\34.png")
            img34 = img34.resize((60, 60), Image.ANTIALIAS)            
            img34 = ImageTk.PhotoImage(img34)
            sclab34 = Label(frame2showcap, image=img34,height=60,width=60).grid(row=2,column=11, padx=1, pady=1)

        if os.path.isfile("images\\numbers\\35.png"):
            img35 = Image.open("images\\numbers\\35.png")
            img35 = img35.resize((60, 60), Image.ANTIALIAS)            
            img35 = ImageTk.PhotoImage(img35)
            sclab34 = Label(frame2showcap, image=img35,height=60,width=60).grid(row=1,column=11, padx=1, pady=1)

        if os.path.isfile("images\\numbers\\36.png"):
            img36 = Image.open("images\\numbers\\36.png")
            img36 = img36.resize((60, 60), Image.ANTIALIAS)            
            img36 = ImageTk.PhotoImage(img36)
            sclab36 = Label(frame2showcap, image=img36,height=60,width=60).grid(row=0,column=11, padx=1, pady=1)
        # numbers.png
    # numbers Images

    displaywindow()
    showcapimagesframe()
    numberarea_numbers()