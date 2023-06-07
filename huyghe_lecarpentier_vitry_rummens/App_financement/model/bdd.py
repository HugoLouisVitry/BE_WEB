import mysql.connector
from flask import session
from ..config import DB_SERVER
from ..controller import function
import hashlib
###################################################################################
# connexion au serveur de la base de données


def connexion():
    try:
        cnx = mysql.connector.connect(**DB_SERVER)
        return cnx
    except mysql.connector.Error as err:
        session['errorDB'] = format(err)

        print(session['errorDB'])  # le problème s'affiche dans le terminal
        return None

#################################################################################
# fermeture de la connexion au serveur de la base de données


def close_bd(cursor, cnx):
    cursor.close()
    cnx.close()


#################################################################################
# Retourne les données de la table identification
def get_membresData():
    cnx = connexion()
    if cnx is None:
        return None

    try:
        cursor = cnx.cursor(dictionary=True)
        sql = "SELECT * FROM user"
        cursor.execute(sql)
        listeMembres = cursor.fetchall()
        close_bd(cursor, cnx)
        # session['successDB'] = "OK get_membresData"
    except mysql.connector.Error as err:
        listeMembres = None
        session['errorDB'] = "Failed get membres data : {}".format(err)
        print(session['errorDB'])  # le problème s'affiche dans le terminal
    return listeMembres

#################################################################################
# suppression d'un membre


def del_membreData(idUser):
    cnx = connexion()
    if cnx is None:
        return None
    try:
        cursor = cnx.cursor()
        sql = "DELETE FROM user WHERE idUser=%s;"
        param = (idUser,)
        cursor.execute(sql, param)
        cnx.commit()
        close_bd(cursor, cnx)
        # session['successDB'] = "OK del_membreData"
    except mysql.connector.Error as err:
        session['errorDB'] = "Failed del membres data : {}".format(err)
        print(session['errorDB'])  # le problème s'affiche dans le terminal
    return 1

#################################################################################
# #ajout d'un membre
# def add_membreData(nom, prenom, mail, login, motPasse, statut, avatar):
#     cnx = connexion()
#     if cnx is None:
#         return None
#     try:
#         cursor = cnx.cursor()
#         sql = "INSERT INTO identification (nom, prenom, mail, login, motPasse, statut, avatar) VALUES (%s, %s, %s, %s, %s, %s, %s);"
#         param = (nom, prenom, mail, login, motPasse, statut, avatar)
#         cursor.execute(sql, param)
#         lastId = cursor.lastrowid  # récupère le dernier idUser, généré par le serveur sql
#         cnx.commit()
#         close_bd(cursor, cnx)
#         #session['successDB'] = "OK add_membreData"
#     except mysql.connector.Error as err:
#         lastId = None
#         session['errorDB'] = "Failed add membres data : {}".format(err)
#         print(session['errorDB']) #le problème s'affiche dans le terminal
#     return lastId

#################################################################################
# modification d'une donnée dans la table identification


def update_membreData(champ, idUser, newvalue):
    cnx = connexion()
    if cnx is None:
        return None

    try:
        cursor = cnx.cursor()
        sql = "UPDATE user SET "+champ+" = %s WHERE idUser = %s;"
        param = (newvalue, idUser)
        cursor.execute(sql, param)
        cnx.commit()
        close_bd(cursor, cnx)
        # session['successDB'] = "OK update_membreData"
    except mysql.connector.Error as err:
        session['errorDB'] = "Failed update membres data : {}".format(err)
        print(session['errorDB'])  # le problème s'affiche dans le terminal
    return 1

#################################################################################
# authentification des utilisateurs


def verifAuthData(login, mdp):
    mdpC = function.chiffrement_mdp(mdp)
    cnx = connexion()
    if cnx is None:
        return None
    try:
        cursor = cnx.cursor(dictionary=True)
        sql = "SELECT * FROM user WHERE login=%s and password=%s"
        param = (login, mdpC)
        cursor.execute(sql, param)
        user = cursor.fetchone()
        close_bd(cursor, cnx)
        # session['successDB'] = "OK verifAuthData"
    except mysql.connector.Error as err:
        user = None
        session['errorDB'] = "Failed verif Auth data : {}".format(err)
        print(session['errorDB'], 2)  # le problème s'affiche dans le terminal
    return user

##########################################################################
# enregistrement des données provenant du fichier excel


def saveDataFromFile(data):
    cnx = connexion()
    if cnx is None:
        return None
    try:
        cursor = cnx.cursor()
        # suppression des données précédentes
        sql1 = "TRUNCATE TABLE identification;"
        cursor.execute(sql1)
        # insertion des nouvelles données
        for d in data:
            sql = "INSERT INTO user (nom, prenom, mail, login, motPasse, statut, avatar) VALUES (%s, %s, %s, %s, %s, %s, %s);"
            param = (d['nom'], d['prenom'], d['mail'], d['login'],
                     d['motPasse'], d['statut'], d['avatar'])
            cursor.execute(sql, param)
            cnx.commit()
        close_bd(cursor, cnx)
        # session['successDB'] = "OK saveDataFromFile"
    except mysql.connector.Error as err:
        session['errorDB'] = "Failed saveDataFromFile data : {}".format(err)
        print(session['errorDB'])  # le problème s'affiche dans le terminal
    return 1


