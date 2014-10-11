#!/usr/local/bin/python
#coding=utf-8


import Read_In

def Translate_To_Roman_Numerals(Info):
	"""
		转义为罗马数字模块

		提取输入信息中对星际货币与罗马数字的转换信息
	"""
	Translate_To_Roman=[[],[],[],[],[],[],[]]
	currency={}


	for key,value in Info.items():
		if(key=='condition_roman'):
			for index,number in enumerate(value):
				Translate_To_Roman[index]=number.split()

	for i in Translate_To_Roman:
		if i:
			currency[i[0]]=i[2]

	return currency





if __name__ == "__main__":

	Info = Read_In.Read_In()
	Translate_To_Roman_Numerals(Info)