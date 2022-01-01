import socket
host='localhost'
port=6000
s=socket.socket()
#socket.AF_INET represents an IP address version 4
#socket.SOCK_STREAM represents that we are using TCP/IP protocol

#connect to the server and port number
s.connect((host,port))

str=input("enter data: ")

while str!='exit':
    #send data from client to server
    s.send(str.encode())
    #receive the response data from server
    data=s.recv(1024)
    #print(data)
    data=data.decode()
    print("From server: "+data)
    #enter data
    str=input("Enter data: ")

s.close()