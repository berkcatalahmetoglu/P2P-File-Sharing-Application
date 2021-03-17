
import socket
import json
import time



announcerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Initiliasing UDP Socket
announcerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) #Setting socket option to broadcast.

port = 6000
ip_address = socket.gethostbyname(socket.gethostname()) #Get ip address
username = input("Please enter your username: ")
print("Broadcasting...")


usersFiles = username + "_file.png"
sendData = {

    "username" : username,
    "files" : usersFiles,
    "ipAddress" : ip_address


}
dataToSend = json.dumps(sendData) #Converting sendData dictionary to JSON format
while True:

    announcerSocket.sendto(dataToSend.encode('utf-8'), ('25.255.255.255', port)) #Broadcasting files every 60 seconds.
    time.sleep(60)







