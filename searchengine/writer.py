from whoosh.index import create_in, open_dir
from whoosh.fields import *
from parsing import parseit
import os
from request import request
import requests
def getTitle(source):
	idx1 = source.find('<title>')
	idx2 = source.find('</title>', idx1)
	if idx1==-1 or idx2==-1:
		return "Untitled Document"

	title= source[idx1 + len('<title>'):idx2].strip()
	return title

def write(url, source, dirname):
	schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
	if os.path.isdir(dirname):
		ix = open_dir(dirname)
	else:
		os.system("mkdir "+dirname)
		ix = create_in(dirname, schema)
	writer = ix.writer()
	parsedstring = parseit(source)

	try:
		title=getTitle(source).decode('utf-8','strict')
	except:
		title="Untitled".decode('utf-8','strict')
	path=url.decode('utf-8','strict')
	if not parsedstring:
		print path,"skipped"
		return
	writer.add_document(title=title, path=path, content=parsedstring)
	writer.commit()
err=open('error','ab')
i=0
with open('new_links.txt') as links:
	for link in links:
		i+=1
		try:
			link=link[:-1]
			source=request(link)	
			#print source
			#content=parseit(source)
			
			write(link,source,'indexing')
			print i,getTitle(source),link
		except:
			err.write(link+"\n")
			print "EXCEPT",link

# # Tester
# link='http://www.iitg.ernet.in/vdd/'
# source=request(link)
# write(link,source,'test')
# print getTitle(source)
# print requests.get(link, verify=False,proxies={'http':'','https':''}).text
		
