#!/usr/local/bin/python
# -*- coding: utf-8 -*-

def change_to_roman_numerals(input_content):
	change_to_roman = []
	currency = {}

	print(input_content)

	for key, value in input_content.items():
		if key == 'roman_attributes':
			for index, number in enumerate(value):
				change_to_roman.append(number.split())

	## Currency is the end index
	for i in change_to_roman:
		if i:
			currency[i[0]] = i[-1]

	print("change_to_roman: ", change_to_roman)
	print("currency: ", currency)
	
	return currency