# Spécification du module Panier — groupe 01

Application « Liste de Courses ». Le module `panier.py` calcule le total d'un panier, la
remise accordée au client et les frais de livraison. Tous les montants sont en dinars
tunisiens (DT) et arrondis au millime (3 décimales).

## 1. `total_panier(lignes)`

- `lignes` est une liste de couples `(prix_unitaire, quantite)`.
- Le prix unitaire doit être strictement positif ; sinon la fonction lève `ValueError`.
- La quantité est un entier compris entre **1 et 24** (bornes incluses) ; sinon la
  fonction lève `ValueError`.
- Résultat : la somme des prix unitaires multipliés par les quantités. Une liste vide
  donne un total de 0 DT.

## 2. `remise(total, adherent, code_promo=None)`

- `total` est un montant positif ou nul (le résultat de `total_panier`).
- Un **adhérent** dont le total atteint **80 DT** (seuil inclus) bénéficie d'une
  remise de **15 %** du total.
- Un **code promo valide** donne une remise de **3 DT**, à tout client, adhérent ou
  non. Le seul code valide est **`SOLDES3`**, écrit exactement ainsi (majuscules
  comprises). Un code absent (`None`) ou différent ne donne aucune remise.
- Les deux remises se cumulent.
- La remise ne peut **jamais dépasser le total** : si elle le dépasse, elle est ramenée au
  montant du total.

## 3. `frais_livraison(total, zone, premium=False)`

- `total` est le montant après remise. Un total négatif lève `ValueError`.
- `zone` vaut `"GRAND_TUNIS"` ou `"INTERIEUR"`. Toute autre zone lève `ValueError`, même
  pour un client Premium.
- La livraison est **gratuite** (0 DT) pour un client Premium, ou si le total atteint
  **50 DT** (seuil inclus).
- Sinon, les frais sont de **6,000 DT** dans le Grand Tunis et de
  **9,000 DT** à l'intérieur.

## Exemples

| Appel | Résultat |
|---|---|
| `total_panier([(2.5, 4), (1.2, 3)])` | 13,600 DT |
| `remise(130, True)` | 19,500 DT |
| `frais_livraison(25, "INTERIEUR")` | 9,000 DT |
