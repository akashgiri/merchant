#!/usr/local/bin/python
#coding=utf-8
import re

VALID_REGEX = "^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

def is_valid_regex(roman_string):
	if re.search(VALID_REGEX, roman_string) != None:
		return True
	
	return False

def keyword_mapping():
	d = {}

	d["IV"] = " 4 "
	d["IX"] = " 9 "
	d["XL"] = " 40 "
	d["XC"] = " 90 "
	d["CD"] = " 400 "
	d["CM"] = " 900 "
	d["I"] = " 1 "
	d["V"] = " 5 "
	d["X"] = " 10 "
	d["L"] = " 50 "
	d["C"] = " 100 "
	d["D"] = " 500 "
	d["M"] = " 1000 "

	return d

def change_to_earth_numerals(roman_string):

	print("roman string: "+roman_string)
	mapping = keyword_mapping()

	if roman_string in mapping:
		return mapping[roman_string]

	return
	if not is_valid_regex(roman_string):
		print('String is not a valid roman numeral')
		return

	NumDic = {"pattern":"","retNum": 0}
	roman_pattern = {
		"0":('','','','M'),
		"1":('CM','CD','D','C',100),
		"2":('XC','XL','L','X',10),
		"3":('IX','IV','V','I',1)
	}
	i = 3
	pattern_items = sorted(roman_pattern.items())
	#print(pattern_items)
	for item in pattern_items[1:]:
		print("item: ", item)
		print("\n")
		patstr = NumDic["pattern"].join(['',item[1][0]])
		if re.search(patstr,roman_string) != None:
			NumDic["retNum"] += 9*item[1][4]
			NumDic["pattern"] = patstr
		else:
			patstr = NumDic["pattern"].join(['',item[1][1]])
			if re.search(patstr,roman_string) != None:
				NumDic["retNum"] += 4*item[1][4]
				NumDic["pattern"] = patstr
			else:
				patstr = NumDic["pattern"].join(['',item[1][2]])
				if re.search(patstr,roman_string) != None:
					NumDic["retNum"] += 5*item[1][4]
					NumDic["pattern"] = patstr

		print("numDic: ", NumDic)
		print("\n")
		if NumDic["pattern"] == '':
			NumDic["pattern"] = '^'
		tempstr = ''
		sum = 0
		for k in range(0,4):
			pstr = item[1][3].join(['','{']).join(['',str(k)]).join(['','}'])
			patstr = NumDic["pattern"].join(['',pstr])
			if re.search(patstr,roman_string) != None:
				sum = k*(10**i)
				tempstr = patstr
		if tempstr !='':
			NumDic["pattern"] = tempstr
		else:
			NumDic["pattern"] = patstr
		NumDic['retNum'] += sum
		i -= 1

	print(NumDic)
	print("\n")
	return NumDic['retNum']	

def change_to_earth_numerals_back2(roman_string):

	print("roman string: "+roman_string)
	#return
	#if re.search('^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$', roman_string) != None:
	#if re.search('^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$', roman_string) != None:
	if re.search('^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$', roman_string) != None:	
		NumDic = {"pattern":"","retNum": 0}
		roman_pattern = {
			"0":('','','','M'),
			"1":('CM','CD','D','C',100),
			"2":('XC','XL','L','X',10),
			"3":('IX','IV','V','I',1)
		}
		i = 3
		pattern_items = sorted(roman_pattern.items())
		#print(pattern_items)
		for item in pattern_items[1:]:
			print("item: ", item)
			print("\n")
			patstr = NumDic["pattern"].join(['',item[1][0]])
			if re.search(patstr,roman_string) != None:
				NumDic["retNum"] += 9*item[1][4]
				NumDic["pattern"] = patstr
			else:
				patstr = NumDic["pattern"].join(['',item[1][1]])
				if re.search(patstr,roman_string) != None:
					NumDic["retNum"] += 4*item[1][4]
					NumDic["pattern"] = patstr
				else:
					patstr = NumDic["pattern"].join(['',item[1][2]])
					if re.search(patstr,roman_string) != None:
						NumDic["retNum"] += 5*item[1][4]
						NumDic["pattern"] = patstr

			print("numDic: ", NumDic)
			print("\n")
			if NumDic["pattern"] == '':
				NumDic["pattern"] = '^'
			tempstr = ''
			sum = 0
			for k in range(0,4):
				pstr = item[1][3].join(['','{']).join(['',str(k)]).join(['','}'])
				patstr = NumDic["pattern"].join(['',pstr])
				if re.search(patstr,roman_string) != None:
					sum = k*(10**i)
					tempstr = patstr
			if tempstr !='':
				NumDic["pattern"] = tempstr
			else:
				NumDic["pattern"] = patstr
			NumDic['retNum'] += sum
			i -= 1

		print(NumDic)
		print("\n")
		return NumDic['retNum']
	else:
		print('String is not a valid Roman numerals')


def change_to_earth_numerals_back(roman_string):

	print("roman string: "+roman_string)
	#if re.search('^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$', roman_string) != None:
	if re.search('^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$', roman_string) != None:
		NumDic = {"pattern":"","retNum": 0}
		roman_pattern = {
			"0":('','','','M'),
			"1":('CM','CD','D','C',100),
			"2":('XC','XL','L','X',10),
			"3":('IX','IV','V','I',1)
		}
		i = 3
		pattern_items = sorted(roman_pattern.items())
		#print(pattern_items)
		for item in pattern_items:
			#print(item)
			#print("\n")
			if item[0] != '0':
				patstr = NumDic["pattern"].join(['',item[1][0]])
				if re.search(patstr,roman_string) != None:
					NumDic["retNum"] += 9*item[1][4]
					NumDic["pattern"] = patstr
				else:
					patstr = NumDic["pattern"].join(['',item[1][1]])
					if re.search(patstr,roman_string) != None:
						NumDic["retNum"] += 4*item[1][4]
						NumDic["pattern"] = patstr
					else:
						patstr = NumDic["pattern"].join(['',item[1][2]])
						if re.search(patstr,roman_string) != None:
							NumDic["retNum"] += 5*item[1][4]
							NumDic["pattern"] = patstr
			print("numDic: ", NumDic)
			if NumDic["pattern"] == '':
				NumDic["pattern"] = '^'
			tempstr = ''
			sum = 0
			for k in range(0,4):
				pstr = item[1][3].join(['','{']).join(['',str(k)]).join(['','}'])
				patstr = NumDic["pattern"].join(['',pstr])
				if re.search(patstr,roman_string) != None:
					sum = k*(10**i)
					tempstr = patstr
			if tempstr !='':
				NumDic["pattern"] = tempstr
			else:
				NumDic["pattern"] = patstr
			NumDic['retNum'] += sum
			i -= 1

		print(NumDic)
		return NumDic['retNum']
	else:
		print('String is not a valid Roman numerals')
