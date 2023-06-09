from flask import session
import hashlib
import random as rd
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
        print(params['infoRouge'])
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

def chiffrement_mdp(mdp):
    mdp = hashlib.sha256(mdp.encode())
    mdpC = mdp.hexdigest()
    return mdpC
    
