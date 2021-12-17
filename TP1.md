-- ENTRAINEMENT 1
-- SELECT idA,nom,prenom,nationalite FROM acteur
-- SELECT idF,titre,annee,nbSpectateurs,idRealisateur,idGenre FROM film
-- SELECT idG,description FROM genre
-- SELECT idActeur,idFilm,salaire FROM jouer
-- SELECT idR, nom, prenom, nationalite FROM realisateur

--ENTRAINEMENT 3
--SELECT titre, annee FROM film
--WHERE annee >= 2004
--ORDER BY annee

--ENTR 4
--SELECT nom, prenom FROM acteur
--WHERE nationalite="France" AND nom LIKE "d%"

--ENTR 5
--SELECT nom, prenom, nationalite FROM acteur
--WHERE nationalite ="France" or nationalite="Belgique" AND prenom LIKE "%e%"

--ENTR 6
--SELECT DISTINCT nationalite FROM realisateur

--ENTR 7
--SELECT AVG(salaire) FROM jouer ;

--ENTR 8
--UPDATE realisateur SET nom="Scorsese" WHERE idR=16;
--SELECT nom, prenom, nationalite FROM realisateur

--ENTR 9
--SELECT titre FROM film
--WHERE idRealisateur = 16

--ENTR 10
--SELECT titre FROM film
--WHERE idGenre = 2

--ENTR 11
--SELECT titre,annee FROM film
--WHERE idGenre = 4
--ORDER BY annee

--ENTR 12
--SELECT titre FROM film
--JOIN jouer ON jouer.idFilm=film.idF
--JOIN acteur ON jouer.idActeur=acteur.idA
--WHERE acteur.nom = "Dujardin" 

--ENTR 13
--SELECT acteur.nom,salaire,film.titre FROM jouer
--JOIN acteur ON jouer.idActeur=acteur.idA
--JOIN film ON jouer.idFilm=film.idF
--ORDER by salaire DESC

--ENTR 14
--SELECT nom, prenom FROM realisateur
--JOIN film ON film.idRealisateur=realisateur.idR
--WHERE film.titre = "Bienvenus chez les ch'tis"

--ENTR 15
--SELECT description FROM genre
--JOIN film ON film.idGenre=genre.idG
--WHERE film.titre = "La mome"

--ENTR 16
--SELECT count(*) FROM film
--JOIN realisateur ON film.idRealisateur=realisateur.idR
--WHERE realisateur.nom = "Canet"
