# Tests

Les tests utilisent `unittest`, inclus dans la bibliothèque standard de
Python. Depuis la racine du dépôt, avec les dépendances du projet installées,
lancez la suite complète avec :

```powershell
python -m unittest discover -s tests -v
```

## Exécution ciblée

Pour lancer seulement un fichier de tests, indiquez son nom avec `-p` :

```powershell
python -m unittest discover -s tests -p "test_operators.py" -v
```

Pour lancer un seul test, ajoutez `-k` avec le nom de la méthode de test :

```powershell
python -m unittest discover -s tests -p "test_operators.py" -k "test_add_returns_sum" -v
```

Remplacez le nom de fichier ou de méthode pour cibler un autre test.

## Couverture

- `test_operators.py` vérifie les résultats des quatre opérations et le cas
  d'une division par zéro.
- `test_calculator.py` vérifie l'analyse des expressions, le traitement des
  espaces, le rejet d'expressions invalides et les réponses HTTP GET et POST
  de l'application Flask.
