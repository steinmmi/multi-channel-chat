import tornado.ioloop
import tornado.web
import tornado.websocket
import Handlers


def make_app():
    return tornado.web.Application([
        (r"/", Handlers.Index),
        (r"/socket/([^/]+)", Handlers.Socket),
        (r"/salon/([^/]+)", Handlers.Salon),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()