import RPi.GPIO as GPIO
import time
import math
import pigpio

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

myStep = .1

servo0 = 18

pwm = pigpio.pi()
pwm.set_mode(servo0, pigpio.OUTPUT)
pwm.set_PWM_frequency(servo0,50)

input0 = 0


def cosineMap(pos):
    mappedPos = math.cos(pos)
    return mappedPos

def myMapValues(variable,oldLow,oldHigh,newLow,newHigh):
    variable = (variable - oldLow) / (oldHigh - oldLow) * (newHigh - newLow) + newLow
    return variable
    


while True:
    output0 = cosineMap(input0 + myStep)
    
    
    #desiredLow=500
    #desiredHigh=2500
    #output0 = myMapValues(output0, -1,1,desiredLow,desiredHigh)
    
    desiredLow = 45
    desiredHigh = 135
    
    #converts from -1 and 1 to degrees (not necessary)
    output0 = myMapValues(output0,-1,1,desiredLow,desiredHigh)
    #converts from degrees to writable servo values
    servoOutput0 = myMapValues(output0,desiredLow,desiredHigh,500,2500)
    
    pwm.set_servo_pulsewidth(servo0,servoOutput0)
    
    
    input0 = input0 + myStep

    time.sleep(.05)
    


