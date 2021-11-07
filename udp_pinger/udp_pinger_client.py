import socket
import datetime

# Create a UDP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverName = 'localhost'
serverPort = 12000

for i in range(10):
    try:
        curr_time = str(datetime.datetime.now())
        message = f'Ping {i} {curr_time}'
        print(f'message: {message}')
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        clientSocket.settimeout(1)
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        print(f'response: {modifiedMessage.decode()}')
    except:
        print("Request timed out")
        continue

clientSocket.close()

