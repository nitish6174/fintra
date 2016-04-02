import os
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
	
temp=open('temp.pdf','wb')
info=requests.get(link,stream=True, verify=False,proxies={'http':'','https':''})
with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk) 
temp.write(info)
print "hello1"
input1='temp.pdf'
input2='temp.txt'
print os.system("pdftotext '%s' '%s'" % (input1, input2))

#print "hello"
#temp.close()
#data_file=open('temp.txt','r')
#src=data_file.read()
#data_file.close()
#src=src.strip(' \n\t')
os.system("pdftotext temp.pdf temp.txt")