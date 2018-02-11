from flask import Flask
import json 
from weather import Weather
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/weather/<location>")
def get_weather(location):
	try:
		weather_text = Weather().lookup_by_location(location).condition().text()
		return "The weather in " + str(location) + " is " + weather_text + "."
	except Exception, e:
		return 'There is no data about that location currently.'

@app.route("/get_crypto_price/<currency>")
def get_crypto(currency):
	try:
		query_url = 'https://api.coinmarketcap.com/v1/ticker/' + currency + '/'
		currency_data = requests.get(query_url).json()[0]
		return "The current price of " + currency_data['name'] + " is $" + currency_data['price_usd'] + "." 
	except Exception, e:
		return "We do not have information for that currency."

