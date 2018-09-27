import tornado
import tornado.websocket

clients = []
salons = {}
salons[1] = {'name':"Salon 1", 'users': [], 'id':1}
salons[22] = {'name':"Salon 22", 'users': [], 'id':22}
class Index(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", title = "Yes")
        
    def post(self):
        for arg in self.request.arguments:
            print(arg+" :: "+self.get_argument(arg))
        self.render("index.html")

class Salon(tornado.web.RequestHandler):
    def get(self,slug):
        salonId = int(slug)
        if salonId in salons:
            salon = salons[salonId]
            self.render('salon.html', salon = salon)
        else:
            self.write("Aucun salon")

class Socket(tornado.websocket.WebSocketHandler):
    def open(self,slug):
        self.salonId= int(slug)
        salons[self.salonId]['users'].append(self)

    def on_message(self, message):
        for client in salons[self.salonId]['users']:
            client.write_message(message)

    def on_close(self):
        print(self.salonId)
        salons[self.salonId]['users'].remove(self)
        print("WebSocket closed")