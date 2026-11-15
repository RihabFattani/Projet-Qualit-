# Rapport de test — groupe 01

Membres : 1. [NOM Prénom — à compléter]  2. [NOM Prénom — à compléter]  3. [NOM Prénom — à compléter]

Date de remise : [à compléter]

**Résumé.** Nous avons testé `panier.py` à partir de `SPECIFICATION.md`. La suite compte
45 tests. Elle atteint 100 % de couverture des branches et tue 7 mutants sur 8 (le 8e est
équivalent). Elle révèle **2 défauts** dans `panier.py` : le seuil de livraison gratuite est
exclu au lieu d'être inclus, et la remise n'est jamais plafonnée au total. Quatre tests
échouent donc volontairement sur `panier.py`.

## Tâche 1 — Partitions et valeurs limites

### 1.a Partitions de `frais_livraison`

Entrées : `total`, `zone`, `premium`. Les résultats attendus viennent de la spécification.

| N° | Partition | Valide ? | Valeur représentative | Résultat attendu | Test |
|---|---|---|---|---|---|
| P1 | total négatif | non | total = -0,01 | ValueError | test_frais_total_negatif_leve_valueerror |
| P2 | zone inconnue (client non Premium) | non | zone "SFAX" | ValueError | test_frais_zone_inconnue_leve_valueerror |
| P3 | zone inconnue, client Premium | non | zone "SFAX", premium | ValueError | test_frais_zone_inconnue_leve_valueerror_meme_pour_premium |
| P4 | zone vide | non | zone "" | ValueError | test_frais_zone_vide_leve_valueerror |
| P5 | Grand Tunis, total < 50, non Premium | oui | 10 DT, GRAND_TUNIS | 6,000 | test_frais_grand_tunis |
| P6 | Intérieur, total < 50, non Premium | oui | 25 DT, INTERIEUR | 9,000 | test_frais_interieur_sous_seuil |
| P7 | client Premium, total < 50, Grand Tunis | oui | 10 DT, premium | 0 | test_frais_premium_gratuit_grand_tunis |
| P8 | client Premium, total < 50, Intérieur | oui | 10 DT, premium | 0 | test_frais_premium_gratuit_interieur |
| P9 | total ≥ 50, non Premium | oui | 80 DT, INTERIEUR | 0 | test_frais_gratuits_au_dessus_du_seuil |

### 1.b Valeurs limites de `frais_livraison` (analyse à 2 valeurs)

| Frontière | Valeurs testées | Résultats attendus | Tests |
|---|---|---|---|
| total = 0 (limite basse valide, négatif interdit) | -0,01 et 0 | ValueError ; puis 6,000 (GT) et 9,000 (INT) | test_frais_total_negatif_leve_valueerror, test_frais_total_zero_accepte_et_payant, test_frais_total_zero_interieur_payant |
| seuil de gratuité = 50 DT (inclus) | 49,999 et 50 | 6,000 / 9,000 ; puis 0 | test_frais_juste_sous_le_seuil_grand_tunis, test_frais_juste_sous_le_seuil_interieur, test_frais_gratuits_au_seuil, test_frais_gratuits_au_seuil_interieur |
| juste au-dessus du seuil | 50,001 | 0 | test_frais_juste_au_dessus_du_seuil |

### 1.c Valeurs limites et boucle de `total_panier`

| Élément | Valeurs testées | Résultats attendus | Tests |
|---|---|---|---|
| Quantité (bornes 1 et 24) | 0, 1, 24, 25, -1 | ValueError ; 2,0 ; 48,0 ; ValueError ; ValueError | test_total_quantite_zero_leve_valueerror, test_total_quantite_un_acceptee, test_total_quantite_vingt_quatre_acceptee, test_total_quantite_vingt_cinq_leve_valueerror, test_total_quantite_negative_leve_valueerror |
| Prix (strictement positif) | -1, 0, 0,001 | ValueError ; ValueError ; 0,001 | test_total_prix_negatif_leve_valueerror, test_total_prix_zero_leve_valueerror, test_total_prix_minimal_un_millime_accepte |
| Nombre de lignes (boucle) | 0, 1, 2 | 0 ; 10,0 ; 13,6 | test_total_liste_vide_donne_zero, test_total_une_ligne_quantite_superieure_a_un, test_total_deux_lignes_exemple_specification |
| Ligne invalide parmi plusieurs | [(2,1), (3,25)] | ValueError | test_total_ligne_invalide_parmi_plusieurs_leve_valueerror |

