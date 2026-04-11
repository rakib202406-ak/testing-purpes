import socket

domain_name = input("Enter the domain name:")
ip = socket.gethostbyname(domain_name)

print(ip)