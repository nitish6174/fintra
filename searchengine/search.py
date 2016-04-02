import sys
import json
from whoosh.index import create_in, open_dir
from whoosh import scoring
from whoosh.fields import *
from whoosh.qparser import QueryParser
from whoosh.query import Or, Term

def search(dirname, string):
	ret = []
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
			print(r['path'])
	return ret

query=sys.argv[1]
mode=sys.argv[2]

if(mode=='pages'):
	ind_dir='indexing'
else:
	ind_dir='pdf_index'

result = search(ind_dir, query)

for line in result:
	print line