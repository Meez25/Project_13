Procédure de déploiement et gestion
===================================

Prérequis
---------

- Assurez-vous que toutes les dépendances du projet sont installées.
- Vérifiez que les variables d'environnement nécessaires sont correctement configurées.

Déploiement Automatique via GitHub Actions
------------------------------------------

1. **Déclenchement**
   - Le déploiement est déclenché automatiquement lorsqu'un changement est apporté à la branche ``master``.

2. **Conteneurisation et Docker Hub**
   - GitHub Actions construit une image Docker et la pousse sur Docker Hub.

3. **Déploiement sur Render**
   - Une fois l'image créée et stockée sur Docker Hub, une commande est envoyée à Render pour récupérer cette nouvelle image et déployer l'application.

Monitoring et Gestion
----------------------

- Le suivi des erreurs et des performances se fait via l'application Sentry.

Rollback
--------

- En cas de problème avec le nouveau déploiement, un rollback peut être effectué via Render pour revenir à la version précédente de l'application.

Mise à jour de la documentation
-------------------------------

- N'oubliez pas de mettre à jour la documentation technique et utilisateur en cas d'ajout ou de modification des fonctionnalités.
