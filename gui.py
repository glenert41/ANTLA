import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
#import keyboard

root = tk.Tk()
root.title("ANTLA")
frame = tk.Frame(root)
relief=tk.FLAT

#331338 is Dark Purple
darkPurple = "#331338"
#88869c is blueLavender
blueLavender = "#88869C"
#D4b483 is Burlywood
burlywood = "#D4B483"
#59C9A5 is Ocean Green
oceanGreen = "#59C9A5"
#4D7298 is Queen Blue
queenBlue = "#4D7298"
#ffffff is white
white = "#ffffff"

'''fg = white, #text color
                       bg = blueLavender, #button color 
                       activebackground=queenBlue,
                       highlightthickness=0,
                       highlightcolor= blueLavender,
                       highlightbackground= blueLavender,
                       borderwidth=2'''

buttonStyle = {'background':blueLavender,
               'foreground':'white',
               'activebackground':queenBlue,
               'highlightthickness':0,
               'highlightcolor':blueLavender,
               'highlightbackground':blueLavender,
               'borderwidth':2}




lightVar = tk.StringVar()
lightVar.set("No Status Chosen; Lights Off")


def onclick(args):
    
    if args == "lightBtnOn":
        print("Lights are On")
        lightVar.set("Status: Lights are On")
       
    if args == "lightBtnOff":
        print("Lights are Off")
        lightVar.set("Status: Lights are Off")


#create button elements
lightBtnOn = tk.Button(root,buttonStyle, text="Lights On", relief=tk.FLAT,
                       command=lambda:onclick("lightBtnOn")
                       )
lightBtnOff = tk.Button(root,buttonStyle, text="Lights Off",relief=tk.FLAT,
                       command=lambda:onclick("lightBtnOff"))
lightLabel = tk.Label(root,buttonStyle,textvariable=lightVar)



#Put elements on main window

#Lights
#lightBtnOn.pack()
#lightBtnOff.pack()
#lightLabel.pack()


lightBtnOn.grid(row = 1, column = 1, sticky=tk.EW)
lightBtnOff.grid(row=2, column = 1, sticky=tk.EW)
lightLabel.grid(row=3, column = 1, sticky=tk.EW)


root.geometry("400x400")
root.configure(bg=darkPurple)
root.mainloop()

