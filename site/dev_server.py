# Local preview of the site, wrapped in the same skeleton the Claude artifact host adds
# (doctype, charset, viewport, small reset). Usage: python3 site/dev_server.py  -> http://localhost:4173
import http.server, os, socketserver

HERE = os.path.dirname(os.path.abspath(__file__))
PORT = int(os.environ.get("PORT", "4173"))
HEAD = ('<!doctype html><html><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top);padding-bottom:env(safe-area-inset-bottom)}'
        'body{margin:0;font:14px system-ui,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>'
        '</head><body>')


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=HERE, **kw)

    def do_GET(self):
        if self.path.split("?")[0] in ("/", "/index.html"):
            body = (HEAD + open(os.path.join(HERE, "index.html"), encoding="utf-8").read() + "</body></html>").encode()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)
        else:
            super().do_GET()


socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as s:
    print(f"Serving on http://localhost:{PORT}", flush=True)
    s.serve_forever()
