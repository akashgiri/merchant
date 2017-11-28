#!/usr/local/bin/python
#coding=utf-8

import re
import change_to_earth_numerals

def get_resources_list(input_content):
	if "resource_lines" not in input_content:
		return []

	resources = []
	for line in input_content["resource_lines"]:
		line = line.split()
		is_index = line.index("is")
		if is_index > 0:
			resources.append(line[is_index-1])

	return resources

def calculate_unit_price(input_content, currency):
	"""

	"""
	price = {}

	resources = get_resources_list(input_content)

	for line in input_content["resource_lines"]:
		roman_sum = ''
		earth_sum = ''
		value_number = 0

		for resource in resources:
			if re.search(resource, line) != None:
				data = line.split(resource)

				for i in data[0].split(' '):
					if i:
						roman = currency[i]
						roman_sum = roman_sum.join(['',roman])
						earth_sum = change_to_earth_numerals.change_to_earth_numerals(roman_sum)

				for i in data[1].split(' '):
					if i.isdigit():
						value_number = float(i)        #单价可能含小数

				price[resource] = value_number / earth_sum
	return price


def calculate_unit_price_back(input_content, currency):
	"""

	"""
	price = {}

	for key, value in input_content.items():
		if key == 'resource_lines':
			for line in value:
				roman_sum = ''
				earth_sum = ''
				value_number = 0

				resources = get_resources_list()
				for resource in ['Silver','Gold','Iron']:
					if re.search(resource,line) != None:
						data = line.split(resource)

						for i in data[0].split(' '):
							if i:
								roman = currency[i]
								roman_sum = roman_sum.join(['',roman])
								earth_sum = change_to_earth_numerals.change_to_earth_numerals(roman_sum)

						for i in data[1].split(' '):
							if i.isdigit():
								value_number = float(i)        #单价可能含小数

						price[resource] = value_number / earth_sum
	return price

if __name__ == "__main__":
    cal_unit_price('glob glob Silver is 34 Credits')