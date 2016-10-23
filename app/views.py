# this is file contains all of our handlers. Alternatively they're referred to as "views" because they modify the "view" of a website
# you could call this handlers.py or routes.py as well. the name doesn't matter

from flask import render_template, flash, redirect
# render_template uses jinja2 templating engine and returns a string
# flash
# redirect
from app import app # from
from .forms import LoginForm # imports the LoginForm class from forms.py


# this handler will display index.html @ the index of the site (www.site.com/ and www.site.com/index) to display the html returned by the funtion
@app.route('/') # this is a decorator (https://wiki.python.org/moin/PythonDecorators)
@app.route('/index')
def index():
	user = {'nickname': 'Dimitri'} # fake (or mock) user object
	posts = [ # fake array of posts
		{
			'author':{'nickname':'John'},
			'body':'Going on that coding grind!'
		},
		{
			'author':{'nickname':'Aaron'},
			'body':'Yeah dude. Just coding!'
		},
		{
			'author':{'nickname':'David'},
			'body':'Dimi! We gotta hang out.'
		}
	]
	return render_template("index.html", # the render_template function will return an html in the form of a string string, formatted using the templating engine jinja2
											title='Home', # name of the file
											user=user, # beginning of rparameter list
											posts=posts)
# alternatively you can just return an html string

# this handler will display the form.html @ /login
@app.route('/login', methods=['GET', 'POST']) # function accepts GET and POST requests, functions accept GET requests already by default
def login():
	form = LoginForm() # class created in forms.py
	if form.validate_on_submit(): # if the form is valid (using validators), if true => run code, if false, re-render form
		flash('Login requested for OpenID-"%s", remember_me=%s'  % # quick message that will display a message. the site needs to know how to render it, so they need to be rendered in a template, in this case, base.html
			(form.openid.data, str(form.remember_me.data))) #gets the data from the field, puts it into the "flash" funtion
		return (redirect('/index')) # redirect tells the site to login to a different page other than the current page (in this case '/index')
	return render_template('login.html',
										title='Sign In', 
										form=form)