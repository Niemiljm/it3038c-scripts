import requests
import json

print('Please enter your zip code:')
zip = input()

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=12345&appid=3ae260a4ba83736cc889709776cc45ee' .format(zip))
data = r.json()

print(data['weather'][0]['description'])