# Python Imports
import socket
from termcolor import colored, cprint

ports = [80, 443, 135]

class Scanner:
    ip = ''

    def scan(self):
        hosts = []

        print("\nScanning for hosts and ports in "+self.ip)

        splited_ip = self.ip.split('.')
        port = 80

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        # For /24
        for ip in range(0, 255):
            ip_addr = splited_ip[0]+'.'+splited_ip[1]+'.'+splited_ip[2]+'.'+str(ip)
            response = sock.connect_ex((ip_addr, port))
            if response == 0:
                print(colored(ip_addr+':', "green")+colored(port,"yellow"))
                hosts.append(ip_addr)
        sock.close()
        print('')

        return hosts

    def __init__(self, ip):
        self.ip = ip
      