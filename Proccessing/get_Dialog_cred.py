import json
import requests

def get_cred(APIname):
	print 'getting credentials...'
	filename = 'credentials.json'
	print 'importing from:', filename
	cred = open(filename, 'r')
	parsed = json.loads(cred.read())
	cred.close()

	#output = [url, usr, pwd]
	return {'url' : parsed[APIname]['url'],
			'usr' : parsed[APIname]['username'],
			'pwd' : parsed[APIname]['password']}

