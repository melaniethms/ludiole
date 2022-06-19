from flask_wtf import FlaskForm
from wtforms import TextAreaField, BooleanField, TextAreaField, SubmitField
class ContactForm(FlaskForm):
    name = TextAreaField("Name")
    email = TextAreaField("Email")
    subject = TextAreaField("Subject")
    message = TextAreaField("Message")
    submit = SubmitField("Send")