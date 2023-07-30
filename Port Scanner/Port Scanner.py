import socket
import time
import signal
import sys

Scan = True
while Scan:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)

    # Get the target host IP address from the user
    host = input("Enter HOST IP: ")
    # Get the starting and ending ports to scan from the user
    start_port = int(input("Enter starting PORT: "))
    end_port = int(input("Enter ending PORT: "))

    def portScanner(host, port):
        # Function to scan a single port and determine if it's open or closed
        if s.connect_ex((host, port)):
            print("Port {} is closed".format(port))
        else:
            print("Port {} is open".format(port))

    def scan_ports():
        # Function to perform the port scanning within the specified range
        print("\n")
        print("Scanning ports {} to {} on {}...".format(start_port, end_port, host))
        start_time = time.time()

        try:
            for port in range(start_port, end_port + 1):
                portScanner(host, port)

        except KeyboardInterrupt:
            # If the user interrupts the scan (Ctrl+C), stop gracefully
            print("\nPort scanning stopped by user.")
            s.close()
            sys.exit(0)

        end_time = time.time()
        print("Scanning completed in {:.2f} seconds.".format(end_time - start_time))

    # Function to handle SIGINT (Ctrl+C)
    def signal_handler(sig, frame):
        print("\nPort scanning stopped by user.")
        s.close()
        sys.exit(0)

    # Register the signal handler
    signal.signal(signal.SIGINT, signal_handler)

    try:
        scan_ports()

    except socket.gaierror:
        # Handle the case where an invalid hostname or IP address is provided
        print("Invalid Hostname or IP address.")

    except socket.error:
        # Handle the case where the connection to the server fails
        print("Could not connect to the server.")
        s.close()

    print("\n")
    test = input("Do you want to continue (Y/N): ")
    if test.upper() == "N":
        # If the user chooses not to continue, exit the loop
        Scan = False
