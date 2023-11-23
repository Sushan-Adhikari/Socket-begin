import socket
#For samman's wifi hotspot, the IP address is:
#if we want to access the server started on another computer, we need to specify the private IP of that computer
HOST = '192.168.137.176'
PORT = 9948

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#we are not hosting here but we are connecting
#we do not use bind here
socket.connect((HOST, PORT))
#Here, we have only one socket, we connect and send with the same socket

socket.send("Hello World!".encode('Utf-8'))

#print the received data consisting of 1024 bytes
print(socket.recv(1024).decode('utf-8'))