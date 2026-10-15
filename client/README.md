# Module client

## Raison d'être

Le répertoire `client` contient l'interface utilisateur de la calculatrice.
Il présente l'affichage, les boutons et la mise en page permettant à
l'utilisateur de construire une expression, de l'envoyer au serveur et de
voir le résultat retourné.

Le client ne réalise pas lui-même les calculs. Il s'appuie sur la route Flask
du module `server` pour traiter l'expression soumise.

## Fichiers principaux

| Fichier | Responsabilité |
| --- | --- |
| `index.html` | Définit la page de la calculatrice, le formulaire `POST` envoyé à la route `/`, les boutons et les fonctions JavaScript de saisie et d'effacement. |
| `style.css` | Définit la présentation visuelle : disposition, couleurs, dimensions, boutons et états d'interaction. |

## Dépendances et hypothèses

- L'interface est prévue pour être rendue par Flask/Jinja, et utilise
  `url_for('static', filename='style.css')` pour charger la feuille de style.
- Un navigateur Web moderne avec prise en charge de JavaScript est requis
  pour les boutons de saisie et d'effacement.
- Le formulaire est soumis à la route `/` du serveur avec la méthode `POST`.
- Le champ de formulaire nommé `display` est l'interface entre le client et
  la fonction de calcul du serveur.
- Le serveur doit être lancé depuis la racine du projet et doit conserver la
  structure actuelle : `client` et `server` sont deux répertoires frères.

## Flux d'une opération

1. L'utilisateur sélectionne des chiffres et un opérateur dans `index.html`.
2. Le JavaScript ajoute les valeurs sélectionnées au champ `display`.
3. Le bouton `=` soumet le formulaire au serveur avec une requête `POST`.
4. Flask évalue l'expression et rend de nouveau `index.html` avec le résultat.
5. La valeur retournée par le serveur est affichée dans le champ `display`.
