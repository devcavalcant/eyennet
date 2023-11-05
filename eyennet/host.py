# MIT License

# Copyright (c) 2023 Henrique Cavalcante

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


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

