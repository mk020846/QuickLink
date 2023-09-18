from socket import socket
import cv2
hostnport=('localhost',35568)
Socket = socket()

Socket.bind(hostnport)
Socket.listen(1)
print(f"Listening on http://{hostnport[0]}:{hostnport[1]}")

cap = cv2.VideoCapture('/home/mayank/Python/server/.dbconnect')
while True:
    client, client_addr = Socket.accept()
    ret, frame = cap.read()
    if not ret:
        break
    encoded_frame = cv2.imencode('.jpg',frame)[1].tobytes()
    frame_size = len(encoded_frame)
    client.send(str(frame_size).encode().ljust(16))

    client.send(encoded_frame)
cap.release()
client.close()
Socket.close()
