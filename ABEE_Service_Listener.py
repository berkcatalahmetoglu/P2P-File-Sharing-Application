import socket
import json


print("Listening for any broadcast...")
port = 5001
listenerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP Socket for listener.
ip_address = socket.gethostbyname(socket.gethostname())
listenerSocket.bind(('', port))


while True:

    rec = listenerSocket.recvfrom(1024)
    data = json.loads(rec[0].decode('utf-8'))
    print(f"Broadcast from ip: {str(data['ipAddress'])}, Username: {str(data['username'])}, Files: {str(data['files'])} ") #Displaying username and files keys.






