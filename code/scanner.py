

def setze_position(winkel):
    print("Neuer Winkel: ", winkel)

def messe_abstand():
    return 0.0

def ermittle_winkel():
    return -1

def programm():
    winkel = ermittle_winkel()
    if winkel >= 0:
        print("Kleinster Abstand gefunden bei:", winkel)
        setze_position(winkel)        
    else:
        print("Nichts gefunden")

programm()