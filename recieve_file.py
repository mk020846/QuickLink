from socket import socket

sock = socket()

def recv(host,port):
    sock.connect((host,port))
    filename = sock.recv(1024).decode()
    with open((filename),'wb') as file_to_recieve:
        while True:
            data = sock.recv(1024)
            if not data:
                break
            file_to_recieve.write(data)
    sock.close()
    return 0
