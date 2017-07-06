from bs4 import BeautifulSoup
from json import JSONEncoder
import re
import requests
import types

class Bag(JSONEncoder):
	NONALPHA = re.compile('[^a-zA-Z0-9_ ]')
	UNDERLINES = re.compile('__+')

	def __init__(self, data={}):
		self.data = {}

		for key, value in data.iteritems():
			self.setValue(key, value)

	def __getattr__(self, name):
		if self.data.has_key(name):
			return self.data[name]
		else:
			raise AttributeError

	def setValue(self, key, value):
		if type(value) == types.StringType or type(value) == types.UnicodeType:
			value = self.normalizeText(value)
		self.data[self.normalizeKey(key)] = value


	def normalizeText(self, text):
		return ' '.join(text.split())

	def normalizeKey(self, text):
		key = '_'.join(self.NONALPHA.sub('_', text.lower().replace('-', ' ')).split())
		return self.UNDERLINES.sub('_', key)

	def load(self):
		if hasattr(self, 'url') and self.url and not self.loaded:
			url = 'https://qpublic.schneidercorp.com' + self.url
			r = requests.get(url)
			soup = BeautifulSoup(r.text, 'html.parser')
			self.__init__(soup)

	def default(self):
		return self.data

	def __str__(self):
		return str(self.data)

	def __repr__(self):
		return self.__str__()