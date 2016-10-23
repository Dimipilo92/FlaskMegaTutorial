WTF_CSRF_ENABLED = True 
# activates cross-site request forgery prevention 
# usually active by default
# (https://en.wikipedia.org/wiki/Cross-site_request_forgery)
SECRET_KEY = 'I-promise-you-it-will-not-be-this-so-dont-even-try' # This would be changed for public sites

# OPENID is defunct, checkout OAuth2 and OpenID Connect for a better solution
OPENID_PROVIDERS = [ # list of openid providers
    #{'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'}, # deprecated
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'}, 
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'}
    #{'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}] # deprecated
]