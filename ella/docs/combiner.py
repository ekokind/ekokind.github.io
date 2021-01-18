from os import listdir
from os.path import isfile, join

path = "**PATH**"
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

with open('**PATH**\\**REPO**-merged.csv', 'w', encoding="utf-8") as outfile:
	for fname in onlyfiles:
		with open(path + '\\' + fname, 'r', encoding='mac_roman') as infile:
			outfile.write(infile.read())

