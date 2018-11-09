
from http.server import *

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    print(os.getcwd())
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == "__main__":                                           

    print(socket.gethostbyname(socket.gethostname()))
    run()
