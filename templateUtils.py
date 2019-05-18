import copy
import re

def getInterfaceImpl(template):
	template = copy.deepcopy(template)
	template['file'] = template['file'].replace('Impl', '')
	print(template['file'])
	for k in template.keys():
		template[k] = re.sub(r' {\n\t[\s\S]*\n\t}', ';', template[k])
		template[k] = re.sub(r' extend \w+<\w+>', '', template[k])
	return template