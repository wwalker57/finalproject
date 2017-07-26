#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import jinja2
import urllib
import os
import urllib
import webapp2

from google.appengine.api import users
from google.appengine.ext import ndb

env = jinja2.Environment(loader=jinja2.FileSystemLoader('Templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('main.html')
        self.response.out.write(template.render())

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        template=env.get_template('about.html')
        self.response.out.write(template.render())



class FinAidHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('fin_aid_calc.html')
        self.response.out.write(template.render())

    def post(self):

        name = self.request.get("name")
        college = self.request.get("college")
        tuition = self.request.get("Tuition")
        meals = self.request.get("Meals")
        housing = self.request.get("Housing")
        books = self.request.get("Books")
        insurance = self.request.get("Insurance")
        equip = self.request.get("Equipment")
        travel = self.request.get("Transportation")
        entertain = self.request.get("Entertainment")
        other = self.request.get("Other")
        scholarships = self.request.get("University")
        pell = self.request.get("Pell")
        seog = self.request.get("SEOG")
        sub = self.request.get("Sub")
        unsub = self.request.get("Unsub")
        parent = self.request.get("Parent")
        student = self.request.get("Student")
        aidOther = self.request.get("AidOther")



        coa = int(tuition) + int(meals) + int(housing) + int(books) + int(insurance) + int(equip) + int(travel) + int(entertain) + int(other)
        aid = int(scholarships) + int(pell) + int(seog) + int(sub) + int(unsub) + int(parent) + int(student) + int(aidOther)
        bal = int(coa) - int(aid)

        my_vars = {
            'name':name,
            'college' : college,
            'Tuition' : tuition,
            'Meals' : meals,
            'Housing' : housing,
            'Books' : books,
            'Insurance': insurance,
            'Equipment': equip,
            'Transportation': travel,
            'Entertainment' : entertain,
            'Other' : other,
            'University' : scholarships,
            'Pell': pell,
            'SEOG':seog,
            'Sub' : sub,
            'Unsub': unsub,
            'Parent': parent,
            'Student': student,
            'AidOther': aidOther,
            'coa' : coa,
            'aid': aid,
            'bal' : bal}


        template = env.get_template('fin_aid_results.html')
        self.response.out.write(template.render(my_vars))



class ResourcesHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('resources.html')
        self.response.out.write(template.render())

    def get (self):
        search_term = self.request.get('q')
        template = env.get_template('resources.html')
        my_vars = { 'q': search_term }
        self.response.out.write(template.render(my_vars))


class YoutubeHandler(webapp2.RequestHandler):
    def get (self):
        search_term = self.request.get('q')
        template = env.get_template('youtube.html')
        my_vars = { 'q': search_term }
        self.response.out.write(template.render(my_vars))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/FinAid',FinAidHandler),
    ('/About', AboutHandler),
    ('/Youtube', YoutubeHandler),
    ('/Resources', ResourcesHandler),




], debug=True)
