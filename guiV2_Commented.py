#ANTLA GUI/Controller

#Imports
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter import Canvas
import time
import math
import pigpio
import sys
import pyautogui
import os

#imports the library for the Servo Header we are physically using; stating that this header has 16 possible servos that can attach 
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

sys.path
sys.executable


#Runs the "sudo killall pigpiod," essentially clearing everything else and prepping for the GUI to open
os.system("sudo killall pigpiod")
time.sleep(1)
open_io="sudo pigpiod"
os.system(open_io)
time.sleep(1)

#Declares the status variables that the User sees on the tiles on the GUI
currentDirection = "Direction: Forward"
lightStatus = "Lights: Off"
modeStatus = "Mode: Button"


#Servo Control Setup
#change in degree between each iteration that the loop runs. Every time the servos run to a position, they will move by their current position + or - myStep
#myStep should start at .1 degrees per iteration
myStep = .1
#How high and low the servos should be able to turn. Generally both should be the same distance from 90. (e.g. 45 and 135)
desiredLow = 0
desiredHigh = 180
#initial inputs for the servo positions. These variables will be mapped by their cosine values. 
#Each variable is pi/2 apart and increasing at myStep per iteration, thus making each servo rotate around the unit circle equally spaced
input0Left = 0
input1Left = (1*(math.pi))/2
input2Left = math.pi
input3Left = (3*(math.pi))/2


#GUI Setup
#open bottom window
root = tk.Tk()
#name the top window "ANTLA"
root.title("ANTLA")
#Organizer
frame = tk.Frame(root)
#Make it 2d appearing; just for aesthetics
relief=tk.FLAT

#Open bottom window
app = tk.Tk()
#Name the bottom window "Coordinate Plane"
app.title("Coordinate Plane")
#Allow for this lower window to use the Canvas feature (allows one to draw)
canvas = Canvas(app)

#Hex Color shortcuts for the GUI
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

#Sets every button on the top window to this desired style; using the shortcut colors from above
buttonStyle = {'background':blueLavender,
               'foreground':'white',
               'activebackground':queenBlue,
               'highlightthickness':0,
               'highlightcolor':blueLavender,
               'highlightbackground':blueLavender,
               'borderwidth':2}

#cosine function; just because math.cos(x) feels clunky compared to cosineMap(x); this function doesn't necessarily need to exist; this is Graham being Graham
def cosineMap(pos):
    mappedPos = math.cos(pos)
    #print(mappedPos)
    return mappedPos

#Takes the input values (which are generally decimals between 0-1 because they are the outputs of the consine function), 
#and maps them to desired values that the servo can turn (generally 0-180 and 45-135)
def myMapValues(variable,oldLow,oldHigh,newLow,newHigh):
    variable = (variable - oldLow) / (oldHigh - oldLow) * (newHigh - newLow) + newLow
    return variable

#code for taking the mouse movements in the bottom window when in planar control, and converting that data to data
#the movePlanar (the function that actually sets power to the servos) function can use
def movePlane(cursorPosition):
    time.sleep(.2)

    #these scalars change the rate at which each side of servos oscillate; thus spinning the robot
    scalarL = 1
    scalarR = 1
   

    #checks the horizontal position of the mouse on the screen, changing the left or right scalar accordingly, thus allowing for turning
    if cursorPosition[0] < root.winfo_width()/3 and cursorPosition[0] > root.winfo_width()/6:
        scalarL = 2
        scalarR = 1
    elif cursorPosition[0] < root.winfo_width()/3 and cursorPosition[0] < root.winfo_width()/6:
        scalarL = 4
        scalarR = 0
    else:
        scalarL = 1
        scalarR = 1

   
    
    #Checks the vertial position of the mouse, thus changing the forward/backward linear speed of ANTLA
    adjustedCursorY = cursorPosition[1] - root.winfo_height()
    if adjustedCursorY < 100:
        adjustedCursorY = 100
    elif adjustedCursorY > 420:
        adjustedCursorY = 420
        
    #if the y value of the mouse is close enough to the center of the window, set the y value of the mouse to the center
    if 230 < adjustedCursorY < 290:
        adjustedCursorY = 260
    
    #set the desired speed
    desiredSpeed = round(myMapValues(adjustedCursorY,100,420,-.5,.5),2)
    #if the desiredSpeed is close enough to 0, then set it to 0
    if(-.1 < desiredSpeed < .1):
        desiredSpeed = 0
    
    #sends the desired speed for the servos, and both scalars, to the function to move the servos
    movePlanar(desiredSpeed,scalarL,scalarR)
    
    
    
