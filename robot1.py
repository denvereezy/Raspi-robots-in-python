import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.OUT)   #Left motor input 1
GPIO.setup(7,GPIO.OUT)   #Left motor input 2
GPIO.setup(11,GPIO.OUT)  #Right motor input 1
GPIO.setup(13,GPIO.OUT)  #Right motor input 2
GPIO.setwarnings(False)

while True:
        GPIO.output(5,1)
        GPIO.output(7,0)
        GPIO.output(11,1)
        GPIO.output(13,0)
        time.sleep(1)     

        GPIO.output(5,0)
        GPIO.output(7,1)
        GPIO.output(11,0)
        GPIO.output(13,1)
        time.sleep(1)     
