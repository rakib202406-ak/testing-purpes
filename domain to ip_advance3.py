from termcolor import colored
print(colored("******************** Domain to Ip converter ********************",'green'))
print(colored("******************** Created by R@kib ********************",'red'))



import socket
import pyfiglet


banner =colored(pyfiglet.figlet_format("Domain to Ip"),'green')
print(banner)


domain_name = input("Enter the domain name:")
ip = socket.gethostbyname(domain_name)

print("IP for {} : {}".format(domain_name,ip))