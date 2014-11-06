#!/usr/local/bin/python
#coding=utf-8

import os
import read_file, translate_to_roman_numerals,translate_to_earth_numerals,price,answers


def main():
	"""
	主函数

	"""
	info = read_file.read_file("mission.txt")
	currency = translate_to_roman_numerals.translate_to_roman_numerals(info)
	get_price = price.cal_unit_price(info, currency)
	answers.get_answers(info,currency,get_price)


if __name__ == "__main__":
    main()