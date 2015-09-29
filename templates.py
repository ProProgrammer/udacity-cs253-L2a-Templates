"""
Statement Syntax for jinja2:
{% statement %}
    output
{% end statement %}

Eg:
{% if name=="Deep" %}
    Hello Deep
{% else %}
    Who are you?
{% endif %}
"""

"""
for loop syntax for jinja2:
{% for statement %}
    body
{% endfor %}
"""

import os
import jinja2
from jinja2 import Environment
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = Environment(loader = jinja2.FileSystemLoader(template_dir),
                        autoescape = True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.write(*a, **kw)

    def render_str(self, template, **params):
        """
        'template' is the filename
        **params > bunch of extra parameters
        """

        # using the jinja environment that we created above
        # calling get_template() function on it passing in the file name
        # This causes jinja to load that file and create a jinja template object stored in t
        t = jinja_env.get_template(template)

        # This simply renders the template
        return t.render(params)

    def render(self, template, **kw):
        """
        This calls render_str() that we defined above and wraps it into self.write() which actually sends it back to the browser 
        """

        self.write(self.render_str(template, **kw))

class MainPage(Handler):
    def get(self):
        items = self.request.get_all('food')
        self.render("shopping_list.html", items = items)

class FizzBuzzHandler(Handler):
    def get(self):
        n = self.request.get('n', 0)
        n = n and int(n)
        self.render('fizzbuzz.html', n = n)

app = webapp2.WSGIApplication([('/', MainPage),
                            ('/fizzbuzz', FizzBuzzHandler),
                            ],
                            debug=True)