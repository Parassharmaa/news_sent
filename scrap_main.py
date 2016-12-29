from bs4 import BeautifulSoup
import urllib.request
import time
import codecs
from scrap_model import NewsModel
from o_url import OpenUrl
import sqlite3 as sql
t1 = time.time()
print("Starting scraper.....")


#-------------PreData----------
s_date = time.strftime("%d%m%Y%H%M")
d_date = time.strftime("%d-%m-%Y")
news_urls = [ "http://thehindu.com", "http://ndtv.com",
"http://dnaindia.com","http://indianexpress.com", 
"http://firstpost.com", "http://timesofindia.com", "http://hindustantimes.com"]
path_name = "s_data/"
db = sql.connect("db_data/raw_news.db", isolation_level=None)
cur = db.cursor()
#-------------------------------

def file_save(data_list, web_name):
	f_n = path_name+web_name+"-"+s_date+".txt"
	f = codecs.open(f_n, "w", "utf-8")
	data_list = [word.strip() for word in data_list]
	for i in data_list:
		f.write(i+"\n")
	f.close()

def db_save(data_list, web_name):
	n = 0
	for i in data_list:
		i = i.strip()
		query = "Select * from "+ web_name + " where s_data = ?"
		if(len(cur.execute(query, (i,)).fetchall()) is 0):
			n = n+1
			query = "INSERT INTO " + web_name + " (s_date, s_data) VALUES (?, ?)"
			cur.execute(query, (d_date, i))
	db.commit()
	print(str(n)+" new headlines added")
		
try:
	for url in news_urls:
		print("Scraping "+url)
		scrap_data = OpenUrl(url)
		db_save(NewsModel(scrap_data, url), url[7:-4])
except Exception as e:
	print(e)


print("Script Ended...Finishing....")
t2  = time.time()
print("Total Time Taken:"+str(int(t2-t1))+"Sec")
time.sleep(3)


