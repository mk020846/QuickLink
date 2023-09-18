from socket import socket 

sock = socket()
host = 'localhost'
port = 8080

host_address=(host,port)

def send(filename,filepath):
    sock.bind(host_address)
    sock.listen(1)
    client_address = sock.accept()
    client_address[0].send(filename.encode())
    with open((filepath+filename),'rb') as file_to_send:
        data = file_to_send.read(1024)
        while data:
            client_address[0].sendall(data)
            data=file_to_send.read(1024)
    client_address[0].close()
    sock.close()
    return 0
