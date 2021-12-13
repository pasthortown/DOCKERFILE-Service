from tornado.ioloop import IOLoop
import tornado.web
from tornado.escape import json_decode
from tornado.httpserver import HTTPServer

class MainHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Access-Control-Allow-Methods', '*')
    
    def post(self):
        content = json_decode(self.request.body)
        respuesta = { 'echo': content }
        self.write(respuesta)

def main():
    app = tornado.web.Application([
        (r"/?", MainHandler)
    ])
    http_server = HTTPServer(app)
    http_server.listen(5050)
    IOLoop.instance().start()

if __name__ == '__main__':
    main()