# Exercice 01 – Usage hebdomadaire du métro (gabarit)
"""
Objectif :
- DEMANDER le nom complet et le nombre de déplacements par semaine (entier)
- Calculer le nombre de déplacements annuels
- Afficher EXACTEMENT :
    Bonjour {nom}
    Vous effectuez environ {nombre de déplacements annuels} déplacements par an sur le réseau STM.

Prompts (à utiliser quand vous implémenterez input) :
1) "Veuillez entrer votre nom complet : "
2) "Veuillez entrer le nombre de déplacements par semaine : "
"""


# TODO: Lire le nom complet (str) avec le prompt EXACT
nom_complet = input("Veuillez entrer votre nom complet : ")

# TODO: Lire le nombre de déplacements par semaine (int) avec le prompt EXACT
deplacement_hebdommadaire = int(input("Veuillez entrer le nombre de déplacements par semaine : "))

# TODO: Calcul des déplacements annuels
deplacements_annuels = deplacement_hebdommadaire * 52

# TODO: Affichage des deux lignes EXACTES
print("Bonjour " + nom_complet + "\nVous effectuez environ " + str(deplacements_annuels) + " déplacements par an sur le réseau STM.")


