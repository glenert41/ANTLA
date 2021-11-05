import tkinter as tk
import keyboard

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
lightBtnOff = tk.Button(root, text="Lights Off", relief=tk.FLAT,
                       command=lambda:onclick("lightBtnOff"),
                       fg = white,
                       bg = blueLavender, #button color 
                       activebackground=queenBlue,
                       highlightthickness=0,
                       highlightcolor= blueLavender,
                       highlightbackground= blueLavender,
                       borderwidth=2)

keyboard.on_press_key("w", lambda _:print("w_pressed"))
    


def onclick(args):
    
    if args == "lightBtnOn":
        print("Lights are On")
    if args == "lightBtnOff":
        print("Lights are Off")



#Put button elements on main window
lightBtnOn.pack()
lightBtnOff.pack()

root.geometry("400x400")
root.configure(bg=darkPurple)
root.mainloop()
