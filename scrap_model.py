from bs4 import BeautifulSoup

def NewsModel(scrap_data, url):
	if(url == "http://thehindu.com"):
		d_l = []
		scrap_data = scrap_data.select("[data-vr-excerpttitle]")
		for i in scrap_data:
			d_l.append(i.text)
		return d_l
		
	else:
		d_l = []
		scrap_data = [i.text for i in scrap_data.find_all("a")]
		n = AvgHeadLen(scrap_data)
		for i in scrap_data:
			if len(i.strip())>n:
				d_l.append(i)
		return d_l


def AvgHeadLen(head_list):
	total_letter = 0
	for i in head_list:
		total_letter = total_letter+len(i.strip())
	return int(total_letter/len(head_list))