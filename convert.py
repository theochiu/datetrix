import pandas as pd
from pprint import pprint
import sys

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
	for i in range(len(desc)):
		mat_dict.update({desc[i] : rank[i]})

	return mat_dict

def output_html(mat_dict, template_name, out_path):
	with open(template_name, "r") as f:
		template = f.read()

	ind = template.find("<!-- CHECKBOXES -->") + 20		# the string has len=20
	top_half = template[:ind]
	bottom_half = template[ind:]

	insert = ""

	for i, question in enumerate(mat_dict):
		insert += '<div class="form-check">\n'
		insert += '\t<input class="form-check-input" type="checkbox" value="{}"\n'.format(mat_dict[question])
		insert += '\tonclick="update_score();" id="question{}">\n'.format(i)
		insert += '\t<label class="form-check-label" for="question{}">\n'.format(i)
		insert += '\t\t{}\n'.format(question)
		insert += '\t</label>\n'
		insert += '</div>\n\n'

	with open(out_path, "w+") as f:
		f.write(top_half)
		f.write(insert)
		f.write(bottom_half)

		

def main():
	if len(sys.argv) < 2:
		print("Need argument for input file")
		quit()

	matrix = read_spreadsheet(sys.argv[1])
	mat_dict = qual_to_dict(matrix)

	if len(sys.argv) < 3:
		print("No output path given, using default")
		print("Writing index.html to docs/index.html")
		out_path = "docs/index.html"
	else:
		out_path = sys.argv[2]

	output_html(mat_dict, "docs/template.html", out_path)

if __name__ == '__main__':
	matrix = read_spreadsheet("koalifications.xlsx")
	mat_dict = qual_to_dict(matrix)
	output_html(mat_dict, "docs/template.html", "docs/index.html")
