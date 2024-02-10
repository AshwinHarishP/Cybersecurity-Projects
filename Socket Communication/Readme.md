# Socket Communication Examples

This repository contains two Python code snippets demonstrating basic socket communication: a client and a server. These examples showcase how to establish a simple TCP connection between a client and a server, allowing them to exchange messages.

## Client Code Explanation

The `client.py` script establishes a TCP connection with a remote server and receives a message from the server. Here's a breakdown of the script:

1. Import the `socket` module.
2. Create a client socket using `socket.socket()` with the appropriate address family (`socket.AF_INET`) and socket type (`socket.SOCK_STREAM`).
3. Define the server's IP address and port.
4. Connect to the server using `clientsocket.connect((server_ip, port))`.
5. Receive a message from the server with a maximum length of 1024 bytes using `clientsocket.recv(1024)`.
6. Close the client socket.
7. Print and decode the received message.

## Server Code Explanation

The `server.py` script listens for incoming client connections and sends a welcome message to each connected client. Here's an overview of the script:

1. Import the `socket` module.
2. Define a `main()` function to encapsulate the server logic.
3. Create a server socket using `socket.socket()` with address family (`socket.AF_INET`) and socket type (`socket.SOCK_STREAM`).
4. Bind the server socket to the host and port using `serversocket.bind((host, port))`.
5. Start listening for incoming connections using `serversocket.listen(3)` (up to 3 queued connections).
6. Enter a loop to accept connections:
   - When a connection is accepted with `serversocket.accept()`, a client socket and the client's address are returned.
   - Send a welcome message to the client using `clientsocket.send(message.encode('ascii'))`.
   - Close the client socket.
7. Handle socket errors and exceptions using try-except blocks.
8. Call the `main()` function if the script is run directly.

## Usage

1. Clone this repository to your local machine.
2. Open two terminal windows.
3. In one terminal, navigate to the repository folder and run the `server.py` script:
