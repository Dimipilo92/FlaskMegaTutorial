# creates the application object

from flask import Flask 

app = Flask(__name__) # creates application object (which is a Flask object)
# Why is __name__ used? - http://flask.pocoo.org/docs/0.11/quickstart/

from app import views # imports app from views module (which is not yet created)

#import is at the end because views needs the app object and if views is above 
# "app = Flask(__name__)" it will cause a circular logic error

# views are handlers that respond to requests from web browsers and clients.
# as their name suggests, they are functions that handle requests
# every view can be mapped to several request URLs
# but every request URL needs a handler
# so views (program specific name) = handler (abstraction) = function (implementation)