# Port Scanner

This is a simple Python script that allows you to scan for open ports on a target host within a specified range of ports. The script uses the `socket` library for creating sockets and checking the connection status to each port.

## Prerequisites

Before running the script, make sure you have Python installed on your system.

## Usage

1. Clone this repository or download the `port_scanner.py` file.

2. Open a terminal (command prompt) and navigate to the directory where the `port_scanner.py` file is located.

3. Run the script using the following command:

4. The script will prompt you to enter the target host IP address, starting port, and ending port for the scan.

5. The script will then proceed to scan the specified range of ports on the target host. For each port, it will indicate whether the port is open or closed.

6. The scanning process will be interrupted if you press `Ctrl+C` during the scan. In this case, the script will gracefully stop and display the results obtained so far.

7. After completing the scan, the script will ask if you want to continue with another scan. Type `Y` to continue or `N` to exit.

## Important Notes

- The script sets a timeout of 5 seconds for each connection attempt. If the connection takes longer than this timeout, it will be considered unsuccessful.

- If you encounter any issues during the scan, such as an invalid hostname or connection errors, the script will handle those errors and display appropriate messages.

- Ensure that you have proper authorization before scanning any host. Unauthorized scanning of systems or networks may be illegal and can result in severe consequences.

## Disclaimer

This script is provided for educational and informational purposes only. Use it at your own risk and responsibility. The authors of this script are not liable for any misuse, damage, or unauthorized scanning.

## License

This project is licensed under the MIT License. See the [LICENSE file](https://github.com/AshwinHarishP/Cybersecurity-Projects/blob/a9cd41148b794740c8b101699f6a4f0e0856a797/LICENSE) for details.



