


# ============================================
#   Searching IP Address of Websites
#   Author: Javeria
#   GitHub: github.com/javeria-png
# ============================================

import socket

def get_ip(website):
    try:
        website = website.replace("https://", "").replace("http://", "").replace("www.", "")
        ip = socket.gethostbyname(website)
        return ip
    except socket.gaierror:
        return "Error: Website not found or invalid!"

def main():
    print("=" * 45)
    print("      Website IP Address Checker")
    print("              by Javeria")
    print("=" * 45)

    while True:
        print("\nEnter a website to check its IP address.")
        print("Type 'q' to quit.")
        website = input("\nWebsite: ").strip()

        if website == 'q':
            print("please enter website name to check")
            continue
            
        ip = get_ip(website)
        print(f"\nWebsite : {website}") 
        print(f"Ip Address : {ip}")
        print("-" * 45)
        
        
main()
        