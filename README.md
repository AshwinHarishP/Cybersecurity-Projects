# Cybersecurity Projects Repository

Welcome to my Cybersecurity Projects repository! This repository contains various cybersecurity-related projects that I have worked on.

## Table of Contents

- [Introduction](#introduction)
- [Projects](#projects)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [License](#license)

## Introduction

In this repository, you will find a collection of cybersecurity projects that cover a range of topics, tools, and techniques. These projects are intended for educational and learning purposes, as well as to demonstrate practical applications of cybersecurity concepts.

## Projects

Here are some of the projects currently included in this repository:

### 1. [Project 1: Port Scanner](/Port_Scanner)
   #### Description: <br/>
   <ul>
   <li>The project is a basic Python-based port scanner tool. It allows users to input a target host IP address along with a range of port numbers to be scanned. The tool then checks each port within the specified range to determine if it is open or closed on the target host. </li> <br/>
<li>The port scanner provides a quick and straightforward way to identify open ports, which can be valuable for network administrators and security enthusiasts to assess the security posture of a system or network. Users can easily run the scanner and receive immediate feedback on the status of the specified ports.</li> <br/>

<li>Please note that while this project serves as an introductory exploration of port scanning, conducting such activities on networks and systems without proper authorization may violate ethical guidelines and applicable laws. Responsible use of this tool is essential to ensure the security and privacy of network assets.</li> <br/>
</ul>

### 2. [Project 2: Socket Communication](/Socket_Communication)
   #### Description: <br/>
   <ul>
   <li>This repository contains two Python code snippets demonstrating basic socket communication: a client and a server. These examples showcase how to establish a simple TCP connection between a client and a server, allowing them to exchange messages.</li> <br/>
   <li><strong>Client Code Explanation:</strong> The client.py script establishes a TCP connection with a remote server and receives a message from the server. It imports the socket module, creates a client socket, defines the server's IP address and port, connects to the server, receives a message from the server, and closes the client socket. Finally, it prints and decodes the received message.</li> <br/>
   <li><strong>Server Code Explanation:</strong> The server.py script listens for incoming client connections and sends a welcome message to each connected client. It imports the socket module, defines a main() function to encapsulate the server logic, creates a server socket, binds the server socket to the host and port, starts listening for incoming connections, enters a loop to accept connections, sends a welcome message to the client, and handles socket errors and exceptions.</li> <br/>
   <li><strong>Usage:</strong> Clone this repository to your local machine and open two terminal windows to run the client and server scripts.</li> <br/>
</ul>

### 3. [Project 3: WebCrack](/WebCrack)
   #### Description: <br/>
   <ul>
   <li>The project is a Python-based cybersecurity vulnerability detection tool called Web Crack. It provides a range of features to assess the security posture of web applications and websites, including DDOS attack checks, directory enumeration, SQL injection attack checks, and XSS attack checks.</li> <br/>
   <li>Web Crack is designed to help users identify and mitigate various vulnerabilities in web assets, enhancing overall security resilience against common cyber threats. It offers a comprehensive suite of functionalities to analyze web application security and address potential weaknesses effectively.</li> <br/>
   <li>Users can utilize Web Crack to perform targeted assessments of web applications and websites, identify security gaps, and implement appropriate remediation measures. By conducting thorough vulnerability checks, users can bolster the security posture of their web assets and protect against potential cyber attacks.</li> <br/>
   <li>Responsible use of Web Crack is paramount to ensure the ethical and lawful assessment of web assets. Users should adhere to applicable regulations and guidelines when utilizing the tool to assess the security of web applications and websites.</li> <br/>
</ul>

### 4. [Project 4: AES_Encrypter](/AES_Encrypter)
   #### Description: <br/>
   <ul>
<li>This repository contains Python scripts for AES encryption and decryption, leveraging the AES (Advanced Encryption Standard) algorithm in CBC (Cipher Block Chaining) mode.</li> <br/>
<li>The `encrypter.py` script encrypts plaintext data read from `input.txt` and saves the encrypted content to `encrypted.txt`.</li> <br/>
<li>The `decrypter.py` script decrypts ciphertext data read from `encrypted.txt` and prints the decrypted plaintext.</li> <br/>
<li>The `main.py` script provides a menu-driven interface to either encrypt or decrypt data, allowing users to choose the desired option.</li> <br/>
</ul>

### 5. [Project 5: Backdoor](/Backdoor)
   #### Description: <br/>
   <ul>
<li>This repository contains a Python script for a simple backdoor server, allowing remote execution of commands on the server's operating system.</li> <br/>
<li>The `server.py` script sets up a server socket that listens for incoming connections on a specified port.</li> <br/>
<li>When a client connects, the server accepts the connection and creates a new thread to handle communication with that client.</li> <br/>
<li>The server waits to receive commands from the client, executes them on the server's operating system using `subprocess`, and sends back the output of those commands to the client.</li> <br/>
<li>Additionally, the server handles the special command `cd` to change the current working directory of the server's operating system.</li> <br/>
</ul>

### 6. [Project 6: Password_Cracker](/Password_Cracker)
   #### Description: <br/>
   <ul>
<li>This Python script is designed for hash cracking, capable of attempting to crack various hash types including MD5, SHA1, SHA-256, SHA-384, and SHA-512.</li> <br/>
<li>The script provides options to specify a single hash using the `-s` flag, a file containing hashes using the `-f` flag, or a directory containing hashes using the `-d` flag.</li> <br/>
<li>Additionally, the user can specify the number of threads to use for concurrent processing using the `-t` flag.</li> <br/>
<li>The script utilizes various online hash cracking services/APIs to attempt to crack the provided hashes.</li> <br/>
<li>It supports multithreading for efficient processing, allowing multiple hashes to be cracked simultaneously.</li> <br/>
<li>The script includes colorized output for better readability and provides informative messages during execution, such as hash function detection and progress updates.</li> <br/>
<li>It also saves the cracked hashes to a file named `cracked-<filename>` if a file or directory containing hashes is specified.</li> <br/>
</ul>

### 7. [Project 7: Website_Safety_Checker](/Website_Safety_Checker)
   #### Description: <br/>
   <ul>
<li>This Chrome extension, "Website Safety Checker," is designed to enhance browsing security by warning users about potentially unsafe websites.</li> <br/>
<li>The extension checks the SSL validity of websites by examining their SSL certificates. If issues are detected, users are promptly notified to exercise caution.</li> <br/>
<li>Users can input a website URL into the extension's popup interface, which triggers a safety check. The extension then communicates with external APIs to determine the reputation of the website.</li> <br/>
<li>Reputation information obtained from external APIs helps users assess the trustworthiness of websites before engaging with them further.</li> <br/>
<li>The extension utilizes Chrome's capabilities to provide a seamless experience, with color-coded warnings and informative messages displayed in the popup interface.</li> <br/>
<li>Background processing ensures that safety checks occur efficiently and without interrupting the user's browsing experience.</li> <br/>
<li>Should SSL issues or reputation concerns arise, the extension handles them gracefully, providing users with actionable information to make informed decisions.</li> <br/>
</ul>


## Getting Started

To get started with any of my projects, navigate to the corresponding project folder using the links provided above. Each project folder contains a separate `README.md` file that provides specific instructions, setup guidelines, and explanations for the project.

## Contributing

Contributions are welcome and encouraged! If you want to contribute to any of the existing projects or propose a new one, please follow the guidelines outlined in the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## License

This repository is open-source and is licensed under the [LICENSE file](https://github.com/AshwinHarishP/Cybersecurity-Projects/blob/main/LICENSE). You are free to use, modify, and distribute the code as long as you include the original copyright and license notice in any copy of the software/source.

---
