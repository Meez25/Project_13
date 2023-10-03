Base de donnée de modèles
=========================

Structure de la base de données
-------------------------------

La base de donnée contient 3 modèles: Adresse (Address), Locations (Letting), ainsi que Profile (Client).

Voici la liste des tables de la base de données :

.. code-block:: text

    auth_group
    auth_group_permissions
    auth_permission
    auth_user
    auth_user_groups
    auth_user_user_permissions
    django_admin_log
    django_content_type
    django_migrations
    django_session
    lettings_address
    lettings_letting
    profiles_profile

Modèles des données
-------------------

**Voici la table lettings_address :**

.. code-block:: text

    pragma table_info(lettings_address);
    0|id|INTEGER|1||1
    1|number|integer unsigned|1||0
    2|street|varchar(64)|1||0
    3|city|varchar(64)|1||0
    4|state|varchar(2)|1||0
    5|zip_code|integer unsigned|1||0
    6|country_iso_code|varchar(3)|1||0


**Voici la table lettings_letting :**

.. code-block:: text

    0|id|INTEGER|1||1
    1|title|varchar(256)|1||0
    2|address_id|INTEGER|1||0

**Voici la table profiles_profile :**

.. code-block:: text

    0|id|INTEGER|1||1
    1|favorite_city|varchar(64)|1||0
    2|user_id|INTEGER|1||0

Les autres tables sont utilisés par Django.
