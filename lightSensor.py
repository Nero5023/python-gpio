import RPi.GPIO as GPIO
import time
channel = 27

GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel, GPIO.IN)

while True:
    if GPIO.input(channel) == GPIO.LOW:
        print "GPIO 27 Is LOW"
    else:
        print "GPIO 27 is HIGH"
    time.sleep(0.1)