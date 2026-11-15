"""Module Panier de l'application « Liste de Courses » (groupe 01).

Tous les montants sont en dinars tunisiens (DT), arrondis au millime.
Les règles sont décrites dans SPECIFICATION.md.
"""

SEUIL_REMISE = 80             # DT : remise adhérent à partir de ce total
TAUX_REMISE = 15              # pourcentage de la remise adhérent
CODE_PROMO = "SOLDES3"        # seul code promo valide
REMISE_CODE = 3               # DT de remise pour un code promo valide
SEUIL_LIVRAISON = 50          # DT : livraison gratuite à partir de ce total
FRAIS_GRAND_TUNIS = 6.000     # DT
FRAIS_INTERIEUR = 9.000       # DT
QUANTITE_MAX = 24             # quantité maximale d'un article par ligne
ZONES = ("GRAND_TUNIS", "INTERIEUR")


def total_panier(lignes):
    """Total d'une liste de lignes (prix_unitaire, quantite)."""
    total = 0.0
    for prix, quantite in lignes:
        if prix <= 0:
            raise ValueError("prix invalide")
        if quantite < 1 or quantite > QUANTITE_MAX:
            raise ValueError("quantité invalide")
        total += prix * quantite
    return round(total, 3)


def remise(total, adherent, code_promo=None):
    """Montant de la remise accordée sur un total."""
    montant = 0.0
    if adherent and total >= SEUIL_REMISE:
        montant += total * TAUX_REMISE / 100
    if code_promo is not None and code_promo == CODE_PROMO:
        montant += REMISE_CODE
    return round(montant, 3)


def frais_livraison(total, zone, premium=False):
    """Frais de livraison d'une commande (total après remise)."""
    if total < 0:
        raise ValueError("total invalide")
    if zone not in ZONES:
        raise ValueError("zone inconnue")
    if premium or total > SEUIL_LIVRAISON:
        return 0.0
    if zone == "GRAND_TUNIS":
        return FRAIS_GRAND_TUNIS
    return FRAIS_INTERIEUR
