from bs4 import BeautifulSoup
import urllib.request
import time
import codecs
from scrap_model import NewsModel
from o_url import OpenUrl
import sqlite3 as sql
from meta import news_urls, s_date, path_name, d_date

#-------------PreData----------
db = sql.connect("db_data/raw_news.db", isolation_level=None)
cur = db.cursor()
#-------------------------------

def scrap_main():
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


from meta import news_name
from textblob import TextBlob

def analyse_save(site):
	headlines = []
	all_news = []

	
	query = "Select s_data from "+ site + " where s_date = ?"
	cur.execute(query, (d_date,)) 
	headlines.append(cur.fetchall())

	for i in headlines:
		for j in i:
			if j[0] not in all_news:
				all_news.append(j[0])

	pol  = 0
	sub = 0
	t = 0
	for i in all_news:
		polarity, subjectivity = TextBlob(i).sentiment
		pol+=polarity
		sub+=subjectivity
		t+=1
	pol, sub= round(pol/t*100, 2), round(sub/t*100, 2)
	print("Site: %s, Polarity: %s, Subjectivity: %s" %(site,  pol, sub))

while(True):
	# scrap_main()
	print("Staring Sentiment Analysis:")
	for s in news_name:
		analyse_save(s)
	# print("Analyse Complete.. Will Retry In 30 Minutes")
	# time.sleep(60*30)
	exit(0)



