import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


def ereignis(channel):
    print "Taster gedrückt"


tast_pin = 17

GPIO.add_event_detect(tast_pin, GPIO.FALLING, callback = ereignis, bouncetime = 200)

try:
    while True:
        time.sleep(0.5)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
