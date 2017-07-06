from .Bag import Bag

class Parcel(Bag):
	def __init__(self, soup):
		self.url = ''
		self.loaded = False

		super(Parcel, self).__init__()
		
		if soup.name == 'tr':
			tds = soup.findAll('td')
			self.url = tds[1].a['href']

			self.setValue('parcelId', tds[1].text)
			self.setValue('alternateId', tds[2].text)
			self.setValue('owner', tds[3].text)
			self.setValue('propertyAddress', tds[4].text)
			self.setValue('legalDescription', tds[5].text)

		else: 
			self.loaded = True
			for section in soup.findAll('section'):
				# get title
				title = section.header.select('span.title')[0].text

				if section.table:
					if 'tabular-data-two-column' in section.table['class']:
						subData = {}
						for row in section.table.findAll('tr'):
							tds = row.findAll('td')
							subData[tds[0].text] = tds[1].text
						self.setValue(title, Bag(subData))
					elif 'tabular-data' in section.table['class']:
						subData = []
						# get column names
						keys = []
						for th in section.table.thead.tr.findAll('th'):
							keys.append(th.text)

						# get data
						for row in section.table.tbody.findAll('tr'):
							values = []
							for td in row.findAll('td'):
								values.append(td.text)
							subData.append(Bag({k: v for k, v in zip(keys, values)}))
						self.setValue(title, subData)
					elif title =='Owner':
						subData = Bag()
						subData.setValue('name', section.select('#ctlBodyPane_ctl01_ctl01_lnkOwnerName_lblSearch'))
						address = section.select('#ctlBodyPane_ctl01_ctl01_lblAddress') ", " + section.select('#ctlBodyPane_ctl01_ctl01_lblCityStateZip')
						subData.setValue('address', address)

						self.setValue('owner', subData)
				else:
						pass