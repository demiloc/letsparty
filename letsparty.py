"""
Yo Single-Tap Party Finder
"""

import sys
import requests
import oauth2
import facebook
from flask import request, Flask

API_HOST = 'graph.facebook.com'
SEARCH_LIMIT = 5
SEARCH_PATH = '/v2.2/search'

FACEBOOK_APP_TOKEN = '672075099578708|T1yvdE43kWyph2r6MiYmft7VAYs'
YO_API_TOKEN = 'dfead9b0-ddf2-49a4-9fcd-b304b83f9e27'

graph = facebook.GraphAPI(FACEBOOK_APP_TOKEN)

def do_request(host, path, url_params=None):
    
    url = 'http://{0}{1}'.format(host, path)
    consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
    oauth_request = oauth2.Request('GET', url, url_params)
    oauth_request.update(
        {
            'oauth_nonce': oauth2.generate_nonce(),
            'oauth_timestamp': oauth2.generate_timestamp(),
            'oauth_token': TOKEN,
            'oauth_consumer_key': CONSUMER_KEY
        }
    )
    token = oauth2.Token(TOKEN, TOKEN_SECRET)
    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
    signed_url = oauth_request.to_url()

    print 'Querying Yelp {0}'.format(signed_url)

    response = requests.get(signed_url)
    response_object = response.json()
    return response_object

def search(term, city, state):

    # search the Facebook Graph API to find a location based on Lat x Long
    # --- INSERT CODE HERE --- #

    return do_request(API_HOST, SEARCH_PATH, url_params=url_params)


app = Flask(__name__)


@app.route("/yo/")
def yo():

    # extract and parse query parameters
    username = request.args.get('username')
    location = request.args.get('location')
    splitted = location.split(';')
    latitude = splitted[0]
    longitude = splitted[1]

    print "We got a Yo from " + username

    #use Facebook API to get location ID
    # --- INSERT CODE HERE --- #
    
    print username + " is at " + city

    # search for parties in range of location ID
    # return the top 5 parties on the list to the user
    # --- INSERT CODE HERE --- #


    # Yo the result back to the user
    requests.post("http://api.justyo.co/yo/", data={'api_token': YO_API_TOKEN, 'username': username, 'link': bar_url})

    # OK!
    return 'OK'

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)

