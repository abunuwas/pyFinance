import urllib.request
from bs4 import BeautifulSoup

def getUrlContent(ticker):
	_base_url = 'http://finance.yahoo.com/q/hp?s={}}&a=00&b=01&c=1900&d=01&e=17&f=2016&g=d'
	url = _base_url.format(ticker)
	response = urllib.request.urlopen(url)
	data = response.read()
	content = data.decode('utf-8')
	return content

def buildSoup(content):
	soup = BeautifulSoup(text, "html.parser")
	return soup

def find_links(soup):
	links = soup.find_all('a')
	return links

def getCsvLink(links):
	url_csv = [link['href'] for link in links if link['href'].endswith('csv')]
	return url_csv

def downloadCsv(url_csv, ticker):
	for url in url_csv:
		with urllib.request.urlopen(url) as response, open(ticker+'.csv', 'wb') as file:
				data = response.read()
				file.write(data)



import csv

fields = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj', 'Close']

e=0
with open('google.csv') as file:
	reader = csv.DictReader(file)
	while e < 2:
		row = next(reader)
		for field in fields:
			try:
				print(field, ':', row[field])
			except KeyError:
				print(field, ':', '-')
		e+=1