"""This is a full-stack app in a single file"""
import http.server
import socketserver
from http import HTTPStatus
TOTAL_CLICKS = 0

# Front end: Render a HTML+Javascript Page


def html(total_clicks):
    """html"""
    return f"""
        <!DOCTYPE html>
        <head>
            <title>Cookie Clicker</title>
            <script>
const update = count => document.getElementById("count").innerText = `${{count}} cookies clicked`
const doClick = async () => update(await (await fetch('/api/click', {{method: "POST"}})).json())
                const fetchClicks = async () => update(await (await fetch("/api/count")).json())
                setInterval(fetchClicks, 1000)
            </script>
        </head>
        <h3>Click the cookie to pass the time</h3>
        <button onclick="doClick()" >&#129306;</button>
        <span id="count">{total_clicks} cookies clicked</span>
    """

# Back end: Handle API requests


class Handler(http.server.SimpleHTTPRequestHandler):
    """Handler class"""

    def do_GET(self):
        """GET"""
        if self.path == '/':
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(html(TOTAL_CLICKS), "utf8"))

        if self.path == '/api/count':
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(f'{TOTAL_CLICKS}'.encode())

    def do_post(self):
        """POST"""
        global TOTAL_CLICKS
        if self.path == '/api/click':
            TOTAL_CLICKS += 1
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(f'{TOTAL_CLICKS}'.encode())


print('Launch API')
socketserver.TCPServer(('', 5000), Handler).serve_forever()
