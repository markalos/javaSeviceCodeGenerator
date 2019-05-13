import utils
from Interface import Interface

class DaoInterface(Interface):
	def __init__(self, code, models, templateFile):
		super().__init__(code, models)
		self.template = utils.loadJson(templateFile)





	
		