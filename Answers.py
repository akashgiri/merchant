#!/usr/local/bin/python
#coding=utf-8
import re
import Translate_To_Earth_Numerals


def Answers(Info,Currency,Price):
	"""
	返回模块

	读取相关参数

	返回结果

	"""
	for key,value in Info.items():
		if(key=='question_line'):
			for i in value:
				Roman_Sum=''
				Words_Total=''
				Material=''
				if re.search(r'^how much is',i) != None:
					for words in i.split(' '):
						if Currency.has_key(words):
							Valuerance=Currency[words]
							Words_Total = Words_Total.join(['',words])
							Words_Total = Words_Total.join(['',' '])
							Roman_Sum=Roman_Sum.join(['',Valuerance])
					Earth_Sum = Translate_To_Earth_Numerals.Translate_To_Earth_Numerals(Roman_Sum)

					print Words_Total,'is',Earth_Sum

				elif re.search(r'^how many Credits is',i) != None:
					for words in i.split(' '):
						if Currency.has_key(words):
							Valuerance=Currency[words]
							Words_Total = Words_Total.join(['',words])
							Words_Total = Words_Total.join(['',' '])
							Roman_Sum=Roman_Sum.join(['',Valuerance])
						Earth_Sum = Translate_To_Earth_Numerals.Translate_To_Earth_Numerals(Roman_Sum)
						if Price.has_key(words):
							Material_Price = Price[words]
							Material = words

					print Words_Total,Material,'is',Earth_Sum,'Credits'

				else:
					print 'I have no idea what you are talking about'


if __name__ == "__main__":
    Answers()