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
- 📐 Calcul d'hypoténuse avec Pythagore
- 📍 Distance entre deux points
- 📈 Sinus, cosinus, tangente
- 🔄 Conversion degrés ↔ radians

---

# 📁 Structure du projet

```
MathLib/
│
├── calcul.py
├── test.py
├── README.md
└── LICENSE
```

---

# ⚙️ Installation

Aucune installation supplémentaire n'est nécessaire.

Il suffit de placer le fichier `calcul.py` dans votre projet Python.

Exemple :

```
MonProjet/
│
├── main.py
└── calcul.py
```

---

# 🚀 Utilisation

Importez le module :

```python
import calcul
```

Exemple :

```python
import calcul

resultat = calcul.additionner(10, 20, 30)

print(resultat)
```

Résultat :

```
60
```

---

# 📚 Fonctions disponibles

## ➕ additionner()

Additionne plusieurs nombres.

```python
calcul.additionner(10, 20, 30)
```

Résultat :

```
60
```

---

## ➖ soustraire()

Soustrait plusieurs nombres.

```python
calcul.soustraire(100, 20, 10)
```

Résultat :

```
70
```

---

## ✖ multiplier()

Multiplie plusieurs nombres.

```python
calcul.multiplier(2, 3, 4)
```

Résultat :

```
24
```

---

## ➗ diviser()

Divise plusieurs nombres.

```python
calcul.diviser(100, 2, 5)
```

Résultat :

```
10
```

---

## ⬛ carre()

Calcule le carré d'un nombre.

```python
calcul.carre(5)
```

Résultat :

```
25
```

---

## 🔥 puissance()

Calcule une puissance.

```python
calcul.puissance(2, 4)
```

Résultat :

```
16
```

---

## √ racine()

Calcule une racine carrée.

```python
calcul.racine(25)
```

Résultat :

```
5
```

---

# 📐 Géométrie

## pythagoreH()

Calcule l'hypoténuse d'un triangle rectangle.

```python
calcul.pythagoreH(3, 4)
```

Résultat :

```
5
```

---

## pythagoreD()

Calcule la distance entre deux points.

```python
calcul.pythagoreD(0, 0, 3, 4)
```

Résultat :

```
5
```

---

# 📈 Trigonométrie

Les angles doivent être en radians.

## sin()

Calcule le sinus.

```python
calcul.sin(angle)
```

---

## cos()

Calcule le cosinus.

```python
calcul.cos(angle)
```

---

## tan()

Calcule la tangente.

```python
calcul.tan(angle)
```

---

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

## degresVersRadians()

Convertit des degrés en radians.

```python
calcul.degresVersRadians(180)
```

Résultat :

```
3.14159...
```

---

## radiansVersDegres()

Convertit des radians en degrés.

```python
calcul.radiansVersDegres(3.14159)
```

Résultat :

```
180
```

---

# 🧪 Tests

Le fichier `test.py` permet de vérifier le fonctionnement de la bibliothèque.

Lancer les tests :

```bash
python test.py
```

Exemple de résultat :

```
Addition : 50
Soustraction : 70
Multiplication : 24
Division : 10
Carré : 25
Puissance : 16
Racine : 5
Hypoténuse : 5
Sin 90° : 1
```

---

# 📜 Licence

MathLib est distribué sous licence MIT.

Vous pouvez :

- Utiliser le projet
- Modifier le code
- Distribuer le projet

Selon les conditions de la licence MIT.

---

# 👨‍💻 Auteur

Créé par **Youness (unnread)**

Projet Python réalisé pour apprendre la création d'une bibliothèque mathématique.

---

# 🐍 Langage utilisé

Python 3
