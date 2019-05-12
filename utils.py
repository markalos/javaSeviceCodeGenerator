import json

empty_line = ''

def upperFirst(s : str):
	return s[0].upper() + s[1:]

def loadJson(fname : str):
	with open(fname, 'r') as json_file :
		code = json.load(json_file)
	return code

def writeToFile(fname, data):
	with open(fname, 'w') as fout:
		fout.write(data)

def fileNameForModel(name : str):
	return '{}.java'.format(upperFirst(name))