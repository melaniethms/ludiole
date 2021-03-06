from email.policy import default
import flask, io
from flask import Flask, render_template 
from flask import request
from flask_mail import Mail, Message
import os
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'secretKey'

app.config['SQLALCHEMY_DATABSE_URI'] = 'mysql+pymysql://root:Eames2012!@localhost/ateliers'
#Initialize the db
db=SQLAlchemy(app)
#create db model
class Atelier(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(200), nullable=False)
  date_created = db.Column(db.DateTime, default= datetime.utcnow)
  #Create functiom to return a string when we add someting
  def __repr__(self):
    return '<Name %r>' % self.id


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'melanie.thomas.design@gmail.com'
app.config['MAIL_PASSWORD'] = os.getenv("SENSITIVE_PASSWORD")
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = 'melanie.thomas.design@gmail.com'
mail = Mail(app)


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

@app.route('/ecodes')
def ecodes():
    title = "écodés"
    return render_template("ecodes.html", title=title)

@app.route('/habitapero')
def habitapero():
    title = "Habitapéro"
    return render_template("habitapero.html", title=title)

@app.route('/nrj_en_jeu')
def nrj_en_jeu():
    title = "énergies en jeu"
    return render_template("nrj_en_jeu.html", title=title)
        
@app.route('/form', methods=["POST"])
def form():
    nom = request.form.get("nom")
    prenom = request.form.get("prenom")
    e_mail = request.form.get("e_mail")
    message = request.form.get("message")
           
    if not nom or not prenom or not e_mail or not message :
      error_statement = "vous n'avez pas rempli tous les champs"
      return render_template("contact.html",
        error_statement=error_statement,
        nom=nom,
        prenom=prenom,
        e_mail=e_mail,
        message=message)
    else:
      mail_message = Message(
      subject = "un nouveau message pour la ludiole",
      recipients = ["melanie.thomas.design@gmail.com"],
      body = request.form.get("nom") + " " + request.form.get("prenom") + "\n" + request.form.get("e_mail") + "\n" + request.form.get("message"),
      )
      mail.send(mail_message)
      title = "message envoyé"
      return render_template("form.html", title=title, nom=nom, prenom=prenom, e_mail=e_mail, message=message)



if __name__ == '__app__':
    app.run(debug=True)