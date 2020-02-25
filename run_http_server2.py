#coding=utf-8
# http.server --- HTTP 服务器 https://docs.python.org/zh-cn/3/library/http.server.html?highlight=threadingmixin
# socketserver---网络服务器框架 https://docs.python.org/zh-cn/3/library/socketserver.html?highlight=threadingmixin#socketserver.ThreadingMixIn
from http.server  import ThreadingHTTPServer,CGIHTTPRequestHandler
import cgi
import socket
class   PostHandler(CGIHTTPRequestHandler):
    
    post_data = ""
    
    def do_POST(self):
        
        #print("Receiving new data ...")
        content_length = int(self.headers['Content-Length'])
        recv_data = self.rfile.read(content_length)
        str = recv_data.decode()  
        str_array=str.split('=')
        #print(self.path) 
        
        if("play" in str_array[0]):
            PostHandler.post_data = str_array[1]
            print(self.post_data) 
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-length", len(PostHandler.post_data))
        self.end_headers()
        self.wfile.write(PostHandler.post_data.encode())
        return
        
        '''
    def do_GET(self):

        CGIHTTPRequestHandler()
        
        str = "OK"

        print(self.path) 

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-length", len(str))
        self.end_headers()
        self.wfile.write(str.encode())
        
        '''
def get_host_ip():
    #查询本机ip地址
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip        
 
def StartServer():

    print(get_host_ip())
    sever = ThreadingHTTPServer(("",8080),PostHandler)
    sever.serve_forever()
 
if __name__=='__main__':
    print("start server ...")
    StartServer()
