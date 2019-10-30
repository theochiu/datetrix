import pandas as pd
from pprint import pprint

def read_spreadsheet(path):
	df = pd.read_excel(path)
	# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
	# 	print(df)
	heading = list(df.columns)
	matrix = df.values.tolist()
	matrix.insert(0, heading)
	return matrix

def find_indeces(string, matrix):
	for i, row in enumerate(matrix):
		lo_row = [str(item).lower() for item in row]

		if string.lower() in lo_row:
			j = lo_row.index(string)
			return i, j

	return None 	# not found

def qual_to_dict(matrix):
	i1, j1 = find_indeces("description", matrix)
	i2, j2 = find_indeces("red flags", matrix)
	i3, j3 = find_indeces("numeric rating", matrix)

	# print("description = {}, {}".format(i1, j1))
	# print("red flags = {}, {}".format(i2, j2))
	# print("numeric rating = {}, {}".format(i3, j3))

	# populate lists
	desc = [str(row[j1]) for i, row in enumerate(matrix) if i > i1]
	rank = [str(row[j3]) for i, row in enumerate(matrix) if i > i1]

	# remove nans
	if "nan" in desc:
		end = desc.index("nan")
		desc = desc[:end]
		rank = rank[:end]

	mat_dict = {}
	for i in range(len(desc) -1, 0, -1):
		mat_dict.update({desc[i] : rank[i]})

	return mat_dict

def main():
	pass

if __name__ == '__main__':
	matrix = read_spreadsheet("koalifications.xlsx")
	mat_dict = qual_to_dict(matrix)
	
