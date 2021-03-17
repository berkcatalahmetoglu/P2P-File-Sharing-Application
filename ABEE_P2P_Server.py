import socket
import datetime

port = 50000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Initialising TCP Socket


serverSocket.bind(("", port))
print("Server is listening for connections.")

serverSocket.listen(5)

client, addr = serverSocket.accept()
print(f"Connection established with: {addr}")

fileName = client.recv(1024) #Receiving file name inputted by P2P_Client
filename_decoded = fileName.decode("utf-8")

file = open(filename_decoded, 'rb') #Opening file we want to send to client.

chunk = file.read(1024) #Reading and sending first 1024 bytes this is outside the while loop for setting condition to true in first place.

while chunk:

    client.send(chunk)

    chunk = file.read(1024)



file.close()

print("File successfully sent!")

with open("downloadlog.txt", "a") as downloadLog: #Writing download log into txt file.
    currDate = datetime.datetime.now()
    stringToWrite = f"{addr} downloaded {filename_decoded}" + " at " + currDate.strftime("%Y-%m-%d %H:%M:%S")
    downloadLog.write(stringToWrite)





















