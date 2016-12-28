import urllib.request
from bs4 import BeautifulSoup

headers = {}
headers['User-Agent']='Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'

def OpenUrl(url):
	req = urllib.request.Request(url,headers=headers)
	resp = urllib.request.urlopen(req)
	scrap_data = BeautifulSoup(resp.read(), "html.parser")
	return scrap_data
	