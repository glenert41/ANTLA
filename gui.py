import tkinter as tk

root = tk.Tk()
root.title("ANTLA")
frame = tk.Frame(root)


def onclick(args):
    
    if args == "lightBtnOn":
        print("Lights are On")
    if args == "lightBtnOff":
        print("Lights are Off")


#create button elements
lightBtnOn = tk.Button(root, text="Lights On",
                       command=lambda:onclick("lightBtnOn"),
                       fg = "#37d3ff",
                       bg = "#001d26",
                       highlightthickness=4,
                       highlightcolor="#37d3ff",
                       highlightbackground="#37d3ff",
                       borderwidth=4)
lightBtnOff = tk.Button(root, text="Lights Off",command=lambda:onclick("lightBtnOff"))


#Put button elements on main window
lightBtnOn.pack()
lightBtnOff.pack()

root.mainloop()
