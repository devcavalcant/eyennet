# Python Imports
from termcolor import colored
import socket
import platform

def logo():
    print(' ______     __  __     ______     __   __     __   __     ______     ______ ')
    print(f'/\  ___\   /\ \_\ \   /\  ___\   /\ "-.\ \   /\ "-.\ \   /\  ___\   /\__  _\ ')
    print(f'\ \  __\   \ \____ \  \ \  __\   \ \ \-.  \  \ \ \-.  \  \ \  __\   \/_/\ \/')
    print(f' \ \_____\  \/\_____\  \ \_____\  \ \_\\\ \_\  \ \_\\\ \_\  \ \_____\    \ \_\ ')
    print(f'  \/_____/   \/_____/   \/_____/   \/_/ \/_/   \/_/ \/_/   \/_____/     \/_/')
    print(f'\n@Github' + colored(' 0x000b \n', "green"))

def userInfo():
    print(colored("[Local IP Address] ","blue")+ socket.gethostbyname(socket.gethostname))
    print(colored("[FQDN] ", "blue")+ socket.getfqdn())
    print(colored("[Platform] ","blue")+ platform.system())
    