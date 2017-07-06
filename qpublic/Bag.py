class Bag(object):
	def __init__(self, data):
		self.data = data

	def __getattr__(self, name):
		if self.data.has_key(name):
			return self.data[name]
		else:
			raise AttributeError

	def normalizeText(self, text):
		return ' '.join(text.split())