import requests

'''
url for get token: 
https://oauth.vk.com/authorize?client_id=3682744&v=5.53&scope=messages,docs,offline&redirect_uri=http://oauth.vk.com/blank.html&display=page&response_type=token
'''
TOKEN = '___TOKEN___'
IMAGE = 'mlg.png'
PEER = '000' #user_id or chat_id + 2000000000

def apiReq(method, params):
	r = requests.post('https://api.vk.com/method/' + method + '?access_token=' + TOKEN + '&v=5.53', data = params)
	
	return r.json()
	
def sendFile(url, file_name):
	files = {'file': open(file_name, 'rb')}
	r = requests.post(url, files = files)
	
	return r.json()
	
upload_url = apiReq('docs.getUploadServer', {'type': 'graffiti'})['response']['upload_url']
file_secret = sendFile(upload_url, 'll.png')['file']
save_data = apiReq('docs.save', {'file': file_secret})['response'][0]
atach_name = 'doc' + str(save_data['owner_id']) + '_' + str(save_data['id'])

res = apiReq('messages.send', {'peer_id': PEER, 'attachment': atach_name})
print(res)
