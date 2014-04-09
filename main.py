#!/usr/bin/env python

import webapp2
from urllib2 import urlopen
import json
from google.appengine.ext.webapp import template

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        self.response.out.write(template.render("index.html", template_values))
        

class WeatherHandler(webapp2.RequestHandler):
    def get(self):
        try:
            url = 'http://api.openweathermap.org/data/2.5/weather?q=%s' \
                  % self.request.get('zip')
            data = json.load(urlopen(url))

            template_values = {'weather': data["weather"][0]["main"],
                               'description': data["weather"][0]["description"],
                               'temperature': data["main"]["temp"] - 273,
                               'humidity': data["main"]["humidity"],
                               'name': data["name"],
                               'country': data["sys"]["country"]}
            self.response.out.write(template.render("result.html", template_values))                   
        except:
            self.response.out.write(template.render("error.html", {}))    

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/weather', WeatherHandler)
], debug=True)



