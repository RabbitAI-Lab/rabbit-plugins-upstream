#!/usr/bin/env python3
"""mock_provider.py — stdlib OpenAI-compatible mock server for free-tier-ai-router
selftest. Zero dependencies, zero network (binds 127.0.0.1, ephemeral port).

Usage: python3 mock_provider.py <hits-json-file>
Prints {"port": N} on stdout, then serves until killed.

Behavior by model id:
  ok-model     -> 200 echo answer (SSE deltas when "stream": true in the body)
  ratey-model  -> 429 + Retry-After: 30
  dead-model   -> 402 (payment required)

Every /chat/completions hit is counted per model into the hits file:
  {"ok-model": 3, "ratey-model": 1}
"""
import json
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HITS_FILE = sys.argv[1] if len(sys.argv) > 1 else "/tmp/mock_hits.json"
_lock = threading.Lock()


def bump(model):
    with _lock:
        try:
            hits = json.load(open(HITS_FILE))
        except Exception:
            hits = {}
        hits[model] = hits.get(model, 0) + 1
        with open(HITS_FILE, "w") as f:
            json.dump(hits, f)


class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _send(self, code, obj, extra=None):
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path.rstrip("/") == "/v1/models":
            self._send(200, {"object": "list", "data": [
                {"id": "ok-model"}, {"id": "ratey-model"}, {"id": "dead-model"}]})
        else:
            self._send(404, {"error": {"message": "not found"}})

    def do_POST(self):
        n = int(self.headers.get("Content-Length") or 0)
        try:
            req = json.loads(self.rfile.read(n) or b"{}")
        except Exception:
            req = {}
        model = req.get("model", "")
        bump(model)
        if model == "ratey-model":
            self._send(429, {"error": {"message": "rate limited"}}, {"Retry-After": "30"})
            return
        if model == "dead-model":
            self._send(402, {"error": {"message": "payment required"}})
            return
        text = f"mock answer to: {req.get('messages', [{}])[-1].get('content', '')[:40]}"
        if req.get("stream"):
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream")
            self.end_headers()
            for piece in (text[: len(text) // 2], text[len(text) // 2:]):
                chunk = {"choices": [{"delta": {"content": piece}}]}
                self.wfile.write(f"data: {json.dumps(chunk)}\n\n".encode())
            self.wfile.write(b"data: [DONE]\n\n")
            return
        self._send(200, {"choices": [{"message": {"content": text}}]})


if __name__ == "__main__":
    srv = ThreadingHTTPServer(("127.0.0.1", 0), H)
    print(json.dumps({"port": srv.server_address[1]}), flush=True)
    srv.serve_forever()
