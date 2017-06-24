# coding: utf8
from bs4 import BeautifulSoup
import urllib.request
import time
import json


baseUrl = 'http://domino-rf.ru'



def fillingFields_Sale_Flat(soup,Declaration):
	row = soup.find_all('tr')
	if(row is not None):
		for i in row:
			col = i.find_all('td')
			characteristic = col[0].text.strip('\n\t ')

			if(characteristic == 'Общая площадь'):
				Declaration['total area'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Количество комнат'):
				Declaration['number rooms'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Этаж'):
				Declaration['floor'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Этажность'):
				Declaration['number of storeys'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Жилая площадь'):
				Declaration['living space'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Площадь кухни'):
				Declaration['kitchen area'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Тип дома'):
				Declaration['type house'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Ремонт'):
				Declaration['repairs'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Санузел'):
				Declaration['bathroom'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Балкон/лоджия'):
				Declaration['balcony'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Состояние дома'):
				Declaration['condition house'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Наличие лифта'):
				Declaration['elevator'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Наличие мусоропровода'):
				Declaration['garbage chute'] = col[1].text.strip('\n\t ')
			else:
				print('=========I DON`T KNOW WATH IS THIS!!!=========')
def fillingFields_Sale_Room(soup,Declaration):
	row = soup.find_all('tr')
	if(row is not None):
		for i in row:
			col = i.find_all('td')
			characteristic = col[0].text.strip('\n\t ')

			if(characteristic == 'Количество хозяев в квартире'):
				Declaration['number hosts'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Площадь комнаты'):
				Declaration['area room'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Количество комнат'):
				Declaration['number rooms'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Этаж'):
				Declaration['floor'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Этажность'):
				Declaration['number of storeys'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Жилая площадь'):
				Declaration['living space'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Площадь кухни'):
				Declaration['kitchen area'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Тип дома'):
				Declaration['type house'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Ремонт'):
				Declaration['repairs'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Санузел'):
				Declaration['bathroom'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Балкон/лоджия'):
				Declaration['balcony'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Состояние дома'):
				Declaration['condition house'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Наличие лифта'):
				Declaration['elevator'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Наличие мусоропровода'):
				Declaration['garbage chute'] = col[1].text.strip('\n\t ')
			else:
				print('=========I DON`T KNOW WATH IS THIS!!!=========')
def fillingFields_Sale_House(soup,Declaration):
	row = soup.find_all('tr')
	if(row is not None):
		for i in row:
			col = i.find_all('td')
			characteristic = col[0].text.strip('\n\t ')

			if(characteristic == 'Общая площадь'):
				Declaration['total area'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Количество комнат'):
				Declaration['number rooms'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Площадь участка'):
				Declaration['land area'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Продаваемая часть недвижимости'):
				Declaration['sold property'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Удобства'):
				Declaration['facilities'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Материал стен'):
				Declaration['wall material'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Другие строения'):
				Declaration['other buildings'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Наличие электричества'):
				Declaration['availability electricity'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Наличие канализации'):
				Declaration['sewerage'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Проведена вода'):
				Declaration['there is water'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Проведен газ'):
				Declaration['gas'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Наличие отопления'):
				Declaration['areavailability of heating'] = col[1].text.strip('\n\t ')
			else:
				print('=========I DON`T KNOW WATH IS THIS!!!=========')
def fillingFields_Sale_Commercial(soup,Declaration):
	row = soup.find_all('tr')
	if(row is not None):
		for i in row:
			col = i.find_all('td')
			characteristic = col[0].text.strip('\n\t ')

			if(characteristic == 'Общая площадь'):
				Declaration['total area'] = int(col[1].text.strip('\n\t '))
			else:
				print('=========I DON`T KNOW WATH IS THIS!!!=========')
def fillingFields_Sale_nonResidential_Garage(soup,Declaration):
	row = soup.find_all('tr')
	if(row is not None):
		for i in row:
			col = i.find_all('td')
			characteristic = col[0].text.strip('\n\t ')

			if(characteristic == 'ГСК'):
				Declaration['GSK'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Длина гаража'):
				Declaration['length'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Ширина гаража'):
				Declaration['width'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Наличие электричества'):
				Declaration['electricity'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Наличие подвала'):
				Declaration['basement'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Тип объекта'):
				Declaration['Object type'] = col[1].text.strip('\n\t ')
			else:
				print('=========I DON`T KNOW WATH IS THIS!!!=========')
def fillingFields_Sale_nonResidential_Dacha(soup,Declaration):
	row = soup.find_all('tr')
	if(row is not None):
		for i in row:
			col = i.find_all('td')
			characteristic = col[0].text.strip('\n\t ')

			if(characteristic == 'Садовое товарищество'):
				Declaration['garden community'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Площадь участка'):
				Declaration['land area'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Другие строения'):
				Declaration['other buildings'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Наличие электричества'):
				Declaration['electricity'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Проведена вода'):
				Declaration['there is water'] = col[1].text.strip('\n\t ')
			else:
				print('=========I DON`T KNOW WATH IS THIS!!!=========')
def fillingFields_Sale_nonResidential_Other(soup,Declaration):
	row = soup.find_all('tr')
	if(row is not None):
		print('=========I DON`T KNOW WATH IS THIS!!!=========')
def fillingFields_Sale_Building_land(soup,Declaration):
	row = soup.find_all('tr')
	if(row is not None):
		for i in row:
			col = i.find_all('td')
			characteristic = col[0].text.strip('\n\t ')

			if(characteristic == 'Площадь участка'):
				Declaration['land area'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Наличие электричества'):
				Declaration['electricity'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Проведена вода'):
				Declaration['there is water'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Проведен газ'):
				Declaration['gas'] = col[1].text.strip('\n\t ')
			else:
				print('=========I DON`T KNOW WATH IS THIS!!!=========')

def fillingFields_Rental_Flat(soup,Declaration):
	row = soup.find_all('tr')
	if(row is not None):
		for i in row:
			col = i.find_all('td')
			characteristic = col[0].text.strip('\n\t ')

			if(characteristic == 'Общая площадь'):
				Declaration['total area'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Количество комнат'):
				Declaration['number rooms'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Этаж'):
				Declaration['floor'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Этажность'):
				Declaration['number of storeys'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Жилая площадь'):
				Declaration['living space'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Площадь кухни'):
				Declaration['kitchen area'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Тип дома'):
				Declaration['type house'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Ремонт'):
				Declaration['repairs'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Санузел'):
				Declaration['bathroom'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Наличие мебели'):
				Declaration['furniture'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Наличие бытовой техники'):
				Declaration['household appliances'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Наличие интернета'):
				Declaration['internet'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Балкон/лоджия'):
				Declaration['balcony'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Состояние дома'):
				Declaration['condition house'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Наличие лифта'):
				Declaration['elevator'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Наличие мусоропровода'):
				Declaration['garbage chute'] = col[1].text.strip('\n\t ')
			else:
				print('=========I DON`T KNOW WATH IS THIS!!!=========')
def fillingFields_Rental_Room(soup,Declaration):
	row = soup.find_all('tr')
	if(row is not None):
		for i in row:
			col = i.find_all('td')
			characteristic = col[0].text.strip('\n\t ')

			if(characteristic == 'Количество хозяев в квартире'):
				Declaration['number hosts'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Площадь комнаты'):
				Declaration['area room'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Количество комнат'):
				Declaration['number rooms'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Этаж'):
				Declaration['floor'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Этажность'):
				Declaration['number of storeys'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Жилая площадь'):
				Declaration['living space'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Площадь кухни'):
				Declaration['kitchen area'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Тип дома'):
				Declaration['type house'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Ремонт'):
				Declaration['repairs'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Санузел'):
				Declaration['bathroom'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Балкон/лоджия'):
				Declaration['balcony'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Состояние дома'):
				Declaration['condition house'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Наличие лифта'):
				Declaration['elevator'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Наличие мусоропровода'):
				Declaration['garbage chute'] = col[1].text.strip('\n\t ')
			else:
				print('=========I DON`T KNOW WATH IS THIS!!!=========')
def fillingFields_Rental_House(soup,Declaration):
	row = soup.find_all('tr')
	if(row is not None):
		for i in row:
			col = i.find_all('td')
			characteristic = col[0].text.strip('\n\t ')

			if(characteristic == 'Общая площадь'):
				Declaration['total area'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Количество комнат'):
				Declaration['number rooms'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Площадь участка'):
				Declaration['land area'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Продаваемая часть недвижимости'):
				Declaration['sold property'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Удобства'):
				Declaration['facilities'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Материал стен'):
				Declaration['wall material'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Другие строения'):
				Declaration['other buildings'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Наличие электричества'):
				Declaration['availability electricity'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Наличие канализации'):
				Declaration['sewerage'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Проведена вода'):
				Declaration['there is water'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Проведен газ'):
				Declaration['gas'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Наличие отопления'):
				Declaration['areavailability of heating'] = col[1].text.strip('\n\t ')
			else:
				print('=========I DON`T KNOW WATH IS THIS!!!=========')
def fillingFields_Rental_Commercial(soup,Declaration):
	if(row is not None):
		for i in row:
			col = i.find_all('td')
			characteristic = col[0].text.strip('\n\t ')

			if(characteristic == 'Общая площадь'):
				Declaration['total area'] = int(col[1].text.strip('\n\t '))
			else:
				print('=========I DON`T KNOW WATH IS THIS!!!=========')
def fillingFields_Rental_nonResidential_Garage(soup,Declaration):
	row = soup.find_all('tr')
	if(row is not None):
		for i in row:
			col = i.find_all('td')
			characteristic = col[0].text.strip('\n\t ')

			if(characteristic == 'ГСК'):
				Declaration['GSK'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Длина гаража'):
				Declaration['length'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Ширина гаража'):
				Declaration['width'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Наличие электричества'):
				Declaration['electricity'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Наличие подвала'):
				Declaration['basement'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Тип объекта'):
				Declaration['Object type'] = col[1].text.strip('\n\t ')
			else:
				print('=========I DON`T KNOW WATH IS THIS!!!=========')
def fillingFields_Rental_nonResidential_Dacha(soup,Declaration):
	row = soup.find_all('tr')
	if(row is not None):
		print('=========I DON`T KNOW WATH IS THIS!!!=========')
def fillingFields_Purchase_Residential_Properties(soup,Declaration):
	row = soup.find_all('tr')
	if(row is not None):
		for i in row:
			col = i.find_all('td')
			characteristic = col[0].text.strip('\n\t ')

			if(characteristic == 'Продаваемая часть недвижимости'):
				Declaration['sold property'] = col[1].text.strip('\n\t ')
			else:
				print('=========I DON`T KNOW WATH IS THIS!!!=========')
def fillingFields_Purchase_Commercial_Property(soup,Declaration):
	row = soup.find_all('tr')
	if(row is not None):
		for i in row:
			col = i.find_all('td')
			characteristic = col[0].text.strip('\n\t ')

			if(characteristic == 'Тип коммерческого объекта'):
				Declaration['Type commercial object'] = col[1].text.strip('\n\t ')
			else:
				print('=========I DON`T KNOW WATH IS THIS!!!=========')
def fillingFields_Exchange_Residential_Properties(soup,Declaration):
	row = soup.find_all('tr')
	if(row is not None):
		for i in row:
			col = i.find_all('td')
			characteristic = col[0].text.strip('\n\t ')

			if(characteristic == 'Общая площадь'):
				Declaration['total area'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Этаж'):
				Declaration['floor'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Этажность'):
				Declaration['number of storeys'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Жилая площадь'):
				Declaration['living space'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Площадь кухни'):
				Declaration['kitchen area'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Ремонт'):
				Declaration['repairs'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Санузел'):
				Declaration['bathroom'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Балкон/лоджия'):
				Declaration['balcony'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Состояние дома'):
				Declaration['condition house'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Меняю на тип недвижимости'):
				Declaration['exchange for'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Размен'):
				Declaration['type exchange'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Продаваемая часть недвижимости'):
				Declaration['sold property'] = col[1].text.strip('\n\t ')
			else:
				print('=========I DON`T KNOW WATH IS THIS!!!=========')
def fillingFields_Rent_Residential_Properties(soup,Declaration):
	row = soup.find_all('tr')
	if(row is not None):
		for i in row:
			col = i.find_all('td')
			characteristic = col[0].text.strip('\n\t ')

			if(characteristic == 'Продаваемая часть недвижимости'):
				Declaration['sold property'] = col[1].text.strip('\n\t ')
			else:
				print('=========I DON`T KNOW WATH IS THIS!!!=========')

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


def parse(html, urlDeclaration):

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

	#------------------Информация об авторе---------------------------------------------------------


	#------------------Основные поля----------------------------------------------------------------

	if(keyWords[1] == 'продажа'):
		Declaration['type transaction'] = 'продажа'
		if(keyWords[2] == 'квартиры'):
			Declaration['property type'] = 'квартиры'
			Declaration['New building/Resale'] = keyWords[3].strip('\n\t ').capitalize() 
			fillingFields_Sale_Flat(soup,Declaration)
		elif(keyWords[2] == 'комнаты'):
			Declaration['property type'] = 'комнаты'
			fillingFields_Sale_Room(soup,Declaration)
		elif(keyWords[2] == 'дома'):
			Declaration['property type'] = 'дома'
			fillingFields_Sale_House(soup,Declaration)
		elif(keyWords[2] == 'коммерческая недвижимость'):
			Declaration['property type'] = 'коммерческая недвижимость'
			fillingFields_Sale_Commercial(soup,Declaration)
		elif(keyWords[2] == 'нежилая недвижимость'):
			Declaration['property type'] = 'нежилая недвижимость'
			if(keyWords[3] == 'гаражи, стоянки'):
				Declaration['property non-residential type'] = 'гаражи, стоянки'
				fillingFields_Sale_nonResidential_Garage(soup,Declaration)
			elif(keyWords[3] == 'дачи, участки'):
				Declaration['property non-residential type'] = 'дачи, участки'
				fillingFields_Sale_nonResidential_Dacha(soup,Declaration)
			elif(keyWords[3] == 'другие объекты'):
				Declaration['property non-residential type'] = 'другие объекты'
				fillingFields_Sale_nonResidential_Other(soup,Declaration)
		elif(keyWords[2] == 'участки под строительство'):
			fillingFields_Sale_Building_land(soup,Declaration)

	elif(keyWords[1] == 'сдаю'):
		Declaration['type transaction'] = 'сдача'
		if((keyWords[2] == 'квартиры посуточно') or (keyWords[2] == 'квартиры на длительный срок')):
			Declaration['deadline'] = keyWords[2]
			fillingFields_Rental_Flat(soup,Declaration)
		elif(keyWords[2] == 'комнаты'):
			fillingFields_Rental_Room(soup,Declaration)
		elif(keyWords[2] == 'дома'):
			fillingFields_Rental_House(soup,Declaration)
		elif(keyWords[2] == 'коммерческая недвижимость'):
			fillingFields_Rental_Commercial(soup,Declaration)
		elif(keyWords[2] == 'нежилая недвижимость'):
			if(keyWords[3] == 'гаражи, стоянки'):
				fillingFields_Rental_nonResidential_Garage(soup,Declaration)
			elif(keyWords[3] == 'дачи, участки '):
				fillingFields_Rental_nonResidential_Dacha(soup,Declaration)

	elif(keyWords[1] == 'покупка'):
		Declaration['type transaction'] = 'покупка'
		if(keyWords[2] == 'жилая недвижимость'):
			fillingFields_Purchase_Residential_Properties(soup,Declaration)
		elif(keyWords[2] == 'коммерческая недвижимость'):
			fillingFields_Purchase_Commercial_Property(soup,Declaration)

	elif(keyWords[1] == 'обмен'):
		Declaration['type transaction'] = 'обмен'
		if(keyWords[2] == 'жилая недвижимость'):
			fillingFields_Exchange_Residential_Properties(soup,Declaration)
		elif(keyWords[2] == 'нежилая недвижимость'):
			pass

	elif(keyWords[1] == 'сниму'):
		Declaration['type transaction'] = 'съём'
		if(keyWords[2] == 'жилая недвижимость'):
			fillingFields_Rent_Residential_Properties(soup,Declaration)



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
			parse(htmlDeclaration, urlDeclaration)





if __name__ == '__main__':
	main()