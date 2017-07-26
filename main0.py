import webapp2
import logging
import os
import jinja2
import json
import urllib2
import urllib
from google.appengine.api import users
from google.appengine.ext import ndb

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(
    os.path.dirname(__file__) + '/templates'))

class History(ndb.Model):
    username = ndb.StringProperty(indexed=True)
    search_term = ndb.StringProperty()
    count = ndb.IntegerProperty()
    created_at = ndb.DateTimeProperty(auto_now_add=True)
    updated_at = ndb.DateTimeProperty(auto_now=True)


class MainPage(webapp2.RequestHandler):
    def get(self):
        cur_user = users.get_current_user()
        log_url = ''
        if cur_user:
            log_url = users.create_logout_url('/')
        else:
            log_url = users.create_login_url('/')

        search_term = self.request.get('q')

        if cur_user and search_term:
            key = ndb.Key('User', cur_user.email(), 'History', search_term)
            history = key.get()
            if not history:
                history = History(username = cur_user.email(), search_term = search_term)
                history.key = key
            else:
                history.count = history.count + 1

            history.put()

        results = None

        if cur_user:
            query = History.query(ancestor=ndb.Key('User', cur_user.email())).order(-History.created_at)
            results = query.fetch()

        # search_term = 'shiba'
        if not search_term:
                search_term = 'shiba'

        api_url = "http://api.giphy.com/v1/gifs/search?"
        params = {'q': search_term, 'api_key': '9a4f2302855841beb20ff857cf005cbd', 'limit': 30}
        response = urllib2.urlopen(api_url + urllib.urlencode(params))
        content = response.read()
        content_dict = json.loads(content)
        gif_urls = []
        for img in content_dict['data']:
            # content_dict['data'][0]
            url = img['images']['original']['url']
            gif_urls.append(url)

        template = env.get_template('main.html')
        my_vars = { 'gif_urls': gif_urls,
                    'q': search_term,
                    'user': cur_user,
                    'log_url': log_url,
                    'history': results}
        self.response.out.write(template.render(my_vars))



# dc6zaTOxFJmzC
app = webapp2.WSGIApplication([
    ('/', MainPage)
])
