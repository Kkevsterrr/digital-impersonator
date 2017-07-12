
##Not done yet, just uploading to save progress
import os

try:
	import requests
	from bs4 import BeautifulSoup
except ImportError:
	import pip
	pip.main(["install", "requests"])
	pip.main(["install", "BeautifulSoup4"])
	import requests
	from bs4 import BeautifulSoup

url = "http://www.americanrhetoric.com/barackobamaspeeches.htm"
hdr = {'User-Agent': 'Mozilla/5.0'}

r  = requests.get(url,headers=hdr)

data = r.text

soup = BeautifulSoup(data, "html.parser")

#print soup.prettify()
#for link in soup.find_all('a'):
    #print(link.get('href'))
table_body = soup.find('table')
#table_body = table.find('tbody')

rows = table_body.find_all('tr')
for row in rows:
    cells = row.find_all('td')
    if len(cells) == 4:
        link = cells[2]
        pdf = cells[3]
        if(link.find('a') != None and pdf.find('a') != None):
            print link.find('a').get('href') + ", " + pdf.find('a').get('href')
        print'\n'

