#!/usr/bin/env bash
# Python-stdlib JSON-RPC mock for BATS tests. No external deps beyond python3.
set -euo pipefail

MOCK_PORT=""
MOCK_PID=""
MOCK_ACCESS_LOG=""
MOCK_BODY_DIR=""
MOCK_FIXTURE_DIR=""

start_mock_rpc() {
  local port="${1:?port required}"
  local fixture_dir="${2:?fixture_dir required}"
  MOCK_PORT="$port"; MOCK_FIXTURE_DIR="$fixture_dir"
  MOCK_ACCESS_LOG="$(mktemp)"
  : > "$MOCK_ACCESS_LOG"
  MOCK_BODY_DIR="$(mktemp -d)"
  python3 - "$fixture_dir" "$MOCK_ACCESS_LOG" "$MOCK_BODY_DIR" "$port" <<'PY' &
import sys, json, os
from http.server import BaseHTTPRequestHandler, HTTPServer
fixture_dir, access_log, body_dir, port = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
logf = open(access_log, "a")
class H(BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def do_POST(self):
        n = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(n).decode()
        try: req = json.loads(body)
        except Exception: req = {}
        method = req.get("method", "")
        logf.write(method + "\n"); logf.flush()
        if method:
            try:
                with open(os.path.join(body_dir, method + ".body"), "w") as bf:
                    bf.write(body)
            except Exception: pass
        path = os.path.join(fixture_dir, method + ".ERR.json")
        if not os.path.exists(path): path = os.path.join(fixture_dir, method + ".json")
        with open(path) as f: resp = f.read()
        self.send_response(200); self.send_header("Content-Type","application/json")
        self.end_headers(); self.wfile.write(resp.encode())
HTTPServer(("127.0.0.1", port), H).serve_forever()
PY
  MOCK_PID=$!
  for _ in $(seq 1 50); do
    curl -s -o /dev/null "http://127.0.0.1:${MOCK_PORT}/" --max-time 1 2>/dev/null && return 0
    sleep 0.05
  done
}

stop_mock_rpc() {
  [[ -n "${MOCK_PID:-}" ]] && kill "$MOCK_PID" 2>/dev/null || true
  [[ -n "${MOCK_ACCESS_LOG:-}" ]] && rm -f "$MOCK_ACCESS_LOG" || true
  [[ -n "${MOCK_BODY_DIR:-}" ]] && rm -rf "$MOCK_BODY_DIR" || true
  MOCK_PID=""; MOCK_ACCESS_LOG=""; MOCK_BODY_DIR=""
}

mock_clear_calls() {
  : > "$MOCK_ACCESS_LOG"
  if [[ -n "${MOCK_BODY_DIR:-}" ]]; then
    rm -f "$MOCK_BODY_DIR"/*.body 2>/dev/null || true
  fi
}

mock_call_count() {
  local m="$1" c=0
  [[ -f "$MOCK_ACCESS_LOG" ]] && c="$(grep -c "^${m}$" "$MOCK_ACCESS_LOG" 2>/dev/null || true)"
  echo "${c:-0}"
}

# Print the most recent raw request body sent for METHOD. Returns 1 if no
# request for METHOD has been recorded.
mock_last_body() {
  local m="${1:?method required}"
  local f="${MOCK_BODY_DIR:-}/$m.body"
  [[ -f "$f" ]] || return 1
  cat "$f"
}
