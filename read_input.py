#!/usr/local/bin/python
#coding=utf-8

import re

def read_input(file_name):
	"""
	"""
	resource_lines = []
	question_lines = []
	roman_attributes = []
	
	input_content = {'roman_attributes': roman_attributes, \
					 'resource_lines':resource_lines, 'question_lines': question_lines}

	with open(file_name) as txt_file:
		for line in txt_file:
			line = line.strip()
			judge = re.search(r'\?$',line)
			if judge:
				question_lines.append(line)
			else: 
				resource_lines.append(line)

	for condition_case in resource_lines[:]:
		if re.search(r'[IXVLCDM]$',condition_case) != None:
			resource_lines.remove(condition_case)
			roman_attributes.append(condition_case)

	return input_content


if __name__ == "__main__":
    read_file("mission.txt")