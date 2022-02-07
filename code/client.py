import sys
import socket
import time

spieler = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Verbinde zum Spieler ...")
spieler.connect(("192.168.2.21", 51000))
print("Verbunden")

try:
    while True:
        frage = input("Tippe deine Frage ein und dann ENTER: ")
        spieler.sendall(frage.encode())
        print("Warte auf die Antwort")
        antwort = spieler.recv(256)
        print("Antwort: " + antwort.decode())
finally:
    print("Cleanup")
    sock.close()