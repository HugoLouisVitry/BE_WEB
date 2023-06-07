import random
import string

# Génération d'un nom aléatoire
def generate_nom():
    noms = ["Smith", "Johnson", "Brown", "Taylor", "Miller", "Wilson", "Moore", "Davis", "Anderson", "Thomas"]
    return random.choice(noms)

# Génération d'un prénom aléatoire
def generate_prenom():
    prenoms = ["John", "Emma", "Michael", "Olivia", "William", "Ava", "James", "Sophia", "Benjamin", "Isabella"]
    return random.choice(prenoms)

# Génération d'un email aléatoire
def generate_email(prenom, nom):
    domaines = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
    prenom = prenom.lower()
    nom = nom.lower()
    domaine = random.choice(domaines)
    return f"{prenom}.{nom}@{domaine}"

# Génération d'un login aléatoire
def generate_login(prenom, nom):
    prenom = prenom.lower()
    nom = nom.lower()
    return f"{prenom}.{nom}"

# Génération des 15 utilisateurs fictifs
def generate_users():
    utilisateurs = []
    for _ in range(15):
        nom = generate_nom()
        prenom = generate_prenom()
        email = generate_email(prenom, nom)
        login = generate_login(prenom, nom)
        utilisateur = {
            "nom": nom,
            "prenom": prenom,
            "email": email,
            "login": login
        }
        utilisateurs.append(utilisateur)
    return utilisateurs

# Liste d'actions possibles

descriptions_projets = [
    "Ce projet vise à développer un site web de commerce électronique spécialisé dans la vente de produits artisanaux et locaux.",
    "Le projet consiste en la création d'un système de surveillance intelligent utilisant des capteurs IoT pour assurer la sécurité des bâtiments.",
    "Nous cherchons à développer un jeu éducatif interactif pour les enfants afin de les aider à apprendre les mathématiques de manière ludique.",
    "Ce projet a pour ambition de créer une plateforme de réservation en ligne pour les restaurants, simplifiant ainsi le processus de réservation pour les clients.",
    "Nous souhaitons concevoir un système de suivi de la condition physique qui permettra aux utilisateurs de suivre leurs progrès et d'atteindre leurs objectifs de remise en forme.",
    "Le projet consiste en la création d'un réseau social axé sur les passionnés de photographie, offrant un espace pour partager, découvrir et discuter des meilleures photos.",
    "Nous envisageons de développer un outil de gestion de projet collaboratif qui permettra aux équipes de travailler efficacement ensemble, en simplifiant la communication et le suivi des tâches.",
    "Ce projet a pour but de créer une plateforme d'apprentissage en ligne offrant des cours dans divers domaines, permettant aux utilisateurs d'acquérir de nouvelles compétences à leur rythme.",
    "Nous cherchons à concevoir un système de gestion de stock automatisé pour les entreprises, facilitant ainsi le suivi des stocks et la gestion des commandes.",
    "Le projet vise à créer une application de suivi des dépenses personnelles pour aider les utilisateurs à gérer leur budget de manière efficace.",
    "Nous souhaitons développer un système de réservation en ligne pour les salles de sport, permettant aux utilisateurs de réserver des cours et des équipements.",
    "Ce projet consiste en la création d'une application de livraison de nourriture à domicile, offrant une large sélection de restaurants et un service de qualité.",
    "Nous cherchons à concevoir une plateforme d'échange de livres en ligne, permettant aux utilisateurs de partager, échanger et emprunter des livres.",
    "Le projet a pour objectif de créer un outil de traduction automatique, permettant aux utilisateurs de traduire rapidement et précisément entre différentes langues.",
    "Nous souhaitons développer un système de gestion des tâches pour aider les individus et les équipes à organiser, suivre et accomplir leurs tâches quotidiennes.",
    "Ce projet consiste en la création d'une application de suivi de santé qui permettra aux utilisateurs de surveiller leur activité physique, leur sommeil et leur alimentation.",
    "Le projet vise à développer une plateforme de covoiturage pour faciliter les déplacements en offrant un moyen pratique et économique de partager des trajets.",
    "Nous envisageons de créer un site web de recettes de cuisine, offrant une collection variée de recettes avec des instructions détaillées et des conseils pratiques.",
    "Ce projet a pour ambition de créer une application de rencontre en ligne, offrant aux utilisateurs la possibilité de se connecter et de rencontrer de nouvelles personnes.",
    "Nous souhaitons développer une application de gestion de temps pour aider les utilisateurs à planifier leur emploi du temps et à maximiser leur productivité.",
    "Le projet consiste en la création d'une plateforme d'apprentissage des langues en ligne, offrant des cours interactifs et des outils de pratique linguistique.",
    "Nous cherchons à développer une application de gestion des finances personnelles, offrant des fonctionnalités telles que le suivi des dépenses et la gestion des budgets.",
    "Ce projet a pour objectif de créer un système de gestion des stocks pour les entreprises, facilitant ainsi le suivi des inventaires et la gestion des commandes.",
    "Nous souhaitons développer une application de gestion de projets pour les équipes, offrant des fonctionnalités telles que la planification, la collaboration et le suivi des tâches.",
    "Le projet vise à créer une plateforme d'apprentissage en ligne axée sur le développement personnel, offrant des cours et des ressources pour la croissance personnelle.",
    "Nous envisageons de développer une application de suivi des habitudes pour aider les utilisateurs à adopter de nouvelles habitudes et à atteindre leurs objectifs personnels.",
    "Ce projet consiste en la création d'une plateforme de réservation de voyages, offrant des options de réservation pour les vols, les hôtels et les activités touristiques.",
    "Nous souhaitons développer un système de recommandation de films personnalisé, offrant aux utilisateurs des suggestions basées sur leurs préférences et leurs historiques.",
    "Le projet a pour ambition de créer une application de suivi des dépenses professionnelles, permettant aux utilisateurs de gérer et de suivre leurs dépenses liées au travail."
]


# Génération d'une description de projet aléatoire avec le format spécifié
def generate_description_projet():
    action = random.choice(descriptions_projets)
    description = f"L'objectif est de réaliser {action}."
    return description

# Génération des 10 projets fictifs
def generate_projects():
    
    projets = []
    noms_projet = ["Projet A", "Projet B", "Projet C", "Projet D", "Projet E", "Projet F", "Projet G", "Projet H", "Projet I", "Projet J"]
    for  proj in noms_projet:
        nom_projet = proj
        description_projet = generate_description_projet()
        objectif_monetaire = random.randint(1000, 10000)
        date_cloture = f"{random.randint(2023, 2025)}-{random.randint(1, 12)}-{random.randint(1, 30)}"
        projet = {
            "nom_projet": nom_projet,
            "description_projet": description_projet,
            "objectif_monetaire": objectif_monetaire,
            "date_cloture": date_cloture,
        }
        projets.append(projet)
    return projets
    # Affichage des utilisateurs
# for utilisateur in utilisateurs:
#     print(utilisateur)
# # Affichage des projets
# for projet in projets:
#     print(projet)
    