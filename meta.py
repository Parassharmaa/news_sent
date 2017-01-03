import time

s_date = time.strftime("%d%m%Y%H%M")
d_date = time.strftime("%d-%m-%Y")

news_urls = [ "http://thehindu.com", "http://ndtv.com",
			"http://dnaindia.com","http://indianexpress.com", 
			"http://firstpost.com", "http://timesofindia.com", 
			"http://hindustantimes.com"]

news_name = [i[7:-4] for i in news_urls]

path_name = "s_data/"
