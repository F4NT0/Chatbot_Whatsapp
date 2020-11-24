import http.server
import socketserver

PORT = 8080
Handler  = http.server.SimpleHTTPRequestHandler # search for a index.html file

with socketserver.TCPServer(("",PORT), Handler) as httpd:
    print("Server Running on Port {}".format(PORT))
    httpd.serve_forever()