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