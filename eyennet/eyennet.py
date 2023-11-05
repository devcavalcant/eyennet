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
import click

# Local Imports
import host
import starter
import scanner

@click.command()
@click.option('-l',is_flag=True, show_default=True, default=False, help="Search for live hosts in network")
@click.option('-s',is_flag=True, show_default=True, default=False, help="Search target open ports")
@click.argument('ip')
@click.option('-f',type=click.File("a+"), help="Write results to a file")
def main(l, s, ip,f):

    if (len(ip.split('.')) != 4):
        print("Address structure must be X.X.X.X format")
        exit(0)

    starter.logo()

    if s :
        scan = scanner.Scanner()
        scans = scan.scan()
        if f:
            writeInFile(scans, f)

    elif l :
        hosts = host.search_hosts(ip)
        if f:
            writeInFile(hosts, f)

    

def writeInFile(list, file):
    for i in list:
        file.write(i+'\n')



if __name__ == '__main__':
    main()
