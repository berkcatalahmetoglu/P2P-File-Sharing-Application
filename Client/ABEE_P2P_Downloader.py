
import socket

#broadcasters_ip = input("Enter broadcasters IP Address.")
broadcasters_ip = "192.168.1.28"
fileName = input("Enter name of the file you want to download.")

port = 50000

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #TCP Socket
clientSocket.connect((broadcasters_ip, port))


clientSocket.send(fileName.encode())

with open(fileName, 'wb') as file:
    i = 1
    rec = clientSocket.recv(1)
    file.write(rec)
    while rec:
        rec = clientSocket.recv(1024) #Receiving file we want to download from server.
        print("Chunk "+str(i)+" Downloaded.")

        file.write(rec)
        i+=1

file.close()
print(f"Download of {fileName} has completed.")














