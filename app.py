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


# @app.route("/contact")
# def contact():
#       form = ContactForm()
#     if form.validate_on_submit():
#         return redirect(url_for("success"))
#   return get_html("contact")

@app.route('/contact', methods=["GET","POST"])
def get_contact():
    title = "Contact"
    form = ContactForm()
    # ici, si le type de requête est un POST, nous récupérons les données des formulaires de contact et les sauvegardons.
    #formulaires et les sauvegarder, sinon nous retournons la page html des formulaires de contact.
    if request.method == 'POST':
        name =  request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        res = pd.DataFrame({'name':name, 'email':email, 'subject':subject ,'message':message}, index=[0])
        res.to_csv('./contactusMessage.csv')
        print("Votre message a bien été envoyé !")
    else:
        return render_template("contact.html", form=form, title=title)


if __name__ == '__app__':
    app.run(debug=True)