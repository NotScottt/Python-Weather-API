import server
import requests
import ipaddress
import sys

default_ip = "127.0.0.1"
default_port = "5000"

print("Scott's Weather API - Service")
print("-----------------------------\n")

start = input("Start server?: ")
if start == "y":
    ip_string = input("Enter ip-address (leave blank for default): ")
    
    if ip_string != "":
        if ip_string == "localhost":
            ip_string = "127.0.0.1"

        try:
            ipaddress.ip_address(ip_string)
            new_ip = ip_string

        except ValueError:
            print("Not a valid IP address!")
            sys.exit()

    else:
        new_ip = default_ip

    port_string = input("Enter port (leave blank for default): ")
    if port_string == "":
        new_port = int(default_port)

    else:
        new_port = int(port_string)

    print(f"Server will start on: http://{new_ip}:{new_port}\n")

    try:
        result = requests.get(f"http://{new_ip}:{new_port}")
        print("The Server is already running!")

    except requests.exceptions.ConnectionError:
        server.start_server(new_ip, new_port)