# MathLib 🧮

MathLib est une bibliothèque Python qui regroupe plusieurs fonctions mathématiques utiles.

Elle permet de réaliser des calculs simples, de la géométrie, de la trigonométrie et des conversions d'angles.

---

# ✨ Fonctionnalités

MathLib contient :

- ➕ Addition de plusieurs nombres
- ➖ Soustraction de plusieurs nombres
- ✖ Multiplication de plusieurs nombres
- ➗ Division de plusieurs nombres
- ⬛ Carré d'un nombre
- 🔥 Puissance
- √ Racine carrée
- 📐 Hypoténuse avec Pythagore
- 📍 Distance entre deux points
- 📈 Sinus, cosinus, tangente
- 🔄 Conversion degrés ↔ radians
- ! Factoriel d'un nombre
- 
---

# ⚙️ Installation

Téléchargez le projet puis placez-le dans votre environnement Python.

Aucune dépendance externe n'est nécessaire.

---

# 🚀 Utilisation

Importer le module :

```python
import MathLib.calcul as calcul
```

Exemple :

```python
import MathLib.calcul as calcul

resultat = calcul.additionner(10, 20, 30)

print(resultat)
```

Résultat :

```
60
```

---

# 📚 Fonctions disponibles

## ➕ Addition

```python
calcul.additionner(10,20,30)
```

Résultat :

```
60
```

---

## ➖ Soustraction

```python
calcul.soustraire(100,20,10)
```

Résultat :

```
70
```

---

## ✖ Multiplication

```python
calcul.multiplier(2,3,4)
```

Résultat :

```
24
```

---

## ➗ Division

```python
calcul.diviser(100,2,5)
```

Résultat :

```
10
```

---

## ⬛ Carré

```python
calcul.carre(5)
```

Résultat :

```
25
```

---

## 🔥 Puissance

```python
calcul.puissance(2,4)
```

Résultat :

```
16
```

---

## √ Racine carrée

```python
calcul.racine(25)
```

Résultat :

```
5
```

---

# 📐 Géométrie

## Hypoténuse

```python
calcul.pythagoreH(3,4)
```

Résultat :

```
5
```

---

## Distance entre deux points

```python
calcul.pythagoreD(0,0,3,4)
```

Résultat :

```
5
```

---

# 📈 Trigonométrie

Les angles utilisent les radians.

## Sinus

```python
calcul.sin(angle)
```

## Cosinus

```python
calcul.cos(angle)
```

## Tangente

```python
calcul.tan(angle)
```

Exemple :

```python
angle = calcul.degresVersRadians(90)

print(calcul.sin(angle))
```

Résultat :

```
1
```

---

# 🔄 Conversion d'angles

## Degrés vers radians

```python
calcul.degresVersRadians(180)
```

---

## Radians vers degrés

```python
calcul.radiansVersDegres(3.14159)
```

---

# 🧪 Tests

Pour tester la bibliothèque :

```bash
python exemple/test.py
```

---

# 📜 Licence

MathLib est distribué sous licence MIT.

Vous êtes libre d'utiliser, modifier et distribuer ce projet selon les conditions de la licence MIT.

---

# 👨‍💻 Auteur

Créé par **Youness (unnread)**

Projet réalisé en Python pour apprendre la création d'une bibliothèque.
