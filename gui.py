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

buttonStyle = Style()
buttonStyle.configure("buttonStyle", foreground = "red")





lightVar = tk.StringVar()
lightVar.set("No Status Chosen; Lights off")


def onclick(args):
    
    if args == "lightBtnOn":
        print("Lights are On")
        lightVar.set("Status: Lights are On")
       
    if args == "lightBtnOff":
        print("Lights are Off")
        lightVar.set("Status: Lights are Off")


#create button elements
lightBtnOn = tk.Button(root, text="Lights On", relief=tk.FLAT,
                       command=lambda:onclick("lightBtnOn"),
                       fg = white, #text color
                       bg = blueLavender, #button color 
                       activebackground=queenBlue,
                       highlightthickness=0,
                       highlightcolor= blueLavender,
                       highlightbackground= blueLavender,
                       borderwidth=2)
lightBtnOff = ttk.Button(root, text="Lights Off", style="buttonStyle",
                       command=lambda:onclick("lightBtnOff")
                       )
lightLabel = tk.Label(root,textvariable=lightVar,
                      fg=white,
                      bg = blueLavender)

'''
if keyboard.on_press_key("w"):
    print("W is pressed")
    
if keyboard.on_press_key("s"):
    print("S is pressed")
'''



#Put elements on main window
lightBtnOn.pack()
lightBtnOff.pack()
lightLabel.pack()



root.geometry("400x400")
root.configure(bg=darkPurple)
root.mainloop()

