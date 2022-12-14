from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<!doctype html>
<html>
<head>
<title>My web server</title>
</head>
<body>
<h1>Top Five Web Application Frameworks</h1>
<h2>1.Django</h2>
<h2>2.Express</h2>
<h2>3.Angluar</h2>
<h2>4.BootStrap</h2>
<h2>5.Ruby on Rails</h2>
</body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request recieved...")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my web server")
server_address =('',80)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()
