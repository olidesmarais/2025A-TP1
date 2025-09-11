# Exercice 04 – Hauteur atteinte par un escalier mécanique (gabarit)
"""
Objectif :
- DEMANDER longueur (m, float) et angle (° en degrés, float)
- Valider : longueur >= 0 et 0 <= angle <= 90
    -> sinon afficher "Erreur - données invalides."
- Sinon : H = L * sin(radians(angle)) ; afficher avec 2 décimales : "{H:.2f} m"

Prompts EXACTS à utiliser quand vous implémenterez input :
1) "Entrez la longueur de l'escalier (en mètres) : "
2) "Entrez l'angle de l'escalier par rapport à l'horizontale (en degrés) : "
"""

# TODO: Importer la/les bibliothèques nécessaire(s)
import math

# TODO: Lire longueur et angle via input (prompts EXACTS) et convertir en float
longueur = float(input("Entrez la longueur de l'escalier (en mètres) : "))
angle = float(input("Entrez l'angle de l'escalier par rapport à l'horizontale (en degrés) : "))

# TODO: Validation des entrées
if not(longueur >= 0 and 0 <= angle <= 90):
    print("Erreur - données invalides.")
    exit()

# TODO: Calcul hauteur et affichage
hauteur = longueur * math.sin(math.radians(angle))
print(f"{hauteur:.2f} m")


