# this file lists all the forms

# from flask.ext.wtf import Form # deprecated
from flask_wtf import Form # form validation, file uploads, and reCAPTCHAs (https://flask-wtf.readthedocs.io/en/stable/) 
from wtforms import StringField, BooleanField # basically text box and check box field classes
from wtforms.validators import DataRequired
 # Data Required a validator, or a funciton that can be attached to a field to perform validation on the input
 # DataRequired checks to see if the form is empty

# class LoginForm(Form): # deprecated
class LoginForm(Form): # groups the stringfield and booleanfield into something meaningful, the loginform class
	openid = StringField('openid', validators=[DataRequired()]) # adds only one validator to the Stringfield, which is that the data is required (more functions could be added to the array)
	remember_me = BooleanField('remember_me', default=False) # gives the checkbox a name and sets the default state to false