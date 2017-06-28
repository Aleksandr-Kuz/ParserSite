# coding: utf8
from bs4 import BeautifulSoup
import urllib.request
import json


baseUrl = 'http://domino-rf.ru'


def fillingFields_Sale_Flat(soup,Declaration):
	row = soup.find_all('tr')
	if(len(row) != 0):
		for i in row:
			col = i.find_all('td')
			characteristic = col[0].text.strip('\n\t ')

			if(characteristic == 'Общая площадь'):
				try:
					Declaration['total area'] = int(col[1].text.strip('\n\t '))
				except ValueError:
					Declaration['total area'] = float(col[1].text.strip('\n\t '))	
			elif(characteristic == 'Количество комнат'):
				Declaration['number rooms'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Этаж'):
				Declaration['floor'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Этажность'):
				Declaration['number of storeys'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Жилая площадь'):
				try:
					Declaration['living space'] = int(col[1].text.strip('\n\t '))
				except ValueError:
					Declaration['living space'] = float(col[1].text.strip('\n\t '))	
			elif(characteristic == 'Площадь кухни'):
				try:
					Declaration['kitchen area'] = int(col[1].text.strip('\n\t '))
				except ValueError:
					Declaration['kitchen area'] = float(col[1].text.strip('\n\t '))
			elif(characteristic == 'Тип дома'):
				Declaration['type house'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Ремонт'):
				Declaration['repairs'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Санузел'):
				Declaration['bathroom'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Наличие городского телефона'):
				Declaration['city phone'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Наличие интернета'):
				Declaration['internet'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Балкон/лоджия'):
				Declaration['balcony'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Состояние дома'):
				Declaration['condition house'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Наличие лифта'):
				Declaration['elevator'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Наличие мусоропровода'):
				Declaration['garbage chute'] = col[1].text.strip('\n\t ').capitalize()
			else:
				print('=========I DON`T KNOW WATH IS THIS!!!=========')
				print(characteristic)
def fillingFields_Sale_Room(soup,Declaration):
	row = soup.find_all('tr')
	if(len(row) != 0):
		for i in row:
			col = i.find_all('td')
			characteristic = col[0].text.strip('\n\t ')

			if(characteristic == 'Количество хозяев в квартире'):
				Declaration['number hosts'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Площадь комнаты'):
				try:
					Declaration['area room'] = int(col[1].text.strip('\n\t '))
				except ValueError:
					Declaration['area room'] = float(col[1].text.strip('\n\t '))
			elif(characteristic == 'Количество комнат'):
				Declaration['number rooms'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Этаж'):
				Declaration['floor'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Этажность'):
				Declaration['number of storeys'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Жилая площадь'):
				try:
					Declaration['living space'] = int(col[1].text.strip('\n\t '))
				except ValueError:
					Declaration['living space'] = float(col[1].text.strip('\n\t '))	
			elif(characteristic == 'Площадь кухни'):
				try:
					Declaration['kitchen area'] = int(col[1].text.strip('\n\t '))
				except ValueError:
					Declaration['kitchen area'] = float(col[1].text.strip('\n\t '))
			elif(characteristic == 'Тип дома'):
				Declaration['type house'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Ремонт'):
				Declaration['repairs'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Санузел'):
				Declaration['bathroom'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Балкон/лоджия'):
				Declaration['balcony'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Состояние дома'):
				Declaration['condition house'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Наличие лифта'):
				Declaration['elevator'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Наличие мусоропровода'):
				Declaration['garbage chute'] = col[1].text.strip('\n\t ').capitalize()
			else:
				print('=========I DON`T KNOW WATH IS THIS!!!=========')
				print(characteristic)
def fillingFields_Sale_House(soup,Declaration):
	row = soup.find_all('tr')
	if(len(row) != 0):
		for i in row:
			col = i.find_all('td')
			characteristic = col[0].text.strip('\n\t ')

			if(characteristic == 'Общая площадь'):
				try:
					Declaration['total area'] = int(col[1].text.strip('\n\t '))
				except ValueError:
					Declaration['total area'] = float(col[1].text.strip('\n\t '))
			elif(characteristic == 'Количество комнат'):
				Declaration['number rooms'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Площадь участка'):
				try:
					Declaration['land area'] = int(col[1].text.strip('\n\t '))
				except ValueError:
					Declaration['land area'] = float(col[1].text.strip('\n\t '))
			elif(characteristic == 'Продаваемая часть недвижимости'):
				Declaration['sold property'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Удобства'):
				Declaration['facilities'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Материал стен'):
				Declaration['wall material'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Другие строения'):
				Declaration['other buildings'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Наличие электричества'):
				Declaration['availability electricity'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Наличие канализации'):
				Declaration['sewerage'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Проведена вода'):
				Declaration['there is water'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Проведен газ'):
				Declaration['gas'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Наличие отопления'):
				Declaration['areavailability of heating'] = col[1].text.strip('\n\t ').capitalize()
			else:
				print('=========I DON`T KNOW WATH IS THIS!!!=========')
				print(characteristic)
def fillingFields_Sale_Commercial(soup,Declaration):
	row = soup.find_all('tr')
	if(len(row) != 0):
		for i in row:
			col = i.find_all('td')
			characteristic = col[0].text.strip('\n\t ')

			if(characteristic == 'Общая площадь'):
				try:
					Declaration['total area'] = int(col[1].text.strip('\n\t '))
				except ValueError:
					Declaration['total area'] = float(col[1].text.strip('\n\t '))
			else:
				print('=========I DON`T KNOW WATH IS THIS!!!=========')
				print(characteristic)
def fillingFields_Sale_nonResidential_Garage(soup,Declaration):
	row = soup.find_all('tr')
	if(len(row) != 0):
		for i in row:
			col = i.find_all('td')
			characteristic = col[0].text.strip('\n\t ')

			if(characteristic == 'ГСК'):
				Declaration['gsk'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Длина гаража'):
				try:
					Declaration['length'] = int(col[1].text.strip('\n\t '))
				except ValueError:
					Declaration['length'] = float(col[1].text.strip('\n\t '))
			elif(characteristic == 'Ширина гаража'):
				try:
					Declaration['width'] = int(col[1].text.strip('\n\t '))
				except ValueError:
					Declaration['width'] = float(col[1].text.strip('\n\t '))
			elif(characteristic == 'Материал стен'):
				Declaration['wall material'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Наличие электричества'):
				Declaration['electricity'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Наличие смотровой ямы'):
				Declaration['presence of pit'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Наличие подвала'):
				Declaration['basement'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Наличие погреба'):
				Declaration['cellar'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Тип объекта'):
				Declaration['object type'] = col[1].text.strip('\n\t ').capitalize()
			else:
				print('=========I DON`T KNOW WATH IS THIS!!!=========')
				print(characteristic)
def fillingFields_Sale_nonResidential_Dacha(soup,Declaration):
	row = soup.find_all('tr')
	if(len(row) != 0):
		for i in row:
			col = i.find_all('td')
			characteristic = col[0].text.strip('\n\t ')

			if(characteristic == 'Садовое товарищество'):
				Declaration['garden community'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Площадь участка'):
				try:
					Declaration['land area'] = int(col[1].text.strip('\n\t '))
				except ValueError:
					Declaration['land area'] = float(col[1].text.strip('\n\t '))
			elif(characteristic == 'Другие постройки'):
				Declaration['other buildings'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Наличие электричества'):
				Declaration['electricity'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Проведена вода'):
				Declaration['there is water'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Проведен газ'):
				Declaration['gas'] = col[1].text.strip('\n\t ').capitalize()
			else:
				print('=========I DON`T KNOW WATH IS THIS!!!=========')
				print(characteristic)
def fillingFields_Sale_nonResidential_Other(soup,Declaration):
	row = soup.find_all('tr')
	if(len(row) != 0):
		print('=========I DON`T KNOW WATH IS THIS!!!=========')
def fillingFields_Sale_Building_land(soup,Declaration):
	row = soup.find_all('tr')
	if(len(row) != 0):
		for i in row:
			col = i.find_all('td')
			characteristic = col[0].text.strip('\n\t ')

			if(characteristic == 'Площадь участка'):
				try:
					Declaration['land area'] = int(col[1].text.strip('\n\t '))
				except ValueError:
					Declaration['land area'] = float(col[1].text.strip('\n\t '))
			elif(characteristic == 'Другие строения'):
				Declaration['other buildings'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Наличие электричества'):
				Declaration['electricity'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Проведена вода'):
				Declaration['there is water'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Проведен газ'):
				Declaration['gas'] = col[1].text.strip('\n\t ')
			else:
				print('=========I DON`T KNOW WATH IS THIS!!!=========')
				print(characteristic)

def fillingFields_Rental_Flat(soup,Declaration):
	row = soup.find_all('tr')
	if(len(row) != 0):
		for i in row:
			col = i.find_all('td')
			characteristic = col[0].text.strip('\n\t ')

			if(characteristic == 'Общая площадь'):
				try:
					Declaration['total area'] = int(col[1].text.strip('\n\t '))
				except ValueError:
					Declaration['total area'] = float(col[1].text.strip('\n\t '))
			elif(characteristic == 'Количество комнат'):
				Declaration['number rooms'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Этаж'):
				Declaration['floor'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Этажность'):
				Declaration['number of storeys'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Жилая площадь'):
				try:
					Declaration['living space'] = int(col[1].text.strip('\n\t '))
				except ValueError:
					Declaration['living space'] = float(col[1].text.strip('\n\t '))	
			elif(characteristic == 'Площадь кухни'):
				try:
					Declaration['kitchen area'] = int(col[1].text.strip('\n\t '))
				except ValueError:
					Declaration['kitchen area'] = float(col[1].text.strip('\n\t '))
			elif(characteristic == 'Тип дома'):
				Declaration['type house'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Ремонт'):
				Declaration['repairs'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Санузел'):
				Declaration['bathroom'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Наличие городского телефона'):
				Declaration['city phone'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Наличие мебели'):
				Declaration['furniture'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Наличие бытовой техники'):
				Declaration['household appliances'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Наличие интернета'):
				Declaration['internet'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Балкон/лоджия'):
				Declaration['balcony'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Состояние дома'):
				Declaration['condition house'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Наличие лифта'):
				Declaration['elevator'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Наличие мусоропровода'):
				Declaration['garbage chute'] = col[1].text.strip('\n\t ').capitalize()
			else:
				print('=========I DON`T KNOW WATH IS THIS!!!=========')
				print(characteristic)
def fillingFields_Rental_Room(soup,Declaration):
	row = soup.find_all('tr')
	if(len(row) != 0):
		for i in row:
			col = i.find_all('td')
			characteristic = col[0].text.strip('\n\t ')

			if(characteristic == 'Количество хозяев в квартире'):
				Declaration['number hosts'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Площадь комнаты'):
				try:
					Declaration['area room'] = int(col[1].text.strip('\n\t '))
				except ValueError:
					Declaration['area room'] = float(col[1].text.strip('\n\t '))
			elif(characteristic == 'Количество комнат'):
				Declaration['number rooms'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Этаж'):
				Declaration['floor'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Этажность'):
				Declaration['number of storeys'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Жилая площадь'):
				try:
					Declaration['living space'] = int(col[1].text.strip('\n\t '))
				except ValueError:
					Declaration['living space'] = float(col[1].text.strip('\n\t '))	
			elif(characteristic == 'Площадь кухни'):
				try:
					Declaration['kitchen area'] = int(col[1].text.strip('\n\t '))
				except ValueError:
					Declaration['kitchen area'] = float(col[1].text.strip('\n\t '))
			elif(characteristic == 'Тип дома'):
				Declaration['type house'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Ремонт'):
				Declaration['repairs'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Санузел'):
				Declaration['bathroom'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Балкон/лоджия'):
				Declaration['balcony'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Состояние дома'):
				Declaration['condition house'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Наличие лифта'):
				Declaration['elevator'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Наличие мусоропровода'):
				Declaration['garbage chute'] = col[1].text.strip('\n\t ').capitalize()
			else:
				print('=========I DON`T KNOW WATH IS THIS!!!=========')
				print(characteristic)
def fillingFields_Rental_House(soup,Declaration):
	row = soup.find_all('tr')
	if(len(row) != 0):
		for i in row:
			col = i.find_all('td')
			characteristic = col[0].text.strip('\n\t ')

			if(characteristic == 'Общая площадь'):
				try:
					Declaration['total area'] = int(col[1].text.strip('\n\t '))
				except ValueError:
					Declaration['total area'] = float(col[1].text.strip('\n\t '))
			elif(characteristic == 'Количество комнат'):
				Declaration['number rooms'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Площадь участка'):
				try:
					Declaration['land area'] = int(col[1].text.strip('\n\t '))
				except ValueError:
					Declaration['land area'] = float(col[1].text.strip('\n\t '))
			elif(characteristic == 'Продаваемая часть недвижимости'):
				Declaration['sold property'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Удобства'):
				Declaration['facilities'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Материал стен'):
				Declaration['wall material'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Другие строения'):
				Declaration['other buildings'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Наличие электричества'):
				Declaration['availability electricity'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Наличие канализации'):
				Declaration['sewerage'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Проведена вода'):
				Declaration['there is water'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Проведен газ'):
				Declaration['gas'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Наличие отопления'):
				Declaration['areavailability of heating'] = col[1].text.strip('\n\t ').capitalize()
			else:
				print('=========I DON`T KNOW WATH IS THIS!!!=========')
				print(characteristic)
def fillingFields_Rental_Commercial(soup,Declaration):
	row = soup.find_all( 'tr' )
	if(len(row) != 0):
		for i in row:
			col = i.find_all('td')
			characteristic = col[0].text.strip('\n\t ')

			if(characteristic == 'Общая площадь'):
				try:
					Declaration['total area'] = int(col[1].text.strip('\n\t '))
				except ValueError:
					Declaration['total area'] = float(col[1].text.strip('\n\t '))
			else:
				print('=========I DON`T KNOW WATH IS THIS!!!=========')
				print(characteristic)
def fillingFields_Rental_nonResidential_Garage(soup,Declaration):
	row = soup.find_all('tr')
	if(len(row) != 0):
		for i in row:
			col = i.find_all('td')
			characteristic = col[0].text.strip('\n\t ')

			if(characteristic == 'ГСК'):
				Declaration['gsk'] = col[1].text.strip('\n\t ')
			elif(characteristic == 'Длина гаража'):
				try:
					Declaration['length'] = int(col[1].text.strip('\n\t '))
				except ValueError:
					Declaration['length'] = float(col[1].text.strip('\n\t '))
			elif(characteristic == 'Ширина гаража'):
				try:
					Declaration['width'] = int(col[1].text.strip('\n\t '))
				except ValueError:
					Declaration['width'] = float(col[1].text.strip('\n\t '))
			elif(characteristic == 'Материал стен'):
				Declaration['wall material'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Наличие электричества'):
				Declaration['electricity'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Наличие подвала'):
				Declaration['basement'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Наличие погреба'):
				Declaration['cellar'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Тип объекта'):
				Declaration['object type'] = col[1].text.strip('\n\t ').capitalize()
			else:
				print('=========I DON`T KNOW WATH IS THIS!!!=========')
				print(characteristic)
def fillingFields_Rental_nonResidential_Dacha(soup,Declaration):
	row = soup.find_all('tr')
	if(len(row) != 0):
		print('=========I DON`T KNOW WATH IS THIS!!!=========')
def fillingFields_Purchase_Residential_Properties(soup,Declaration):
	row = soup.find_all('tr')
	if(len(row) != 0):
		for i in row:
			col = i.find_all('td')
			characteristic = col[0].text.strip('\n\t ')

			if(characteristic == 'Продаваемая часть недвижимости'):
				Declaration['sold property'] = col[1].text.strip('\n\t ').capitalize()
			else:
				print('=========I DON`T KNOW WATH IS THIS!!!=========')
				print(characteristic)
def fillingFields_Purchase_Commercial_Property(soup,Declaration):
	row = soup.find_all('tr')
	if(len(row) != 0):
		for i in row:
			col = i.find_all('td')
			characteristic = col[0].text.strip('\n\t ')

			if(characteristic == 'Тип коммерческого объекта'):
				Declaration['type commercial object'] = col[1].text.strip('\n\t ').capitalize()
			else:
				print('=========I DON`T KNOW WATH IS THIS!!!=========')
				print(characteristic)
def fillingFields_Exchange_Residential_Properties(soup,Declaration):
	row = soup.find_all('tr')
	if(len(row) != 0):
		for i in row:
			col = i.find_all('td')
			characteristic = col[0].text.strip('\n\t ')

			if(characteristic == 'Общая площадь'):
				try:
					Declaration['total area'] = int(col[1].text.strip('\n\t '))
				except ValueError:
					Declaration['total area'] = float(col[1].text.strip('\n\t '))
			elif(characteristic == 'Этаж'):
				Declaration['floor'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Этажность'):
				Declaration['number of storeys'] = int(col[1].text.strip('\n\t '))
			elif(characteristic == 'Жилая площадь'):
				try:
					Declaration['living space'] = int(col[1].text.strip('\n\t '))
				except ValueError:
					Declaration['living space'] = float(col[1].text.strip('\n\t '))	
			elif(characteristic == 'Площадь кухни'):
				try:
					Declaration['kitchen area'] = int(col[1].text.strip('\n\t '))
				except ValueError:
					Declaration['kitchen area'] = float(col[1].text.strip('\n\t '))
			elif(characteristic == 'Тип дома'):
				Declaration['type house'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Ремонт'):
				Declaration['repairs'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Санузел'):
				Declaration['bathroom'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Наличие городского телефона'):
				Declaration['city phone'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Наличие интернета'):
				Declaration['internet'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Балкон/лоджия'):
				Declaration['balcony'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Наличие лифта'):
				Declaration['elevator'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Состояние дома'):
				Declaration['condition house'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Наличие мусоропровода'):
				Declaration['garbage chute'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Меняю на тип недвижимости'):
				Declaration['exchange for'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Размен'):
				Declaration['type exchange'] = col[1].text.strip('\n\t ').capitalize()
			elif(characteristic == 'Продаваемая часть недвижимости'):
				Declaration['sold property'] = col[1].text.strip('\n\t ').capitalize()
			else:
				print('=========I DON`T KNOW WATH IS THIS!!!=========')
				print(characteristic)
def fillingFields_Rent_Residential_Properties(soup,Declaration):
	row = soup.find_all('tr')
	if(len(row) != 0):
		for i in row:
			col = i.find_all('td')
			characteristic = col[0].text.strip('\n\t ')

			if(characteristic == 'Продаваемая часть недвижимости'):
				Declaration['sold property'] = col[1].text.strip('\n\t ')
			else:
				print('=========I DON`T KNOW WATH IS THIS!!!=========')
				print(characteristic)

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
	# title = soup.find('h1')
	title = soup.findAll('div', class_ = 'col-md-9')[1]
	title = title.find('h1')
	if(title is not None):
		title = title.text
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
	description = soup.find('blockquote')
	if (description != None):
		Declaration['description'] = description.text.strip('\n\t ')
	else:
		Declaration['description'] = 'no information'	

	#------------------Дата опубликования-----------------------------------------------------------
	Declaration['date'] = soup.find('p', class_='detailDate').text[14:24]

	#------------------Адрес объекта----------------------------------------------------------------
	Declaration['address'] = soup.find('div', class_='col-md-7').find('p').text

	#------------------Информация об авторе---------------------------------------------------------
	phone = soup.find('div', class_='panel-body')
	if(phone is not None):
		phone = phone.find('img')
		phone = phone['src']
		phone = baseUrl + phone
		Declaration['about author'] =  phone

	#------------------URL объявления---------------------------------------------------------------
	Declaration['url'] = urlDeclaration

	#------------------Общее число просмотров-------------------------------------------------------
	views = soup.findAll('div', class_='col-md-6')[0]
	views = views.find('p').text.strip('\n\t ').split(' ')
	views = int(views[2])
	Declaration['number of views'] = views

	#------------------Основные поля----------------------------------------------------------------
	if(len(keyWords) >= 3):
		if(keyWords[1] == 'продажа'):
			Declaration['type transaction'] = 'продажа'
			if(keyWords[2] == 'квартиры'):
				Declaration['property type'] = 'Квартиры'
				Declaration['new building/Resale'] = keyWords[3].strip('\n\t ').capitalize() 
				fillingFields_Sale_Flat(soup,Declaration)
			elif(keyWords[2] == 'комнаты'):
				Declaration['property type'] = 'Комнаты'
				fillingFields_Sale_Room(soup,Declaration)
			elif(keyWords[2] == 'дома'):
				Declaration['property type'] = 'Дома'
				fillingFields_Sale_House(soup,Declaration)
			elif(keyWords[2] == 'коммерческая недвижимость'):
				Declaration['property type'] = 'Коммерческая недвижимость'
				fillingFields_Sale_Commercial(soup,Declaration)
			elif(keyWords[2] == 'нежилая недвижимость'):
				Declaration['property type'] = 'Нежилая недвижимость'
				if(keyWords[3] == 'гаражи, стоянки'):
					Declaration['property non-residential type'] = 'Гаражи, стоянки'
					fillingFields_Sale_nonResidential_Garage(soup,Declaration)
				elif(keyWords[3] == 'дачи, участки'):
					Declaration['property non-residential type'] = 'Дачи, участки'
					fillingFields_Sale_nonResidential_Dacha(soup,Declaration)
				elif(keyWords[3] == 'другие объекты'):
					Declaration['property non-residential type'] = 'Другие объекты'
					fillingFields_Sale_nonResidential_Other(soup,Declaration)
			elif(keyWords[2] == 'участки под строительство'):
				Declaration['property type'] = 'Нежилая недвижимость'
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
	else:
		pass

	MassDeclaration.append(Declaration)


def main():
	html = get_html(baseUrl + '/nedvizimost/?page=1')
	countPage = getPageCount(html)


	for i in range(1,countPage + 1):
		urlPage = baseUrl + '/nedvizimost/?page=' + str(i)
		html = get_html(urlPage)
		soup = BeautifulSoup(html, 'html.parser')
		divContent = soup.find('div', class_ = 'col-md-9 cusDirStyle')
		massItm = divContent.findAll('div',class_ = 'col-md-12 catItem unpad premium')
		massItm = massItm + divContent.findAll('div',class_ = 'col-md-12 catItem unpad')

		for j in massItm:
			a = j.find('a')
			href = a['href']
			urlDeclaration = baseUrl + href
			print(urlDeclaration)
			htmlDeclaration = get_html(urlDeclaration)
			parse(htmlDeclaration, urlDeclaration)





if __name__ == '__main__':
	MassDeclaration = []
	print('Я работаю, я не завис...')
	main()

	count = 0
	with open( 'data.json', 'w', encoding = "utf-8" ) as fp:
		fp.write( u'{\n' )
		for i in MassDeclaration:
			fp.write( u'\t"' + str( count ) + '" : ' )
			json.dump( i, fp, sort_keys = True, indent = 5, ensure_ascii = False )
			fp.write( u',\n' )
			count += 1
		fp.write( u'\t"count declaration" : ' + str(count-1) + '\n' )
		fp.write( u'}\n' )
		fp.close()

	print( 'Я закончил работу' )