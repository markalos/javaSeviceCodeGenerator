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

		modelFields = []
		for key in entityFields.keys():
			modelFields.append({'name' : key, 'type' : entityFields[key]['type']})

		allFields = modelFields

		models = [{'name' : self.entity['name'], "fields" : modelFields}]

		modelNames = set()
		for key in entityFields.keys():
			names = entityFields[key]['refed']
			modelNames.update(names)

		
		print(allFields, 'allfileds')

		for name in modelNames:
			modelFields = []
			for key in entityFields.keys():
				if name in entityFields[key]['refed']:
					modelFields.append({'name' : key, 'type' : entityFields[key]['type']})
			models.append({
							'name' : name,
							'fields' : modelFields
						})

		return models
		

	def generateForModel(self, model):
		self.classStartLine = "public class {} {{".format(utils.upperFirst(model["name"]))
		lines = [self.packageLine, utils.empty_line,self.classStartLine]
		lines.extend(self.generateFiledLies(model['fields']))
		lines.append(self.endLine)
		return '\n'.join(lines)

	def generateFiledLies(self, fields):
		lines = [utils.empty_line]
		for field in fields :
			lines.append(self.lineForField(field))
		lines.append(utils.empty_line)
		return lines

		