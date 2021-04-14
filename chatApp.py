# Test chap app
import time
import twisted

import threading
import socket

# for sql
from requests import put, get

import m_client as mc

# using ipify.org : https://stackoverflow.com/questions/2311510/getting-a-machines-external-ip-address-with-python/41432835

# ip function from: https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

# startup display
welcomeMessage = "#*#*#*#*#*# \n \nWelcome to Chat App! Developed by Maxime, Nikhil, and Ryan \n \n#*#*#*#*#*# \n \n \n \n "
print(welcomeMessage)
# ask for username
username = input("Enter your username to get started: ")

# send reqest to database to update ip and name association
#hostname = socket.gethostname()
ip_address = ip = get('https://api.ipify.org').text
print("Updated " + username + " with IP address: " + ip_address + " in central server! \n")

# password functionality

# functions
# list contacts
def contacts():
    output = "John Doe: 192.168.1.1"
    return output

# search main database for name and ip address
def search(username):
    # query to database username
    output = "Found " + username + " 10.0.0.1"
    return output


# print currently implemented functions
def help():
    print("Available Commands: \n")
    print("contacts : \n")
    print("    prints list of contacts \n")
    print("chat : \n")
    print("    type chat and a contact name to chat with someone \n")
    print("search : \n")
    print("    type search and a name to search for their name and IP \n")
    print("exit : \n")
    print("    exit application \n")


# start chat with another user via name lookup
def chat(username):
    # from username make request to sql database for ip
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    #port = randint(1000,5000)
    port = 2444
    friend_port = 2555
    mc.startClient(port)
    # client thread
    #threading.start_new_thread(startClient(port, ip_address))



# wait for command
while True:
    command = ""
    data = ""
    user_input = input("$chatApp/" + username + ": ")
    # parse user input
    if user_input == None:
        print("")
    else:
        tmp = user_input.split(" ", 1)
        command = tmp[0]
        if len(tmp) > 1:
            data = tmp[1]

        # perform functionality    
        if command == "exit":
            exit()
        elif command == "contacts":
            print(contacts())
        elif command == "chat":
            print(data)
            chat(data)
        elif command == "help":
            help()
        elif command == "search":
            print(data)
            search(data)
        else:
            print(command)
