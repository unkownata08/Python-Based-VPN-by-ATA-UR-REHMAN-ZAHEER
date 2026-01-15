import socket

SERVER_IP = "127.0.0.1"
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

response = client.recv(1024).decode()
print("[+] Server:", response)

while True:
    msg = input("Send data through VPN: ")
    if msg.lower() == "exit":
        break
    client.send(msg.encode())

client.close()
