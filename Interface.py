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

	def getModel(self, name):
		for model in self.models:
			if name ==  model['name']:
				return model

	def getCode(self):
		lines = [self.packageLine, utils.empty_line, self.interfaceLine]
		methodsLines = self.getMethodsLines()
		lines.extend(methodsLines)
		lines.append(self.endLine)
		return '\n'.join(lines)

	def incarnateEntity(self, template):
		template = template.replace('Entity', self.EntityName)
		template = template.replace('entity', self.entityName)
		return template

	def getMethodsLines(self):
		template = self.template['createLine']

		createLine = self.incarnateEntity(template)

		lines = [utils.empty_line, createLine, utils.empty_line]
		lines.extend(self.getOrDelLines('get'))
		lines.append(utils.empty_line)
		lines.extend(self.getOrDelLines('delete'))
		lines.append(utils.empty_line)
		lines.extend(self.updateLines())
		lines.append(utils.empty_line)
		return lines

	def generateFormalParam(self, param):
		if self.inModels(param):
			res = utils.upperFirst(param) + ' ' + param
		else :
			if isinstance(param, str):
				param = [param]
			res = ['{} {}'.format(self.entityModel[p], p)for p in param]
			res = ', '.join(res)
		return res

	def generateCode(self):
		utils.writeToFile(
			'{}{}.java'.format(self.EntityName,self.template['file']),
			self.getCode()
			)

	def getOrDelLines(self, getOrDel):
		lines = []
		template = self.template['{}Line'.format(getOrDel)]
		template = self.incarnateEntity(template)
		params = self.code['methods'][getOrDel]
		for param in params:
			query = self.generateFormalParam(param)
			lines.append(template.replace('Query', query))
		return lines

	def updateLines(self):
		lines = []
		template = self.template['updateLine']
		template = self.incarnateEntity(template)
		params = self.code['methods']['update']

		for param in params:
			query = self.generateFormalParam(param['query'])
			if 'set' not in param:
				update = self.entityName
			else :
				update = param['set']
			update = self.generateFormalParam(update)
			lines.append(
				template.replace('Query', query).replace('Update', update)
				)
		return lines

	def generateGetter(self, field):
		if field['type'] in ['Boolean', 'boolean']:
			template = 'is{}'
		else :
			template = 'get{}'
		return template.format(utils.upperFirst(field['name']))

	def generateSetter(self, field):
		template = 'get{}'
		return template.format(utils.upperFirst(field['name']))

	def generateQueryOp(self, param):
		return ""

		
		