## Tâche 2 — Table de décision de `remise`

Conditions : C1 = adhérent ; C2 = total ≥ 80 DT ; C3 = code promo valide.

### 2.a Table complète (8 colonnes)

| | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| C1 adhérent | O | O | O | O | N | N | N | N |
| C2 total ≥ 80 DT | O | O | N | N | O | O | N | N |
| C3 code valide | O | N | O | N | O | N | O | N |
| Remise adhérent (15 %) | oui | oui | non | non | non | non | non | non |
| Remise code (3 DT) | oui | non | oui | non | oui | non | oui | non |

### 2.b Table simplifiée et tests

Quand C1 = N, C2 ne change rien (les colonnes 5/7 et 6/8 donnent le même résultat), on les
fusionne : 8 colonnes deviennent 6.

| Colonne | C1 | C2 | C3 | Données de test | Remise attendue | Test |
|---|---|---|---|---|---|---|
| A (1) | O | O | O | remise(100, True, "SOLDES3") | 15 + 3 = 18,0 | test_remise_adherent_seuil_atteint_avec_code |
| B (2) | O | O | N | remise(100, True) | 15,0 | test_remise_adherent_seuil_atteint_sans_code |
| C (3) | O | N | O | remise(50, True, "SOLDES3") | 3,0 | test_remise_adherent_sous_seuil_avec_code |
| D (4) | O | N | N | remise(50, True) | 0 | test_remise_adherent_sous_seuil_sans_code |
| E (5, 7) | N | – | O | remise(100, False, "SOLDES3") | 3,0 | test_remise_non_adherent_avec_code |
| F (6, 8) | N | – | N | remise(100, False) | 0 | test_remise_non_adherent_sans_code |

Tests complémentaires : exemple de la spécification `remise(130, True)` = 19,5
(test_remise_exemple_specification) ; seuil inclus `remise(80, True)` = 12,0
(test_remise_adherent_au_seuil_80_inclus) ; juste sous le seuil `remise(79.999, True)` = 0
(test_remise_adherent_juste_sous_le_seuil) ; codes invalides "soldes3", "SOLDES4", "" et
`None` → 0 (quatre tests test_remise_code_...).

Test de la règle du plafond : `remise(2, False, "SOLDES3")` doit donner 2,0 (la remise de
3 DT est ramenée au total) → test_remise_plafonnee_au_total. Variantes :
`remise(0, False, "SOLDES3")` = 0 (test_remise_plafonnee_total_zero) et
`remise(3, False, "SOLDES3")` = 3,0, cas où remise = total, qui ne doit pas changer
(test_remise_egale_au_total_non_modifiee).

## Tâche 3 — Couverture des branches

| Mesure | Couverture des branches | Branches non couvertes |
|---|---|---|
| Avec les 2 tests de départ | 58 % (12 lignes non exécutées, 6 branches partielles) | lignes 23, 25, 32-37, 43, 45, 47, 50 |
| Avec votre suite finale | 100 % (18 branches sur 18) | aucune |

Sortie de `python -m pytest --cov=panier --cov-branch --cov-report=term-missing` pour la suite
finale :

```
Name        Stmts   Miss Branch BrPart  Cover   Missing
-------------------------------------------------------
panier.py      35      0     18      0   100%
-------------------------------------------------------
TOTAL          35      0     18      0   100%
======================== 4 failed, 41 passed in 0.18s =========================
```

Explication des branches non couvertes : il n'y en a plus. Les 4 tests en échec
s'exécutent quand même, donc ils comptent dans la couverture. Attention : 100 % de couverture
ne veut pas dire « code sans défaut ». Les deux défauts trouvés étaient dans des lignes
déjà couvertes. Ce sont les valeurs de test choisies (seuil exact, plafond) qui les
révèlent.

## Tâche 4 — Mutants

Commande : `python verifier_mutants.py`.

