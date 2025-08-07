# app.py
from http.server import SimpleHTTPRequestHandler, HTTPServer

host = "0.0.0.0"
port = 80

server = HTTPServer((host, port), SimpleHTTPRequestHandler)
print(f"Starting server on http://{host}:{port}")
server.serve_forever()
