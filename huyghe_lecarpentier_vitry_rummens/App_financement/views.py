from flask import Flask, render_template

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

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/pricing")
def pricing():
    return render_template("pricing.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/case-study")
def case_study():
    return render_template("case-study.html")