from random import randint

print("Rate eine Zahl zwischen 1 und 100")
zufallszahl = randint(1,100)
zahl = int(input("Dein Vorschlag: "))

while zahl != zufallszahl:
    if zahl < zufallszahl:
        print("Zu klein")
    else:
        print("Zu groß")
    zahl = int(input("Dein Vorschlag: "))

print("Richtig!")