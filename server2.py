import socket
host='localhost'
port=6000
s=socket.socket()
#socket.AF_INET represents an IP address version 4
#socket.SOCK_STREAM represents that we are using TCP/IP protocol

#Bind the socket with server and port number
s.bind((host,port))

#allow maximum 1 connection to the socket
s.listen(1)

#wait till a aclient accept connection
c,address=s.accept()

#we will reun the server continously
while True:
    data=c.recv(1024)
    #if client send empty string, then come out
    if not data:
        break
    print("from client "+str(data.decode()))
    #enter response data from server
    data1=input("Enter response:")
    c.send(data1.encode())


c.close()