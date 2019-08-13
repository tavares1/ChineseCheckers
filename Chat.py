import socket
import threading
import sys

class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Clientes conectados no servidor.
    connections = []
    def __init__(self):
        self.sock.bind(("0.0.0.0",10000))
        self.sock.listen(1)

    def handler(self,c,a):
        while True:
            data = c.recv(1024)
            for connection in self.connections:
                connection.send(data)
            if not data:
                break
    
    def run(self):
        while True:
            c, a = self.sock.accept()
            cThread = threading.Thread(target = self.handler, args = (c, a))
            cThread.daemon = True
            cThread.start()
            self.connections.append(c)
            print(self.connections)

class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def send_msg(self):
        while True:
            msg = input("Digite uma mensagem para o servidor: ")
            user_input = f"{self.client_name} : {msg}"
            self.sock.send(bytes(user_input, "utf-8"))
        
    def __init__(self, client_name,address):
        self.sock.connect((address, 10000))
        self.client_name = client_name
        iThread = threading.Thread(target = self.send_msg)
        iThread.daemon = True
        iThread.start()

        while True:
            data = self.sock.recv(1024)
            if not data:
                break


if (len(sys.argv) > 1):
    print(sys.argv[1])
    client = Client(sys.argv[1],sys.argv[2])
    print("Client created.")
else:
    server = Server()
    print("Running Server, waiting for connections")
    server.run()