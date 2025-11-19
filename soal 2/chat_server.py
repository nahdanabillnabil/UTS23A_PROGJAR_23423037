import socket
import threading

HOST = "127.0.0.1"
PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

def broadcast(message, connection):
    for client in clients:
        if client != connection:
            client.send(message)

def handle_client(conn):
    while True:
        try:
            msg = conn.recv(1024)
            broadcast(msg, conn)
        except:
            clients.remove(conn)
            conn.close()
            break

def start():
    print("Chat Server berjalan...")
    while True:
        conn, addr = server.accept()
        print("Terhubung:", addr)
        clients.append(conn)

        thread = threading.Thread(target=handle_client, args=(conn,))
        thread.start()

start()
