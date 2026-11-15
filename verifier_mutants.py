#!/usr/bin/env python3
"""Exécute votre suite de tests sur chacun des mutants du dossier mutants/.

Usage (depuis la racine du projet) :   python verifier_mutants.py

Un mutant est TUÉ si au moins un test qui réussit sur panier.py échoue sur le mutant.
Les tests qui échouent déjà sur panier.py (ils révèlent un défaut) ne comptent pas.
"""

import os, shutil, subprocess, sys, tempfile
import xml.etree.ElementTree as ET

PYTEST_INI = "[pytest]\npythonpath = .\ntestpaths = tests\n"


def executer(tests_dir, module_path, timeout=120):
    """Exécute les tests de tests_dir sur le module donné (copié sous le nom panier.py).
    Renvoie (resultats, message) ; resultats = {nom_du_test: 'ok' | 'echec'}."""
    tmp = tempfile.mkdtemp(prefix="sqt_")
    try:
        shutil.copytree(tests_dir, os.path.join(tmp, "tests"),
                        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        shutil.copy(module_path, os.path.join(tmp, "panier.py"))
        with open(os.path.join(tmp, "pytest.ini"), "w", encoding="utf-8") as f:
            f.write(PYTEST_INI)
        rapport = os.path.join(tmp, "resultats.xml")
        cmd = [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider",
               "--runxfail", "--junitxml=" + rapport]
        try:
            proc = subprocess.run(cmd, cwd=tmp, capture_output=True, text=True,
                                  timeout=timeout)
        except subprocess.TimeoutExpired:
            return None, "délai dépassé"
        if not os.path.exists(rapport):
            return None, (proc.stdout + proc.stderr)[-1500:]
        resultats = {}
        for cas in ET.parse(rapport).getroot().iter("testcase"):
            nom = cas.get("classname", "") + "::" + cas.get("name", "")
            if cas.find("failure") is not None or cas.find("error") is not None:
                resultats[nom] = "echec"
            elif cas.find("skipped") is not None:
                resultats[nom] = "ignore"
            else:
                resultats[nom] = "ok"
        if not resultats:
            return None, (proc.stdout + proc.stderr)[-1500:]
        return resultats, ""
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def court(nom):
    return nom.split("::")[-1]


def main():
    racine = os.path.dirname(os.path.abspath(__file__))
    tests = os.path.join(racine, "tests")
    original, msg = executer(tests, os.path.join(racine, "panier.py"))
    if original is None:
        print("Impossible d'exécuter les tests sur panier.py :\n" + msg)
        sys.exit(1)
    valides = {n for n, r in original.items() if r == "ok"}
    echecs = sorted(n for n, r in original.items() if r == "echec")
    print(f"Tests sur panier.py : {len(valides)} réussis, {len(echecs)} en échec")
    for n in echecs:
        print(f"   en échec (défaut révélé ?) : {court(n)}")
    print()
    dossier = os.path.join(racine, "mutants")
    fichiers = sorted((f for f in os.listdir(dossier) if f.startswith("mutant_")
                       and f.endswith(".py")), key=lambda f: int(f[7:-3]))
    tues = 0
    for f in fichiers:
        res, msg = executer(tests, os.path.join(dossier, f))
        if res is None:
            print(f"{f:<14} ERREUR : {msg.strip()[:200]}")
            continue
        tueurs = sorted(court(n) for n in valides if res.get(n) == "echec")
        if tueurs:
            tues += 1
            print(f"{f:<14} TUÉ par {', '.join(tueurs[:3])}"
                  + (f" (+{len(tueurs) - 3})" if len(tueurs) > 3 else ""))
        else:
            print(f"{f:<14} SURVIVANT")
    print(f"\nMutants tués : {tues} / {len(fichiers)}")


if __name__ == "__main__":
    main()
