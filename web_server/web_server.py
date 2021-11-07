from socket import AF_INET, SOCK_STREAM
from socket import socket, gethostbyname, gethostname
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

# prepare server socket
serverPort = 8080
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    # Establish connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        f.close()
        #Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\n".encode())
        connectionSocket.send("Content-Type: text/html\n".encode())
        connectionSocket.send("\n".encode())
        # Send the content of the requested file to the client
        # connectionSocket.sendall(outputdata.encode())
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        error_msg = ("HTTP/1.1 404 Not Found\n")
        connectionSocket.send(error_msg.encode())
        connectionSocket.close()

serverSocket.close()
sys.exit()


# local_ip = gethostbyname(gethostname())
