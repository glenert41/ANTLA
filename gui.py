import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
#import keyboard

import RPi.GPIO as GPIO
import time
import math
import pigpio

#Servo Set Up
import os
os.system("sudo killall pigpiod")
time.sleep(1)

open_io="sudo pigpiod"
os.system(open_io)
time.sleep(1)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
pwm = pigpio.pi()

iterations = 0
myStep = .1
desiredLow = 0
desiredHigh = 180

servo0 = 18
pwm.set_mode(servo0, pigpio.OUTPUT)
pwm.set_PWM_frequency(servo0,50)
input0 = 0

servo1 = 26
pwm.set_mode(servo1, pigpio.OUTPUT)
pwm.set_PWM_frequency(servo1,50)
input1 = (1*(math.pi))/2

servo2 = 13
pwm.set_mode(servo2,pigpio.OUTPUT)
pwm.set_PWM_frequency(servo2,50)
input2 = math.pi

servo3 = 17
pwm.set_mode(servo3,pigpio.OUTPUT)
pwm.set_PWM_frequency(servo3,50)
input3 = (3*(math.pi))/2



#GUI Setup
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

buttonStyle = {'background':blueLavender,
               'foreground':'white',
               'activebackground':queenBlue,
               'highlightthickness':0,
               'highlightcolor':blueLavender,
               'highlightbackground':blueLavender,
               'borderwidth':2}
lightVar = tk.StringVar()
lightVar.set("No Status Chosen; Lights Off")


def cosineMap(pos):
    mappedPos = math.cos(pos)
    #print(mappedPos)
    return mappedPos

def myMapValues(variable,oldLow,oldHigh,newLow,newHigh):
    variable = (variable - oldLow) / (oldHigh - oldLow) * (newHigh - newLow) + newLow
    return variable


def moveForward():
        global input0
        global input1
        global input2
        global input3
        
        output0 = cosineMap(input0)
        output1 = cosineMap(input1)
        output2 = cosineMap(input2)
        output3 = cosineMap(input3)
        
    
        output0 = myMapValues(output0,-1,1,desiredLow,desiredHigh)
        output1 = myMapValues(output1,-1,1,desiredLow,desiredHigh)
        output2 = myMapValues(output2,-1,1,desiredLow,desiredHigh)
        output3 = myMapValues(output3,-1,1,desiredLow,desiredHigh)
        
        servoOutput0 = myMapValues(output0,desiredLow,desiredHigh,500,2500)
        servoOutput1 = myMapValues(output1,desiredLow,desiredHigh,500,2500)
        servoOutput2 = myMapValues(output2,desiredLow,desiredHigh,500,2500)
        servoOutput3 = myMapValues(output3,desiredLow,desiredHigh,500,2500)

        pwm.set_servo_pulsewidth(servo0,servoOutput0)
        pwm.set_servo_pulsewidth(servo1,servoOutput1)
        pwm.set_servo_pulsewidth(servo2,servoOutput2)
        pwm.set_servo_pulsewidth(servo3,servoOutput3)


        input0 = input0 - myStep
        input1 = input1 - myStep
        input2 = input2 - myStep
        input3 = input3 - myStep
        
        


def onclick(args):
    
    if args == "lightBtnOn":
        print("Lights are On")
        lightVar.set("Lights are On")
       
    if args == "lightBtnOff":
        print("Lights are Off")
        lightVar.set("Lights are Off")
        
    if(args == "moveForward"):
        moveForward()


#create button elements
lightBtnOn = tk.Button(root,buttonStyle, text="Lights On", relief=tk.FLAT,
                       command=lambda:onclick("lightBtnOn")
                       )
lightBtnOff = tk.Button(root,buttonStyle, text="Lights Off",relief=tk.FLAT,
                       command=lambda:onclick("lightBtnOff"))
lightLabel = tk.Label(root,buttonStyle,textvariable=lightVar)

moveForwardButton = tk.Button(root,buttonStyle,text="Move Forward",relief=tk.FLAT,
                        command=lambda:onclick("moveForward"),
                        repeatdelay=50,repeatinterval=50)



#Put elements on main window

#Lights
#lightBtnOn.pack()
#lightBtnOff.pack()
#lightLabel.pack()


lightBtnOn.grid(row = 1, column = 1, sticky=tk.EW)
lightBtnOff.grid(row=2, column = 1, sticky=tk.EW)
lightLabel.grid(row=3, column = 1, sticky=tk.EW)

moveForwardButton.grid(row = 1,column=2,sticky=tk.EW)


root.geometry("800x400")
root.configure(bg=darkPurple)
root.mainloop()

