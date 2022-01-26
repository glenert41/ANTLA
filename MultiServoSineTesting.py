import RPi.GPIO as GPIO
import time
import math
import pigpio

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
pwm = pigpio.pi()

iterations = 0
myStep = .1

servo0 = 18
pwm.set_mode(servo0, pigpio.OUTPUT)
pwm.set_PWM_frequency(servo0,50)
input0 = 0

servo1 = 26
pwm.set_mode(servo1, pigpio.OUTPUT)
pwm.set_PWM_frequency(servo1,50)
input1 = math.pi/2


def cosineMap(pos):
    mappedPos = math.cos(pos)
    return mappedPos

def myMapValues(variable,oldLow,oldHigh,newLow,newHigh):
    variable = (variable - oldLow) / (oldHigh - oldLow) * (newHigh - newLow) + newLow
    return variable
    


while True:
    output0 = cosineMap(input0)
    output1 = cosineMap(input1)
    
    
    desiredLow = 0
    desiredHigh = 180
    
    
    output0 = myMapValues(output0,-1,1,desiredLow,desiredHigh)
    output1 = myMapValues(output1,-1,1,desiredLow,desiredHigh)
    
    servoOutput0 = myMapValues(output0,desiredLow,desiredHigh,500,2500)
    servoOutput1 = myMapValues(output1,desiredLow,desiredHigh,500,2500)
    
    pwm.set_servo_pulsewidth(servo0,servoOutput0)
    pwm.set_servo_pulsewidth(servo1,servoOutput1)
    
    #pwm.set_servo_pulsewidth(servo0,500)
    #pwm.set_servo_pulsewidth(servo1,500)
    

    input0 = input0 + myStep
    input1 = input1 + myStep

    iterations += 1
    time.sleep(.05)
    



