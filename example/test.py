import lib.calcul as calcul


print("=== TEST CALCUL ===")

# Addition
print("Addition :", calcul.additionner(10, 20, 30))

# Soustraction
print("Soustraction :", calcul.soustraire(100, 25, 15))

# Multiplication
print("Multiplication :", calcul.multiplier(5, 4, 2))

# Division
print("Division :", calcul.diviser(100, 2, 5))


print("\n=== TEST MATH ===")

# Carré
print("Carré de 12 :", calcul.carre(12))

# Puissance
print("3 puissance 4 :", calcul.puissance(3, 4))

# Racine
print("Racine de 81 :", calcul.racine(81))


print("\n=== TEST PYTHAGORE ===")

# Hypoténuse
print("Hypoténuse (6,8) :", calcul.pythagoreH(6, 8))

# Distance entre deux points
print("Distance (0,0) -> (5,12) :", calcul.pythagoreD(0, 0, 5, 12))


print("\n=== TEST TRIGONOMETRIE ===")

angle = calcul.degresVersRadians(90)

print("Sin 90° :", calcul.sin(angle))
print("Cos 90° :", calcul.cos(angle))
print("Tan 90° :", calcul.tan(angle))


print("\n=== TEST CONVERSION ANGLE ===")

print("90 degrés en radians :", calcul.degresVersRadians(90))
print("Pi radians en degrés :", calcul.radiansVersDegres(3.141592653589793))


print("\n=== FIN DES TESTS ===")