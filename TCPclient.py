# This client socket mimics what a browser does 
# for each type of HTTP request (GET, POST, ...)
# server reads the instruction and responds accordingly

from socket import socket, AF_INET, SOCK_STREAM

client = socket(AF_INET, SOCK_STREAM)
client.connect(('localhost', 1234))


HEADERSIZE = 10 # used for buffering data
STREAMSIZE = 16
full = ""
message = client.recv(1024)
print(message.decode("utf-8")[HEADERSIZE:])
new = True


while True:
    instruction = input("Type in an HTTP instr ('end' to terminate): ").strip()
    client.send(bytes(instruction, "utf-8"))
    received = False

    while not received:
        response = client.recv(STREAMSIZE)

        if len(response) <= 0:
            break

        if new:
            msglen = int(response[:HEADERSIZE])
            print(f"New message received, length is {msglen}")
            new = False

        full += response.decode("utf-8")

        if len(full) - HEADERSIZE == msglen:
            print("Full message received\n")
            print(full[HEADERSIZE:])
            new = received = True
            full = ""

    if instruction.strip().lower() == "end":
        break



