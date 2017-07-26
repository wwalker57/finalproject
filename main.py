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
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

DEFAULT_GUESTBOOK_NAME = 'Anon'

def guestbook_key(guestbook_name=DEFAULT_GUESTBOOK_NAME):
    """Constructs a Datastore key for a Guestbook entity.

    We use guestbook_name as the key.
    """
    return ndb.Key('Guestbook', guestbook_name)

class Author(ndb.Model):
    identity = ndb.StringProperty(indexed=False)
    email = ndb.StringProperty(indexed=False)


class Greeting(ndb.Model):
    author = ndb.StructuredProperty(Author)
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)

class GreetingHandler(webapp2.RequestHandler):

    def get(self):
        guestbook_name = self.request.get('guestbook_name',
                                          DEFAULT_GUESTBOOK_NAME)
        greetings_query = Greeting.query(
            ancestor=guestbook_key(guestbook_name)).order(-Greeting.date)
        greetings = greetings_query.fetch(10)

        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'user': user,
            'greetings': greetings,
            'guestbook_name': urllib.quote_plus(guestbook_name),
            'url': url,
            'url_linktext': url_linktext,
        }

        template = JINJA_ENVIRONMENT.get_template('/Templates/index.html')
        self.response.write(template.render(template_values))


    # [START guestbook]
class Guestbook(webapp2.RequestHandler):

    def post(self):
        guestbook_name = self.request.get('guestbook_name',
                                          DEFAULT_GUESTBOOK_NAME)
        greeting = Greeting(parent=guestbook_key(guestbook_name))

        if users.get_current_user():
            greeting.author = Author(
                    identity=users.get_current_user().user_id(),
                    email=users.get_current_user().email())

        greeting.content = self.request.get('content')
        greeting.put()

        query_params = {'guestbook_name': guestbook_name}
        self.redirect('/Comments')
class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('home.html')

        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        my_vars = {
        'user': user,
        'url': url,
        'url_linktext': url_linktext, }

        self.response.out.write(template.render(my_vars))

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        template=env.get_template('about.html')
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        my_vars = {
        'user': user,
        'url': url,
        'url_linktext': url_linktext, }

        self.response.out.write(template.render(my_vars))

class FinAidHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('fin_aid_calc.html')

        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        my_vars = {
        'user': user,
        'url': url,
        'url_linktext': url_linktext, }

        self.response.out.write(template.render(my_vars))

    def post(self):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

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
            'bal' : bal,
            'user': user,
            'url': url,
            'url_linktext': url_linktext,}


        template = env.get_template('fin_aid_results.html')
        self.response.out.write(template.render(my_vars))



class ResourcesHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('resources.html')
        self.response.out.write(template.render())


    def get (self):
        search_term = self.request.get('q')
        template = env.get_template('resources.html')

        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        my_vars = {
        'user': user,
        'url': url,
        'url_linktext': url_linktext,
        'q': search_term }

        self.response.out.write(template.render(my_vars))


class YoutubeHandler(webapp2.RequestHandler):
    def get (self):

        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        search_term = self.request.get('q')
        template = env.get_template('youtube.html')
        my_vars = { 'q': search_term,
        'user': user,
        'url': url,
        'url_linktext': url_linktext, }
        self.response.out.write(template.render(my_vars))

        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'




app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/FinAid',FinAidHandler),
    ('/About', AboutHandler),
    ('/Youtube', YoutubeHandler),
    ('/Resources', ResourcesHandler),
    ('/Comments', GreetingHandler),
    ('/sign', Guestbook),




], debug=True)
