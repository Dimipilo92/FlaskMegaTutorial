# this is one of many views or handlers
# this handler will set the index of the site to display the html

from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Miguel'} # fake (or mock) user object
	return ''' 

<html>
	<head>
		<title>Home Page</title>
	</head>
	<body>
		<h1>Hello, ''' + user['nickname'] + '''</h1>
	</body>
</html>
'''

# HTML is returned to the client. ''' is actually used as a longform string.
# it is just like "" except you need to use something to nest quotes in