#function for driving ANTLA back and forth linearly with buttons on the top window
def moveLinearSlider():
        #grab the inputs, so they can be changed below, and updated for planar control
        global input0Left
        global input1Left
        global input2Left
        global input3Left
        

        #take the cosine of the inputs
        output0L = cosineMap(input0Left)
        output1L = cosineMap(input1Left)
        output2L = cosineMap(input2Left)
        output3L = cosineMap(input3Left)
        
 
        
        #scale these cosine values from -1-1 to desiredLow-desiredHigh for the servos (generally 0-180)
        output0L = myMapValues(output0L,-1,1,desiredLow,desiredHigh)
        output1L = myMapValues(output1L,-1,1,desiredLow,desiredHigh)
        output2L = myMapValues(output2L,-1,1,desiredLow,desiredHigh)
        output3L = myMapValues(output3L,-1,1,desiredLow,desiredHigh)
        
 
        
        #set the left side servos to their positions
        kit.servo[0].angle=output0L
        kit.servo[1].angle=output1L
        kit.servo[2].angle=output2L
        kit.servo[3].angle=output3L
        
        kit.servo[4].angle=output0L
        kit.servo[5].angle=output1L
        kit.servo[6].angle=output2L
        kit.servo[7].angle=output3L
        
        #set the right side servos to their positions (which are 180 minus the left side)(as to mirror across ANTLA's vertical line of symmetry)
        kit.servo[8].angle= 180 - output0L
        kit.servo[9].angle=180 - output1L
        kit.servo[10].angle=180 - output2L
        kit.servo[11].angle=180 - output3L
        
        kit.servo[12].angle=180 - output0L
        kit.servo[13].angle=180 - output1L
        kit.servo[14].angle=180 - output2L
        kit.servo[15].angle=180 - output3L

        #take the input from this iteration, and change it according to the product of the desired step size and the speed slider
        #this allows for the next iteration's position to be close to the previous, thus making a smooth motion
        input0Left = round(input0Left + (myStep * speedSlider.get()/10),5)
        input1Left = round(input1Left + (myStep * speedSlider.get()/10),5)
        input2Left = round(input2Left + (myStep * speedSlider.get()/10),5)
        input3Left = round(input3Left + (myStep * speedSlider.get()/10),5)
        
           

#actually move the servos when in planar control
def movePlanar(speed, scalarL, scalarR):
        #grab the inputs so they can be used later, and updated for LinearSlider
        global input0Left
        global input1Left
        global input2Left
        global input3Left
        
      
        #take the cosine of the inputs
        output0L = cosineMap(input0Left)
        output1L = cosineMap(input1Left)
        output2L = cosineMap(input2Left)
        output3L = cosineMap(input3Left)
        
        #scale these cosine values from -1-1 to desiredLow-desiredHigh for the servos (generally 0-180)
        output0L = myMapValues(output0L,-1,1,desiredLow,desiredHigh)
        output1L = myMapValues(output1L,-1,1,desiredLow,desiredHigh)
        output2L = myMapValues(output2L,-1,1,desiredLow,desiredHigh)
        output3L = myMapValues(output3L,-1,1,desiredLow,desiredHigh)
        
    
    
        #set the left side servos to their positions
        kit.servo[0].angle=output0L
        kit.servo[1].angle=output1L
        kit.servo[2].angle=output2L
        kit.servo[3].angle=output3L
        
        kit.servo[4].angle=output0L
        kit.servo[5].angle=output1L
        kit.servo[6].angle=output2L
        kit.servo[7].angle=output3L
        
        #Right side in Progress
        

        #update the inputs for the next iteration by adding the product of the scalar and speed to the current input
        input0Left = (input0Left + (scalarL * speed)) 
        input1Left = (input1Left + (scalarL * speed)) 
        input2Left = (input2Left + (scalarL * speed)) 
        input3Left = (input3Left + (scalarL * speed)) 
        
     
        
        

        

