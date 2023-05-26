- **Programme nécessaire :**
  - *Clicker [ici](https://www.python.org/downloads/) pour installer Python*
  - *Clicker [ici](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) pour installer Postgres*
- **Instalation des packages Pyhton :**
  - *`pip install -r requirements.txt`*
- **Initialisation de la base de données :**
  - *Mettre le dossier `PostgreSQL\15\bin` dans le path pour utiliser la commande psql ([une aide si vous ne savez pas faire](https://www.malekal.com/comment-modifier-la-variable-path-sous-windows-10-11/),par defaut c'est :`C:\\PostgreSQL\15\bin`)*
  - *se connecter a la base de données en tant que postgres (`psql --username=postgres` a éxecuter dans un invite de commande(win + r et taper cmd))*
  - *`create user lexika password 'lexika';`*
  - *`create database lexika with owner lexika;`*
  - *Créer un fichier .env qui contient*
    ```ini
    HOST=localhost
    PORT=5432
    DATABASE=flask
    USER=flask
    PASSWORD=flask
    ```
  - *double clicker sur database.py*
- **Lancer le serveur :**
  - *double clicker sur server.py*
  - *aller a l'url http://localhost*