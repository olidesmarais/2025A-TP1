# Exercice 02 – Taux d’occupation d’un bus (gabarit)
"""
Objectif :
- DEMANDER un taux (int), 0..100 inclus.
- Si invalide : afficher "Taux d'occupation invalide."
- Sinon : afficher barre de 10 caractères (❚ pour ~10%), arrondi à la dizaine la plus proche,
         puis afficher "{taux}%"

Prompt EXACT à utiliser quand vous implémenterez input :
"Entrez le taux d'occupation d'un bus (en %): "
"""

# TODO: Lire le taux (int) via input avec le prompt EXACT
taux_occupation = int(input("Entrez le taux d'occupation d'un bus (en %): "))

# TODO: Valider 0 <= taux <= 100
if not(0 <= taux_occupation <= 100):
    print("Taux d'occupation invalide.")
    exit()

# TODO: Calculer blocs = (taux + 5) // 10  (arrondi à la dizaine)
blocs = ( (taux_occupation + 5) // 10)

# TODO: Afficher barre et pourcentage dans le format correct.
print("[" + blocs*"❚" + (10-blocs)*" " + "]" + "\n" + str(taux_occupation) + "%")
