#!/usr/bin/python3

import pandas as pd


def main():
	''' main function'''

	filename='Marathon-Log.csv'
	df = pd.read_csv(filename)
	print(df)


if __name__ == '__main__':
	main()
