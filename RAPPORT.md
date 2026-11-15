# Rapport de test — groupe 01

Membres : 1. ............................  2. ............................  3. ............................

> Remplacez les lignes d'exemple (en italique) par les vôtres. Ajoutez autant de lignes
> que nécessaire. La colonne « Test » donne le nom de la fonction de test correspondante.

## Tâche 1 — Partitions et valeurs limites

### 1.a Partitions de `frais_livraison`

| N° | Partition | Valide ? | Valeur représentative | Résultat attendu | Test |
|---|---|---|---|---|---|
| P1 | *exemple : zone inconnue* | *non* | *zone "SFAX"* | *ValueError* | *test_frais_zone_inconnue* |
| P2 | | | | | |

### 1.b Valeurs limites de `frais_livraison` (analyse à 2 valeurs)

| Frontière | Valeurs testées | Résultats attendus | Tests |
|---|---|---|---|
| | | | |

### 1.c Valeurs limites et boucle de `total_panier`

| Élément | Valeurs testées | Résultats attendus | Tests |
|---|---|---|---|
| Quantité | | | |
| Prix | | | |
| Nombre de lignes (boucle) | 0, 1, 2 | | |

## Tâche 2 — Table de décision de `remise`

Conditions : C1 = adhérent ; C2 = total ≥ 80 DT ; C3 = code promo valide.

### 2.a Table complète (8 colonnes)

| | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| C1 adhérent | | | | | | | | |
| C2 total ≥ 80 DT | | | | | | | | |
| C3 code valide | | | | | | | | |
| Remise adhérent (15 %) | | | | | | | | |
| Remise code (3 DT) | | | | | | | | |

### 2.b Table simplifiée et tests

| Colonne | C1 | C2 | C3 | Données de test | Remise attendue | Test |
|---|---|---|---|---|---|---|
| | | | | | | |

Test de la règle du plafond (données, résultat attendu, nom du test) : ..................

## Tâche 3 — Couverture des branches

| Mesure | Couverture des branches | Branches non couvertes |
|---|---|---|
| Avec les 2 tests de départ | | |
| Avec votre suite finale | | |

Copiez ici la sortie de `python -m pytest --cov=panier --cov-branch --cov-report=term-missing`
pour votre suite finale :

```
(sortie à coller)
```

Explication des branches non couvertes, s'il en reste : ..................

## Tâche 4 — Mutants

| Mutant | Résultat avec votre suite | Test qui le tue | Si survivant : test ajouté, ou pourquoi il est équivalent |
|---|---|---|---|
| mutant_1 | | | |
| mutant_2 | | | |
| mutant_3 | | | |
| mutant_4 | | | |
| mutant_5 | | | |
| mutant_6 | | | |
| mutant_7 | | | |
| mutant_8 | | | |

Score de mutation final : ..... / ..... (en excluant les mutants équivalents)

## Tâche 5 — Défauts

### Défaut 1

| Champ | Contenu |
|---|---|
| Titre | |
| Fonction | |
| Étapes pour reproduire (appel exact) | |
| Résultat attendu (selon la spécification) | |
| Résultat obtenu | |
| Sévérité (bloquante, majeure, mineure) | |
| Priorité (haute, moyenne, basse) | |
| Technique qui l'a révélé | |
| Test qui le révèle | |

### Défaut 2

(même tableau)

## Tâche 5 — Journal d'usage de l'IA

| N° | Outil | Ce que vous avez demandé | Ce que l'IA a produit (résumé) | Ce que vous avez gardé, corrigé ou rejeté, et pourquoi |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

Erreur de l'IA détectée (au moins une) : décrivez-la précisément et dites comment vous
l'avez repérée : ..................
