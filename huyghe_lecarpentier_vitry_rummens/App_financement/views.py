from flask import Flask, render_template, session, request, redirect
from .model import bdd as bdd
from .controller import function as f
from werkzeug.utils import secure_filename
import pandas, os 
import random as rd
Upload_avatar_picture=os.path.dirname(__file__)+"/static/images/avatar" 
Upload_project_picture=os.path.dirname(__file__)+"/static/images/projectsPictures"


app = Flask(__name__)
app.template_folder = "template"
app.static_folder = "static"
app.config.from_object('App_financement.config')

# page accueil


@app.route("/")
def index():

    params = f.messageInfo(None)
    liste_projets = bdd.get_project_index()
    params = {'liste': liste_projets}

    return render_template("index.html", title="Accueil", **params)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/login")
def login():
    params = f.messageInfo(None)
    return render_template("login.html", **params)


@app.route("/signin")
def signin():
    params = f.messageInfo(None)
    return render_template("signin.html", **params)


@app.route("/pricing")
def pricing():
    return render_template("pricing.html")


@app.route("/visual")
def visual():
    return render_template("visual_test.html")


@app.route("/community")
def community():
    Projets = bdd.get_projectData()
    params = {'liste': Projets}
    params = f.messageInfo(params)
    return render_template("community.html", **params)


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
    avatar = request.files['avatar']
    nom_avatar = secure_filename(avatar.filename)
    avatar.save(os.path.join(Upload_avatar_picture, nom_avatar))

    statut = 0
    bdd.add_membreData(nom, prenom, mail,
                       login, motPasse, nom_avatar, statut, )

    # dernier id créé par la BDD
    if "errorDB" not in session:
        session["infoVert"] = "Nouveau membre inséré"
        return redirect("/login")
    else:
        session["infoRouge"] = "Problème ajout utilisateur"
        return redirect("/signin")


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
        session["isAdmin"] = user["isAdmin"]
        session["infoVert"] = "Authentification réussie"
        session["login"] = login
        session["password"] = f.chiffrement_mdp(mdp)
        session["avatar"] = user["avatar"]
        session["solde"] = user["solde"]
        return redirect("/")
    except TypeError as err:
        # Authentification refusée

        session["infoRouge"] = "Authentification refusée"
        return redirect("/login")

@app.route("/update_solde",methods=['POST'])
def update_solde():
    add_solde=request.form["amount-astrocoins"]
    
    session["solde"]+=int(add_solde)
    bdd.update_solde(idUser=session["idUser"], newvalue=session["solde"])
    return redirect("/profil")

@app.route("/solde_pub",methods=['POST'])
def solde_pub():
    session["solde"]+=20
    bdd.update_solde(idUser=session["idUser"], newvalue=session["solde"])
    return redirect("/profil")
 

@app.route("/logout")
def logout():
    session.clear()
    session["infoBleu"] = "Merci de votre visite"
    return redirect("/login")

# page sgbd


@app.route("/sgbd")
def sgbd():
    listeMembres = bdd.get_membresData()
    params = {'liste': listeMembres}
    params = f.messageInfo(params)
    return render_template("sgbd.html", **params)


@app.route("/profil")
def profil():
    url_yt=choisir_pub()
    contribution_totale  = bdd.get_contribution_totale(session['idUser'])
    params ={'url':url_yt, 'contribution_totale':contribution_totale}
    params=f.messageInfo(params)
    return render_template("profil.html",**params) 


@app.route("/update_mdp", methods=['POST'])
def update_mdp():

    # réception des données du formulaire
    crt_mdp = request.form['old_mdp']
    new_mdp = request.form['new_mdp']
    confirm_mdp = request.form['confirm_mdp']

    if f.chiffrement_mdp(crt_mdp) != session["password"]:
        session["infoRouge"] = "Votre ancien mot de passe est faux"
        return redirect("/profil")

    if new_mdp != confirm_mdp:
        session["infoRouge"] = "Les mots de passe ne correspondent pas"
        return redirect("/profil")
    try:
        MDP = f.chiffrement_mdp(new_mdp)
        bdd.update_mdp(idUser=session["idUser"], newvalue=MDP)
        session["password"] = MDP

        if "errorDB" not in session:
            session["infoVert"] = "Le mot de passe a été mis à jour"
        else:
            session["infoRouge"] = "Problème maj utilisateur"
    except:
        pass
    return redirect("/profil")

# suppression d'un membre
@app.route("/suppMembre/<idUser>")
def suppMembre(idUser=None):
    bdd.del_membreData(idUser)
    # la suppression a bien fonctionné
    if "errorDB" not in session:
        session["infoVert"] = "L'utilisateur a bien été supprimé"
    else:
        session["infoRouge"] = "Problème suppression utilisateur"
    return redirect("/sgbd")

# Mise à jour du nom et du statut d'un membre


