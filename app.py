from flask import Flask, jsonify, redirect, request, current_app
import json 
from weather import Weather
import requests

app = Flask(__name__)

def json_wrapper(input_val):
	return jsonify({'payload': input_val})

@app.route("/")
def hello():
    return 'var h = "Hello World"'

@app.route("/weather/<location>")
def get_weather(location):
	try:
		weather_text = Weather().lookup_by_location(location).condition().text()
		return json_wrapper('"The weather in ' + str(location) + " is " + weather_text + '."')
	except Exception, e:
		return json_wrapper('There is no data about that location currently.')

@app.route("/get_crypto_price/<currency>")
def get_crypto(currency):
	try:
		query_url = 'https://api.coinmarketcap.com/v1/ticker/' + currency + '/'
		currency_data = requests.get(query_url).json()[0]
		return json_wrapper('The current price of ' + currency_data['name'] + " is $" + currency_data['price_usd'] + '.')
	except Exception, e:
		return e
		return json_wrapper("We do not have information for that currency.")

@app.route('/get_business_name/<keyword>/<location>')
def get_business_name(keyword, location):
	try:
		search_term = 'https://api.yelp.com/v3/businesses/search'
		params = {
			'term': str(keyword),
			'location': location,
		}
		headers = {
			'authorization': 'Bearer LShSIBnaqSv6ybcTWZV9P4eObV157TU5gsfXHU-SOD3nvDvYP6q7JD8KBpKS2Py-nN1FHXc6ONAPc65XPiCpJgmp1vHDmEfu2UAhzK3go8CRD9WFqMAa4EPeah6AWnYx'
		}
		response = requests.get(search_term, params=params, headers=headers).json()
		res = ''
		for business in response['businesses']:
			res += business['name'] + ','
		return json_wrapper(res)
	except Exception, e:
		return e
		return json_wrapper('We do not have information about anything about that.')

@app.route('/play_music')
def play_music():
	return json_wrapper("Somebody once told me the world is gonna roll me I ain't the sharpest tool in the shed She was looking kind of dumb with her finger and her thumb In the shape of an "L" on her forehead Well the years start coming and they don't stop coming Fed to the rules and I hit the ground running Didn't make sense not to live for fun Your brain gets smart but your head gets dumb So much to do, so much to see So what's wrong with taking the back streets? You'll never know if you don't go You'll never shine if you don't glow Hey now, you're an all-star, get your game on, go play Hey now, you're a rock star, get the show on, get paid And all that glitters is gold Only shooting stars break the mold It's a cool place and they say it gets colder You're bundled up now, wait till you get older But the meteor men beg to differ Judging by the hole in the satellite picture The ice we skate is getting pretty thin The water's getting warm so you might as well swim My world's on fire, how about yours? That's the way I like it and I never get bored Hey now, you're an all-star, get your game on, go play Hey now, you're a rock star, get the show on, get paid All that glitters is gold Only shooting stars break the mold Hey now, you're an all-star, get your game on, go play Hey now, you're a rock star, get the show, on get paid And all that glitters is gold Only shooting stars Somebody once asked could I spare some change for gas? I need to get myself away from this place I said yep what a concept I could use a little fuel myself And we could all use a little change Well, the years start coming and they don't stop coming Fed to the rules and I hit the ground running Didn't make sense not to live for fun Your brain gets smart but your head gets dumb So much to do, so much to see So what's wrong with taking the back streets? You'll never know if you don't go (go!) You'll never shine if you don't glow Hey now, you're an all-star, get your game on, go play Hey now, you're a rock star, get the show on, get paid And all that glitters is gold Only shooting stars break the mold And all that glitters is gold Only shooting stars break the mold")

@app.route('/tell_a_joke')
def tell_a_joke():
	return json_wrapper("You should invest in bitcoin.")