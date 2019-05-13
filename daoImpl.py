import utils
from Interface import Interface

class Interface(object):
	"""docstring for Interface"""
	def __init__(self, code, models, templateFile):
		super().__init__(code, models)
		self.code = code
		self.models = models
		self.templateFile = templateFile
		self.template = utils.loadJson(templateFile)

	def eqOpForField(self, param):
		eqOne = self.template['eqOne']
		return eqOne.replace('field', param).replace('Field', param)

	def eqOpForModel(self, modelName):
		model = self.getModel(modelName)
		queryOp = []
		prefix = '{}.'.format(modelName)
		for field in model['fields']:
			eqOne = self.template['eqOne']
			eqOne = eqOne.replace('field', field['name'])
			eqOne = eqOne.replace('field', prefix + self.generateGetter(field))
			queryOp.append(eqOne)
		if len(queryOp) == 1:
			return queryOp[0]
		else :
			queryOp = ',\n'.join(queryOp)
			self.template['eqMany'].replace('eqOnes', queryOp)


	def generateQueryOp(self, param):
		template = self.template
		
		if self.inModels(param):
			return self.eqOpForModel(param)
		else :
			if isinstance(param, str):
				return self.eqOpForField(param)
			queryOp = [self.eqOpForField(p) for p in param]
			queryOp = ',\n'.join(queryOp)
			return template['eqMany'].replace('eqOnes', queryOp)

	def updateCodeForField(self, param):
		return 'var updateMap = Map.of({});'.format(self.mapCodeForField(param))

	def mapCodeForField(self, param):
		return '"{}", {}'.format(param, param)

	def updateCodeForFields(self, param):
		code = [self.mapCodeForField(p) for p in param]
		code = ',\n'.join(code)
		code = 'var updateMap = Map.of({});'.format(code)
		return code

	def updateCodeForModel(self, modelName, queryParam):
		pass

	def generateUpdateCode(self, param, queryParam):
		template = self.template
		
		if self.inModels(param):
			return self.eqOpForModel(param)
		else :
			if isinstance(param, str):
				return self.updateCodeForField(param)
			return self.updateCodeForFields(param)
