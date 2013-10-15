#!/usr/bin/env python

import webapp2
from urllib2 import urlopen
import json

FORM = """
<html>
<head></head>
<form method="get" action="/weather">
<input type="text" cols="10" name="zip">
<input type="submit" value="How's it?">
</form>
</html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(FORM)

class WeatherHandler(webapp2.RequestHandler):
    def get(self):
        url = 'http://api.openweathermap.org/data/2.5/weather?q=%s' \
              % self.request.get('zip')
        data = json.load(urlopen(url))
        self.response.write('<p>%s - %s</p>' % (data["weather"][0]["main"], data["weather"][0]["description"]))
        self.response.write('<p>Temp: %d C</br>Humidity: %s</p>' % (data["main"]["temp"] - 273, data["main"]["humidity"]))
        self.response.write('<p>%s - %s</p>' % (data["name"], data["sys"]["country"]))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/weather', WeatherHandler)
], debug=True)
