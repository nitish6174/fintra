import os
import requests

def getText(link):
	temp='temp.pdf'
	r=requests.get(link,stream=True, verify=False,proxies={'http':'','https':''})
	with open(temp, 'wb') as f:
	        for chunk in r.iter_content(chunk_size=1024): 
	            if chunk: # filter out keep-alive new chunks
	                f.write(chunk)
	input1='temp.pdf'
	input2='temp.txt'
	os.system("pdftotext '%s' '%s'" % (input1, input2))
	data_file=open('temp.txt','r')
	data=data_file.read()
	data_file.close()
	return data

url='http://shilloi.iitg.ernet.in/~design/portfolio/bio-mm1.pdf'
print getText(url)