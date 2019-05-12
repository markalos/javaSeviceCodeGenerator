import utils

class Interface(object):
	def __init__(self, code, models):
		super().__init__()
		self.package = code['package']
		self.code = code
		self.models = models

		self.entityName = code['entity']['name']
		self.EntityName =  utils.upperFirst(self.entityName)

		self.packageLine = 'package {}.db;'.format(self.package)
		self.interfaceLine = 'public interface {} {{'.format(self.EntityName)
		self.endLine = '}'

		self.entityModel = {}
		for model in models:
			if self.entityName ==  model['name']:
				for field in model['fields']:
					self.entityModel[field['name']] = field['type']
				break

	def inModels(self, name):
		if not isinstance(name, str):
			return False
		for model in self.models:
			if name ==  model['name']:
				return True
		return False

		
		




