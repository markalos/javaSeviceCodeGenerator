import utils
from BaseGenerator import BaseGenerator



class ModelGenerator(BaseGenerator):
	"""generate java code from json model"""
	def __init__(self, package, entity):
		super().__init__(package, entity)

	def generate(self):
		models = self.getModels()
		for model in models:
			utils.writeToFile(
				utils.fileNameForModel(model['name']),
				self.generateForModel(model)
				)
		return models

	def getModels(self):
		
		entityFields = self.entity['fields']
		self.entityName = self.entity['name']

		modelFields = []
		for key in entityFields.keys():
			ftype, fname = key.split(' ')
			modelFields.append({'name' : fname, 'type' : ftype})

		allFields = modelFields

		models = [{'name' : self.entity['name'], "fields" : modelFields}]

		modelNames = set()
		for key in entityFields.keys():
			if 'refed' not in entityFields[key]:
				continue
			names = entityFields[key]['refed']
			modelNames.update(names)

		for name in modelNames:
			modelFields = []
			for key, value in entityFields.items():
				if 'refed' not in value:
					continue
				if name in value['refed']:
					ftype, fname = key.split(' ')
					modelFields.append({'name' : fname, 'type' : ftype})
			models.append({
							'name' : name,
							'fields' : modelFields
						})

		return models
		

	def generateForModel(self, model):
		self.classStartLine = "public class {} {{".format(utils.upperFirst(model["name"]))
		lines = [self.packageLine, utils.empty_line,self.classStartLine]
		lines.extend(self.generateFiledLies(model['fields']))
		if model['name'] != self.entityName:
			lines.extend(self.mapOf(model))
		lines.append(self.endLine)
		return '\n'.join(lines)

	def generateFiledLies(self, fields):
		lines = [utils.empty_line]
		for field in fields :
			lines.append(self.lineForField(field))
		lines.append(utils.empty_line)
		return lines

	def mapOf(self, model):
		
		ofStartLine = '\tpublic static {} of({} {}) {{'
		ofStartCode = ofStartLine.format(utils.upperFirst(model['name']), utils.upperFirst(self.entityName), self.entityName)
		declareLine = '\t\tvar {} = new {}'
		declareCode = declareLine.format(model['name'], utils.upperFirst(model['name']))
		codes = [ofStartCode]
		ofBodyLine = '\t\t{}.{}({}.{});'
		bodyCodes = [ofBodyLine.format(model['name'], self.generateSetter(field), self.entityName, self.generateGetter(field)) for field in model['fields']]
		codes.extend(bodyCodes)
		codes.append('\t}')
		return codes


		