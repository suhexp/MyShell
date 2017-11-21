import sys
import socket
import datetime
import json

if __name__ =='__main__':
    sock = socket.socket()
    sock.bind(('localhost',8004))
    sock.listen(5)

    while True:
        try:
            client, addr = sock.accept()
            print('='*50,'\nConnected with {} \n'.format(addr), '='*50)
            #dt=datetime.datetime()
            #dt_str = dt.strftime('%d-%B-%Y')
            message_text = 'Hello User  '

            #print('message text:', message_text)

            message_object = {'message': message_text, 'from': 'User1'}

            #print('message object', message_object)

            message_string = json.dumps(message_object)
            #print('message string', message_string)
            message_bytes = message_string.encode('utf-8')
            #print('message bytes', message_bytes)

            client.send(message_bytes)
            client.close()


        except KeyboardInterrupt:
            print('='*50, '\n Server stopped.\n', '='*50)
            sock.close()
            sys.exit()
        except Exception as err:
            print(err)
        
            sock.close()
            sys.exit()
