import time
import RPi.GPIO as GPIO

tast_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(tast_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
try:
    while True:
        time.sleep(0.5)
        if GPIO.input(tast_pin) == GPIO.HIGH:
            print "Taster (nicht) gedrückt"
        else:
            print "Taster (nicht) gedrückt"
    
except KeyboardInterrupt:
    pass

GPIO.cleanup()

