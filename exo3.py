# Exercice 03 – Marcher ou attendre le bus ? (gabarit)
"""
Objectif :
- DEMANDER distance (km, float) et attente (min, float/int)
- Temps marche (min) = distance * 60 / 5
- Temps bus (min) = attente + distance * 60 / 20
- Afficher EXACTEMENT UNE des phrases :
    "Il est plus rapide de marcher."
    "Il est plus rapide de prendre le bus."
    "Les deux options prennent le même temps."

Prompts EXACTS à utiliser quand vous implémenterez input :
1) "Entrez la distance jusqu'à la destination (en kilomètres) : "
2) "Entrez le temps d'attente avant le prochain bus (en minutes) : "
"""


# TODO: Lire distance et attente via input (prompts EXACTS)
distance = float(input("Entrez la distance jusqu'à la destination (en kilomètres) : "))
attente = float(input("Entrez le temps d'attente avant le prochain bus (en minutes) : "))

# TODO: Calcul temps_marche et temps_bus (en minutes)
temps_marche = distance * 60 / 5
temps_bus = attente + distance * 60 / 20

# TODO: Comparaison et affichage de la phrase EXACTE (une seule)
if temps_bus < temps_marche:
    print("Il est plus rapide de prendre le bus.")
elif temps_bus > temps_marche:
    print("Il est plus rapide de marcher.")
else:
    print("Les deux options prennent le même temps.")
    

