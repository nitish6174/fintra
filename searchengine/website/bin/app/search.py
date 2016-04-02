from whoosh.index import create_in, open_dir
from whoosh import scoring
from whoosh.fields import *
from whoosh.qparser import QueryParser

def search(dirname, string):
	ret = []
	ix = open_dir(dirname)
	with ix.searcher(weighting=scoring.TF_IDF()) as searcher:
		query_c = Or([Term("content", word) for word in string.split(" ")])
		query_t = Or([Term("title", word) for word in string.split(" ")])
		query_p = Or([Term("path", word) for word in string.split(" ")])
		results_c = searcher.search(query_c,limit=500)
		results_t = searcher.search(query_t,limit=500)
		results_p = searcher.search(query_p,limit=500)
		results_c.upgrade_and_extend(results_t)
		results_c.upgrade_and_extend(results_p)
		for r in results_c:
			ret.append({'title':str(r['title']), 'path':str(r['path'])})
	return ret