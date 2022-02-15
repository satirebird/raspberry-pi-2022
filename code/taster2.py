import time
import RPi.GPIO as GPIO

tast_pin = 17

GPIO.setmode(GPIO.BOARD)
GPIO.setup(tast_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def ereignis(channel):
    print("Taster gedrückt")

GPIO.add_event_detect(tast_pin, GPIO.FALLING, callback = ereignis, bouncetime = 200)

try:
    while True:
        time.sleep(0.5)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
