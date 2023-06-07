from flask import Flask, jsonify, render_template, request, redirect, url_for, session
from mysql import connector
from Netfix import *

app = Flask(__name__, static_folder='static')

app.secret_key = "secret_key"

# Connexion à la BD MySQL
connection = connector.connect(
    host="localhost",
    port=3306,
    user="root",        # user de la BD
    password="root",    # mot de passe de la BD
    database="Projet_Netfix"  # nom du schéma
)
# Création du curseur
cursor = connection.cursor()


@app.route('/', methods=['GET'])
def home():
    return render_template('search.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':

        return render_template('search.html')
    elif request.method == 'GET' and request.args.get('_method') == 'POST':

        return render_template('search.html')
    else:
        return render_template('search.html')

@app.route('/films', methods=['GET'])
def films_page():
    return render_template('films.html')


@app.route("/api/films", methods=['GET'])
def films():
    result = get_films(connection, cursor)
    return jsonify(result)

@app.route('/séries', methods=['GET'])
def series_page():
    return render_template('series.html')


@app.route("/api/séries", methods=['GET'])
def series():
    result = get_series(connection, cursor)
    return jsonify(result)


@app.route("/<film>/infos", methods=['GET'])
def filmRecherche(film):
    result = get_films1(connection, cursor, film)
    return jsonify(result)

@app.route("/<acteur>/actor", methods=['GET'])
def acteurRecherche(acteur):
    result = get_acteur(connection,cursor, acteur)
    return jsonify(result)

@app.route("/<serie>/watch", methods=['GET'])
def seriesRecherche(serie):
    result = get_series1(connection,cursor,serie)
    return jsonify(result)

@app.route("/<realisateur>/director", methods=['GET'])
def realisateurRecherche(realisateur,):
    result = get_realisateur(connection, cursor, realisateur)
    return jsonify(result)

@app.route("/<gfilm>/gfilms", methods=['GET'])
def genresfilmRecherche(gfilm):
    result = getgenresfilm(connection,cursor, gfilm)
    return jsonify(result)

@app.route("/<gserie>/gseries", methods=['GET'])
def genreseriesRecherche(gserie):
    result = getgenresseries(connection, cursor, gserie)
    return jsonify(result)


if __name__ == "__main__":
    app.run(port=8000, debug=True)


