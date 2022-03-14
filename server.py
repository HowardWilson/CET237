import socket #Instructs the script to access the socket module required for network connectivity
import secrets #Instructs the script to access the secret module required

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creates a socket object, AF_INET specifies IPV4 will be used and SOCK_STREAM specifies TCP will be used.
s.bind((127.0.0.1,4)) #Binds the socket to a public host so it can be accessed from the outside world, port 4 is used as this is an unassigned port
s.listen(5) #Puts the socket into listening mode ready to accept a connection

while True: #Creates an infinite loop so the server is always ready to accept incoming connections
    clientsocket, address = s.accept() #Instructs the server to accept any incoming connections from clients
    print("Connection has been established!") #A connection message is displayed to alert the server admin that a connection has been made

    logindetails=clientsocket.recv(1024) #Creates a variable for storing the login details and instructs the server to recieve these from the client
    logindetailsdecoded=logindetails.decode() #Decodes the recieved login details so that they are in a usable format
    
    if logindetailsdecoded=="howardx123": #Verifies that the username and password are correct before proceeding.
        clientsocket.send(bytes("Authenticated! ","utf-8")) #Transmits feedback to the client that the login details are correct.
        OTP=secrets.token_bytes(32) #Generates the 32 bit one time password, more information can be found in the OTP generator section of the report
        clientsocket.send(bytes("Your OTP is:","utf-8")) #Transmites a confirmation message to the client that the OTP will follow.
        clientsocket.send(OTP) #Transmits the OTP to the client
    else: #Provides backup code incase the username or password werent correct.
        print("Incorrect username or password, the connection will be closed") #Displays that the username or password were incorrect on the server 
        clientsocket.send(bytes("Incorrect username or password, the connection will be closed","utf-8")) #Transmits an error message that the username and password were incorrect
        break #Exits the loop so that the connection is closed.





   




