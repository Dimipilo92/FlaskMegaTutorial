# this is one of many views or handlers
# this handler will set the index of the site to display the html

from flask import render_template # imports render_template from flask
from app import app # from

@app.route('/')
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
	return render_template("index.html",
											title='Home',
											user=user,
											posts=posts)


# above does this in a single statement using templates
# 	return ''' 
#  <html>
# 		<head>
# 			<title>Home Page</title>
# 		</head>
# 		<body>
# 			<h1>Hello, ''' + user['nickname'] + '''</h1>
# 		</body>
# 	</html>
# 	'''
# HTML is returned to the client. ''' is actually used as a longform string.
# it is just like "" except you need to use something to nest quotes in