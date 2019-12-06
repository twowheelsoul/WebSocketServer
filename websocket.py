from SimpleWebSocketServer import WebSocket, SimpleWebSocketServer

class SimpleEcho(WebSocket):
    def handleMessage(self):

        if self.data is None:
            self.data = ''

        #Reply to all Clients
        for client in self.server.connections.itervalues():
            client.sendMessage(str(self.data))


    def handleConnected(self):
        print self.address, 'connected'

    def handleClose(self):
        print self.address, 'closed'

server = SimpleWebSocketServer('', 9000, SimpleEcho)
server.serveforever()
