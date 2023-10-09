# Documentation 

https://project-13.readthedocs.io/fr/latest/

## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/Meez25/Project_13.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


### Déploiement

#### Vue d'ensemble de haut niveau

Le processus de déploiement est automatisé via GitHub Actions, qui exécute diverses tâches pour construire, tester et déployer l'application. L'application est conteneurisée avec Docker, et l'image est poussée vers Docker Hub. Le pipeline exécute des contrôles de lint et des tests avant de passer à la construction et au push de l'image Docker.

#### Configuration requise

Pour activer le pipeline CI/CD, vous devez configurer quelques secrets GitHub pour stocker des informations sensibles telles que les identifiants Docker Hub et les clés secrètes de l'application. Voici les secrets nécessaires :

- **DOCKER_HUB_USERNAME**: Votre nom d'utilisateur Docker Hub.
- **DOCKER_HUB_PASSWORD**: Votre mot de passe Docker Hub.
- **SECRET_KEY**: La clé secrète de votre application Django.
- **SENTRY_URL**: L'URL Sentry pour le suivi des erreurs (facultatif).

#### Étapes de déploiement

Suivez ces étapes pour déployer l'application :

1. **Configurer les Secrets GitHub**: Accédez à votre dépôt sur GitHub, cliquez sur `Paramètres` -> `Secrets` et ajoutez les secrets mentionnés dans la section "Configuration requise".
  
2. **Fusionner vers Master**: Tout code fusionné dans la branche master déclenchera le pipeline GitHub Actions.

3. **Surveiller GitHub Actions**: Naviguez vers l'onglet `Actions` sur GitHub pour surveiller la progression des tâches.

4. **Exécuter localement**: Après que l'image Docker est construite avec succès et poussée sur Docker Hub, vous pouvez la récupérer pour l'exécuter localement avec ces commandes (remplacez `GITHUB_SHA` par la valeur SHA réelle) :

    ```bash
    docker pull meez25/lettings:GITHUB_SHA
    docker run -p 8000:8000 meez25/lettings:GITHUB_SHA
    ```

Votre successeur devrait être capable de suivre ces instructions pour déployer avec succès l'application sans aucun problème.
