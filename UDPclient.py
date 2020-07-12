from socket import socket, AF_INET, SOCK_DGRAM

client = socket(AF_INET, SOCK_DGRAM)
address = ("localhost", 1235)

while True:
    send = input("\nDo you want to send a message to server?? (yes or no): ").strip()
    if send.lower() == "yes":
        message = input("Type in message: ").strip()
        client.sendto(bytes(message, "utf-8"), address)
    elif send.lower() == "no":
        print("Session Terminating")
        break
    else:
        print("please enter valid answers")

client.close()