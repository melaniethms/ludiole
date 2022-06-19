import flask, io
from flask import Flask, render_template 
from forms import ContactForm
from flask import request
import pandas as pd

app = flask.Flask("app")
app.secret_key = 'secretKey'

#functions : 
#   get page :
def get_html(page_name):
  html_file = io.open(page_name + ".html", mode="r", encoding="utf-8")
  content = html_file.read()
  html_file.close()
  return content

if __name__ == "__main__":
    app.run(host='0.0.0.0')

#routes :

@app.route("/")
def home():
  title = "Accueil"
  return render_template("index.html", title=title)
  
@app.route("/ateliers")
def ateliers():
  title = "Ateliers"
  return render_template("ateliers.html", title=title)

@app.route("/a_propos")
def a_propos():
  title ="à propos"
  return render_template("a_propos.html", title=title)

@app.route('/contact')
def get_contact():
    title = "Contact"
    return render_template("contact.html", title=title)
        
@app.route('/form', methods=["GET","POST"])
def get_form():
    title = "message envoyé"
    return render_template("form.html", title=title)

if __name__ == '__app__':
    app.run(debug=True)