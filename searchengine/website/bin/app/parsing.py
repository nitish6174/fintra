from HTMLParser import HTMLParser

dat = []
dono = [0, 0]

class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		global dat
		global dono
		if tag == "style":
			dono[0] = dono[0] + 1
		if tag == "script":
			dono[1] = dono[1] + 1
	def handle_endtag(self, tag):
		global dat
		global dono
		if tag == "style" and dono[0] > 0:
			dono[0] = dono[0] - 1
		if tag == "script" and dono[1] > 0:
			dono[1] = dono[1] - 1
	def handle_data(self, data):
		global dat
		global dono
		if(data) and "".join(data.split()) and dono[0] == 0 and dono[1] == 0:
			dat.append(data.strip(' \n\t'))

def parseit(string):
	global dat
	global dono
	dat = []
	dono = [0, 0]
	parser = MyHTMLParser()
	parser.feed(string)
#	print dat
	return " ".join(dat)

