import socket

#this is the server, it has to keep running so that the users can connect to it
#we need the host for the server
#specify your private IP because the host is in a network, the users will search for the host, hence no need of public IP
#one way to do it is to type it manually like:
#HOST = '192.168.18.10'

#Or use: for making your code dynamic
HOST = socket.gethostbyname(socket.gethostname())
#the client needs to use the HOST IP address for accessing the server
# HOST = '192.168.137.176' #For samman's hotspot
#for port, don't choose reserved ports
PORT = 9948 

#we will mostly be using socket. .... so remember the syntax
#this socket is only for accepting connections
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #internet socket and TCP

#bind the server by using the host and port
server.bind((HOST, PORT))

#now listen for the incoming requests
server.listen(5) #listen for 5 requests and discard the rest(how many unaccepted connections do we allow before we reject new ones)

#the socket that is going to be established after the communication is accepted is:
while True:
    communication_socket, address = server.accept() #accept() returns the address of the client and the socket used for communication with that client
    #communication_socket is the created end point for the client after accepting it
    print(f"connected to {address}")    #message to be printed
    message = communication_socket.recv(1024).decode('utf-8')   #the sent message is encrypted by the client, we usually take 1024 bytes as buffer size
    print(f"Message from client is: {message}") #After decoding, display the message
    communication_socket.send(f"Got your message! Thank You!".encode('utf-8')) #sending another message to the client, we need to encode it
    communication_socket.close()
    print(f"connection with {address} ended!")

#This only accepts a single request, for multiple requests at a time, multithreading is needed.


