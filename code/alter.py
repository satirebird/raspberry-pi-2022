alter = int(input("Wie alt bist du? "))
if alter < 10:
    print("Kind")
elif alter < 18:
    print("Jugendlich")
else:
    print("Erwachsen")