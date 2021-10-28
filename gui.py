import tkinter as tk

root = tk.Tk()
root.title("ANTLA")
frame = tk.Frame(root)
relief=tk.FLAT


def onclick(args):
    
    if args == "lightBtnOn":
        print("Lights are On")
    if args == "lightBtnOff":
        print("Lights are Off")


#create button elements
lightBtnOn = tk.Button(root, text="Lights On", relief=tk.FLAT,
                       command=lambda:onclick("lightBtnOn"),
                       fg = "#ffffff",
                       bg = "#37d3ff",
                       activebackground="#3791ff",
                       highlightthickness=0,
                       highlightcolor="#37d3ff",
                       highlightbackground="#37d3ff",
                       borderwidth=2)
lightBtnOff = tk.Button(root, text="Lights Off",command=lambda:onclick("lightBtnOff"))


#Put button elements on main window
lightBtnOn.pack()
lightBtnOff.pack()

root.geometry("400x400")
root.configure(bg="#FFFDD0")
root.mainloop()