| Mutant | Résultat avec votre suite | Test qui le tue | Si survivant : test ajouté, ou pourquoi il est équivalent |
|---|---|---|---|
| mutant_1 | tué | test_total_deux_lignes_exemple_specification (et 5 autres) | – |
| mutant_2 | tué | test_total_prix_zero_leve_valueerror | – |
| mutant_3 | tué | test_remise_exemple_specification (et 2 autres) | – |
| mutant_4 | tué | test_remise_adherent_au_seuil_80_inclus (et 5 autres) | – |
| mutant_5 | tué | test_remise_adherent_seuil_atteint_avec_code (et 3 autres) | – |
| mutant_6 | tué | test_frais_total_zero_accepte_et_payant, test_frais_total_zero_interieur_payant | – |
| mutant_7 | tué | test_frais_grand_tunis (et 12 autres) | – |
| mutant_8 | **survivant** | aucun | **Équivalent.** Le mutant supprime `code_promo is not None and`. Si `code_promo` vaut `None`, la comparaison `None == "SOLDES3"` donne `False`, donc le résultat est identique à l'original pour toute entrée. Aucun test ne peut le tuer. |

Score de mutation final : 7 / 7 (en excluant le mutant équivalent mutant_8). Score brut : 7 / 8.

## Tâche 5 — Défauts

### Défaut 1

| Champ | Contenu |
|---|---|
| Titre | La livraison n'est pas gratuite quand le total vaut exactement 50 DT |
| Fonction | `frais_livraison` (ligne 46 de `panier.py`) |
| Étapes pour reproduire (appel exact) | `frais_livraison(50, "GRAND_TUNIS")` (idem avec `"INTERIEUR"`) |
| Résultat attendu (selon la spécification) | 0 DT : la livraison est gratuite si le total atteint 50 DT, seuil inclus (§3) |
| Résultat obtenu | 6,0 (Grand Tunis) ou 9,0 (Intérieur) |
| Sévérité (bloquante, majeure, mineure) | Majeure : le client paie des frais qu'il ne doit pas, pile au seuil |
| Priorité (haute, moyenne, basse) | Haute : correction d'un seul caractère (`>` devient `>=`) |
| Technique qui l'a révélé | Analyse des valeurs limites à 2 valeurs (49,999 et 50) |
| Test qui le révèle | test_frais_gratuits_au_seuil, test_frais_gratuits_au_seuil_interieur |

### Défaut 2

| Champ | Contenu |
|---|---|
| Titre | La remise n'est pas plafonnée au total |
| Fonction | `remise` (lignes 32 à 37 de `panier.py` : le plafond est absent) |
| Étapes pour reproduire (appel exact) | `remise(2, False, "SOLDES3")` |
| Résultat attendu (selon la spécification) | 2,0 DT : la remise ne peut jamais dépasser le total, elle est ramenée au montant du total (§2) |
| Résultat obtenu | 3,0 DT : la remise est supérieure au total |
| Sévérité (bloquante, majeure, mineure) | Majeure : le montant à payer peut devenir négatif |
| Priorité (haute, moyenne, basse) | Haute : règle métier qui protège le chiffre d'affaires |
| Technique qui l'a révélé | Table de décision, puis test dédié de la règle du plafond |
| Test qui le révèle | test_remise_plafonnee_au_total, test_remise_plafonnee_total_zero |

## Tâche 5 — Journal d'usage de l'IA

Outil utilisé : Claude Code (assistant IA en ligne de commande).

| N° | Outil | Ce que vous avez demandé | Ce que l'IA a produit (résumé) | Ce que vous avez gardé, corrigé ou rejeté, et pourquoi |
|---|---|---|---|---|
| 1 | Claude Code | Lire et analyser tout le dossier du projet | Résumé du sujet, repérage de 2 défauts probables en comparant `panier.py` à la spécification, hypothèse que mutant_8 est équivalent | Gardé comme point de départ. Nous avons relu nous-mêmes la spécification et le code (lignes 33-37 et 46) avant de l'accepter. |
| 2 | Claude Code | Écrire la suite de tests (partitions, limites, table de décision, plafond) | 45 tests dont les résultats attendus viennent de la spécification | Gardé après relecture test par test. Nous avons vérifié que chaque valeur attendue se déduit de la spécification et non d'une exécution de `panier.py`. |
| 3 | Claude Code | Mesurer la couverture et exécuter les mutants, puis rédiger le rapport | Couverture 58 % → 100 %, 7 mutants tués sur 8, tableaux du rapport | Gardé. Chiffres recopiés des sorties réelles de pytest et de `verifier_mutants.py`. |

Erreur de l'IA détectée (au moins une) : [À COMPLÉTER PAR LE GROUPE — décrivez une erreur
réelle que vous avez repérée dans une réponse de l'IA et comment vous l'avez corrigée. Ne pas
inventer : l'enseignant peut poser la question à la soutenance.]
