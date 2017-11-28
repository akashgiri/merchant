#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import read_file

def change_to_roman_numerals(info):
	change_to_roman = []
	currency = {}

	print info

	for key, value in info.items():
		if key == 'condition_roman':
			for index, number in enumerate(value):
				change_to_roman.append(number.split())

	## Currency is the end index
	for i in change_to_roman:
		if i:
			currency[i[0]]=i[-1]

	print change_to_roman
	print currency
	
	return currency

if __name__ == "__main__":

	info = read_file.read_file()
	change_to_roman_numerals(info)
