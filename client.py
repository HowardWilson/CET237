import socket
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((127.0.0.1,4))

divide="x"
username=input("Please enter your username:   ")
password=input("Please enter your password:   ")
logindetails=username+divide+password
s.send(logindetails.encode())

message=s.recv(1024)
print(message)
message=s.recv(1024)
print(message)
message=s.recv(1024)
print(message)




