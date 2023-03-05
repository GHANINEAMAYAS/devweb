Introduction
Devweb est une application web qui permet de stocker et de visualiser des données de séquençage d'ARN. L'application est développée en Python avec le framework Flask et utilise une base de données MySQL pour stocker les données.  On a utilisé également la bibliothèque Chart.js pour générer des graphiques.

Installation
Installer Docker pour pouvoir utiliser les images nécessaires.
Cloner le repository Github de Devweb.
Installer les dépendances à partir du fichier requirements.txt en utilisant la commande pip install -r requirements.txt.
Configurer le fichier docker-compose.yml en indiquant les images Docker nécessaires et les ports pour chaque serveur.
Lancer l'application en utilisant la commande flask run.
Utilisation
Une fois l'application lancée, elle est accessible dans un navigateur web à l'adresse http://localhost:5000. Voici les principales fonctionnalités de l'application :

Recherche de données de séquençage d'ARN
La page d'accueil de l'application permet de rechercher des données de séquençage d'ARN en entrant un identifiant de séquence. Les résultats de recherche sont affichés dans un tableau, avec la possibilité de modifier,supprimer et ajouter une ligne dans la base de donnée.

Affichage de graphiques de données de séquençage d'ARN
La page de graphique permet d'afficher un graphique des données de séquençage d'ARN pour un identifiant de séquence donné.

Technologies utilisées


Docker pour faciliter l'installation et la configuration de l'application.
HTML5 et CSS3
Python 3 pour développer l'application web.
Flask pour créer l'application web.
SQLAlchemy pour interagir avec la base de données MySQL.
Chart.js pour générer des graphiques.


