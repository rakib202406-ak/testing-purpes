import socket
import pyfiglet

banner = pyfiglet.figlet_format("Domain to Ip")
print(banner)


domain_name = input("Enter the domain name:")
ip = socket.gethostbyname(domain_name)

print(ip)