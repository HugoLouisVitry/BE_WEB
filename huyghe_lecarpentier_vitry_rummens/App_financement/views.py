from flask import Flask, render_template

app=Flask(__name__)

#page accueil
@app.route("/")
def index():
    return render_template("index.html",title="Acueil")