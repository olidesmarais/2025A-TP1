# TP1 : Exercices d’introduction à Python

📅 **Date de remise : 21 Septembre à 23:59**

Bienvenue dans cette série de cinq exercices Python pour votre TP1! Vous trouverez ci-dessous la description de chaque exercice. 

⚠️ Assurez-vous de respecter exactement les formats d’entrée et de sortie demandés (y compris l’orthographe, la ponctuation et les espaces), car un script de tests automatisés va aider à valider vos solutions.

⚠️ Chaque exercice est un problème **Indépendant** et le niveau de difficulté est progressif, avec seulement une légère augmentation de la complexité d’un exercice à l’autre.

⚠️ L'utilisation de tout outil basé sur l'Intelligence Artificielle est interdite!

## Exercices:

Le réseau de transport de montréal (STM), tout comme d'habitude, cherche à améliorer son réseau et demande votre aide pour accomplir cette tâche.  Ces exercices vous permettront de pratiquer les bases de la programmation Python : **entrées/sorties, opérations mathématiques simples, conditions et formatage de texte**.

## 01. Usage hebdomadaire du métro
Écrivez un programme qui salue l’utilisateur et estime sa fréquence annuelle de déplacements en transport en commun. Le programme devra demander le nom complet de l’utilisateur, puis le nombre de déplacements qu’il effectue en moyenne chaque semaine sur le réseau de la STM. Il affichera ensuite un message de bienvenue personnalisé suivi d’une estimation du nombre de déplacements annuels correspondants (en supposant 52 semaines dans l’année). 

Exemple :

Entrées (utilisateur) :

```python
Veuillez entrer votre nom complet :
Veuillez entrer le nombre de déplacements par semaine :
```

Sorties (programme) :
```python
Bonjour Jean Dupont
Vous effectuez environ 520 déplacements par an sur le réseau STM.
```
 
Explication : Dans cet exemple, l’utilisateur a indiqué effectuer 10 trajets par semaine. Le programme calcule alors 10 × 52 = 520 déplacements par an et affiche le message avec cette valeur.

NB : Vous devez convertir le nombre de déplacements par semaine en entier avant de faire vos opérations. 

## 02. Taux d’occupation d’un bus

Dans cet exercice, vous écrivez un programme de surveillance du taux d’occupation d’un bus de la STM. 

Le programme demande à l’utilisateur le **pourcentage** de remplissage actuel du bus (une valeur de 0 à 100). S’il s’agit d’une valeur valide (dans l’intervalle [0, 100]), le programme affiche une barre de progression visuelle du taux d’occupation ainsi que le pourcentage saisi. La barre de progression est composée de 10 caractères, où chaque bloc ❚ représente 10% d’occupation. Le nombre de blocs affichés doit refléter le pourcentage le plus proche (arrondi à la dizaine près). Les positions non occupées de la barre seront laissées vides (espaces). En cas de pourcentage invalide (nombre négatif ou supérieur à 100), le programme affiche un message d’erreur approprié. 

Exemples :

Entrée (utilisateur) :

```python
Entrez le taux d'occupation d'un bus (en %): 0
```

Sorties (programme) :

```python
[          ]  
0%
```

Entrée (utilisateur) : 
```python
Entrez le taux d'occupation d'un bus (en %): 12
```
Sorties :
```python
[❚         ]  
12%  
```

Entrée (utilisateur) : 
```python
Entrez le taux d'occupation d'un bus (en %): 68
```

Sorties :
```python
[❚❚❚❚❚❚❚   ]  
68%
```

Entrée (utilisateur) : 
```python
Entrez le taux d'occupation d'un bus (en %): 304
```
Sortie :
```python
Erreur : taux d'occupation invalide.  
```

N.B. : Pour construire facilement la barre d’occupation, vous pouvez utiliser l’opérateur de multiplication sur les chaînes de caractères en Python. Par exemple, '❚' * 3 produit ❚❚❚.

## 03. Marcher ou attendre le bus ?

Montréal est une ville où l’on peut parfois choisir entre marcher ou prendre le bus pour de courts trajets. Écrivez un programme qui aide à décider le moyen le plus rapide pour se rendre à destination.

Le programme demande à l’utilisateur la distance jusqu’à la destination (en kilomètres), puis le temps d’attente estimé avant le prochain bus (en minutes). En considérant qu’un piéton marche à une vitesse moyenne de 5 km/h et qu’un bus se déplace à une vitesse moyenne de 20 km/h, le programme calcule le temps de trajet en marchant et le temps de trajet en bus (incluant l’attente). Il compare ensuite ces durées et affiche un conseil sur le moyen de transport le plus rapide.

