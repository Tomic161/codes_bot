import requests
from bs4 import BeautifulSoup
import json

def get_codes(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'html.parser')
	content = soup.find('div', id = 'content')
	table = content.find('table', class_ = 'article-table')
	codes_html = table.findAll('tr')
	codes = []
	game = soup.find('a', class_ = 'fandom-community-header__community-name').text.replace('\n', '').replace(' Wiki', ' Codes').replace('\t', '')

	for code in codes_html:
		codes.append(code.text)

	return codes, game


def template(codes, game):
	text = f"** {game} **:"
	for i in range(1, len(codes)):
		try:
			codes[i] = codes[i].replace('\n', ' ')
			text = text + f"\n {i}. {codes[i]}"
		except Exception as e:
			codes[len(codes) - 1] = codes[len(codes) - 1].replace('\n', ' ')
			text = text + f"\n {i + 1}. {codes[len(codes) - 1]}"
	
	return text + '\n'


def get_server_info(ip, port=""):
	r = requests.get('https://api.minetools.eu/ping/{0}/{1}'.format(ip, port))
	data = json.loads(r.text)
	try:
		error = data['error']
		status = 'Off'
		online = '0'
	except KeyError:
		status = 'On'
		online = data['players']['online']

	return status, online
