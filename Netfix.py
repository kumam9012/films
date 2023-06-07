import dico as dico
from mysql import connector


def get_films(conn, curs):

    mysql_query ="""
                SELECT *
                FROM Films
                """
    curs.execute(mysql_query)
    films = curs.fetchall()

    resultat = {}

    resultat["data"] = []

    for film in films:
        dico = {}
        dico["Titre_film"]=  film[-5]
        dico["Durée_film"] = film[-4]
        dico["Année_film"] = film[-3]
        dico["Genres_film"] = film[-2]
        dico["Nom_réalisateur"] = film[-1]

        resultat["data"].append(dico)

    return resultat

def get_series(conn, curs):
    mysql_query = """
                    SELECT *
                    FROM Series
                    """


    curs.execute(mysql_query)
    séries = curs.fetchall()

    resultat = {}  # création du dictionnaire

    resultat["data"] = []

    for series in séries:
        dico={}
        dico = {}
        dico["Titre_séries"] = series[-4]
        dico["Durée_séries"] = series[-3]
        dico["Année_séries"] = series[-2]
        dico["Genres_séries"] = series[-1]

        resultat["data"].append(dico)

    return resultat

def get_films1(conn, curs, titre_film):
    mysql_query = """
        SELECT * FROM Films 
        WHERE Titre_film = %s
        """

    params = (titre_film,)
    curs.execute(mysql_query, params)
    films = curs.fetchall()

    resultat = {}

    resultat["data"] = []



    for film in films:
        dico = {}
        dico["Titre_film"] = film[0]
        dico["Durée_film"] = film[1]
        dico["Année_film"] = film[2]
        dico["Genres_film"] = film[3]
        dico["Nom_réalisateur"] = film[4]

        resultat["data"].append(dico)


    return resultat

def get_series1(conn, curs, titre_series):
    mysql_query = """
        SELECT * FROM Series 
        WHERE Titre_séries = %s
        """

    params = (titre_series,)

    curs.execute(mysql_query, params)
    series = curs.fetchall()

    resultat = {}

    resultat["data"] = []

    for serie in series:
        dico = {}
        dico["Titre_séries"] = serie[0]
        dico["Durée_séries"] = serie[1]
        dico["Année_séries"] = serie[2]
        dico["Genres_séries"] = serie[3]

        resultat["data"].append(dico)

    return resultat




def get_acteur(conn, curs, nomActeur):
    mysql_query = """
        SELECT * FROM Acteur 
        WHERE Nom_Acteur = %s
        """

    params = (nomActeur,)

    curs.execute(mysql_query, params)
    acteurs = curs.fetchall()

    resultat = {}

    resultat["data"] = []

    for acteur in acteurs:
        dico = {}
        dico["Nom_Acteur"] = acteur[0]
        dico["film_joué"] = acteur[1]
        dico["Date_de_naissance_acteur"] = acteur[2]

        resultat["data"].append(dico)

    return resultat




def get_realisateur(conn, curs, nomRealisateur):
    mysql_query = """
        SELECT * FROM Réalisateur 
        WHERE Nom_réalisateur = %s
        """

    params = (nomRealisateur,)

    curs.execute(mysql_query, params)
    realisateurs = curs.fetchall()

    resultat = {}

    resultat["data"] = []

    for realisateur in realisateurs:
        dico = {}
        dico["Nom_réalisateur"] = realisateur[0]
        dico["Film_connu"] = realisateur[1]
        dico["Date_de_naissance_réalisateur"] = realisateur[2]

        resultat["data"].append(dico)

    return resultat

def getgenresfilm(conn, curs, Genresfilm): #
    mysql_query = """
                        SELECT * FROM Films WHERE Genres_film LIKE CONCAT('%', %s, '%') 
                          """
    #print(mysql_query)
    curs.execute(mysql_query, (Genresfilm,))
    print(mysql_query)
    Genresfilms = curs.fetchall()
    resultat = {}
    resultat["data"] = []

    for genres_film in Genresfilms:
        dico = {}
        dico["Genresfilm"] = {}
        dico["Genresfilm"]["Titre_film"] = genres_film[0]
        dico["Genresfilm"]["Durée_film"] = genres_film[1]
        dico["Genresfilm"]["Année_film"] = genres_film[2]
        dico["Genresfilm"]["Nom_réalisateur"] = genres_film[3]


        resultat["data"].append(dico)

    return resultat

def getgenresseries(conn, curs, Genresseries): #
    mysql_query = """
                        SELECT * FROM Series WHERE Genres_séries LIKE CONCAT('%', %s, '%') 
                          """
    #print(mysql_query)
    curs.execute(mysql_query, (Genresseries,))
    Genresseries = curs.fetchall()
    resultat = {}
    resultat["data"] = []

    for genres_serie in Genresseries:
        dico = {}
        dico["Genresseries"] = {}
        dico["Genresseries"]["Titre_séries"] = genres_serie[0]
        dico["Genresseries"]["Durée_séries"] = genres_serie[1]
        dico["Genresseries"]["Année_séries"] = genres_serie[2]

        resultat["data"].append(dico)

    return resultat





#print(get_films(connection, cursor))

def films_actor(conn, curs, Acteur):
    mysql_query = """
                    SELECT a.Nom_Acteur, f.Titre,  f.Année
                    FROM Acteur a
                    INNER JOIN Films f ON a.film_joué = f.Titre;
                    AND Acteur.Nom_Acteur = %s
                      """
    curs.execute(mysql_query,(Acteur))
    Acteur = curs.fetchall()
    resultat={}
    resultat["Acteur"] = []

    for films_actor in Acteur:
        dico = {}
        dico["Acteur"] = {}
        dico["Acteur"]["Nom_Acteur"] = films_actor[0]
        dico["Acteur"]["film_joué"] = films_actor[1]
        dico["Acteur"]["Date_de_naissance_acteur"] = films_actor[2]

        resultat["Acteur"].append(dico)

    return resultat

def series_actor(conn, curs, Acteur):
    mysql_query = """
                    SELECT a.Nom_Acteur, s.Titre,  s.Année
                    FROM Acteur a
                    INNER JOIN Series s ON a.film_joué = s.Titre;
                    AND Acteur.Nom_Acteur = %s
                      """
    curs.execute(mysql_query,(Acteur))
    Acteur = curs.fetchall()
    resultat={}
    resultat["Acteur"] = []

    for series_actor in Acteur:
        dico = {}
        dico["Acteur"] = {}
        dico["Acteur"]["Nom_Acteur"] = series_actor[0]
        dico["Acteur"]["film_joué"] = series_actor[1]
        dico["Acteur"]["Date_de_naissance_acteur"] = series_actor[2]

        resultat["Acteur"].append(dico)

    return resultat

def films_réalisateur(conn, curs, Realisateurs):
    mysql_query = """
                    SELECT a.Nom_réalisateur, f.Titre,  f.Année
                    FROM Réalisateur r
                    INNER JOIN Films f ON r.film_connu = f.Titre;
                    AND Réalisateur.Nom_réalisateur = %s
                      """
    curs.execute(mysql_query,(Realisateurs))
    Realisateurs = curs.fetchall()
    resultat={}
    resultat["Réalisateur"] = []

    for films_réalisateur in Realisateurs:
        dico = {}
        dico["Réalisateur"] = {}
        dico["Réalisateur"]["Nom_réalisateur"] = films_réalisateur[0]
        dico["Réalisateur"]["film_connu"] = films_réalisateur[1]
        dico["Réalisateur"]["Date_de_naissance_réalisateur"] = films_réalisateur[2]

        resultat["Réalisateur"].append(dico)

    return resultat








