import socket
from threading import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


server.bind(("127.0.0.1", 3000))


server.listen(100)

list_of_clients = []


def clientthread(conn, addr):
    conn.send(bytes("Welcome to this chatroom!","utf-8"))
    while True:
        try:
            message = conn.recv(2048)
            if message != None :

                message_to_send = (f"<{addr[0]}>{message}")
                broadcast(message_to_send, conn)

            else:
                remove(conn)

        except:
            continue



def broadcast(message, connection):
    for clients in list_of_clients:
        if clients != connection:
            try:
                clients.send(bytes(message,"utf-8"))
            except:
                clients.close()

                # if the link is broken, we remove the client


def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)


while True:
    print("Waiting for connections...")
    conn, addr = server.accept()
    list_of_clients.append(conn)
    print(list_of_clients)
    print(addr[0] + " connected")
    Thread(target=clientthread, args=(conn,addr)).start()

conn.close()
server.close()