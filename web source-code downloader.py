import urllib.request as u
website_name = input("Enter target web :")

source =u.urlopen(website_name)
source_read = source.read()
print(source_read)
