import socket
import os

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 45_000))

def get_marks(client):
    get_request_template = \
        """
        GET / HTTP/1.1\r\n
        Host: localhost\r\n\r\n
        """
    client.send(get_request_template.encode('utf-8'))
    response = client.recv(4096)
    print(response.decode('utf-8'))

def add_mark(client):
    subject = input('Введите предмет: ')
    mark = input('Введите оценку (1-5): ').strip()
    if mark not in ['1', '2', '3', '4', '5']:
        return
    body = f"{subject} : {mark}"
    post_request_template = \
        f"""
        POST / HTTP/1.1\r\n
        Host: localhost\r\n
        Content-Length: {len(body.encode('utf-8'))}\r\n\r\n
        {body}
        """
    print('send')
    client.send(post_request_template.encode('utf-8'))
    response = client.recv(4096)
    print(response.decode('utf-8'))

while True:
    os.system('clear')
    print('Журнал оценок')
    print('1. Просмотреть все оценки')
    print('2. Добавить новую оценку')
    print('0. Выход')
    inp = input('Введите цифру -> ')
    if inp == '0':
        break
    if inp == '1':
        get_marks(client)
        input()
    if inp == '2':
        add_mark(client)
        input()
