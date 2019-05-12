import utils
from Interface import Interface

class DaoInterface(Interface):
	def __init__(self, code, models, templateFile):
		super().__init__(code, models)
		self.template = utils.loadJson(templateFile)

	def generateCode(self):
		utils.writeToFile(
			'{}{}.java'.format(self.EntityName,self.template['file']),
			self.getCode()
			)

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





	
		