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

	Declaration = {}

	soup = BeautifulSoup(html,'html.parser')
	title = soup.find('h1').text
	Declaration['title'] = title.strip('\n\t ')
	

	#------------------Цена и Цена за метр (если есть)----------------------------------------------
	price = soup.find('p', class_='price')
	if (price is not None):
		price = int(price.text[:-5].replace(' ',''))
		Declaration['price'] = int(soup.find('p', class_='price').text[:-5].replace(' ',''))
		
	meterPrice = soup.find('p', class_='meterPrice')
	if (meterPrice is not None):
		meterPrice = meterPrice.text[:-13]
		try:
			Declaration['meterPrice'] = int(meterPrice)
		except ValueError:
			pass

	#------------------Теги поиска------------------------------------------------------------------
	keyWords = soup.find('div', class_='col-md-6 unpad')
	keyWords = keyWords.find('a').text.split('/')
	for i in range(len(keyWords)):
		keyWords[i] = keyWords[i].strip('\n\t ')

	Declaration['keyWords'] = keyWords

	#------------------Описание от автора-----------------------------------------------------------
	Declaration['description'] = soup.find('blockquote').text.strip('\n\t ')

	#------------------Дата опубликования-----------------------------------------------------------
	Declaration['date'] = soup.find('p', class_='detailDate').text[14:24]

	#------------------Адрес объекта----------------------------------------------------------------
	Declaration['address'] = soup.find('div', class_='col-md-7').find('p').text

	#------------------Основные поля----------------------------------------------------------------

	if(keyWords[1] == 'продажа'):
		if(keyWords[2] == 'квартиры'):
			Declaration['New building/Resale'] = keyWords[3].strip('\n\t ').capitalize() # не знаю как назвать, это "Новострой / Вторичка", пусть будет q
			fillingFields_Sale_Flat(soup,Declaration)
		elif(keyWords[2] == 'комнаты'):
			print(2)
		elif(keyWords[2] == 'дома'):
			print(3)
		elif(keyWords[2] == 'коммерческая недвижимость'):
			print(4)
		elif(keyWords[2] == 'нежилая недвижимость'):
			if(keyWords[3] == 'гаражи, стоянки'):
				print(5)
			elif(keyWords[3] == 'дачи, участки'):
				print(6)
			elif(keyWords[3] == 'другие объекты'):
				print(61)
		elif(keyWords[2] == 'участки под строительство'):
			print(7)
	elif(keyWords[1] == 'сдаю'):
		if((keyWords[2] == 'квартиры посуточно') or (keyWords[2] == 'квартиры на длительный срок')):
			print(8)
		elif(keyWords[2] == 'комнаты'):
			print(9)
		elif(keyWords[2] == 'дома'):
			print(10)
		elif(keyWords[2] == 'коммерческая недвижимость'):
			print(11)
		elif(keyWords[2] == 'нежилая недвижимость'):
			if(keyWords[3] == 'гаражи, стоянки'):
				print(12)
			elif(keyWords[3] == 'дачи, участки '):
				print(13)
	elif(keyWords[1] == 'покупка'):
		if(keyWords[2] == 'жилая недвижимость'):
			print(14)
		elif(keyWords[2] == 'коммерческая недвижимость'):
			print(15)
	elif(keyWords[1] == 'обмен'):
		if(keyWords[2] == 'жилая недвижимость'):
			print(16)
		elif(keyWords[2] == 'нежилая недвижимость'):
			print(17)
	elif(keyWords[1] == 'сниму'):
		if(keyWords[2] == 'жилая недвижимость'):
			print(18)















# 		q = keyWords[3].strip('\n\t ').capitalize() # не знаю как назвать, это "Новострой / Вторичка", пусть будет q
# 		fillingFields_Flat()
# 	elif(keyWords[2] is 'комнаты'):
# 		fillingFields_Room()
# 	elif(keyWords[2] is 'комнаты'):
# 		fillingFields_House()
# 	elif(keyWords[2] is 'дома'):
# 		fillingFields_Room()
# 			fillingFields_Commercial()
	


# fillingFields_Dacha()
# fillingFields_Garage()

	


def main():
	html = get_html(baseUrl + '/nedvizimost/?page=1')
	countPage = getPageCount(html)

	# htmlDeclaration = get_html('http://domino-rf.ru/nedvizimost/prodazha/nezhilaya-nedvizhimost/drugie-obekty/ovoshchekhranilishche-obshch-quot-zarya-quot-1444870.html?fSearch=&fReg=&prop_2_from=&prop_2_to=&prop_1_from=&prop_1_to=')
	# parse(htmlDeclaration)




	for i in range(1,countPage + 1):
		urlPage = baseUrl + '/nedvizimost/?page=' + str(i)
		
		html = get_html(urlPage)
		soup = BeautifulSoup(html, 'html.parser')
		divContent = soup.find('div', class_ = 'col-md-9 cusDirStyle')
		massItm = divContent.findAll('div',class_ = 'col-md-12 catItem unpad')
		massItm = massItm + divContent.findAll('div',class_ = 'col-md-12 catItem unpad premium')

		for j in massItm:
			a = j.find('a')
			href = a['href']
			urlDeclaration = baseUrl + href
			print(urlDeclaration)
			htmlDeclaration = get_html(urlDeclaration)
			parse(htmlDeclaration)





if __name__ == '__main__':
	main()





def fillingFields_Sale_Flat(soup,Declaration):
	