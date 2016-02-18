import csv

import psycopg2

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


yahoo_fields = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj', 'Close']

engine = create_engine('postgresql+psycopg2://scott:tiger@localhost/mydatabase')

Base = declarative_base()

class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	fullname = Column(String)
	password = Column(String)

	def __repr__(self):
		return "<User(name='{}', fullname='{}', password='{}'".format(
			self.name, self.fullname, self.password)

Base.metadata.create_all(engine)


'''
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
'''