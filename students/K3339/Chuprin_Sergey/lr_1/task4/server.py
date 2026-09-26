import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 40_000))
server.listen()

all_clients = dict()
lock = threading.Lock()

def chat_worker(client, address):
    try:
        while True:
            message = client.recv(1024)
            if not message:
                break
            else:
                for addr in all_clients:
                    if addr != address:
                        text = f'{address}: {message.decode("utf-8")}'
                        all_clients[addr].send(text.encode("utf-8"))
                print(f'{address}: {message.decode("utf-8")}')
    except:
        with lock:
            all_clients.pop(address)
        client.close()
        print(f'{address} отключился')




while True:
    client, address = server.accept()
    print(f'{address} подключился')
    all_clients[address] = client

    t = threading.Thread(target=chat_worker, args=(client, address))
    t.start()


