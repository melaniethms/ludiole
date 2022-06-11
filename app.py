import flask
app = flask.Flask("app")

#functions : 
#   get page :
def get_html(page_name):
  html_file = open(page_name + ".html")
  content = html_file.read()
  html_file.close()
  return content

app.config['MAIL_SERVER'] = 'mail.web-design-johannesburg.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'testing@web-design-johannesburg.com'
app.config['MAIL_PASSWORD'] = 'testingpassword'

mail = Mail(app)


def sendTestEmail():
    msg = Message("Our first Python Email",
                  sender="testing@web-design-johannesburg.com",
                  recipients=["matshidis@gmail.com", "bertha.kgokong@tatisoftware.com"])

    msg.body = """ 
    Hello there,
    I am sending this message from python.
    say Hello
    regards,
    Me
    """


    msg.html = """
    <div>
    <h5>Hello there</h5>
    <br>
    <p>
    I am sending this message from Python 
    <br>
    Say hello 
    <br>
    Regards
    </p>
    </div>
    """

    mail.send(msg)


def sendContactForm(result):
    msg = Message("Contact Form from Skolo Website",
                  sender="testing@web-design-johannesburg.com",
                  recipients=["matshidis@gmail.com", "bertha.kgokong@tatisoftware.com"])

    msg.body = """
    Hello there,
    You just received a contact form.
    Name: {}
    Email: {}
    Message: {}
    regards,
    Webmaster
    """.format(result['name'], result['email'], result['message'])

    mail.send(msg)


@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == 'POST':
        result = {}
        
        result['name'] = request.form['name']
        result['email'] = request.form['email'].replace(' ', '').lower()
        result['message'] = request.form['message']

        sendContactForm(result)

        return render_template('contact.html', **locals())


    return render_template('contact.html', **locals())



if __name__ == "__main__":
    app.run(host='0.0.0.0')

#routes :

@app.route("/")
def home():
  return get_html("index")
  
@app.route("/ateliers")
def ateliers():
  return get_html("ateliers")

@app.route("/a_propos")
def a_propos():
  return get_html("a_propos")


@app.route("/contact")
def contact():
  return get_html("contact")
