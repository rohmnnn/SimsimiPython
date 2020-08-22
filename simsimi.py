# original code : https://simsimi.github.io/SmallTalk-API/example.html#python

import requests
import os

os.system('cls' if os.name=='nt' else 'clear')

print("Simple SimSimi CLI Python\nby. rhxx\n")
print('='*40)
print('type "end" u/ close\n')
b = raw_input('kamu: ' )
while True:
	if b == 'end':
		exit()
	else:
		headers = {
		    'Content-Type': 'application/json',
		    'x-api-key': 'YOUR-API-KEY-HERE',#W~Xh87uruJ-BzPLKl~lDJG1iqjG0J0eQ74qxxxx_
		}
		data = '{\n            "utext": "'+b+'", \n            "lang": "id" \n     }'
		response = requests.post('https://wsapi.simsimi.com/190410/talk', headers=	headers	, data=data)	
		a=response.json()	
		if a['status'] ==	 200:	
			print('simi: '+a['atext'])	
		else:
			print('maaf simsimi, sedang tidur. error '+a['statusMessage'])
	b = raw_input('kamu: ')
	