from .Bag import Bag

class Parcel(Bag):
	def __init__(self, soup):
		self.url = ''
		self.notLoaded = False
		
		if soup.name == 'tr':
			tds = soup.findAll('td')
			self.url = tds[1].a['href']
			
			super(Parcel, self).__init__({
				'parcelId': self.normalizeText(tds[1].text),
				'alternateId': self.normalizeText(tds[2].text),
				'owner': self.normalizeText(tds[3].text),
				'propertyAddress': self.normalizeText(tds[4].text),
				'legalDescription': self.normalizeText(tds[5].text)
				})
		else:
			pass