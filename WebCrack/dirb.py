import argparse
import requests
import sys
import termcolor
import os

class MyDirb:
    def __init__(self):
        self.url_base, self.traversal_attack = self.get_info()

    def get_info(self):
        parser = argparse.ArgumentParser(description="Our Own Directory Enumeration Tool")
        parser.add_argument("-u", "--url", dest="url", type=str, help="Specify URL to enumerate")
        parser.add_argument("-d", "--dir-traversal", dest="traversal_attack", action="store_true", help="Enable directory traversal attack")
        args = parser.parse_args()

        if not args.url:
            url = input("Enter URL to enumerate: ")
            if not url:
                print("Please provide the URL.")
                sys.exit()

            if not url.startswith("http://") and not url.startswith("https://"):
                url = "http://" + url

            if not url.endswith("/"):
                url = url + "/"

        else:
            url = args.url

        return url, args.traversal_attack

    def check_page(self, url):
        try:
            response = requests.get(url)
            response_code = response.status_code
            response_size = len(response.content)
            if response_code == 200:
                print(termcolor.colored("+ %s (CODE: %d SIZE: %d)" % (url, response_code, response_size), "green"))
                return True  # Found a directory
            elif response_code == 404:
                return False  # Directory not found
            else:
                print("+ %s (CODE: %d SIZE: %d)" % (url, response_code, response_size))
        except Exception as e:
            print("Error:", e)
            return False  # Directory not found due to error

    def run(self):
        found_directory = False  # Flag to track if any directories were found
        # Construct the path to Basic_wordList.txt in the same directory as the script
        wordlist = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Basic_wordList.txt")

        if not os.path.exists(wordlist):
            print("[-] The wordlist file does not exist!")
            sys.exit()

        with open(wordlist, "r") as f:
            for word in f.readlines():
                url = self.url_base + word.strip()
                if self.traversal_attack:
                    url = url.replace("../", "")  # Remove any existing "../" in the URL for the sake of demonstration
                    url += "../"  # Append directory traversal string
                if self.check_page(url):
                    found_directory = True

        if not found_directory:
            print("Not vulnerable to directory traversal attack")

if __name__ == "__main__":
    dirb = MyDirb()
    dirb.run()
