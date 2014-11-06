#!/usr/local/bin/python
#coding=utf-8


import read_file

def translate_to_roman_numerals(info):
	"""
		转义为罗马数字模块

		提取输入信息中对星际货币与罗马数字的转换信息


	"""
	translate_to_roman=[[],[],[],[],[],[],[]]
	currency={}


	for key,value in info.items():
		if(key=='condition_roman'):
			for index,number in enumerate(value):
				translate_to_roman[index]=number.split()


	for i in translate_to_roman:
		if i:
			currency[i[0]]=i[2]
	return currency





if __name__ == "__main__":

	info = read_file.read_file()
	translate_to_roman_numerals(info)