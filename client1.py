import socket
import json

if __name__ =='__main__':
    sock = socket.socket()
    sock.connect(('localhost',8004))
    message_byt = sock.recv(1024)
    sock.close()
    message_string = message_byt.decode('utf-8')
    message_object = json.loads(message_string)
    from_user = message_object.get('from')
    print('from user:', from_user)
    message_text = message_object.get('message')
    print('message text:', message_text)

