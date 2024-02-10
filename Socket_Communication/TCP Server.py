#!/usr/bin/python3

import socket

def main():
    # Creating the socket object
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = socket.gethostname()  # Host is the server IP
    port = 444  # Port to listen on

    try:
        # Binding the socket
        serversocket.bind((host, port))

        # Starting TCP listener, allowing up to 3 queued connections
        serversocket.listen(3)

        print(f"Server listening on {host}:{port}")

        while True:
            # Starting the connection
            clientsocket, address = serversocket.accept()

            print("Received connection from " + str(address))

            # Message sent to client after successful connection
            message = 'Hello! Thank you for connecting to the server\r\n'
            
            clientsocket.send(message.encode('ascii'))

            clientsocket.close()
    except socket.error as e:
        print(f"Socket error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
