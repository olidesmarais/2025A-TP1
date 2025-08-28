import os, re, subprocess, sys

# ---- Réglages ----
IGNORE_PROMPTS = True
REQUIRE_BONUS_EXO5 = False   # passe à True si tu veux rendre la ligne bonus obligatoire

PROMPT_RE = re.compile(
    r"(?:^|\n)\s*(?:Veuillez entrer|Entrez|Entrez l'|Entrez la|Entrez le)[^\n]*:\s*",
    flags=re.IGNORECASE
)

def clean_output(s: str) -> str:
    # Normalisation des fins de ligne
    s = s.replace("\r\n", "\n")
    if IGNORE_PROMPTS:
        s = PROMPT_RE.sub("\n", s)
        # Enlève lignes vides causées par la suppression des prompts
        s = "\n".join([line for line in s.split("\n") if line.strip() != ""]) + ("\n" if s.endswith("\n") else "")
    return s

def run_exercice(filename, input_data):
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"  # force stdout/stderr UTF-8 côté enfant
    try:
        completed = subprocess.run(
            [sys.executable, filename],
            input=input_data, text=True, encoding="utf-8",
            capture_output=True, timeout=2, env=env
        )
    except Exception as e:
        return f"Erreur lors de l'exécution de {filename} : {e}"
    out = clean_output(completed.stdout)
    err = clean_output(completed.stderr)
    if completed.returncode != 0:
        return (f"Le programme {filename} s'est terminé avec le code d'erreur {completed.returncode}.\n"
                f"Sortie standard : {out}\nErreurs : {err}")
    return out

tests = {
    "exo1.py": [
        {"input": "Jean Dupont\n10\n",
         "expected": "Bonjour Jean Dupont\nVous effectuez environ 520 déplacements par an sur le réseau STM.\n"},
        {"input": "Alice\n1\n",
         "expected": "Bonjour Alice\nVous effectuez environ 52 déplacements par an sur le réseau STM.\n"},
    ],
    "exo2.py": [
        {"input": "0\n",  "expected": "[          ]\n0%\n"},
        {"input": "12\n", "expected": "[❚         ]\n12%\n"},
        {"input": "68\n", "expected": "[❚❚❚❚❚❚❚   ]\n68%\n"},
        {"input": "123\n","expected": "Taux d'occupation invalide.\n"},
        {"input": "-42\n","expected": "Taux d'occupation invalide.\n"},
    ],
    "exo3.py": [
        {"input": "0.5\n10\n", "expected": "Il est plus rapide de marcher.\n"},
        {"input": "5\n0\n",    "expected": "Il est plus rapide de prendre le bus.\n"},
        {"input": "1\n9\n",    "expected": "Les deux options prennent le même temps.\n"},
    ],
    "exo4.py": [
        {"input": "10\n30\n", "expected": "5.00 m\n"},
        {"input": "10\n90\n", "expected": "10.00 m\n"},
        {"input": "5\n0\n",   "expected": "0.00 m\n"},
        # validations demandées dans le README
        {"input": "-1\n30\n",  "expected": "Erreur : données invalides.\n"},
        {"input": "10\n120\n", "expected": "Erreur : données invalides.\n"},
    ],
    # Pour exo5, on accepte sans la ligne bonus si REQUIRE_BONUS_EXO5 = False
    "exo5.py": [
        {
            "input": "87\n",
            "expected_base": ("Carnets de 30 billets : 2\n"
                              "Carnets de 10 billets : 2\n"
                              "Billets simples : 7\n"
                              "Prix total : 236.25$\n"),
            "expected_bonus": ("Carnets de 30 billets : 2\n"
                               "Carnets de 10 billets : 2\n"
                               "Billets simples : 7\n"
                               "Prix total : 236.25$\n"
                               "Il existe une combinaison sur-couvrante moins chère : 3, 0, 0 : 225.00$ (surplus : 3 trajet(s))\n")
        },
        {
            "input": "7\n",
            "expected_base": ("Carnets de 30 billets : 0\n"
                              "Carnets de 10 billets : 0\n"
                              "Billets simples : 7\n"
                              "Prix total : 26.25$\n"),
            "expected_bonus": ("Carnets de 30 billets : 0\n"
                               "Carnets de 10 billets : 0\n"
                               "Billets simples : 7\n"
                               "Prix total : 26.25$\n")  # pas de bonus plus avantageux ici
        },
        {
            "input": "89\n",
            "expected_base": ("Carnets de 30 billets : 2\n"
                              "Carnets de 10 billets : 2\n"
                              "Billets simples : 9\n"
                              "Prix total : 243.75$\n"),
            "expected_bonus": ("Carnets de 30 billets : 2\n"
                               "Carnets de 10 billets : 2\n"
                               "Billets simples : 9\n"
                               "Prix total : 243.75$\n"
                               "Il existe une combinaison sur-couvrante moins chère : 3, 0, 0 : 225.00$ (surplus : 1 trajet(s))\n")
        },
    ],
}

all_ok = True
for filename, cases in tests.items():
    exercise_ok = True
    for case in cases:
        out = run_exercice(filename, case["input"])
        # exo5: gérer bonus optionnel
        if filename == "exo5.py":
            base = case["expected_base"]
            bonus = case["expected_bonus"]
            if REQUIRE_BONUS_EXO5:
                expected = bonus
                ok = (out == expected)
            else:
                ok = (out == base) or (out == bonus)
            if not ok:
                all_ok = exercise_ok = False
                print(f"[ÉCHEC] {filename} avec entrée {repr(case['input'])}:")
                print("Attendu (base ou bonus) :", repr(base if out != bonus else bonus))
                print("Obtenu :", repr(out))
            continue

        # autres exos: comparaison directe
        expected = case["expected"]
        if out != expected:
            all_ok = exercise_ok = False
            print(f"[ÉCHEC] {filename} avec entrée {repr(case['input'])}:")
            print(f"Attendu : {repr(expected)}")
            print(f"Obtenu  : {repr(out)}")
    if exercise_ok:
        print(f"{filename} : OK ({len(cases)}/{len(cases)} tests réussis)")
if all_ok:
    print("\nTous les tests de base ont réussi. Bien joué !")
else:
    print("\nCertains tests ont échoué. Vérifiez les résultats ci-dessus.")
