import os
import jinja2
from jinja2 import Environment
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = Environment(loader = jinja2.FileSystemLoader(template_dir))

hidden_html = """
<input type='hidden' name='food' value='%s'>
"""

item_html = """
<li>%s</li>
"""

shopping_list_html = """
<br>
<br>
<h2> Shopping List </h2>
<ul>
%s
</ul>
"""


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



# We will prefix all the variables that are holding the output html with the word "output"

class MainPage(Handler):
	def get(self):
		self.render("shopping_list.html", name=self.request.get('name'))

		# Commenting out other stuff (as below) for now
		"""
		output = form_html
		output_hidden = ""

		items = self.request.get_all('food')
		if items:
			output_items = ""
			for item in items:
				output_hidden = hidden_html % item
				output_items = item_html % item

			output_shopping = shopping_list_html % output_items
			output += output_shopping
		
		output = output % output_hidden
		self.write(output)
		"""

app = webapp2.WSGIApplication([('/', MainPage),
							],
							debug=True)