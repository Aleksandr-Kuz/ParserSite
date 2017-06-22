import urllib.request
import time
import json
from bs4 import BeautifulSoup

baseUrlPagе = 'http://domino-rf.ru/nedvizimost/?page=1'



def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def getPageCount(html):
	soup = BeautifulSoup(html)
	div_A = soup.find('div', class_ = 'pull-left')
	print(div_A.text)
	div = soup.find('div', class_ = 'pull-right')
	return int(div.find_all('li')[-2].text)


def parse(html):
	soup = BeautifulSoup(html)










def main():
	html = get_html(baseUrlPagе)
	countPage = getPageCount(html)
    print(countPage)





if __name__ == '__main__':
	main()
