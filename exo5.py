# Exercice 05 – Répartition optimale des titres (gabarit)
"""
Objectif :
- DEMANDER n (int), le nombre total de trajets.
- Trouver une combinaison EXACTE minimal coût en utilisant :
    30 trajets -> 75.00$
    10 trajets -> 30.00$
     1 trajet  ->  3.75$
- Afficher EXACTEMENT :
    Carnets de 30 billets - X
    Carnets de 10 billets - Y
    Billets simples - Z
    Prix total - TTT.TT$

BONUS (optionnel mais recommandé) :
- Si une SUR-COUVERTURE (acheter un peu plus de trajets) est moins chère,
  afficher en plus :
  "Il existe une combinaison sur-couvrante moins chère : A, B, C : PPP.PP$ (surplus : S trajet(s))"

Prompt EXACT à utiliser quand vous implémenterez input :
"Entrez le nombre total de trajets à effectuer : "
"""

# TODO: Lire n via input (prompt EXACT) et convertir en int
nb_trajets = int(input("Entrez le nombre total de trajets à effectuer : "))

# TODO: calculer la répartition exacte (30 -> 10 -> 1)
carnet30 = nb_trajets // 30
nb_trajets -= carnet30 * 30
carnet10 = nb_trajets // 10
nb_trajets -= carnet10 * 10
billets_simple = nb_trajets

# TODO: Calcul prix total
prix = carnet30 * 75 + carnet10 * 30 + billets_simple * 3.75

# TODO: Affichage des résultats de la répartition exacte (4 lignes)
print("Carnets de 30 billets -", carnet30)
print("Carnets de 10 billets -", carnet10)
print("Billets simples -", billets_simple)
print("Prix total - " + str(round(prix, 2)) + "$")

# TODO: BONUS (optionnel)

