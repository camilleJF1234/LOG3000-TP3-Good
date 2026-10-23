# Calculatrice simple

## TP 3

Équipe: 11

Collaborateurs: Anne-Marie Laurendeau (2291027) et Camille Jean-François (2269899)

## Objectif:

Ce projet a pour objectif de fournir un site web d'une calcultrice simple. Les opérations possibles sont l'addition, la soustraction, la division et la multiplication. Le but de ce dépôt git est de fournir une même base de code documenté et sans bogues pour tous les professionnels de la startup pour qu'ils puisosent exécuter l'application avec succès.

## Prérequis d'installation

- Avoir Python 3 d'installer
- Avoir pip de Python d'installer 
- Installer les dépendances avec `pip install -r requirements.txt`

## Instructions d'installation

1) Créer un environnement virtuel avant d'installer les dépendances (le faire à la racine du projet)
   1) `python -m venv .venv`
   2) Sur windows: `.\.venv\Scripts\Activate.ps1`, Sur macOS ou linux: `source .venv/bin/activate`

2) Installer les dépendances du projet:
   `pip install -r requirements.txt`

## Lancer le projet
1) Ouvrir un terminal à la racine du projet
2) Activer l'environnement virtuel: `.\.venv\Scripts\Activate.ps1`
3) Lancer l'application: `python -m server.app`
4) Ouvrir l'adresse `http://127.0.0.1:5000` dans le navigateur

# Tests

Les tests utilisent `unittest`, inclus dans la bibliothèque standard de
Python. Depuis la racine du dépôt, avec les dépendances du projet installées,
lancez la suite complète avec :

```powershell
python -m unittest discover -s tests -v
```

## Flux du projet
- La branche main est la branche principale et fonctionnelle du projet
- Chaque nouvelle branche est reliée à un issue
- Un issue est numéroté et la branche doit contenir le numéro du issue
- Il existe plusieurs types de changements: `fix, test, refactor, feat,` 
- Le nommage de la branche se fait comme suit: `type_du_changement/numero_du_issue/titre`
- Pour Merge une branche sur la branche principale `main`, il faut faire un Pull Request (PR)
- Une autre personne que le contributeur de la branche doit faire la révision de la demande
- Chaque PR doit passer tous les tests avant de pouvoir la merge sur la branche principale
- Le correcteur de la PR doit tester en local en plus de réviser sur github. 
