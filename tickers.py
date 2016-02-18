
import urllib.request
from bs4 import BeautifulSoup


url = 'http://eoddata.com/symbols.aspx'
response = urllib.request.urlopen(url)
data = response.read()
text = data.decode('utf-8')

soup = BeautifulSoup(text, "html.parser")
links = soup.find_all('a')
tickers = [link.text for link in links if 'stockquote/NYSE/' in link['href'] and link.text != '']
print(len(tickers))
for ticker in tickers[:15]:
	print(ticker)