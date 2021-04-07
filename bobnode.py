from pyp2p.net import *

#Setup Bob's p2p node.
bob = Net(passive_bind="73.114.134.228", passive_port=44445, interface="en0", node_type="passive", debug=1)
bob.start()
bob.bootstrap()
bob.advertise()

#Event loop.
while 1:
    for con in bob:
        con.send_line("test")

    time.sleep(1)