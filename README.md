## Remarque importante

Les liens de téléchargement dans le rapport sont de la version du 8 janvier alors qu'on a utilisé les datasets de décembre. 
Il est recommandé d'exécuter d'abord  les programmes 3,4 et 5 car le dataset_avec_details_financiers.parquet est de la bonne version (résultant
de la version de décembre) et ensuite lancer le code de nouv_dataset.ipynb et data_preparation.ipynb avec les versions du 8 janvier parce que cela peut affecter le fichier de dataset_avec_details_financiers.parquet. 

## Présentation des fichiers

1. nouv_dataset.ipynb : convertit le fichier des bilans financiers de csv vers parquet
2. data_preparation.ipynb : fait la mise en forme et la préparation du dataset final
3. models.ipynb : implémentation des modèles hors réseaux de neurones
4. reseau_dense.ipynb : implémentation des modèles de réseaux de neurones 
5. data_analyse.ipynb : analyse des données
6. utils.py : implémentation de fonctions utiles pour la préparation de données
