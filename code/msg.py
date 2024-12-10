import sendmail

inhalt = "hallo text"

sender = "tn1@phaenovum.de"
empfänger = "tn2@phaenovum.de"

nachricht = sendmail.create_msg(sender, empfänger, inhalt)

sendmail.send_msg(sender, nachricht)
