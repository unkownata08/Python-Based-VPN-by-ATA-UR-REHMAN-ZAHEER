import socket

SERVER_IP = "0.0.0.0"
PORT = 5555

IP_POOL = [
    "10.0.0.2",
    "10.0.0.3",
    "10.0.0.4",
    "10.0.0.5"
]

assigned_ips = {}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_IP, PORT))
server.listen(5)

print("[+] VPN Server running on port", PORT)

while True:
    client, addr = server.accept()
    print(f"[+] Client connected: {addr}")

    if not IP_POOL:
        client.send(b"No IPs available")
        client.close()
        continue

    ip = IP_POOL.pop(0)
    assigned_ips[client] = ip

    client.send(f"ASSIGNED_IP:{ip}".encode())

    while True:
        data = client.recv(1024)
        if not data:
            print(f"[-] Client disconnected: {ip}")
            IP_POOL.append(ip)
            client.close()
            break

        print(f"[{ip}] -> {data.decode()}")
