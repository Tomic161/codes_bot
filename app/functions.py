import requests
from bs4 import BeautifulSoup


def get_codes(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'html.parser')
	content = soup.find('article')
	codes_li = content.find('ul').findAll('li')

	codes = []

	for code in codes_li:
		codes.append(code.text)

	game = content.find('h2').text

	return [codes, game]



def template(game, codes):
	text = f"**{game}**:"
	for code in codes:
		text = text + f"\n{code}"
	
	return text + '\n'
