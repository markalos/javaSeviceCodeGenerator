import utils
from ModelGenerator import ModelGenerator
from DaoInterface import DaoInterface
from InterfaceImpl import InterfaceImpl
from templateUtils import getInterfaceImpl

def main():
	codeFileName = 'code.json'
	code = utils.loadJson(codeFileName)
	package = code['package']

	model = ModelGenerator(package, code['entity'])
	models = model.generate()

	InterfaceImpl(code, models, 'dao_impl_template.json').generateCode()

	#template = utils.loadJson('dao_impl_template.json')
	#itemplate = getInterfaceImpl(template)
	



if __name__ == '__main__':
	main()
