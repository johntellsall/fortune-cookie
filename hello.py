# INSTALL:
# brew install fortune

import SimpleHTTPServer
import SocketServer
import StringIO
import logging
import subprocess
import sys


PORT = 8000


class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def send_head(self):        # XX should work nicely with parent class
        self.send_response(200)
        self.send_header("Content-type", 'text/plain')
        self.end_headers()
        
    def do_GET(self):
        self.send_head()
        output_str = subprocess.check_output(['fortune'])
        fortunef = StringIO.StringIO(output_str)
        self.copyfile(fortunef, self.wfile)
    

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logger = logging.getLogger(__name__)

httpd = SocketServer.TCPServer(("", PORT), MyHandler)

logger.info("serving at port %d", PORT)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
logger.info("done")
