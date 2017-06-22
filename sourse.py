# coding: utf8
from bs4 import BeautifulSoup
import urllib.request
import time
import json


baseUrl = 'http://domino-rf.ru'



def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def getPageCount(html):
	soup = BeautifulSoup(html, 'html.parser')
	div = soup.find('div', class_ = 'pull-left')
	countDeclaration = int(div.text[28:35])
	
	div = soup.find('div', class_ = 'pull-right')
	return int(div.find_all('li')[-2].text)
	# return countDeclaration//getCountDeclarationOnPage(html) + 1


def getCountDeclarationOnPage(html):
	soup = BeautifulSoup(html, 'html.parser')
	divContent = soup.find('div', class_ = 'col-md-9 cusDirStyle')
	massItm = divContent.findAll('div',class_ = 'col-md-12 catItem unpad')
	massItm = massItm + divContent.findAll('div',class_ = 'col-md-12 catItem unpad premium')
	return len(massItm)


def parse(html):
	soup = BeautifulSoup(html,'html.parser')
	title = soup.find('h1').text
	title = title.strip('\n\t ')
	#--Доделать парсинг хедера

	#------------------Цена и Цена за метр (если есть)----------------------------------------------
	price = int(soup.find('p', class_='price').text[:-5].replace(' ',''))

	meterPrice = soup.find('p', class_='meterPrice')
	if (meterPrice is not None):
		meterPrice = meterPrice.text[:-13]
		try:
			meterPrice = int(meterPrice)
		except ValueError:
			meterPrice = soup.find('p', class_='meterPrice').text
			meterPrice.strip('\n\t ')

	#------------------Теги поиска------------------------------------------------------------------
	keyWords = soup.find('div', class_='col-md-6 unpad')    
	keyWords = keyWords.find('a').text.replace(' ','').split('/')

	#------------------Описание от автора-----------------------------------------------------------
	Description = soup.find('blockquote').text.strip('\n\t ')








	


def main():
	# html = get_html(baseUrl + '/nedvizimost/?page=1')
	# countPage = getPageCount(html)

	htmlDeclaration = get_html('http://domino-rf.ru/nedvizimost/prodazha/nezhilaya-nedvizhimost/garazhi-stoyanki/garazh-kirpichnyy-8-m-na-3-m-1447733.html?page=1')
	parse(htmlDeclaration)




	# for i in range(1,countPage + 1):
	# 	urlPage = baseUrl + '/nedvizimost/?page=' + str(i)
		
	# 	html = get_html(urlPage)
	# 	soup = BeautifulSoup(html, 'html.parser')
	# 	divContent = soup.find('div', class_ = 'col-md-9 cusDirStyle')
	# 	massItm = divContent.findAll('div',class_ = 'col-md-12 catItem unpad')
	# 	massItm = massItm + divContent.findAll('div',class_ = 'col-md-12 catItem unpad premium')

	# 	for j in massItm:
	# 		a = j.find('a')
	# 		href = a['href']
	# 		urlDeclaration = baseUrl + href
	# 		htmlDeclaration = get_html(urlDeclaration)
	# 		parse(htmlDeclaration)





if __name__ == '__main__':
	main()






# http://domino-rf.ru/nedvizimost/prodazha/nezhilaya-nedvizhimost/garazhi-stoyanki/garazh-kirpichnyy-8-m-na-3-m-1447733.html?page=1
# http://domino-rf.ru/nedvizimost/prodazha/komnaty/prodam-komnatu-v-4-k-kvartire-volgograd-krasnoarmeyskiy-r-n-pr-stoletova-2a-1432866.html?page=1
# http://domino-rf.ru/nedvizimost/prodazha/doma/prodam-dom-volgograd-krasnoarmeyskiy-r-n-minskaya-1374165.html?page=1
# http://domino-rf.ru/nedvizimost/prodazha/kvartiry/vtorichka/prodam-2-k-kvartiru-volgograd-krasnoarmeyskiy-r-n-stoletova-44-1191055.html?page=1
# http://domino-rf.ru/nedvizimost/prodazha/doma/prodam-dom-volgograd-krasnoarmeyskiy-r-n-ul-keramicheskaya-1174773.html?page=1
# http://domino-rf.ru/nedvizimost/prodazha/kvartiry/vtorichka/prodam-3-k-kvartiru-sredneakhtubinskiy-krasnyy-sad-rechnaya-25-1447712.html?page=1
# http://domino-rf.ru/nedvizimost/prodazha/doma/prodam-dom-tovarkovo-bogoroditskiy-rayon-tovarkovskiy-1447704.html?page=1
# http://domino-rf.ru/nedvizimost/prodazha/kvartiry/vtorichka/prodam-1-k-kvartiru-volgograd-krasnoarmeyskiy-r-n-dotsenko-43-1447700.html?page=1
# http://domino-rf.ru/nedvizimost/prodazha/kvartiry/vtorichka/prodam-2-k-kvartiru-volgograd-dzerzhinskiy-r-n-ul-51-y-gvardeyskoy-9-1447693.html?page=1
# http://domino-rf.ru/nedvizimost/prodazha/kvartiry/vtorichka/prodam-1-k-kvartiru-volgograd-kirovskiy-r-n-topolevaya-9-1255596.html?page=1
# http://domino-rf.ru/nedvizimost/prodazha/nezhilaya-nedvizhimost/drugie-obekty/ovoshchekhranilishche-1447689.html?page=1
# http://domino-rf.ru/nedvizimost/prodazha/nezhilaya-nedvizhimost/garazhi-stoyanki/garazh-kirpichnyy-5-m-na-3-m-1447682.html?page=1