Si marcher est plus rapide, affichez : « Il est plus rapide de marcher. »

Si prendre le bus est plus rapide, affichez : « Il est plus rapide de prendre le bus. »

Si les deux options prennent exactement le même temps, affichez : « Les deux options prennent le même temps. »

Types : distance float (km), attente entier (min) — à préciser.

Exemples :

Pour une distance de 0,5 km et une attente de 10 minutes, marcher prendra environ 6 minutes et le bus environ 11,5 minutes : le programme affichera « Il est plus rapide de marcher. ».

Pour une distance de 5 km sans aucune attente de bus, marcher prend ~60 min contre ~15 min en bus : le programme affichera « Il est plus rapide de prendre le bus. ».

Pour une distance de 1 km avec 9 minutes d’attente, marcher et prendre le bus prennent chacun ~12 minutes : le programme affichera « Les deux options prennent le même temps. ».

## 04. Hauteur atteinte par un escalier mécanique
Les stations de métro de Montréal sont équipées d’escaliers mécaniques pour faciliter l’accès. Dans cet exercice, vous devez calculer la hauteur verticale atteinte par un escalier mécanique en fonction de sa longueur et de son inclinaison. Le programme demande à l’utilisateur la longueur de l’escalier (en mètres) et l’angle de l’escalier par rapport à l’horizontale (en degrés). Il calcule ensuite la hauteur verticale correspondante en utilisant la formule : 

$$
𝐻 = 𝐿 × sin(𝜃)
$$

où L est la longueur de l’escalier et $\theta$ l’angle en degrés. La hauteur H est exprimée en mètres. Le programme affichera la hauteur calculée, arrondie à deux décimales.

Note : En Python, la fonction math.sin() attend un angle en radians. Vous devrez donc convertir l’angle fourni en degrés vers des radians avant le calcul. (Indice : consultez la fonction math.radians ou rappelez-vous que $\pi$ radians = 180°.)

NB : N'ouvbliez pas la validation d'entrées! (Message : Erreur : données invalides.)

Exemples :

Un escalier de 10 m avec un angle de 30° atteindra une hauteur d’environ 5,00 m.

Un escalier de 10 m avec un angle de 90° (vertical) permettra de monter d’environ 10,00 m (soit la longueur de l’escalier).

Un escalier de 5 m avec un angle de 0° (parfaitement horizontal) ne monte pas : hauteur de 0,00 m.

## 05. Répartition optimale des titres

La STM vend des titres de transport (valables par utilisation) :

- **Carnet 30 billets** → couvre **30 trajets** → **75.00 $** (soit **2.50 $** par trajet)  
- **Carnet de 10 billets** → couvre **10 trajets** → **30.00 $** (soit **3.00 $** par trajet)  
- **Billet simple** → couvre **1 trajet** → **3.75 $** (soit **3.75 $** par trajet)

> Le prix par trajet **diminue** avec la taille du titre : 30 > 10 > 1.  
> Votre programme doit calculer la **combinaison la moins chère** pour un nombre de trajets donné.

### Consignes
1. Demandez à l’utilisateur :

```python
Entrez le nombre total de trajets à effectuer :
```

2. Calculez une combinaison qui **couvre exactement tous les trajets**.  
  
3. Affichez **exactement** les quatre lignes suivantes :

```python
Carnets de 30 billets : X
Carnets de 10 billets : Y
Billets simples : Z
Prix total : TTT.TT$
```

où `TTT.TT` est le coût total **formaté avec 2 décimales**.

### Exemple

Entrée :

```python
Entrez le nombre total de trajets à effectuer : 89
```

Sortie attendue :

```
Carnets de 30 billets : 2
Carnets de 10 billets : 2
Billets simples : 9
Prix total : 243.75$
```

**Détails de calcul :**  
- 2 × (30 trajets) = 60 trajets → reste 29  
- 2 × (10 trajets) = 20 trajets → reste 9 
- 9 × (1 trajet) = 9 trajets → reste 0  
- Coût : 2×75.00 + 2×30.00 + 9×3.75 = **243.75$**


> 🎯 Question bonus : Si une sur-couverture (acheter plus de trajets que nécessaire) donne un coût total plus bas, afficher en plus une ligne :

 ```
Il existe une combinaison sur-couvrante moins chère : A, B, C : PPP.PP$ (surplus : S trajet(s))
```

Exemple pour 89 trajets : acheter 3 carnets de 30 (90 trajets) coûte 225.00$, ce qui est moins cher que 243.75$ (exact).
Ligne bonus :

