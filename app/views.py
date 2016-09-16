# this is one of many views or handlers
# this view handles what to do with the index URL, in this case just returning "Hello World"

from app import app 		# from this project import the flask object

@app.route('/') 				# this will create mappings to '/' and '/index'
@app.route('/index')
def index():					# this handler is called index, because it handles indexes
	return "Hello, World" 	# essentially '/' and '/index' will display the same content
	