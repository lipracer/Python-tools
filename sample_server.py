
from http.server import *
import socket,os
from threading import *
import json
import copy


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    print(os.getcwd())
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

Default_adder = ("0.0.0.0", 8082)

origin_data = '''
{"msg":"success","data":{"total":9,"size":3,"offset":6,"contents":[{"orderCode":"823808858326170200","partnerCode":"vEvXsyk1uuoQdhTi","productId":25927,"name":"500金币","type":5,"subType":7,"status":1,"productStatus":2,"photoList":[{"photoKey":"largepic","url":"http://pic3.iqiyipic.com/common/20190905/daoju1567673146.png"},{"photoKey":"movepic","url":"http://pic2.iqiyipic.com/common/20190905/daoju1567673138.png"}],"payTime":1571290699000,"expiredTime":1599321599000,"useTime":1571290699000,"expired":false},{"orderCode":"823769679169976913","partnerCode":"OruEkGMskqxKm2cG","productId":26603,"name":"500金币","type":5,"subType":7,"status":1,"productStatus":2,"photoList":[{"photoKey":"largepic","url":"http://pic3.iqiyipic.com/common/20190905/daoju1567673146.png"},{"photoKey":"movepic","url":"http://pic2.iqiyipic.com/common/20190905/daoju1567673138.png"}],"payTime":1571215971000,"expiredTime":1602863999000,"useTime":1571215971000,"expired":false},{"orderCode":"823769676115474881","partnerCode":"OruEkGMskqxKm2cG","productId":26603,"name":"500金币","type":5,"subType":7,"status":1,"productStatus":2,"photoList":[{"photoKey":"largepic","url":"http://pic3.iqiyipic.com/common/20190905/daoju1567673146.png"},{"photoKey":"movepic","url":"http://pic2.iqiyipic.com/common/20190905/daoju1567673138.png"}],"payTime":1571215965000,"expiredTime":1602863999000,"useTime":1571215965000,"expired":false}]},"code":"A00000"}
'''
origin_json_dict = json.loads(origin_data)
origin_json_dict["data"]["total"] = 270
while len(origin_json_dict["data"]["contents"]) != 30:
    origin_json_dict["data"]["contents"].append(copy.deepcopy(origin_json_dict["data"]["contents"]))

class CnnHandle(Thread):
    def __init__(self, client):
        Thread.__init__(self)
        self.client = client
        self.start()
        self.buf = bytearray(1024)
    def run(self):        
        data = self.client.recv(1024)
        print("recv data:", data)
        self.client.send(json.dumps(origin_json_dict).encode("utf-8"))
        

class SimpleServer:
    def __init__(self, ip, port):
        self.ser = socket.socket()
        self.ser.bind((ip, port))
        self.ser.listen(10)
        handlers = []
        while True:
            client, addr = self.ser.accept()
            handlers.append(CnnHandle(client))
        

if __name__ == "__main__":

    #print(socket.gethostbyname(socket.gethostname()))
    run()
    #ser = SimpleServer(*Default_adder)

