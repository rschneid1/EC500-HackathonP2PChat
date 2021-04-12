# Test chap app
import time
import twisted

import threading
import socket

# for sql
from requests import put

import m_client as mc

# startup display
welcomeMessage = "#*#*#*#*#*# \n \nWelcome to Chat App! Developed by Maxime, Nikhil, and Ryan \n \n#*#*#*#*#*# \n \n \n \n "
print(welcomeMessage)
# ask for username
username = input("Enter your username to get started: ")

# password functionality

# functions
# list contacts
def contacts():
    output = "John Doe: 192.168.1.1"
    return output

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
        else:
            print(command)
