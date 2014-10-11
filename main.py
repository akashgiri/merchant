#!/usr/local/bin/python
#coding=utf-8

import os
import Read_In,Write_Out,Translate_To_Roman_Numerals,Translate_To_Earth_Numerals


def main():
	Info = Read_In();
	Translate_To_Roman_Numerals(Info);
	Translate_To_Earth_Numerals();
	Write_Out();



if __name__ == "__main__":
    main()