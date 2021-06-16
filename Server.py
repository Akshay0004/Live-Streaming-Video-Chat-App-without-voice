import socket
import sys
import time


#using socket function for and SOCK_Stram is for TCP connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#this will retrive the host name where server is runing
host = "ip of host"
print("connection successfull")

#This is the uniqe port no given by us for connection
port =  1234
s.bind((host,port))
print("SERVER IS BOUND PERFECTLY:")

# 2 clients can connect to server at a time
s.listen(2)

#this will store address
conn,addr = s.accept()
print("Connected Succefully to client")

while True:
        #this will send message to address which is saved in conn variable
        message = input(str("SERVER:"))
        message = message.encode()
        conn.send(message)


        # Receive message coming from the client save in conn variable
        message_rcv = conn.recv(1024)
        # Decode message in string from binary
        message_rcv = message_rcv.decode()
        print("message from client:", message_rcv)