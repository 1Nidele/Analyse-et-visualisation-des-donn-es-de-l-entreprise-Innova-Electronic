# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 11:46:53 2024

@author: DELL_E5580
"""

"""
    statistiques descriotive
"""

def statistique_desc(nom_liste):
    maximum = max(nom_liste)
    minimum = min(nom_liste)
    somme_liste = sum(nom_liste)
    moyenne = somme_liste / len (nom_liste)
    res = {
        "min": minimum,
        "max": maximum,
        "somme": somme_liste,
        "moyenne": moyenne
        } 
    return res

def somme_elt(liste_elt):
    """
    

    Parameters
    ----------
    liste_elt : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    return sum(liste_elt)