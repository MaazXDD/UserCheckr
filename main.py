import requests, threading
from colorama import Fore, init

init(autoreset=False)
purple = Fore.MAGENTA
white = Fore.WHITE
green = Fore.GREEN
red = Fore.RED

print(f""" {purple}
██╗   ██╗███████╗███████╗██████╗      ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗██████╗ 
██║   ██║██╔════╝██╔════╝██╔══██╗    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔══██╗
██║   ██║███████╗█████╗  ██████╔╝    ██║     ███████║█████╗  ██║     █████╔╝ ██████╔╝
██║   ██║╚════██║██╔══╝  ██╔══██╗    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══██╗
╚██████╔╝███████║███████╗██║  ██║    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗██║  ██║
 ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝
                                                                                     
{white}usrnm chckr by @maazxdd <3
{purple}Follow Github : @MaazXDD
 """)
                                  
print(f"""{purple}threads{white}: """, end="")
threads = int(input())

def split_list(alist, wanted_parts=1):
    return [ alist[i*len(alist) // wanted_parts: (i+1)*len(alist) // wanted_parts] for i in range(wanted_parts) ]

def thrd(usernames):
    for username in usernames:
        z = requests.get(f"https://www.discord.com/{username}")
        if z.status_code == 200:
            print(f"{red}{username}{white} is taken")
        
        elif z.status_code == 404:
            print(f"{green}{username}{white} is not taken")
            with open("available.txt", 'a') as f:
                f.write(f"{username}\n")
        else:
            print(f"{red}x {white} Your IP might be temporarily blocked.{red}[Status code {z.status_code}]")

usernames = split_list([line.strip() for line in open("usernames.txt")], threads)

for userlist in usernames:
    threading.Thread(target=thrd, args=(userlist,)).start()

