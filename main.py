#!/usr/local/bin/python
#coding=utf-8

import read_input, change_to_roman_numerals, \
		change_to_earth_numerals, price, answers

def main():
	"""
	Main program to process input file and generate required answers
	"""
	input_content = read_input.read_input("input.txt")
	currency = change_to_roman_numerals.change_to_roman_numerals(input_content)
	unit_price = price.calculate_unit_price(input_content, currency)
	answers.get_answers(input_content, currency, unit_price)

if __name__ == "__main__":
    main()