from whoosh.index import create_in, open_dir
from whoosh.fields import *
import os
import requests
#from Pdfdata import getText
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
	parsedstring = source.decode('utf-8','strict')

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
err=open('pdf_error','ab')
i=0
# with open('pdf_list') as links:
# 	for link in links:
# 		i+=1
# 		try:
# 			link=link[:-1]
# 			if 'iitg.ernet.in' not in link and 'iitg.ac.in' not in link:
# 				continue
# 			print i,"Sending : ",link
# 			header=requests.head(link).headers
# 			print header['Content-Length']
# 			if int(header['Content-Length'])>5000000:
# 				print "Larger than expected : ",link
# 				continue
# 			temp=open('temp.pdf','w')
# 			info=requests.get(url, verify=False,proxies={'http':'','https':''}).content 
# 			temp.write(info)
# 			os.system('pdftotext temp.pdf temp.txt')
# 			temp.close()
# 			data_file=open('temp.txt','r')
# 			src=data_file.read()
# 			data_file.close()
	
# 			src=src.strip(' \n\t')
# 			print i
# 			# #
# 		except:
# 			err.write(link+"\n")
# 			print "EXCEPT",link
# 			continue
# 		write(link,src,'pdf_index')
# 		print "wrote",link
		# print i,getTitle(source),link

# link='http://shilloi.iitg.ernet.in/~design/portfolio/bio-SB.pdf'

# print header
# # Tester
# link='http://www.iitg.ernet.in/vdd/'
# source=request(link)
# write(link,source,'test')
# print getTitle(source)
# print requests.get(link, verify=False,proxies={'http':'','https':''}).text
#toAppend='[...]\nendobj\nxref \n0 8 \n0000000000 65535 f \n0000000010 00000 n \n0000000020 00000 n \n0000000030 00000 n \n0000000040 00000 n \n0000000050 00000 n \n0000000060 00000 n \n0000000070 00000 n \ntrailer \n<</Size 8/Root 1 0 R>> \nstartxref \n555 \n%%EOF '


link='http://shilloi.iitg.ernet.in/~design/portfolio/bio-mm1.pdf'
i=0
if 'iitg.ernet.in' not in link and 'iitg.ac.in' not in link:
	#continue
	print "gg"
print "Sending : ",link
header=requests.head(link).headers
print header['Content-Length']
if int(header['Content-Length'])>5000000:
	print "Larger than expected : ",link
	
 
#temp.write(info)
#temp.close()
print "hello1"
input1='temp.pdf'
input2='temp.txt'
print "hello"
print os.system("pdftotext '%s' '%s'" % (input1, input2))
data_file=open('temp.txt','r')
src=data_file.read()
data_file.close()

src=src.strip(' \n\t')
#print i