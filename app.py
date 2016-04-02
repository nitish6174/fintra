from flask import Flask,request,render_template

import sys
import json
from whoosh.index import create_in, open_dir
from whoosh import scoring
from whoosh.fields import *
from whoosh.qparser import QueryParser
from whoosh.query import Or, Term

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
	if request.method == 'GET':
	    return render_template('index.html',links=False)
	elif request.method == 'POST':
		def search(dirname, string):
			links = []
			ret = []
			text = ""
			ix = open_dir(dirname)
			with ix.searcher(weighting=scoring.TF_IDF()) as searcher:
				query_c = Or([Term("content", word) for word in string.split(" ")])
				query_t = Or([Term("title", word) for word in string.split(" ")])
				query_p = Or([Term("path", word) for word in string.split(" ")])
				results_c = searcher.search(query_c,limit=10)
				results_t = searcher.search(query_t,limit=10)
				results_p = searcher.search(query_p,limit=10)
				results_c.upgrade_and_extend(results_t)
				results_c.upgrade_and_extend(results_p)
				for r in results_c:
					text = text + r['path'] + "\n"
					links.append(r['path'])
			# return ret
			# return text
			return links

		query = request.form['query']
		mode = request.form['mode']
		if mode=='pages':
			ind_dir = 'searchengine/indexing'
		elif mode=='files':
			ind_dir = 'searchengine/pdf_index'
		links = search(ind_dir, query)
		# links = links.join('\n')
		return json.dumps({'results':'true','links':links});
		# return render_template('index.html',links=links)

if __name__ == '__main__':
    app.run(host='0.0.0.0')