def add_membreData(nom, prenom, mail, login, password, photo, isAdmin=1, reponse="Null"):
    cnx = connexion()
    if cnx is None:
        return None
    try:
        encrypted_password = function.chiffrement_mdp(password)
        cursor = cnx.cursor()
        sql = "INSERT INTO user (nom, prenom, mail, login, password, isAdmin, reponse, avatar) VALUES (%s, %s, %s, %s, %s, %s, %s,%s);"
        param = (nom, prenom, mail, login,
                 encrypted_password, isAdmin, reponse, photo)
        cursor.execute(sql, param)
        lastId = cursor.lastrowid  # dernier idUser généré
        cnx.commit()
        close_bd(cursor, cnx)
        # session['successDB'] = "OK add_membreData"
    except mysql.connector.Error as err:
        lastId = None
        session['errorDB'] = "Failed add membres data : {}".format(err)
        print(session['errorDB'])  # le problème s'affiche dans le terminal
    return lastId


def update_mdp(idUser, newvalue):
    cnx = connexion()
    if cnx is None:
        return None

    try:
        cursor = cnx.cursor()
        sql = "UPDATE user SET password = %s WHERE idUser = %s;"
        param = (newvalue, idUser)
        cursor.execute(sql, param)
        cnx.commit()
        close_bd(cursor, cnx)
        # session['successDB'] = "OK update_membreData"
    except mysql.connector.Error as err:
        session['errorDB'] = "Failed update membres data : {}".format(err)
        print(session['errorDB'])  # le problème s'affiche dans le terminal
    return 1


def update_solde(idUser, newvalue):
    cnx = connexion()
    if cnx is None:
        return None

    try:
        cursor = cnx.cursor()
        sql = "UPDATE user SET solde = %s WHERE idUser = %s;"
        param = (newvalue, idUser)
        cursor.execute(sql, param)
        cnx.commit()
        close_bd(cursor, cnx)
        # session['successDB'] = "OK update_membreData"
    except mysql.connector.Error as err:
        session['errorDB'] = "Failed update solde data : {}".format(err)
        print(session['errorDB'])  # le problème s'affiche dans le terminal
    return 1


def add_projectData(name, description, target, endDate, isOpen, idUser, picture):
    cnx = connexion()
    if cnx is None:
        return None
    try:
        cursor = cnx.cursor()
        sql = "INSERT INTO project (name, description, target, endDate, isOpen, idUser, picture) VALUES (%s, %s, %s, %s, %s, %s,%s);"
        param = (name, description, target, endDate, isOpen, idUser, picture)
        cursor.execute(sql, param)
        lastId = cursor.lastrowid  # dernier idProject généré
        cnx.commit()
        close_bd(cursor, cnx)
        # session['successDB'] = "OK add_projectData"
    except mysql.connector.Error as err:
        lastId = None
        session['errorDB'] = "Failed add project data : {}".format(err)
        print(session['errorDB'])  # le problème s'affiche dans le terminal
    return lastId

# fermeture d'un projet


def close_projectData(idProject):
    cnx = connexion()
    if cnx is None:
        return None
    try:
        cursor = cnx.cursor()
        sql = "UPDATE project SET isOpen = 0 WHERE idProject=%s;"
        param = (idProject,)
        cursor.execute(sql, param)
        lastId = cursor.lastrowid  # dernier idProject généré
        cnx.commit()
        close_bd(cursor, cnx)
        # session['successDB'] = "OK close_projectData"
    except mysql.connector.Error as err:
        session['errorDB'] = "Failed close project : {}".format(err)
        print(session['errorDB'])  # le problème s'affiche dans le terminal
    return lastId

# modification d'une donnée dans la table project


def update_projectData(champ, idProject, newvalue):
    cnx = connexion()
    if cnx is None:
        return None

    try:
        cursor = cnx.cursor()
        sql = "UPDATE project SET "+champ+" = %s WHERE idProject = %s;"
        param = (newvalue, idProject)
        cursor.execute(sql, param)
        cnx.commit()
        close_bd(cursor, cnx)
        # session['successDB'] = "OK update_projectData"
    except mysql.connector.Error as err:
        session['errorDB'] = "Failed update project : {}".format(err)
        print(session['errorDB'])  # le problème s'affiche dans le terminal
    return 1

# Retourne les données de la table project


