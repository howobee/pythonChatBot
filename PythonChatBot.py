import apiai
import json

def textMessage(s):
	# Тoken API request to Dialogflow
	request = apiai.ApiAI('236bc188447948ebb3f75495bc22d06e').text_request()
	# language
	request.lang = 'ru'
	# ID Session 
	request.session_id = 'mizer'
	# Send request to II with message from user_client
	request.query = s
	responseJson = json.loads(request.getresponse().read().decode('utf-8'))
	#get JSON and take a message
	response = responseJson['result']['fulfillment']['speech']
	
	#Check response
	if response:
		return response
	else:
		return '''Я Вас не совсем понял.
		Можете повторить, пожалуйста'''
		  
a = ''
print('Введите "Выход" чтобы выйти из программы ')

while(a!='Выход'):
	s = input('Введите ваш вопрос >>> ')
	print(textMessage(s))