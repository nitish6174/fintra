import os
from bs4 import BeautifulSoup
from request import request

link_file ='link_file'
files=open('pdf_list','ab')
exc=open('exc_file','ab')

def join(href,link):
	if ".../" in href:
		exc.write(link+" => "+href+"\n")
		return ""
	if "http://" in href:
		return href
	if href[0]=='/':
		href=href[1:]
	if link.count('/')>2 and ('.html' in link.split('/')[-1] or '.php' in link.split('/')[-1]):
		pos=link.rfind('/')
		link=link[:pos]
	if link[-1]!='/':
		link=link+'/'
	url=link+href
	return url

start=977
i=0
with open(link_file) as links:
	for link in links:
		i+=1
		print i
		if i<start:
			continue
		try:
			link=link[:-1]
			source = request(link)
			soup = BeautifulSoup(source)

			for a in soup.find_all('a',href=True):

				href=a['href']
				if '.pdf' in href or '.doc' in href:
					url=join(href,link)
					if url:
						print url
						files.write(url+"\n")
		except:
			exc.write("Link "+link+"/n")
