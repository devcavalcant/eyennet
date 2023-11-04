# Python Imports
from termcolor import colored
import platform
import subprocess


def __ping(ip):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    cmd = ['ping', param, '1', ip]

    return subprocess.call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) == 0

    

def search_hosts(ip):
    try:
        hosts = []

        splited_ip = ip.split('.')

        for ip in range(1, 255):
            ip_addr = splited_ip[0]+'.'+splited_ip[1]+'.'+splited_ip[2]+'.'+str(ip)
            response = __ping(ip_addr)
            if response :
                print(colored(ip_addr, "green"))
                hosts.append(ip_addr)
        return hosts
    except KeyboardInterrupt:
        return hosts

