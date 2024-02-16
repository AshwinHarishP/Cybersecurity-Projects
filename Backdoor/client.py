import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '123.63.236.166'  
# host = socket.gethostname()

port = 9999

serversocket.connect((host, port))  
message = serversocket.recv(1024).decode()  
print(message)

serversocket.close()  
