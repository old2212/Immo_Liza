# Deuxième README car je touche rien à git

## Explications par rapport à get_data_01.py
* Extracte toutes les URLs des 2 premières pages de recherche Immoweb.
* Extracte toutes les données sur chaque page, à partir des URLs extraites, les retourne dans une liste de dictionnaires (1 dico par page). 

> **PROBLEMES** : Vitesse beaucoup trop lente => besoin d'optimiser la vitesse en consultant le fichier "Faster Requests" (dans 05.Scraping) ou le dossier "06. Concurrency". J'ai essayé d'améliorer la vitesse avec **ThreadPoolExecutor**, mais ça plante, à mon avis les .get ou .find_elements se lancent avant que la page soit chargée, DONC besoin de quelqu'un qui se renseigne sur les commandes **Wait** avant nos requetes. Aussi, chercher pour remplacer les **.get()** par des **Sessions()**, ça pourrait accelérer le processus.

* Quand on aura réglé le problème de la vitesse, viendra le problème du **CAPTCHA**

> Voir de la doc dessus.

* Ensuite viendra le moment de clean les données extraites pour prendre juste celles requises dans le Readme.

* Ensuite viendra la partie ou on utilisera panda ou csv pour faire un tableau excel. (Rapide et facile).

> HTTPX doit marcher avec Async. BeautifulSoup pas obligé (méthode alternative)

