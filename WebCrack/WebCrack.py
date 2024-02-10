"""
Tool Name: Web Crack
Author: Ashwin Harish
Version: 1.0
"""

import argparse
import os
from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text
from DDOS_attack import attack as DDOS_attack
from dirb import MyDirb
from sql_injection_checker import SQLInjectionChecker
from XSS_attack_checker import XSSAttackchecker

def main():
    console = Console()
    print("\n")

    console.print("[bold magenta]Select an option:[/bold magenta]")
    console.print("[cyan]1. DDOS attack check[/cyan]")
    console.print("[blue]2. Directory enumeration[/blue]")
    console.print("[green]3. SQL attack check[/green]")
    console.print("[yellow]4. XSS attack check[/yellow]")
    
    choice = Prompt.ask("[bold]Enter your choice: [/bold]", choices=["1", "2", "3", "4"])

    if choice == "1":
        target = input("Enter the target website or IP address: ")
        DDOS_attack(target)
    elif choice == "2":
        dirb = MyDirb()
        dirb.run()
    elif choice == "3":
        # Get the directory of the script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        SQLpayloads = os.path.join(script_dir, "SQLpayloads.txt")
        
        target = input("Enter the URL or IP address to check for SQL injection vulnerability: ")
        checker = SQLInjectionChecker()
        checker.check_vulnerability(target, SQLpayloads)
    elif choice == "4":
        # Get the directory of the script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        XSSpayloads = os.path.join(script_dir, "XSSpayloads.txt")
        
        target = input("Enter the URL or IP address to check for XSS vulnerability: ")
        checker = XSSAttackchecker()
        checker.check_vulnerability(target, XSSpayloads)
    else:
        console.print("[bold red]Invalid choice. Please enter a valid option (1/2/3/4).[/bold red]")

if __name__ == "__main__":
    console = Console()
    logo = """
            
 ##   ##  ######   #####     ####    #####      ##      ####    ##  ##  
 ##   ##  ##       ##  ##   ##  ##   ##  ##    ####    ##  ##   ## ##   
 ##   ##  ##       ##  ##   ##       ##  ##   ##  ##   ##       ####    
 ## # ##  ####     #####    ##       #####    ######   ##       ###     
 #######  ##       ##  ##   ##       ####     ##  ##   ##       ####    
 ### ###  ##       ##  ##   ##  ##   ## ##    ##  ##   ##  ##   ## ##   
 ##   ##  ######   #####     ####    ##  ##   ##  ##    ####    ##  ##

                                                  
                                        
    """
    description = "A tool to detect vulnerabilities in websites"
    console.print(Text(logo, style="bold green") + Text("\n\n \t\t\t\t\t\t\t" + description, style="green"))
    main()

