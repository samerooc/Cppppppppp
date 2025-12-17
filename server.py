import http.server
import socketserver
from urllib.parse import urlparse

PORT = 5000
HOST = "0.0.0.0"

class NoCacheHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        self.path = parsed_path.path
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()
    
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

class ReuseAddrTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

with ReuseAddrTCPServer((HOST, PORT), NoCacheHTTPRequestHandler) as httpd:
    print(f"Serving at http://{HOST}:{PORT}")
    httpd.serve_forever()
