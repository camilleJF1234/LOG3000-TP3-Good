# Module serveur

## Raison d'être

Le répertoire `server` contient le module applicatif de la calculatrice. Il
reçoit les requêtes HTTP de l'interface, valide et évalue les expressions
numériques soumises, puis rend la page du client avec le résultat ou un
message d'erreur.

Le serveur est également responsable de configurer Flask pour servir les
fichiers situés dans le répertoire `client`. Il constitue donc le point
d'entrée de l'application complète.

## Fichiers principaux

| Fichier | Responsabilité |
| --- | --- |
| `app.py` | Crée l'application Flask, configure les répertoires `client`, expose la route `/`, valide les expressions et appelle l'opération appropriée. |
| `operators.py` | Regroupe les fonctions arithmétiques utilisées par `app.py` : addition, soustraction, multiplication et division. |

## Dépendances et hypothèses

- Python 3 est requis.
- Flask est la seule dépendance externe directe; elle est déclarée dans le
  fichier `requirements.txt` à la racine du projet.
- L'application est lancée depuis la racine du projet avec
  `python -m server.app`. Le répertoire `server` est alors importable comme
  module Python.
- La route `/` accepte les requêtes `GET` et `POST`. Lors d'une requête
  `POST`, l'expression est lue dans le champ de formulaire `display`.
- Une expression doit contenir un seul opérateur parmi `+`, `-`, `*` et `/`,
  avec deux opérandes numériques.
- Le serveur suppose que le répertoire `client` se trouve au même niveau que
  `server`; cette relation est utilisée pour trouver `index.html` et
  `style.css`.

## Démarrage rapide

Depuis la racine du projet :

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m server.app
```

L'application est ensuite accessible à l'adresse `http://127.0.0.1:5000/`.