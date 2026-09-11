#!/usr/bin/env python3
"""Mock Telegram/Discord API server for autothread offline tests.

Listens on 127.0.0.1:<port> and emulates:
  Telegram Bot API endpoints: /bot<token>/createForumTopic, /sendMessage,
                              /forwardMessage
  Discord API endpoints:      /channels/<id>, /channels/<id>/messages/<mid>/threads,
                              /channels/<tid>/messages

Every request is appended (one JSON line each) to a log file so tests can
assert on the exact requests made.
"""

import json
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

LOG_FILE = sys.argv[2] if len(sys.argv) > 2 else "/tmp/autothread_mock_requests.log"


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):  # silence default stderr logging
        pass

    def _log(self, path, body=None):
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps({"path": path, "body": body}) + "\n")

    def _reply(self, payload, status=200):
        data = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        path = urlparse(self.path).path
        self._log(path)
        # Discord: resolve channel -> guild
        if "/channels/" in path and path.count("/") == 2:
            self._reply({"id": path.split("/")[-1], "guild_id": "999", "type": 0})
            return
        self._reply({"error": "unknown GET " + path}, 404)

    def do_POST(self):
        path = urlparse(self.path).path
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length).decode() if length else ""
        ctype = self.headers.get("Content-Type", "")
        body = raw
        if "json" in ctype and raw:
            try:
                body = json.loads(raw)
            except ValueError:
                pass
        else:
            body = {k: v[0] for k, v in parse_qs(raw).items()}
        self._log(path, body)

        # Telegram endpoints (path contains /bot<token>/...)
        if path.endswith("/createForumTopic"):
            self._reply({"ok": True, "result": {"message_thread_id": 777,
                         "message": {"message_id": 1}}})
        elif path.endswith("/sendMessage"):
            self._reply({"ok": True, "result": {"message_id": 2}})
        elif path.endswith("/forwardMessage"):
            self._reply({"ok": True, "result": {"message_id": 3}})
        # Discord endpoints
        elif "/threads" in path:
            self._reply({"id": "555", "name": body.get("name", "")})
        elif "/channels/" in path:
            self._reply({"id": "4242"})
        else:
            self._reply({"message": "unknown POST " + path}, 404)


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8977
    HTTPServer(("127.0.0.1", port), Handler).serve_forever()
