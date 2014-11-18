"""
Yo Single-Tap Party Finder
"""

from __future__ import division
import json
import requests
import string, os, sys, subprocess
import urllib
import urllib2
import cookielib
import facebook
from pprint import pprint
import urlparse
from flask import request, Flask

API_HOST = 'graph.facebook.com'
SEARCH_LIMIT = 1
SEARCH_PATH = '/v2.2/search'

APP_ID = ''
APP_SECRET = ''
YO_API_TOKEN = 'dfead9b0-ddf2-49a4-9fcd-b304b83f9e27'

#uses the app id and secret from Facebook to generate the token
def get_token():
    
    oauth_args = dict(client_id = APP_ID, client_secret = APP_SECRET, grant_type = 'client_credentials')
    try:
        url = 'https://'+API_HOST+'/ouath/access_token?'+ urllib.urlencode(oauth_args)
        r = requests.get(url)
        access_token = r.text
    except:
        access_token = ""

    return access_token

#loads the returned JSON data and finds the Facebook ID of the location
def get_location_id(access_token, code):

    url = 'https://'+API_HOST+'/'+SEARCH_PATH+'?center='+latitude+','+longitude+'&type=place&distance=100&access_token='+access_token
    data = json.load(url)
    location_id = data["Local business"]['id']
    
    return location_id

#loads the returned JSON data and finds the city name
def get_city_name(access_token, code):

    url = 'https://'+API_HOST+'/'+SEARCH_PATH+'?center='+latitude+','+longitude+'&type=place&distance=100&access_token='+access_token
    data = json.load(url)
    location_id = data['Location']['city']
    
    return city

#uses the location id to find parties nearby
def parties_search(location_id):
    url = 'https://'+API_HOST+'/search/'+location_id+'/events-near/today/date/events/intersect'
    result = requests.get(url)

    return result
    
    

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
    access_token = get_token()
    location_id = get_location_id(access_token,latitude,longitude)
    city = get_city_name(access_token,latitude,longitude)
    
    print username + " is at " + city

    # search for parties in range of location ID
    # return the top party on the list to the user
    events_url = parties_search(location_id)


    # Yo the result back to the user
    requests.post("http://api.justyo.co/yo/", data={'api_token': YO_API_TOKEN, 'username': username, 'link': events_url})

    # OK!
    return 'OK'

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)

