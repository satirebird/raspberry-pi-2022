import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
 
GPIO_TRIGGER = 17
GPIO_ECHO = 24
 
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


pwm_gpio = 18
frequence = 50
GPIO.setup(pwm_gpio, GPIO.OUT)
pwm = GPIO.PWM(pwm_gpio, frequence)

def ermittle_winkel():
    b = range(1, 181, 10)
    e = 15
    f = 16
    for c in b:
        setze_position(c)
        a = messe_abstand()
        if e > a:
            e = a
            f = c
    return f

def setze_position(winkel):
    print("Winkel:",winkel)
    pwm.start(angle_to_percent(winkel))
    time.sleep(0.5)

def angle_to_percent(angle):
    
    if angle > 180 or angle < 0 :
        return False

    start = 4
    end = 12.5
    ratio = (end - start)/180 

    angle_as_percent = angle * ratio
    
    return start + angle_as_percent


def messe_abstand():
    GPIO.output(GPIO_TRIGGER, True)
 
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartZeit = time.time()
    StopZeit = time.time()
 
    while GPIO.input(GPIO_ECHO) == 0:
        StartZeit = time.time()

    while GPIO.input(GPIO_ECHO) == 1:
        StopZeit = time.time()

    TimeElapsed = StopZeit - StartZeit
    distanz = (TimeElapsed * 34300) / 2
    print("Distanz:",distanz)
 
    return distanz

def programm():
    g = ermittle_winkel()
    if g >= 0:
        print("Kleinster Abstand gefunden bei:", g)
        setze_position(g)
    else:
        print("Nichts gefunden")

programm()
"""
winkel = a | b = range | c = set | d = abstand | e,f,g = hilfs variablen
"""
