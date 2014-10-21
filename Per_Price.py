#!/usr/local/bin/python
#coding=utf-8

import re
import Translate_To_Earth_Numerals

def Per_Price(Info,currency):
	"""
	计算单个材料价格

	读取相关信息

	输出一个字典，key为材料，value为价格

	"""
	Price={}
	for key,value in Info.items():
		if(key=='condition_line'):
			for condition in value:
				Roman_Sum=''
				Earth_Sum=''
				Value_Number=0
				for temp in ['Silver','Gold','Iron']:
					if re.search(temp,condition) != None:
						sentense = condition.split(temp)
						for i in sentense[0].split(' '):
							if i:
								Roman = currency[i]
								Roman_Sum = Roman_Sum.join(['',Roman])
								Earth_Sum = Translate_To_Earth_Numerals.Translate_To_Earth_Numerals(Roman_Sum)

						for i in sentense[1].split(' '):
							if i.isdigit():
								Value_Number = int(i)
						Price[temp] = Value_Number/Earth_Sum

	return Price

if __name__ == "__main__":
    Per_Price('glob glob Silver is 34 Credits')