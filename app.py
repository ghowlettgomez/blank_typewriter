from flask import Flask, jsonify, redirect, request, current_app
import json 
from weather import Weather
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    return 'var h = "Hello World"'

@app.route("/weather/<location>")
def get_weather(location):
	try:
		weather_text = Weather().lookup_by_location(location).condition().text()
		return '"The weather in "' + str(location) + " is " + weather_text + '."'
	except Exception, e:
		return '"There is no data about that location currently."'

@app.route("/get_crypto_price/<currency>")
def get_crypto(currency):
	try:
		query_url = 'https://api.coinmarketcap.com/v1/ticker/' + currency + '/'
		currency_data = requests.get(query_url).json()[0]
		return '"The current price of ' + currency_data['name'] + " is $" + currency_data['price_usd'] + '."' 
	except Exception, e:
		return e
		return '"We do not have information for that currency."'

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
		res = '"'
		for business in response['businesses']:
			res += business['name'] + ','
		return res + '"'
	except Exception, e:
		return e
		return '"We do not have information about anything about that."'

@app.route('/get_business_reviews/')

@app.route('/tell_a_joke')
def tell_a_joke():
	return '"You should invest in bitcoin."'