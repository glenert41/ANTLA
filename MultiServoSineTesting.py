import RPi.GPIO as GPIO
import time
import math
import pigpio

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


def cosineMap(pos):
    mappedPos = math.cos(pos)
    #print(mappedPos)
    return mappedPos

def myMapValues(variable,oldLow,oldHigh,newLow,newHigh):
    variable = (variable - oldLow) / (oldHigh - oldLow) * (newHigh - newLow) + newLow
    return variable
    


while True:
    output0 = cosineMap(input0)
    output1 = cosineMap(input1)
    output2 = cosineMap(input2)
    output3 = cosineMap(input3)
    
    
    desiredLow = 0
    desiredHigh = 180
    
    
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
       
    #print("Servo0: " + str(servoOutput0))
    #print("Servo1: " + str(servoOutput1))
    #print("Servo2: " + str(servoOutput2))
    #print("\n")
    '''
    pwm.set_servo_pulsewidth(servo0,500)
    pwm.set_servo_pulsewidth(servo1,500)
    pwm.set_servo_pulsewidth(servo2,500)
    pwm.set_servo_pulsewidth(servo3,500)
    '''
    input0 = input0 - myStep
    input1 = input1 - myStep
    input2 = input2 - myStep
    input3 = input3 - myStep

    iterations += 1
    time.sleep(.05)
    



