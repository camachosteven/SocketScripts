from socket import socket, AF_INET, SOCK_STREAM

server = socket(AF_INET, SOCK_STREAM)
server.bind(('', 1234))
server.listen(5)
HEADERSIZE = 10


client, address = server.accept()

# Connection acknowledgement
print(f"Connection with {address} has been established")
msg = "Congratulations you have connected with the server!!\n"
msg = f"{len(msg):<{HEADERSIZE}}" + msg
client.send(bytes(msg, "utf-8"))

# as long as client send requests, send back responses 
# until client wishes to terminate
while True: 
    msg = ""
    instr = client.recv(24).decode("utf-8").upper()
    if instr == "GET":
        print(f"{instr} was received")
        msg += "HTTP GET response\n"
    elif instr == "POST":
        print(f"{instr} was received")
        msg += "HTTP POST response\n"
    elif instr == "PUT":
        print(f"{instr} was received")
        msg += "HTTP PUT response\n"
    elif instr == "PATCH":
        print(f"{instr} was received")
        msg += "HTTP PATCH response\n"
    elif instr == "HEAD":
        print(f"{instr} was received")
        msg += "HTTP HEAD response\n"
    elif instr == "END":
        print("Request to terminate was received")
        print("Session terminating")
        msg += "Termination by yours truly"
        msg = f"{len(msg):<{HEADERSIZE}}" + msg
        client.send(bytes(msg, "utf-8"))
        client.close()
        break
    else:
        print("invalid instruction was received")
        msg += "Invalid instruction\n"
        msg += "Enter GET, POST, PUT, PATCH, or HEAD\n"

    msg = f"{len(msg):<{HEADERSIZE}}" + msg
    client.send(bytes(msg, "utf-8"))

server.close()


