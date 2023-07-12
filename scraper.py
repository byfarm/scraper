import json
import sorting
import pandas as pd
import openpyxl
import bs4
import requests
import house as hs

if __name__ == "__main__":
	# access the zillow website
	url = "https://www.zillow.com/homes/for_sale/?searchQueryState=%7B%22mapBounds%22%3A%7B%22north%22%3A35.52183575577944%2C%22south%22%3A35.348683342398694%2C%22east%22%3A-97.35160685639457%2C%22west%22%3A-97.62145854096488%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

	headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
	}

	result = requests.get(url, headers=headers)
	assert result.status_code == 200

	# parse the html. note that zillow does not use js
	soup = bs4.BeautifulSoup(result.text, 'html.parser')
	tbl = soup.find('ul', class_="List-c11n-8-89-0__sc-1smrmqp-0 StyledSearchListWrapper-srp__sc-1ieen0c-0 kZyCWU fgiidE photo-cards photo-cards_extra-attribution")

	# find all houses in the table
	houses = tbl.find_all('li')
	all_houses = []
	for house in houses:
		try:
			# find all info for the houses and create a new house object
			all_info = house.div.div.contents
			if len(all_info) > 0:
				info = list(all_info[-1].strings)
				prc = info[2].replace(',', '')[1:]
				all_houses.append(hs.House(info[0], info[1].split(',')[1], int(prc), int(info[3]), int(info[6]), int(info[9].replace(',', ''))))
		except AttributeError:
			pass

	# create a price table to sort based on price (can change to any other characteristic you want to sort)
	hs = []
	for i in all_houses:
		hs.append(i.price)

	# sort the prices using quicksort and an index table
	s_prices = sorting.qick_sort_lh(list(enumerate(hs)))
	s_houses = []
	for i in s_prices:
		s_houses.append(all_houses[i[0]])

	# initialize what is needed for the pandas dataframe
	data = []
	index = []
	for i in s_houses:
		data.append([i.price, i.sqft, i.beds, i.baths, i.company])
		index.append(i.address)

	# print the pandas dataframe to a xcel file
	df = pd.DataFrame(data, index=index, columns=['price', 'square ft', 'bed', 'bath', 'realtor'])
	df.to_excel('Zillow_Houses.xlsx', sheet_name='Houses on Zil')