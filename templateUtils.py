import copy
import re

def getInterfaceImpl(template):
	template = copy.deepcopy(template)
	template['file'].replace('Impl', '')
	for k in template.keys():
		template[k] = re.sub(r' {[\s\S]*}', ';', template[k])
		template[k] = re.sub(r' extend \w+<\w+>', '', template[k])
	return template