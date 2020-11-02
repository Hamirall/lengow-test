# Requirements

- Python
- Django


# Installation

```bash
git clone git@github.com:Hamirall/lengow-test.git
```

```bash
cd lengow-test\lengow
```
Créer la base de donnée
```bash
python manage.py makemigrations
```

Commande d'importation des données (http://test.lengow.io/orders-test.xml)
```bash
python manage.py import
```

Démarre le serveur web
```bash
python manage.py runsever
```

Url de départ: http://127.0.0.1:8000/orders/list

# Test
- :heavy_check_mark: Créer un projet Django
- :heavy_check_mark: Créer une app "orders".
- :heavy_check_mark: Créer un modèle "Order" reflétant les données présentent dans l'API: http://test.lengow.io/orders-test.xml Vous n'êtes pas obligé de gérer tout les champs, 4-5 champs suffisent.
- :heavy_check_mark: Dans cette app créer une commande Django permettant de récupérer les commandes de l'API suivante et de les enregistrer en utilisant le modèle que vous venez de créer.
- :heavy_check_mark: Créer les vues nécessaires pour lister les commandes, lister 1 commande et rechercher selon les champs du modèle et afficher les résultats.

Pour aller plus loin

- :heavy_check_mark: Ajouter/modifier une commande
- Utiliser Django Rest Framework pour mettre à disposition les commandes précédemment enregistrées en base de données via une API


