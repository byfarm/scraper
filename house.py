class House(object):
	"""
	is the house object and stores important information
	"""
	def __init__(self, address: str, company: str=None, price: int=None, beds: float=None, baths: float=None, sqft: int=None):
		"""
		inits the house object with all the info
		:param address: the adress of the house.
		:param company: which company is selling the house
		:param price: the price of the house
		:param beds: how many beds in the house
		:param baths: how many baths in the house
		:param sqft: the sqft of the house
		"""
		self.address = address
		self.company = company
		self.price = price
		self.beds = beds
		self.baths = baths
		self.sqft = sqft

	def __repr__(self):
		"""
		prints the name of the house as the address
		"""
		return f'{self.address}'