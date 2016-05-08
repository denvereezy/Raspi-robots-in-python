import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.OUT)


while True:
        GPIO.output(5,3)
        GPIO.output(5,0)
GPIO.cleanup()
