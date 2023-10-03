Installation
============

Cloner le repository
--------------------

- cd /path/to/put/project/in

  .. code-block:: bash

     cd /path/to/put/project/in

- git clone https://github.com/Meez25/Project_13.git

  .. code-block:: bash

     git clone https://github.com/Meez25/Project_13.git

Créer l'environnement virtuel
-----------------------------

- cd /path/to/Python-OC-Lettings-FR

  .. code-block:: bash

     cd /path/to/Python-OC-Lettings-FR

- python -m venv venv

  .. code-block:: bash

     python -m venv venv

- apt-get install python3-venv (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)

  .. code-block:: bash

     apt-get install python3-venv

- Activer l'environnement source venv/bin/activate

  .. code-block:: bash

     source venv/bin/activate

- Confirmer que la commande python exécute l'interpréteur Python dans l'environnement virtuel which python

  .. code-block:: bash

     which python

- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure python --version

  .. code-block:: bash

     python --version

- Confirmer que la commande pip exécute l'exécutable pip dans l'environnement virtuel, which pip

  .. code-block:: bash

     which pip

- Pour désactiver l'environnement, deactivate

  .. code-block:: bash

     deactivate

Exécuter le site
----------------

- cd /path/to/Python-OC-Lettings-FR

  .. code-block:: bash

     cd /path/to/Python-OC-Lettings-FR

- source venv/bin/activate

  .. code-block:: bash

     source venv/bin/activate

- pip install --requirement requirements.txt

  .. code-block:: bash

     pip install --requirement requirements.txt

- python manage.py runserver

  .. code-block:: bash

     python manage.py runserver

- Aller sur http://localhost:8000 dans un navigateur.

  .. code-block:: text

     http://localhost:8000

