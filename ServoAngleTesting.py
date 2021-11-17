import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12,GPIO.OUT)
servo1 = GPIO.PWM(12,50)

servo1.start(0)



try:
    while True:
        angle = float(input("Desired Angle: "))
        servo1.ChangeDutyCycle(2+(angle/18))
        time.sleep(.5)
        servo1.ChangeDutyCycle(0)
finally:
    servo1.stop()
    GPIO.cleanup()
    print("done")