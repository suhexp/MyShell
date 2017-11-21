import json

message_text = 'Hello User  '
print('message text:', message_text)

message_object = {'message': message_text, 'from': 'User1'}

print('message object', message_object)

message_string = json.dumps(message_object)
print('message string', message_string)
message_bytes = message_string.encode('utf-8')
print('message bytes', message_bytes)
