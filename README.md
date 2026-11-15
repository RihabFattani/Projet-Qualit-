# Projet de fin de module — Qualité et Test du Logiciel

**Groupe 01** — 3 étudiants — à rendre le [date de remise à compléter]

## Contexte

Un développeur a livré le module `panier.py` de l'application « Liste de Courses ».
Votre équipe qualité doit le tester **à partir de sa spécification** (`SPECIFICATION.md`),
mesurer l'efficacité de ses tests et signaler les défauts trouvés.

Vous ne corrigez pas `panier.py` : vous écrivez les tests et vous signalez les défauts.

## Contenu du dossier

```
SPECIFICATION.md       les règles à tester (valeurs propres à votre groupe)
panier.py              le module à tester (ne pas modifier)
tests/test_panier.py   deux tests de départ, à compléter
RAPPORT.md             le rapport à remplir
mutants/               8 versions modifiées de panier.py et leur description
verifier_mutants.py    exécute vos tests sur chaque mutant
requirements.txt       pytest et pytest-cov
```

## Installation et commandes

Python 3.10 ou plus récent. Depuis le dossier du projet :

```
python -m pip install -r requirements.txt
python -m pytest                       # exécuter les tests
python -m pytest --cov=panier --cov-branch --cov-report=term-missing
python verifier_mutants.py             # exécuter les tests sur les 8 mutants
```

## Travail demandé

Chaque tâche se rend à deux endroits : les tests dans `tests/test_panier.py` (ou d'autres
fichiers `tests/test_*.py`) et les tableaux correspondants dans `RAPPORT.md`.

**Tâche 1 — Partitions d'équivalence et valeurs limites (chapitre 8)**
- Pour `frais_livraison` : identifier les partitions valides et invalides, puis les valeurs
  limites (analyse à 2 valeurs).
- Pour `total_panier` : valeurs limites de la quantité et du prix, et tests de la boucle
  (0, 1 et 2 lignes).
- Écrire un test pour chaque cas retenu.

**Tâche 2 — Table de décision (chapitre 8)**
- Pour `remise` : construire la table de décision complète (3 conditions, 8 colonnes),
  puis la table simplifiée.
- Écrire un test par colonne de la table simplifiée, plus un test de la règle du plafond.

**Tâche 3 — Couverture des branches (chapitre 9)**
- Mesurer la couverture des branches avec les 2 tests de départ, puis avec votre suite.
- Viser 100 % des branches de `panier.py` ; expliquer toute branche non couverte.

**Tâche 4 — Test de mutation (chapitre 9)**
- Exécuter `python verifier_mutants.py`.
- Pour chaque mutant survivant : ajouter un test qui le tue, ou démontrer qu'il est
  équivalent (aucun test ne peut le tuer).

**Tâche 5 — Défauts et usage de l'IA (chapitres 7 et 9)**
- `panier.py` contient au moins deux défauts. Rédiger un rapport de défaut pour chacun.
- Tenir le journal d'usage de l'IA : au moins 3 entrées, dont au moins une erreur de
  l'IA que vous avez détectée et corrigée.

## Règles

- **L'IA est autorisée**, à condition de la déclarer dans le journal du rapport.
- **Le résultat attendu de chaque test vient de la spécification**, jamais d'une exécution
  de `panier.py`. Un test recopié du comportement du code valide ses défauts.
- **Un test qui révèle un défaut doit échouer** sur `panier.py`. Gardez-le tel quel : ne le
  supprimez pas, ne le marquez ni `skip` ni `xfail`.
- Ne modifiez ni `panier.py`, ni le dossier `mutants/`, ni `verifier_mutants.py`.
- Donnez à chaque test un nom qui dit ce qu'il vérifie (par exemple
  `test_frais_gratuits_au_seuil`).

## Livrable

Une archive `groupe_01.zip` du dossier complet, avec `tests/` et `RAPPORT.md` remplis.

## Évaluation (sur 20)

| Critère | Points |
|---|---|
| Défauts détectés : votre suite est exécutée sur des versions boguées de `panier.py` que vous ne connaissez pas | 6 |
| Partitions, valeurs limites et table de décision | 5 |
| Couverture des branches et mutants | 3 |
| Rapports de défauts | 2 |
| Journal d'usage de l'IA | 1 |
| Soutenance (note individuelle) | 3 |

Un test qui échoue sur une version correcte du module est considéré comme faux : il est
écarté du calcul des défauts détectés.

## Soutenance

10 minutes par groupe. L'enseignant ouvre un test de votre dépôt et pose une question à
chaque membre du groupe : quelle partition ou quelle colonne ce test couvre, pourquoi ce
résultat attendu, quel mutant il tue, quelle erreur de l'IA vous avez corrigée...
Chaque membre doit pouvoir expliquer n'importe quel test du groupe. Un étudiant qui ne
peut répondre à aucune question a une note plafonnée à 10/20.
