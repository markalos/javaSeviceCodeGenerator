import utils

class BaseGenerator(object):
	"""docstring for BaseGenerator"""
	def __init__(self, package, entity):
		super().__init__()
		self.package = package
		self.entity = entity

		self.packageLine = "package {};".format(self.package)
		
		self.endLine = "}"

	def lineForField(self, filed):
		return '\tprivate {} {}'.format(filed['type'], filed['name'])

	def generateGetter(self, field):
		if field['type'] in ['Boolean', 'boolean']:
			template = 'is{}()'
		else :
			template = 'get{}()'
		return template.format(utils.upperFirst(field['name']))

	def generateSetter(self, field):
		template = 'set{}'
		return template.format(utils.upperFirst(field['name']))
