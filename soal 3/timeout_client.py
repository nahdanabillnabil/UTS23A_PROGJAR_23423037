import socket

HOST = "127.0.0.1"
PORT = 5050

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.settimeout(3)  # timeout connect
    client.connect((HOST, PORT))
    print("Terhubung ke server")

    client.settimeout(2)  # timeout read
    data = client.recv(1024)
    print("Dari server:", data.decode())

except socket.timeout:
    print("Koneksi timeout!")

finally:
    client.close()