```
Il existe une combinaison sur-couvrante moins chère : A, B, C : PPP.PP$ (surplus : S trajet(s))
```

## Fichiers du projet
- README.md – le fichier que vous lisez actuellement, contenant les consignes et informations générales.
- exo1.py – exercice 01
- exo2.py – exercice 02
- exo3.py – exercice 03
- exo4.py – exercice 04
- exo5.py – exercice 05
- test.py – script de tests automatisés pour valider vos solutions (simule des entrées utilisateur et compare les sorties du programme aux résultats attendus). Veillez à créer chacun des fichiers exo1.py à exo5.py et à y écrire votre code conformément aux consignes ci-dessus. Une fois terminé, vous pouvez exécuter test.py pour vérifier automatiquement la conformité de vos programmes.


# Directives pour la remise

Pour remettre votre travail, vous devez créer un fichier **zip** nommé : XXXXX_YYYYY-PR01.zip

où **XXXXX** est votre nom de famille et **YYYYY** votre prénom.  

Ce fichier zip devra contenir **tous les fichiers `.py` du TP** (`exo1.py` à `exo5.py`).  

➡️ Votre fichier zip est à remettre dans la boîte de remise sur **Moodle** prévue à cet effet, **le 21 Septembre à 23:59**.

# Barème de correction

Le barème de correction est le suivant :  

| Partie | Tâche | Points |
|--------|-------|--------|
| **Exercice 1 : Usage hebdomadaire du métro ** | | **/3** |
| 1.1 | Lecture du nom complet (avec `input`) | 0.5 |
| 1.2 | Lecture du nombre de déplacements par semaine (cast en entier) | 0.5 |
| 1.3 | Calcul correct du nombre annuel (`52 * déplacements`) | 1 |
| 1.4 | Affichage correct du message de bienvenue avec le nom | 0.5 |
| 1.5 | Affichage correct de la phrase complète avec le nombre annuel | 0.5 |
| **Exercice 2 : Taux d’occupation d’un bus 🚌** | | **/4** |
| 2.1 | Lecture du pourcentage avec `input` | 0.5 |
| 2.2 | Vérification validité de l’entrée (0 ≤ taux ≤ 100) | 0.5 |
| 2.3 | Construction correcte de la barre avec ❚ et espaces | 1 |
| 2.4 | Arrondi du nombre de blocs à la dizaine près | 0.5 |
| 2.5 | Affichage de la barre + du pourcentage | 0.5 |
| 2.6 | Gestion de l’erreur « Erreur : taux d'occupation invalide. » | 1 |
| **Exercice 3 : Marcher ou attendre le bus ? 🚶‍♂️🚌** | | **/4** |
| 3.1 | Lecture de la distance (float) et du temps d’attente (int) | 0.5 |
| 3.2 | Calcul du temps de marche (vitesse 5 km/h) | 0.5 |
| 3.3 | Calcul du temps de bus (20 km/h + attente) | 0.5 |
| 3.4 | Comparaison correcte des durées | 1 |
| 3.5 | Affichage du bon message (« marcher », « bus », ou égalité) | 1.5 |
| **Exercice 4 : Hauteur atteinte par un escalier mécanique ** | | **/4** |
| 4.1 | Lecture de la longueur (float) et de l’angle (float) | 0.5 |
| 4.2 | Conversion de l’angle en radians (via `math.radians`) | 0.5 |
| 4.3 | Application correcte de la formule H = L × sin(θ) | 1 |
| 4.4 | Résultat arrondi à 2 décimales | 0.5 |
| 4.5 | Affichage correct (avec « m » à la fin) | 0.5 |
| 4.6 | Gestion des entrées invalides (affichage du message d’erreur) | 1 |
| **Exercice 5 : Répartition optimale des titres ** | | **/5** |
| 5.1 | Lecture du nombre de trajets (int) | 0.5 |
| 5.2 | Calcul correct du nombre de carnets de 30 | 1 |
| 5.3 | Calcul correct du nombre de carnets de 10 | 1 |
| 5.4 | Calcul correct des billets simples | 0.5 |
| 5.5 | Calcul du prix total avec formatage à 2 décimales | 1 |
| 5.6 | Affichage correct des 4 lignes demandées (ordre exact) | 1 |
| **Total** |  | **/20** |

---

🎯 **Question bonus** :  
- Vérification d’une combinaison sur-couvrante moins chère  
- Affichage du message additionnel avec le surplus de trajets  
*(+1 pt bonus)*  

---

Bonne programmation !
