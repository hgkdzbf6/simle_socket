#!/usr/local/python3
import socket
import argparse

class MySocket(socket.socket):
    def __init__(self):
        self.port = 12306
        # self.ip_address = "192.168.1.3"
        self.ip_address = "127.0.0.1"
        pass

    def create_server(self):
        server = socket.socket()
        server.bind((self.ip_address, self.port))
        server.listen(3)

        conn, address = server.accept()
        server.sendall(bytes("Hello world" + str(address), encoding="utf-8"))

    def create_client(self):
        client = socket.socket()
        client.connect((self.ip_address, self.port))
        ret = str(client.recv(1024), encoding="utf-8")
        print(ret)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('function')
    args = parser.parse_args()
    my_socket = MySocket()
    print(args.function)
    if args.function == "1":
        my_socket.create_client()
    else:
        my_socket.create_server()
    
        
if __name__ == '__main__':
    main()