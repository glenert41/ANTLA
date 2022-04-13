import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter import Canvas
#import keyboard

from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

import time
import math
import pigpio


import sys
sys.path
sys.executable
import pyautogui

#Servo Set Up
import os
os.system("sudo killall pigpiod")
time.sleep(1)

open_io="sudo pigpiod"
os.system(open_io)
time.sleep(1)


iterations = 0
myStep = .1

currentDirection = "Direction: Forward"
lightStatus = "Lights: Off"
modeStatus = "Mode: Button"

desiredLow = 0
desiredHigh = 180


input0Left = 0
input1Left = (1*(math.pi))/2
input2Left = math.pi
input3Left = (3*(math.pi))/2

input0Right = 0


#GUI Setup
root = tk.Tk()
root.title("ANTLA")
frame = tk.Frame(root)
relief=tk.FLAT

app = tk.Tk()
app.title("Coordinate Plane")
canvas = Canvas(app)

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

def movePlane(cursorPosition):
    time.sleep(.2)

    scalarL = 1
    scalarR = 1
    
  
        
        
    #scalarL = round((cursorX,0,453,0,3),2)
    
    if cursorPosition[0] < root.winfo_width()/3 and cursorPosition[0] > root.winfo_width()/6:
        scalarL = 2
        scalarR = 1
    elif cursorPosition[0] < root.winfo_width()/3 and cursorPosition[0] < root.winfo_width()/6:
        scalarL = 4
        scalarR = 0
    else:
        scalarL = 1
        scalarR = 1
    #print("scalarL: " + str(scalarL))
    #print("scalarR: " + str(scalarR))
    

    
    
    adjustedCursorY = cursorPosition[1] - root.winfo_height()
    if adjustedCursorY < 100:
        adjustedCursorY = 100
    elif adjustedCursorY > 420:
        adjustedCursorY = 420
        
    if 230 < adjustedCursorY < 290:
        adjustedCursorY = 260
        
    desiredSpeed = round(myMapValues(adjustedCursorY,100,420,-.5,.5),2)
    if(-.1 < desiredSpeed < .1):
        desiredSpeed = 0
    
    
    movePlanar(desiredSpeed,scalarL,scalarR)
    
    
    

def moveLinearSlider():
        global input0Left
        global input1Left
        global input2Left
        global input3Left
        
        global input0Right
        
        output0L = cosineMap(input0Left)
        output1L = cosineMap(input1Left)
        output2L = cosineMap(input2Left)
        output3L = cosineMap(input3Left)
        
        output0R = cosineMap(input0Right)    
        
    
        output0L = myMapValues(output0L,-1,1,desiredLow,desiredHigh)
        output1L = myMapValues(output1L,-1,1,desiredLow,desiredHigh)
        output2L = myMapValues(output2L,-1,1,desiredLow,desiredHigh)
        output3L = myMapValues(output3L,-1,1,desiredLow,desiredHigh)
        
        output0R = myMapValues(output0R,-1,1,desiredLow,desiredHigh)
        
        kit.servo[0].angle=output0L
        kit.servo[1].angle=output1L
        kit.servo[2].angle=output2L
        kit.servo[3].angle=output3L


        input0Left = round(input0Left + (myStep * speedSlider.get()/10),5)
        input1Left = round(input1Left + (myStep * speedSlider.get()/10),5)
        input2Left = round(input2Left + (myStep * speedSlider.get()/10),5)
        input3Left = round(input3Left + (myStep * speedSlider.get()/10),5)
        
        input0Right = round(input0Right + (myStep * speedSlider.get()/10),5)
        
       

        
def movePlanar(speed, scalarL, scalarR):
        global input0Left
        global input1Left
        global input2Left
        global input3Left
        
      
        
        output0 = cosineMap(input0Left)
        output1 = cosineMap(input1Left)
        output2 = cosineMap(input2Left)
        output3 = cosineMap(input3Left)
        
    
        output0 = myMapValues(output0,-1,1,desiredLow,desiredHigh)
        output1 = myMapValues(output1,-1,1,desiredLow,desiredHigh)
        output2 = myMapValues(output2,-1,1,desiredLow,desiredHigh)
        output3 = myMapValues(output3,-1,1,desiredLow,desiredHigh)
        
        servoOutput0 = myMapValues(output0,desiredLow,desiredHigh,500,2500)
        servoOutput1 = myMapValues(output1,desiredLow,desiredHigh,500,2500)
        servoOutput2 = myMapValues(output2,desiredLow,desiredHigh,500,2500)
        servoOutput3 = myMapValues(output3,desiredLow,desiredHigh,500,2500)
        

        
        pwm.set_servo_pulsewidth(servo0L,servoOutput0)
        pwm.set_servo_pulsewidth(servo1L,servoOutput1)
        pwm.set_servo_pulsewidth(servo2L,servoOutput2)
        pwm.set_servo_pulsewidth(servo3L,servoOutput3)
        

        

        input0Left = (input0Left + (scalarL * speed)) 
        input1Left = (input1Left + (scalarL * speed)) 
        input2Left = (input2Left + (scalarL * speed)) 
        input3Left = (input3Left + (scalarL * speed)) 
        
        #print(scalarL * speed)
        
        

        

def onclick(args):
    global lightStatus
    global modeStatus
    
    if args == "lightButton":
        if(lightStatus == "Lights: Off"):
            lightStatus = "Lights: On"
            lightButton['text'] = lightStatus
        elif(lightStatus == "Lights: On"):
            lightStatus = "Lights: Off"
            lightButton['text'] = lightStatus

       
    
        
    if(args == "moveLinearSlider" and modeStatus == "Mode: Button"):
        moveLinearSlider()
    
        
    if(args == "changeDirection"):
        global myStep
        global currentDirection
        if(currentDirection == "Direction: Backward"):
            currentDirection = "Direction: Forward"
            changeDirectionButton['text'] = "Direction: Forward"
            myStep = abs(myStep)
            print(currentDirection)
        elif (currentDirection == "Direction: Forward"):
            currentDirection = "Direction: Backward"
            changeDirectionButton['text'] = "Direction: Backward"
            myStep = -1 * abs(myStep)
            print(currentDirection)
            
    if(args == "switchModeButton"):
        #global modeStatus
        if(modeStatus == "Mode: Button"):
            modeStatus = "Mode: Plane"
            switchModeButton['text'] = modeStatus
            time.sleep(1)
            while 0 not in pyautogui.position():
                #time.sleep(1)
                movePlane(pyautogui.position())
                #print(pyautogui.position())
            print("Exited Planar Control")
        elif(modeStatus == "Mode: Plane"):
            modeStatus = "Mode: Button"
            switchModeButton['text'] = modeStatus
        
        


#create button elements

switchModeButton = tk.Button(root,buttonStyle,text=modeStatus,relief=tk.FLAT,
                       command=lambda:onclick("switchModeButton"),width=25) 

lightButton = tk.Button(root,buttonStyle, text=lightStatus, relief=tk.FLAT,
                       command=lambda:onclick("lightButton"),
                       width=25
                       )


moveLinearButton = tk.Button(root,buttonStyle,text="Move Linear",relief=tk.FLAT,
                        command=lambda:onclick("moveLinearSlider"),
                        repeatdelay=50,repeatinterval=25,width = 25)

changeDirectionButton =tk.Button(root,buttonStyle,
                                 text=currentDirection,
                                 relief=tk.FLAT,
                                 command=lambda:onclick("changeDirection"),
                                 width=25)

speedSlider = tk.Scale(root,from_=10,to=20,orient=tk.HORIZONTAL,
                    length = 250,
                    tickinterval = 2)



switchModeButton.grid(row = 1,column =1, sticky=tk.EW)


lightButton.grid(row = 1, column = 2, sticky=tk.EW)



moveLinearButton.grid(row = 1,column=3,sticky=tk.EW)
changeDirectionButton.grid(row=2,column=3,sticky=tk.EW)

speedSlider.grid(row=3,column=3)

#canvas.create_rectangle(100,100,200,200,fill="green")
canvas.create_rectangle(0,160,500,220,fill="green")
canvas.pack()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
windowHeight = int(4.5*height/10)
halfHeight = int(1*height/2)
zero=0
root.geometry(f'{width}x{windowHeight}+{zero}+{zero}')
root.resizable(False,False)
root.configure(bg=darkPurple)

app.resizable(False,False)
app.geometry(f'1400x{windowHeight}+0+{halfHeight}')


root.mainloop()
app.mainloop()


