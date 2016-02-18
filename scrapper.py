import urllib.request
from bs4 import BeautifulSoup

yahoo_base_url = 'http://finance.yahoo.com/q/hp?s={}&a=00&b=01&c=1900&d=01&e=17&f=2016&g=d'

def buildUrl(base_url, value=None):
	'''
	Takes a base url as an argument and an optional value to substitute in it. It returns
	the final url. 
	'''
	if value is not None:
		url = base_url.format(value)
	else: 
		url = base_url
	return url

def getUrlContent(url):
	'''
	It fetches and returns the contents of a url. The contents are expected to be encoded in utf-8,
	and so are decoded following this protocol. 
	'''
	response = urllib.request.urlopen(url)
	data = response.read()
	content = data.decode('utf-8')
	return content

def buildSoup(content):
	'''
	Takes the contents of a webpage as an argument and uses it to build a BeautifulSoup object,
	which the function returns. 
	'''
	soup = BeautifulSoup(content, "html.parser")
	return soup

def buildSoupUrl(base_url, value=None):
	'''
	Helper function that takes a base url and an optional value to substitute on it, and returns 
	a BeautifulSoup object of the contents of the url. 
	'''
	url = buildUrl(base_url, value)
	content = getUrlContent(url)
	soup = buildSoup(content)
	return soup

def find_anchor_tags(soup):
	'''
	Takes a BeautifulSoup object as an argument and returns a list of all HTML anchor elements in it.
	'''
	anchors = soup.find_all('a')
	return anchors

def get_links(anchors):
	'''
	Takes a list of anchor tag elements from a BeautifulSoup object and returns a list of links out of 
	the tags. 
	'''
	links = [anchor['href'] for anchor in anchors]
	return links

def get_links_from_url(base_url, value=None):
	'''
	Helper function that takes a base url and an optional value to substitute on it as an argument,
	and returns a list of links from the contents of the url. 
	'''
	soup = buildSoupUrl(base_url, value)
	anchors = find_anchor_tags(soup)
	links = get_links(anchors)
	return links

def getCsvLinks(links):
	'''
	Takes a list of links as an argument and returns a list of only those which end in csv. 
	'''
	csv_links = [link for link in links if link.endswith('csv')]
	return csv_links

def downloadCsv(csv_links, ticker, *file_names):
	'''
	Takes a list of links to csv files and downloads their content to a file. If the number of file names 
	is not equivalent to the number of csv links, it tries to make up a name with the last element of the 
	file_names tuple plus an index number. 
	'''
	for index, url in enumerate(csv_links):
		try:
			file_name = file_names[index]
		except IndexError:
			file_name = file_names[-1]+str(index)
		with urllib.request.urlopen(url) as response, open(file_name+'.csv', 'wb') as file:
			data = response.read()
			file.write(data)
	return None

def getTickerData(base_url, value=None, *file_names):
	'''
	Helper function that takes a base url and an optional value to substitute on it as an argument.
	Finds links to csv files in the contents of the url, and downloads those contents to a filename. 
	'''
	links = get_links_from_url(base_url, value)
	csv_links = getCsvLinks(links)
	downloadCsv(csv_links, value, *file_names)
	return None


if __name__ == '__main__':
	getTickerData(yahoo_base_url, 'goog', 'google')