# calcul.py
import math

# Addition de plusieurs nombres
def additionner(*nombres):
    total = 0

    for nombre in nombres:
        total += nombre

    return total


# Soustraction de plusieurs nombres
def soustraire(premier, *nombres):
    resultat = premier

    for nombre in nombres:
        resultat -= nombre

    return resultat


# Multiplication de plusieurs nombres
def multiplier(*nombres):
    resultat = 1

    for nombre in nombres:
        resultat *= nombre

    return resultat


# Division de plusieurs nombres
def diviser(premier, *nombres):
    resultat = premier

    for nombre in nombres:
        resultat /= nombre

    return resultat


# Carré d'un nombre
def carre(nombre):
    return nombre * nombre


# Puissance
def puissance(nombre, exposant):
    return nombre ** exposant


# Racine carrée
def racine(nombre):
    return math.sqrt(nombre)


# Distance entre deux points
def pythagoreD(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    distance = math.sqrt(dx**2 + dy**2)

    return distance


# Hypoténuse
def pythagoreH(a, b):
    return math.sqrt(a**2 + b**2)


# Sinus (angle en radians)
def sin(angle):
    return math.sin(angle)


# Cosinus (angle en radians)
def cos(angle):
    return math.cos(angle)


# Tangente (angle en radians)
def tan(angle):
    return math.tan(angle)


# Degrés vers radians
def degresVersRadians(degres):
    return degres * math.pi / 180


# Radians vers degrés
def radiansVersDegres(radians):
    return radians * 180 / math.pi



# Test
if __name__ == "__main__":
    print("Addition :", additionner(23, 23, 4))
    print("Soustraction :", soustraire(100, 20, 10))
    print("Multiplication :", multiplier(2, 3, 4))
    print("Division :", diviser(100, 2, 5))

    print("Carré :", carre(5))
    print("Puissance :", puissance(2, 4))
    print("Racine :", racine(25))

    print("Pythagore Distance A B :", pythagoreD(0, 0, 3, 4))
    print("Pythagore Hypoténuse :", pythagoreH(3, 4))

    angle = degresVersRadians(90)

    print("Sin 90° :", sin(angle))
    print("Cos 90° :", cos(angle))
    print("Tan 90° :", tan(angle))

    print("90 degrés en radians :", degresVersRadians(90))
    print("π radians en degrés :", radiansVersDegres(math.pi))