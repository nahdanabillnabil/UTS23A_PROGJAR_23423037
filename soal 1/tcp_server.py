import socket

HOST = "127.0.0.1"   # alamat lokal
PORT = 5050          # port server

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Server berjalan di {HOST}:{PORT} ...")

conn, addr = server.accept()
print(f"Terhubung dengan client: {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        break

    print("Dari client:", data.decode())   # tampilkan di server

    conn.sendall(data)                     # kirim balik (echo)

conn.close()
