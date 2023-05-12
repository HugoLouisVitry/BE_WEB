from flask import Flask, render_template, session,request,redirect
from .model import bdd as bdd
from .controller import function as f
from werkzeug.utils import secure_filename
import pandas, os 
Upload_avatar=os.path.dirname(__file__)+"\\static\\images\\avatar" 


app=Flask(__name__)
app.template_folder = "template"
app.static_folder = "static"
app.config.from_object('App_financement.config')

#page accueil
@app.route("/")
def index():
    
    params=f.messageInfo(None)
    
    return render_template("index.html",title="Acueil",**params)

@app.route("/about")
def about():
    return render_template("about.html") 

@app.route("/login")
def login():
    params=f.messageInfo(None)
    return render_template("login.html",**params)

@app.route("/signin")
def signin():
    params=f.messageInfo(None)
    return render_template("signin.html", **params)


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
    avatar=request.files['avatar']
    nom_avatar=secure_filename(avatar.filename)
    avatar.save(os.path.join(Upload_avatar, nom_avatar))
    
    statut=0 
    bdd.add_membreData(nom, prenom, mail,
    login, motPasse,nom_avatar, statut, )
    
    # dernier id créé par la BDD
    if "errorDB" not in session:
        session["infoVert"]="Nouveau membre inséré"
        return redirect("/login")
    else:
        session["infoRouge"]="Problème ajout utilisateur"
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
        session["infoVert"]="Authentification réussie"
        session["login"] = login
        session["password"] = f.chiffrement_mdp(mdp)
        return redirect("/")
    except TypeError as err:
        # Authentification refusée
        
        
        session["infoRouge"]="Authentification refusée"
        return redirect("/login")
    
@app.route("/logout")
def logout():
    session.clear()
    session["infoBleu"]="Merci de votre visite"
    return redirect("/login")

#page sgbd
@app.route("/sgbd")
def sgbd():
    listeMembres = bdd.get_membresData()
    params ={'liste':listeMembres}
    params = f.messageInfo(params)
    return render_template("sgbd.html", **params)

@app.route("/profil")
def profil():
    params=f.messageInfo(None)
    return render_template("profil.html",**params) 

@app.route("/update_mdp", methods=['POST'])
def update_mdp():

    # réception des données du formulaire
    crt_mdp = request.form['old_mdp']
    new_mdp = request.form['new_mdp']
    confirm_mdp = request.form['confirm_mdp']  
    
    
    if f.chiffrement_mdp(crt_mdp) != session["password"] :
        session["infoRouge"]="Votre ancien mot de passe est faux"
        return redirect("/profil")
    
    if new_mdp != confirm_mdp : 
        session["infoRouge"]="Les mots de passe ne correspondent pas"
        return redirect("/profil")
    try : 
        MDP = f.chiffrement_mdp(new_mdp)
        bdd.update_mdp(idUser=session["idUser"],newvalue=MDP)
        session["password"]=MDP
        
        if "errorDB" not in session:
            session["infoVert"]="Le mot de passe a été mis à jour"
        else:
            session["infoRouge"]="Problème maj utilisateur"
    except:
        pass    
    return redirect("/profil")