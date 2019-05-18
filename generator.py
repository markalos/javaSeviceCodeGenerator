import utils
from ModelGenerator import ModelGenerator
from DaoInterface import DaoInterface
from InterfaceImpl import InterfaceImpl
from templateUtils import getInterfaceImpl


def generateCode(fname : str):
	codeFileName = 'code.json'
	code = utils.loadJson(codeFileName)
	package = code['package']

	model = ModelGenerator(package, code['entity'])
	models = model.generate()

	template = utils.loadJson(fname)

	InterfaceImpl(code, models, template).generateCode()
	

	DaoInterface(code, models, getInterfaceImpl(template)).generateCode()

def main():
	generateCode('dao_impl_template.json')
	generateCode('service_impl_template.json')

	
	



if __name__ == '__main__':
	main()
