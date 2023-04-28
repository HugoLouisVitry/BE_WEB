from flask import Flask, render_template, request, session

app=Flask(__name__)
app.template_folder = "template"
app.static_folder = "static"
app.config.from_object('App_financement.config')

#page accueil
@app.route("/")
def index():
    # déclaration des variables de sessions
    session["idUser"]=2
    session["prenom"]="Louis"
    session["nom"]="Blériot"
    session["mail"]="louis.bleriot@enac.fr"
    session["avatar"]="8.png"
    print(session) # affichage des sessions dans le terminal
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