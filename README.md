# Analyse-et-visualisation-des-donn-es-de-l-entreprise-Innova-Electronic
Ce dépôt Git contient le code source utilisé pour analyser les données de ventes mensuelles de l'entreprise Innova Electronic à l'aide de Python, notamment les bibliothèques NumPy, Pandas et Matplotlib. Voici les différentes étapes réalisées :

Importation des bibliothèques :
	Nous avons importé les bibliothèques nécessaires pour l'analyse des données : NumPy, Pandas et Matplotlib.

Chargement des données :
        Les données de ventes mensuelles ont été chargées à partir d'un fichier CSV à l'aide de la fonction pd.read_csv() de Pandas.

Exploration des données :
        Nous avons exploré les données pour comprendre leur structure et leur contenu. Nous avons utilisé des fonctions telles que data_vente.describe(), data_vente.info() et data_vente.isnull().sum() pour détecter d'éventuelles données manquantes ou aberrantes.

Calcul des ventes totales par mois :
        Nous avons calculé les ventes totales pour chaque mois en regroupant les données par mois et en summant les revenus correspondants.

Identification des 5 produits les plus vendus chaque mois :
        En regroupant les données par mois et par produit, nous avons déterminé les 5 produits les plus vendus chaque mois.

Création de graphiques :
        Nous avons utilisé Matplotlib pour créer des graphiques représentant les ventes mensuelles sous forme de barres, ainsi que les ventes des produits les plus populaires chaque mois.

Analyse des graphiques et conclusions :
        Nous avons analysé les tendances de vente mensuelles ainsi que les performances des produits pour tirer des conclusions et formuler des recommandations pour améliorer les performances de vente de l'entreprise.
