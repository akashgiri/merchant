#!/usr/local/bin/python
#coding=utf-8

import re

import translate_to_earth_numerals


def get_answers(info, currency, price):
	"""
	返回模块
	读取相关参数
	返回结果
	"""
	for key,value in info.items():
		if(key=='question_line'):
			for i in value:
				roman_sum=''
				words_total=''
				material=''

				if re.search(r'^how much is',i) != None:
					for words in i.split(' '):
						if currency.has_key(words):
							valuerance=currency[words]
							words_total = words_total.join(['',words])
							words_total = words_total.join(['',' '])
							roman_sum=roman_sum.join(['',valuerance])

					earth_sum = translate_to_earth_numerals.translate_to_earth_numerals(roman_sum)
					print words_total,'is',earth_sum
				elif re.search(r'^how many Credits is',i) != None:
					for words in i.split(' '):
						if currency.has_key(words):
							valuerance = currency[words]
							words_total = words_total.join(['',words])
							words_total = words_total.join(['',' '])
							roman_sum = roman_sum.join(['',valuerance])

						earth_sum = translate_to_earth_numerals.translate_to_earth_numerals(roman_sum)
						if price.has_key(words):
							material_price = price[words]
							material = words
							total_price = earth_sum * material_price
					print words_total,material,'is',int(total_price),'Credits'                      #为了保持与原题输出一致，省略小数点
				else:
					print 'I have no idea what you are talking about'


if __name__ == "__main__":
    #get_answers()
    pass