def get_projectData():
    cnx = connexion()
    if cnx is None:
        return None

    try:
        cursor = cnx.cursor(dictionary=True)
        sql = "SELECT * FROM project"
        cursor.execute(sql)
        listeProjets = cursor.fetchall()
        cnx.commit()
        close_bd(cursor, cnx)
        # session['successDB'] = "OK get_projectData"
    except mysql.connector.Error as err:
        listeProjets = None
        session['errorDB'] = "Failed get projets data : {}".format(err)
        print(session['errorDB'])  # le problème s'affiche dans le terminal
    return listeProjets

#Retourne les projets et les utilisateurs qui y ont contribué
def get_participate():
    cnx = connexion() 
    if cnx is None: return None
    
    try:
        cursor = cnx.cursor(dictionary=True)
        sql = "SELECT * FROM project JOIN participate ON project.idProject = participate.idProject JOIN user on user.idUser = participate.idUser"
        cursor.execute(sql)
        listeContribution = cursor.fetchall()
        cnx.commit()
        close_bd(cursor, cnx)
        # session['successDB'] = "OK get_participate"
    except mysql.connector.Error as err:
        listeContribution = None
        session['errorDB'] = "Failed get contribution : {}".format(err)
        print(session['errorDB']) #le problème s'affiche dans le terminal
    return listeContribution

#Contribution totale de l'utilisateur
def get_contribution_totale(idUser):
    cnx = connexion() 
    if cnx is None: return None
    
    try:
        cursor = cnx.cursor(dictionary=True)
        sql = "SELECT SUM(somme) FROM project JOIN participate ON project.idProject = participate.idProject JOIN user on user.idUser = participate.idUser WHERE participate.idUser = %s;"
        param = (idUser,)
        cursor.execute(sql, param)
        contribution_totale = cursor.fetchone()['SUM(somme)']
        cnx.commit()
        close_bd(cursor, cnx)
        # session['successDB'] = "OK get_contribution_totale"
    except mysql.connector.Error as err:
        contribution_totale = None
        session['errorDB'] = "Failed get contribution totale : {}".format(err)
        print(session['errorDB']) #le problème s'affiche dans le terminal
    return contribution_totale

def get_project_index():
    cnx = connexion()
    if cnx is None:
        return None

    try:
        cursor = cnx.cursor(dictionary=True)
        sql = "SELECT * FROM project LIMIT 9"
        cursor.execute(sql)
        listeProjets = cursor.fetchall()
        close_bd(cursor, cnx)
        # session['successDB'] = "OK get_projectData"
    except mysql.connector.Error as err:
        listeProjets = None
        session['errorDB'] = "Failed get projets data : {}".format(err)
        print(session['errorDB'])  # le problème s'affiche dans le terminal
    return listeProjets

# participation financière, modification table project (current) et participate


def update_participation(idProject, idUser, value):
    cnx = connexion()
    if cnx is None:
        return None
    try:
        cursor = cnx.cursor()
        current = "SELECT current FROM project WHERE idProject = %s;"
        param_current = (idProject,)
        cursor.execute(current, param_current)
        current = cursor.fetchone()
        sql_project = "UPDATE project SET current = current + %s WHERE idProject = %s;"
        sql_user = "UPDATE user SET solde = solde - %s WHERE idUser = %s;"
        param_project = (value, idProject)
        param_user = (value, idUser)
        cursor.execute(sql_project, param_project)
        cursor.execute(sql_user, param_user)
        try :
            sql_participate = "INSERT INTO participate (idUser, idProject, somme) VALUES (%s, %s, %s);"
            param_participate = (idUser, idProject, value)
            cursor.execute(sql_participate, param_participate)
        except :
            sql_participate = "UPDATE participate SET somme = somme + %s WHERE idUser = %s AND idProject = %s;"
            param_participate = (value, idUser, idProject)
            cursor.execute(sql_participate, param_participate)
        cnx.commit()
        close_bd(cursor, cnx)
        # session['successDB'] = "OK update_participation"
    except mysql.connector.Error as err:
        session['errorDB'] = "Failed update participation : {}".format(err)
        print(session['errorDB'])  # le problème s'affiche dans le terminal
    return 1

#Liste des contributeurs à un projet
def get_contributions(idProject):
    cnx = connexion() 
    if cnx is None: return None
    
    try:
        cursor = cnx.cursor(dictionary=True)
        sql = "SELECT participate.idProject, login, somme FROM project JOIN participate ON project.idProject = participate.idProject JOIN user on user.idUser = participate.idUser WHERE participate.idProject = %s ORDER BY somme DESC;"
        param = (idProject,)
        cursor.execute(sql, param)
        contributions = cursor.fetchall()
        for i in range(min(len(contributions),3)):
            contributions[i]['classement'] = i+1
            
        print(contributions)
        
        cnx.commit()
        close_bd(cursor, cnx)
        # session['successDB'] = "OK get_contribution_totale"
    except mysql.connector.Error as err:
        contributions = None
        session['errorDB'] = "Failed get contributeurs : {}".format(err)
        print(session['errorDB']) #le problème s'affiche dans le terminal
    return contributions