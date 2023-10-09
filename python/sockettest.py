import socket

# array hostnames
hosts = ["www.uc.edu", "www.google.com", "www.bing.com"]

print("Working from host: " + socket.getfqdn())

# For Loop
for host in hosts:
	print(socket.gethostbyname(host))


