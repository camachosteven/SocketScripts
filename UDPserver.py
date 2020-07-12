from socket import socket, AF_INET, SOCK_DGRAM

server = socket(AF_INET, SOCK_DGRAM)
server.bind(('', 1235))

while True:
    message = server.recv(1024)
    print("The message '" + message.decode("utf-8") + "' was received by server.")
    print("delay")

server.close()
    