#!/usr/bin/env python3
#
# Udacian activity to practice get and post http
#

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from ud import udacian


memory = []
form = '''<!DOCTYPE html>
  <title>Udacian</title>
  <form method="POST" action="http://localhost:8000/">
    <textarea name="name">name</textarea>
    <br>
    <textarea name="city">city</textarea>
    <br>
    <textarea name="enrollment">enrollment</textarea>
    <br>
    <textarea name="nanodegree">nanodegree</textarea>
    <br>
    <textarea name="status">status</textarea>
    <br>
    <button type="submit">Post it!</button>
  </form>
  <pre>
{}
  </pre>
'''

class MessageHandler(BaseHTTPRequestHandler):
  def do_POST(self):
    length = int(self.headers.get('Content-length', 0))
    data = self.rfile.read(length).decode()

    name = parse_qs(data)["name"][0]
    city = parse_qs(data)["city"][0]
    enrollment = parse_qs(data)["enrollment"][0]
    nanodegree = parse_qs(data)["nanodegree"][0]
    status = parse_qs(data)["status"][0]
    fun = udacian(name,city,enrollment,nanodegree,status)
    memory.append(fun)

    self.send_response(303)
    self.send_header('Location', '/')
    self.end_headers()
    
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type','text/html')
    self.end_headers()
    self.wfile.write(form.encode())
    for fun in memory:
      user = fun.myfunc()
      self.wfile.write(user.encode())



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))   # Use PORT if it's there.
    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, Shortener)
    httpd.serve_forever()