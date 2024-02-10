import argparse
import os
import requests
import socket
from requests.exceptions import InvalidURL, ConnectionError

class SQLInjectionChecker:
    def __init__(self):
        pass

    def ip_to_url(self, ip_address):
        try:
            return socket.gethostbyaddr(ip_address)[0]
        except socket.herror:
            print("Failed to resolve IP address to URL.")
            return None

    def check_vulnerability(self, target, SQLpayloads):
        try:
            # Convert target to URL or IP address
            if target.startswith("http://") or target.startswith("https://"):
                url = target
            else:
                url = self.ip_to_url(target)
                if url is None:
                    return  # Stop execution if IP cannot be resolved to URL

            with open(SQLpayloads, "r") as f:
                payloads = f.readlines()

            vulnerable = False  # Flag to track if any payload is vulnerable
            for payload in payloads:
                payload = payload.strip()
                modified_url = f"{url}' OR {payload} --"

                try:
                    response = requests.get(modified_url)
                    if "error" in response.text.lower():
                        print(f"Vulnerable to SQL injection with payload: {payload}")
                        vulnerable = True  # Set flag to True if vulnerable
                    # else:
                    #     print(f"Not Vulnerable to SQL injection with payload: {payload}")
                except (InvalidURL, ConnectionError) as e:
                    print(f"Invalid URL or connection error with payload: {payload}. Skipping...")
                    continue  # Continue to the next payload

            # If none of the payloads were vulnerable, print appropriate message
            if not vulnerable:
                print("Not vulnerable to SQL injection attack.")

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Combine the directory and file name for payloads
    SQLpayloads = os.path.join(script_dir, "SQLpayloads.txt")

    # Prompt the user to enter the URL or IP address
    target = input("Enter the URL or IP address to check for SQL injection vulnerability: ")

    # Initialize the SQLInjectionChecker object and check vulnerability
    checker = SQLInjectionChecker()
    checker.check_vulnerability(target, SQLpayloads)
