from flask import Flask, render_template, session,request,redirect
from .model import bdd as bdd


app=Flask(__name__)
app.template_folder = "template"
app.static_folder = "static"
app.config.from_object('App_financement.config')

#page accueil
@app.route("/")
def index():
    return render_template("index.html",title="Acueil")

@app.route("/about")
def about():
    return render_template("about.html") 

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signin")
def signin():
    return render_template("signin.html")


@app.route("/pricing")
def pricing():
    return render_template("pricing.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/case-study")
def case_study():
    return render_template("case-study.html")

@app.route("/webmaster")
def webmaster():
    return render_template("webmaster.html")

@app.route("/addMembre", methods=['POST'])
def addMembre():
    # réception des données du formulaire
    nom = request.form['nom']
    prenom = request.form['prenom']
    mail = request.form['mail']
    login = request.form['login']
    motPasse = request.form['mdp']
    statut = request.form['statut']
    lastId = bdd.add_membreData(nom, prenom, mail,
    login, motPasse, statut)
    print(lastId) # dernier id créé par la BDD
    if "errorDB" not in session:
        session["infoVert"]="Nouveau membre inséré"
    else:
        session["infoRouge"]="Problème ajout utilisateur"
    return redirect("/sgbd")

# passe les messages d'info en paramètres
def messageInfo(params):
    if params is None:
        params = {}
    #messages d'infos du views.py
    if "infoVert" in session:
        params["infoVert"] = session['infoVert']
        session.pop("infoVert", None)
    if "infoRouge" in session:
        params["infoRouge"] = session['infoRouge']
        session.pop("infoRouge", None)
    if "infoBleu" in session:
        params["infoBleu"] = session['infoBleu']
        session.pop("infoBleu", None)
    #messages d'info du bdd.py
    if "errorDB" in session:
        params["errorDB"] = session['errorDB']
        session.pop("errorDB", None)
    if "successDB" in session:
        params["successDB"] = session['successDB']
        session.pop("successDB", None)
    return params

# authentification
@app.route("/connecter", methods=["POST"])
def connect():
    login = request.form['login']
    mdp = request.form['mdp']
    user = bdd.verifAuthData(login, mdp)
    try:
        # Authentification réussie
        session["idUser"] = user["idUser"]
        session["nom"] = user["nom"]
        session["prenom"] = user["prenom"]
        session["mail"] = user["mail"]
        session["statut"] = user["statut"]
        session["avatar"] = user["avatar"]
        session["infoVert"]="Authentification réussie"
        return redirect("/")
    except TypeError as err:
        # Authentification refusée
        session["infoRouge"]="Authentification refusée"
        return redirect("/login")