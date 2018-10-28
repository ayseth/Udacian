

from http.server import HTTPServer, BaseHTTPRequestHandler
from http import cookies
from urllib.parse import parse_qs
from html import escape as html_escape

form = '''<!DOCTYPE html>
<title>I Remember You</title>
<p>
{}
<p>
<form method="POST">
<label>What's your age again?
<input type="text" name="yourage">
</label>
<br>
<button type="submit">Tell me!</button>
</form>
'''


class NameHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        
        length = int(self.headers.get('Content-length', 0))

        
        data = self.rfile.read(length).decode()
        yourage = parse_qs(data)["yourage"][0]

        # Create cookie.
        c = cookies.SimpleCookie()
        c['yourage'] = yourage
        c['yourage']['domain'] = 'localhost'
        c['yourage']['max-age'] = 120

        # Send a 303 back to the root page, with a cookie!
        self.send_response(303)  # redirect via GET
        self.send_header('Location', '/')
        self.send_header('Set-Cookie', c['yourage'].OutputString())
        self.end_headers()

    def do_GET(self):
        # Default message if we don't know age
        message = "I don't know your age yet!"

        # Look for a cookie in the request.
        if 'cookie' in self.headers:
            try:
                
                c = cookies.SimpleCookie(self.headers['cookie'])
                age = c['yourage'].value

                
                message = "Hey there, you're " + html_escape(age) + "years old!"
            except (KeyError, cookies.CookieError) as e:
                message = "I'm not sure what your age is!"
                print(e)

        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        mesg = form.format(message)
        self.wfile.write(mesg.encode())


if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, NameHandler)
    httpd.serve_forever()
