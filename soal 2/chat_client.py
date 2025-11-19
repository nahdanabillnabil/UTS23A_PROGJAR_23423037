import socket
import threading

HOST = "127.0.0.1"
PORT = 5050

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def terima():
    while True:
        msg = client.recv(1024).decode()
        print(msg)

def kirim():
    while True:
        pesan = input("")
        client.send(pesan.encode())

thread_terima = threading.Thread(target=terima)
thread_terima.start()

thread_kirim = threading.Thread(target=kirim)
thread_kirim.start()
