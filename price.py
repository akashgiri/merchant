#!/usr/local/bin/python
#coding=utf-8

import re

import Translate_To_Earth_Numerals


def cal_unit_price(Info,currency):
	"""
	计算单个材料价格
	读取相关信息
	输出一个字典，key为材料，value为价格
	"""
	price={}

	for key,value in Info.items():
		if(key=='condition_line'):
			for condition in value:
				roman_sum=''
				earth_sum=''
				value_number=0

				for temp in ['Silver','Gold','Iron']:
					if re.search(temp,condition) != None:
						sentense = condition.split(temp)

						for i in sentense[0].split(' '):
							if i:
								roman = currency[i]
								roman_sum = roman_sum.join(['',roman])
								earth_sum = Translate_To_Earth_Numerals.Translate_To_Earth_Numerals(roman_sum)

						for i in sentense[1].split(' '):
							if i.isdigit():
								value_number = int(i)

						price[temp] = value_number / earth_sum
	return price

if __name__ == "__main__":
    cal_unit_price('glob glob Silver is 34 Credits')