@app.route("/updateMembre/<champ>", methods=['POST'])
def updateMembre(champ=None):
    # réception des données du formulaire
    idUser = request.form['pk']
    newvalue = request.form['value']
    if champ == "N":
        bdd.update_membreData("nom", idUser, newvalue)
    if champ == "S":
        bdd.update_membreData("statut", idUser, newvalue)
    return "1"

#Mise à jour du solde d'un membre
@app.route("/refillSolde")
def refillSolde(idUser=None):
    
    crt_solde=request.form('solde')
    
#choisir la pub
def choisir_pub():
    L=["https://www.youtube.com/watch?v=g8d4rvT29z8",
        "https://www.youtube.com/watch?v=-9XnWvnU8fk",
        "https://www.youtube.com/watch?v=2wYy-oaMPOA&t=5s",
        "https://www.youtube.com/watch?v=4M61pYUII5Y",
        "https://www.youtube.com/watch?v=Z9xLEmxp4ds",
        "https://www.youtube.com/watch?v=PtGQVWzkjsg",
        "https://www.youtube.com/watch?v=q30s32F27ko",
        "https://www.youtube.com/watch?v=Enm6pJUhiYg",
        "https://www.youtube.com/watch?v=yP3Ch0uwYtE",
        "https://www.youtube.com/watch?v=9Ky4-Kp-l5w",
        "https://www.youtube.com/watch?v=DonKn7Bbw-E",
        "https://www.youtube.com/watch?v=xdmCP_hfrCo",
        "https://www.youtube.com/watch?v=bAF5-XzBDvc",
        "https://www.youtube.com/watch?v=rSSONZHKSaM",
        "https://www.youtube.com/watch?v=9KQKJgr_fLI",
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        ]
    k = rd.randint(0,15)
    n=len(L[k])
    return L[k][0:n]

#page new-project
@app.route("/myProjects")
def myProjects():
    listeProjets = bdd.get_projectData()
    listeContribution = bdd.get_participate()
    params ={'liste':listeProjets, 'contribution':listeContribution}
    params = f.messageInfo(params)
    return render_template("myProjects.html", **params)


@app.route("/seeProject/<id>")
def seeProject(id=''):
    listeProjets = bdd.get_projectData()
    for i in range(len(listeProjets)):
        if listeProjets[i]['idProject'] == int(id):
            params = {'currentProject': listeProjets[i]}
            params = f.messageInfo(params)
    return render_template("seeProject.html", **params)


@app.route("/addProject", methods=['POST'])
def addProject():
    # réception des données du formulaire
    name = request.form['name']
    description = request.form['description']
    target = request.form['target']
    endDate = request.form['endDate']
    isOpen = 1
    idUser = session['idUser']
    picture = request.files['picture']
    if picture.filename:
        nom_picture = secure_filename(picture.filename)
        picture.save(os.path.join(Upload_project_picture, nom_picture))
    else:
        nom_picture = "default_picture.png"
    bdd.add_projectData(name, description, target, endDate,
                        isOpen, idUser, nom_picture)

    # dernier id créé par la BDD
    if "errorDB" not in session:
        session["infoVert"] = "Nouveau projet inséré"
        return redirect("/myProjects")
    else:
        session["infoRouge"] = "Problème ajout projet"
        return redirect("/myProjects")

# fermeture d'un projet


@app.route("/closeProject/<idProject>")
def closeProject(idProject=None):
    bdd.close_projectData(idProject)
    # la fermeture a bien fonctionné
    if "errorDB" not in session:
        session["infoVert"] = "Le projet a bien été fermé"
    else:
        session["infoRouge"] = "Problème fermeture projet"
    return redirect("/myProjects")

# Mise à jour du projet


@app.route("/updateProject/<champ>", methods=['POST'])
def updateProject(champ=None):
    # réception des données du formulaire
    idProject = request.form['pk']
    newvalue = request.form['value']
    if champ == "N":
        bdd.update_projectData("nom", idProject, newvalue)
    if champ == "S":
        bdd.update_membreData("statut", idProject, newvalue)
    return "1"

# Contribution financière au projet

@app.route("/participateProject/<id>")
def participate(id=''):
    listeProjets = bdd.get_projectData()
    users=bdd.get_membresData()

    for i in range(len(listeProjets)):
        if listeProjets[i]['idProject'] == int(id):
            params = {'currentProject': listeProjets[i]}
            for j in range(len(users)):
                if listeProjets[i]['idUser']==users[j]['idUser']:
                    params['projectUser']=users[j]

    params = f.messageInfo(params)

    return render_template("participateProject.html",**params)
    
 
@app.route("/tip/<id>", methods=['POST'])
def tip(id=''):
    money = int(request.form['paiement'])
    if money > session['solde'] : 
        session["infoRouge"] = "Votre solde est insufisant"
        return redirect("/participateProject/"+str(id))
    try:
        bdd.update_participation(int(id), int(session["idUser"]), money)
        session["infoVert"] = "Paiement réussi"
        return redirect("/myProjects")
    except:
        session["infoRouge"] = "Erreur Innatendue"
        return redirect("/participateProject/"+str(id))