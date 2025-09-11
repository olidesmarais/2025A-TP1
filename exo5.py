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

# TODO: Importer la/les bibliothèques nécessaire(s)
import math

# TODO: Lire n via input (prompt EXACT) et convertir en int
nb_trajets = int(input("Entrez le nombre total de trajets à effectuer : "))

# TODO: calculer la répartition exacte (30 -> 10 -> 1)
def get_quantites_billets( total_trajet ):
    carnet30 = total_trajet // 30
    carnet10 = ( total_trajet - 30 * carnet30 )// 10
    billets_simple = total_trajet - 30 * carnet30 - 10 * carnet10
    return carnet30, carnet10, billets_simple

carnet30, carnet10, billets_simple = get_quantites_billets( nb_trajets )

# TODO: Calcul prix total
def calculer_prix( carnet30, carnet10, billets_simple):
    return round( carnet30 * 75 + carnet10 * 30 + billets_simple * 3.75, 2 )

prix = calculer_prix( carnet30, carnet10, billets_simple)

# TODO: Affichage des résultats de la répartition exacte (4 lignes)
print("Carnets de 30 billets -", carnet30)
print("Carnets de 10 billets -", carnet10)
print("Billets simples -", billets_simple)
print("Prix total - " + str( prix ) + "$")

# TODO: BONUS (optionnel)
def arrondir_ceilling( valeur, precision ):
    return math.ceil(valeur / precision) * precision

nb_trajets_optimise = arrondir_ceilling( nb_trajets, 30 )
carnet30_optimise, carnet10_optimise, billets_simple_optimise = get_quantites_billets( nb_trajets_optimise )
prix_optimise = calculer_prix( carnet30_optimise, carnet10_optimise, billets_simple_optimise )

if prix_optimise < prix:
    print("Il existe une combinaison sur-couvrante moins chère : " + str(carnet30_optimise) + ", " + str(carnet10_optimise) + ", " + str(billets_simple_optimise) + " : " + f"{prix_optimise:.2f}" + "$ (surplus : " + str(nb_trajets_optimise - nb_trajets) + " trajet(s))")


