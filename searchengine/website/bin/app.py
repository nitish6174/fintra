import web
from app import search

urls = (
	'/', 'index', '/search', 'searchq'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class index(object):
	def GET(self):
		return render.index()
	def POST(self):
		i = web.input()
		return web.seeother('/search?q=' + i['query'])

class searchq(object):
	def GET(self):
		greetings = web.input()['q']
		result=search.search('../indexing',greetings)
		#print result
		return render.response(greeting = result)

if __name__ == "__main__":
	app.run()

