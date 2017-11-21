import json

message_text = 'Hello world'

print('message text:', message_text)

message_object = {'message':message_text, 'from':'User1'}

print('message object', message_object)

message_string = json.dumps(message_object)

print('message string', message_string)

message_bytes = message_string.encode('utf-8')

print('message bytes', message_bytes)

'''
По прошествии всей цепочки преобразований данные будут прегодны для отправки на сервер

import socket

sock = socket.socket()

socket.connect(('<HOST>', <PORT>))

socket.send(message_bytes)
'''

'''
Для того чтобы преобразовать данные на сервере из набора байтов обратно в json
можно выполнить следующую цепочку преобразований после получения запроса от клиента

import socket

...

client, addr = sock.accept()

message_bytes = client.recv(1024)

'''
print('='*50)
message_string = message_bytes.decode('utf-8')

print('message string:', message_string)

message_object = json.loads(message_string)

print('message object:', message_object)

from_user = message_object.get('from')

print('from user:', from_user)

message_text = message_object.get('message')

print('message text:', message_text)
