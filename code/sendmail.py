import smtplib, ssl

from email.message import EmailMessage

def create_msg(from_addr, to_addr, inhalt):
    msg = EmailMessage()
    msg.set_content(inhalt)

    msg['Subject'] = "Mein Betreff"
    msg['From'] = from_addr
    msg['To'] = to_addr
    return msg
    

def send_msg(from_addr, msg):

    server = "w00962be.kasserver.com"
    port = 465

    # Login Passwort abfragen
    prompt = "Login für {}: ".format(from_addr)
    passwort = input(prompt)

    # Sichere Verbindung aufbauen, einloggen und senden
    ssl_ctx = ssl.create_default_context()
    s = smtplib.SMTP_SSL(server, port, context=ssl_ctx)
    s.login(from_addr, passwort)
    s.send_message(msg)
    s.quit()


if __name__ == '__main__':
    inhalt = "hallo text"

    sender = "tn1@phaenovum.de"
    empfänger = "sven.krauss@phaenovum.de"

    nachricht = create_msg(sender, empfänger, inhalt)

    send_msg(sender, nachricht)
    