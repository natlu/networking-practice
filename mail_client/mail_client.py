from socket import *
import ssl

msg = "\r\n Hello"
endmsg = "\r\n.\r\n"

mailserver = "smtp.gmail.com"
mailserverPort = 465

# Create socket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket = ssl.wrap_socket(
    clientSocket,
    ssl_version=ssl.PROTOCOL_TLS,
    )

clientSocket.connect((mailserver,mailserverPort))


recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
authCommand = 'AUTH LOGIN\r\n'
clientSocket.send(authCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)

# https://myaccount.google.com/lesssecureapps
import base64
import getpass
myemail = "abc@gmail.com"
mypass = getpass.getpass()
clientSocket.send((base64.b64encode(myemail.encode()))+('\r\n').encode())
print(clientSocket.recv(1024).decode())

clientSocket.send((base64.b64encode(mypass.encode()))+('\r\n').encode())
print(clientSocket.recv(1024).decode())

# Send MAIL FROM command and print server response.
mailFromCommand = 'MAIL FROM: <testemail@test.com>\r\n'
clientSocket.send(mailFromCommand.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
    print('250 reply not received from server.')


# Send 
# Send RCPT TO command and print server response.
rcptToCommand = 'RCPT TO: <toemail@email.com>\r\n'
clientSocket.send(rcptToCommand.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
    print('250 reply not received from server.')

# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '354':
    print('250 reply not received from server.')

clientSocket.send(msg.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)

# Message ends with a single period.
clientSocket.send(endmsg.encode())

quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)
if recv6[:3] != '354':
    print('250 reply not received from server.')

clientSocket.close()
