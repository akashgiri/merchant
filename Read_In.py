#!/usr/local/bin/python
#coding=utf-8

import re


def Read_In():
	"""
		读取模块

		实现对源文件信息的读取和解析，并将其分为三块内容并返回：已知条件-罗马定义块（condition_roman），
		已知条件-物价计算块（condition_line），未知问题-处理疑问块（question_line）
	"""
	condition_line=[]
	question_line=[]
	condition_roman=[]
	info={'condition_roman':condition_roman,'condition_line':condition_line,'question_line':question_line}

	for line in  open ("mission.txt"):
		judge = re.search(r'\?$',line)
		if judge:
			question_line.append(line)
		else: 
			condition_line.append(line)


	for condition_case in condition_line[:]:
		if re.search(r'[IXVLCDM]$',condition_case) != None:
			condition_line.remove(condition_case)
			condition_roman.append(condition_case)
	return info


if __name__ == "__main__":
    Read_In()