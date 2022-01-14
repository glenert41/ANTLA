import RPi.GPIO as GPIO
import time
import math

GPIO.setmode(GPIO.BOARD)

myStep = .1



GPIO.setup(12,GPIO.OUT)
servo0 = GPIO.PWM(12,50)
servo0.start(0)

input0 = 0


def cosineMap(pos):
    mappedPos = math.cos(pos)
    return mappedPos

def myMapValues(variable,oldLow,oldHigh,newLow,newHigh):
    variable = (variable - oldLow) / (oldHigh - oldLow) * (newHigh - newLow) + newLow
    return variable
    


while True:
    output0 = cosineMap(input0 + myStep)
    
    
    desiredLow=0
    desiredHigh=180
    output0 = myMapValues(output0, -1,1,desiredLow,desiredHigh)
    #print("Post-Map output: " + str(output0))
    
    
    
    servoWriteOutput0 = 2+(output0/18)
    #print("servoWriteOutput0: " + str(servoWriteOutput0))
    
    
    servo0.ChangeDutyCycle(servoWriteOutput0)
    
    
    
    time.sleep(.05)
    servo0.ChangeDutyCycle(0)
   
   
   
   
    input0 = input0 + myStep
    
    
    
    
    

