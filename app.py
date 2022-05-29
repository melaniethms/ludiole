import flask
app = flask.Flask("app")

#functions : 
#   get page :
def get_html(page_name):
  html_file = open(page_name + ".html")
  content = html_file.read()
  html_file.close()
  return content

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
