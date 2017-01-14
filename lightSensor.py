import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)


while True:
    if GPIO.input(27) == GPIO.LOW:
        print "GPIO 27 Is LOW"
    else:
        print "GPIO 27 is HIGH"
    time.sleep(0.1)