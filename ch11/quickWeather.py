#! python3
# Prints the weather based on location given by command line

import sys
import requests
import json

if len(sys.argv) < 2:
	raise Exception('Need to run it as quickWeather.py <location-name>')

location = ' '.join(sys.argv[1:])


# Download the data from openweathermap.org's API
url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&appid=6cdca5daa4442fc0ea11829012b4935f' % (location) # %s style, guarentees string I think

response = requests.get(url)
response.raise_for_status()
weatherData = json.loads(response.text)

#print(weatherData)
w = weatherData['main'] # this is the section we want

print('Weather today in %s:' % location)
templist = {'Current:':w['temp'], 'Low:':w['temp_min'], 'High:':w['temp_max']}
for k, v in templist.items():
    print(k, round(float(v) - 273.15),round((float(v) - 273.15)*9/5 + 32))

#print('Humidity:', w['humidity'])

#print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])

