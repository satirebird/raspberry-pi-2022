import sys
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("", 51000))
sock.listen(1)

while True:
    print("Warte auf deinen Spieler ")
    spieler, addr = sock.accept()
    print("Spieler hat sich verbunden. Seine Adresse ist ", addr)
    try:
        while True:
            print("Warte auf Frage...")
            frage = spieler.recv(256)
            if frage:
                print("Emfangen: " + frage.decode())
                antwort = input("Tippe die Antwort ein und dann ENTER: ")
                spieler.sendall(antwort.encode())
            else:
                print("EOF")
                break
    finally:
        spieler.close()