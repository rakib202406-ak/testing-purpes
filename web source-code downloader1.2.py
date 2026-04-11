#Get any website source code:

import turtle
import urllib.request as u
import pyfiglet

banner = pyfiglet.figlet_format("Source code Downloader")
print(banner)

website_Domain =turtle.textinput("Domain Name","Url Address") 


source_code =u.urlopen(website_Domain)
source_code_read = source_code.read()
print(source_code_read)
