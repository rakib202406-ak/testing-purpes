import socket
import pyfiglet
from termcolor import colored

banner =colored(pyfiglet.figlet_format("Domain to Ip"),'green')
print(banner)


domain_name = input("Enter the domain name:")
ip = socket.gethostbyname(domain_name)

print(ip)