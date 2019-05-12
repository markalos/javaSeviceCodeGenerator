import utils
from ModelGenerator import ModelGenerator
from DaoInterface import DaoInterface

def main():
	codeFileName = 'code.json'
	code = utils.loadJson(codeFileName)
	package = code['package']

	model = ModelGenerator(package, code['entity'])
	models = model.generate()

	DaoInterface(code, models, 'dao_template.json').generateCode()



if __name__ == '__main__':
	main()