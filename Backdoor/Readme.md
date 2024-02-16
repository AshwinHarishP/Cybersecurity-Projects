# Simple Remote Command Execution System

This is a simple Python-based remote command execution system consisting of a server (`server.py`) and a client (`client.py`). The server listens for incoming connections from clients and executes commands sent by the client. The client connects to the server and sends commands to be executed remotely.

## Features

- Execute shell commands remotely.
- Change directory on the server remotely.
- Handle multiple clients concurrently using threading.

## Usage

### Prerequisites

- Python 3.x

### Server

Run the `server.py` script on the machine you want to act as the server.
   ```bash
   python server.py
  ```

### Client

Run the `client.py` script on the machine you want to act as the client.
   ```bash
   python client.py
  ```

### Notes

Ensure that both the server and client have network connectivity and can communicate over the specified port.
Use caution when executing commands remotely, as it may have security implications.
This is a basic implementation and may need additional error handling and security measures for production use.

## License

This project is licensed under the MIT License - see the [LICENSE] file for details.