def onclick(args):
    #global variables to be used to switch between states and modes
    global lightStatus
    global modeStatus
    
    #light button switch (used to test switch toggle currently, will be hooked up to a light switch)
    if args == "lightButton":
        if(lightStatus == "Lights: Off"):
            lightStatus = "Lights: On"
            lightButton['text'] = lightStatus
        elif(lightStatus == "Lights: On"):
            lightStatus = "Lights: Off"
            lightButton['text'] = lightStatus

       
    
    #This runs when the "moveLinearSlider" button is pressed; this calls the moveLinearSlider() function to begin moving the servos. 
    if(args == "moveLinearSlider" and modeStatus == "Mode: Button"):
        moveLinearSlider()
    
    #this is what runs when the changeDirection button is pressed; this changes the direction
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
            
    #this is what runs when the "switchModeButton" is pressed; this is what changes between linearSlider and Planar Control
    if(args == "switchModeButton"):
        #global modeStatus
        if(modeStatus == "Mode: Button"):
            modeStatus = "Mode: Plane"
            switchModeButton['text'] = modeStatus
            time.sleep(1)
            #while the cursor is on the screen, keep running; if the cursor leaves the screen during planar control,
            #then stop ANTLA and hang out until button control is called for
            while 0 not in pyautogui.position():
                #time.sleep(1)
                movePlane(pyautogui.position())
                #print(pyautogui.position())
            print("Exited Planar Control")
        elif(modeStatus == "Mode: Plane"):
            modeStatus = "Mode: Button"
            switchModeButton['text'] = modeStatus
        
        


#create button elements

#Button to toggle between Planar and LinearSlider operation modes
switchModeButton = tk.Button(root,buttonStyle,text=modeStatus,relief=tk.FLAT,
                       command=lambda:onclick("switchModeButton"),width=25) 

#button to turn on and off LED lights; used for testing buttons as well
lightButton = tk.Button(root,buttonStyle, text=lightStatus, relief=tk.FLAT,
                       command=lambda:onclick("lightButton"),
                       width=25
                       )

#Button to  move robot when in LinearSlider operation mode
moveLinearButton = tk.Button(root,buttonStyle,text="Move Linear",relief=tk.FLAT,
                        command=lambda:onclick("moveLinearSlider"),
                        repeatdelay=50,repeatinterval=25,width = 25)

#Button to switch the robots direction when in LinearSlider operation mode
changeDirectionButton =tk.Button(root,buttonStyle,
                                 text=currentDirection,
                                 relief=tk.FLAT,
                                 command=lambda:onclick("changeDirection"),
                                 width=25)
#Slider that changes the robots speed when in LinearSlider operation mode
speedSlider = tk.Scale(root,from_=10,to=20,orient=tk.HORIZONTAL,
                    length = 250,
                    tickinterval = 2)


#Button placement and Aesthetics
switchModeButton.grid(row = 1,column =1, sticky=tk.EW)
lightButton.grid(row = 1, column = 2, sticky=tk.EW)
moveLinearButton.grid(row = 1,column=3,sticky=tk.EW)
changeDirectionButton.grid(row=2,column=3,sticky=tk.EW)
speedSlider.grid(row=3,column=3)


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

