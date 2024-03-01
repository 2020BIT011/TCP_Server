# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass
import socket

# Define required parameters :
PORT = 5050
HOST = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'
HEADER = 1024  # Buffer size
ADDR = (HOST , PORT)

# Create socket and connect to the loacal address :
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# Before sned msg to server use same buffer size as server use:
# Encode the message because socket not send plain string or text :
def SendMessage(msg):
    client.send(msg.encode(FORMAT))
    data = client.recv(HEADER)
    if data :
        print(str(data.decode(FORMAT)))
    # client.close()

# send messtge :
# we can use input to add dynamic input :

print("How many times you want to send data")
n=int(input())
i=0
for i in range (n):
    print("Enter the message",i)
    SendMessage(input(""))


