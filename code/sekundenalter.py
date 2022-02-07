# Funktionsdefinition
def sekunden_alter(name, alter):
    print(name, "ist", alter, "Jahre alt!")
    sekunden = alter * 365 * 24 * 60 * 60
    print(name, "ist an seinem Geburtstag", sekunden, "Sekunden alt")
    print()

# Funktionsaufrufe
sekunden_alter("Paul", 12)
sekunden_alter("Jonas", 15)
sekunden_alter("Herbert", 42)
sekunden_alter("Luise", 66)