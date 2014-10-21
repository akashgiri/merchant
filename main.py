#!/usr/local/bin/python
#coding=utf-8

import os
import Read_In,Write_Out,Translate_To_Roman_Numerals,Translate_To_Earth_Numerals,Per_Price,Answers


def main():
	"""
	主函数

	"""
	Info = Read_In.Read_In()
	Currency = Translate_To_Roman_Numerals.Translate_To_Roman_Numerals(Info)
	Price = Per_Price.Per_Price(Info,Currency)
	Answers.Answers(Info,Currency,Price)


if __name__ == "__main__":
    main()