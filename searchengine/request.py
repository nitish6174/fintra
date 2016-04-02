import requests
# proxy = { 
#               "http"  : 'http://172.16.117.6:8080', 
#               "https" : 'https://172.16.117.6:8080', 
#               "ftp"   : ''
#             }
def request(url):
	return requests.get(url, verify=False,proxies={'http':'','https':''}).text