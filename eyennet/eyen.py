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
        writeInFile(scans, f)

    elif l :
        hosts = host.search_hosts(ip)
        writeInFile(hosts, f)

    

def writeInFile(list, file):

    for i in list:
        file.write(i+'\n')



if __name__ == '__main__':
    main()
