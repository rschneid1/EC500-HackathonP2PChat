# import socket
# serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# serv.bind(('0.0.0.0', 8080))
# serv.listen(5)
# while True:
#     conn, addr = serv.accept()
#     from_client = ''
#     while True:
#         data = conn.recv(4096)
#         data = data.decode()
#         if not data: break
#         from_client += data
#         print(from_client)
#         conn.send("I am SERVER<br>".encode())
#     conn.close()
#     print('client disconnected')



from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class Server(DatagramProtocol):
    def __init__(self):
        self.client = set()

    def datagramReceived(self, datagram, addr):
        datagram = datagram.decode('ISO-8859-1')
        if datagram == "ready":
            addresses = "\n".join([str(x) for x in self.client])
            self.transport.write(addresses.encode('utf-8'), addr)
            self.client.add(addr)

def StartServer():
# if __name__ == "__main__":
    reactor.listenUDP(9999, Server())
    reactor.run()