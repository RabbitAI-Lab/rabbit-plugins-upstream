#!/usr/bin/env python3
"""Render a validated infographic plan into a PNG image via headless Chrome CDP.

Pipeline: plan JSON -> self-contained HTML (reuse render_infographic_html) ->
PNG (full-page screenshot via Chrome DevTools Protocol).

Zero Python dependencies beyond the standard library. Requires Google Chrome
or Chromium available on the system (PATH lookup or CHROME_PATH env var).

Usage:
    python3 scripts/render_infographic_png.py examples/infographic-flywheel-demo.json
    python3 scripts/render_infographic_png.py plan.json --out /tmp/out.png --scale 2
    python3 scripts/render_infographic_png.py plan.json --width 900 --scale 2
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import shutil
import socket
import struct
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path
from typing import Optional, Tuple

# Reuse the HTML renderer
sys.path.insert(0, str(Path(__file__).parent))
from render_infographic_html import (  # noqa: E402
    DEFAULT_SCHEMA_PATH,
    build_html,
    render_plan,
)

DEFAULT_SCALE = 2          # 2x for crisp output (small red book / public account)
DEFAULT_WIDTH = 1000       # CSS viewport width
DEFAULT_DEBUG_PORT = 9222  # Chrome remote debugging port
DEFAULT_NAV_TIMEOUT_S = 20


# ---------------------------------------------------------------------------
# Chrome lifecycle
# ---------------------------------------------------------------------------

def find_chrome() -> str:
    """Locate Chrome/Chromium binary."""
    env = os.environ.get("CHROME_PATH")
    if env and Path(env).exists():
        return env
    for cand in (
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/usr/bin/google-chrome",
        "/usr/bin/chromium",
        "/usr/bin/chromium-browser",
        shutil.which("chrome"),
        shutil.which("google-chrome"),
        shutil.which("chromium"),
    ):
        if cand and Path(cand).exists():
            return cand
    raise FileNotFoundError(
        "Chrome/Chromium not found. Set CHROME_PATH or install Google Chrome."
    )


def start_chrome(port: int = DEFAULT_DEBUG_PORT, viewport_width: int = DEFAULT_WIDTH, scale: int = DEFAULT_SCALE) -> subprocess.Popen:
    """Start headless Chrome with a debug port. The caller will navigate to a file via CDP."""
    chrome = find_chrome()
    cmd = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--hide-scrollbars",
        "--disable-extensions",
        "--disable-background-networking",
        f"--remote-debugging-port={port}",
        f"--window-size={viewport_width},800",
        f"--force-device-scale-factor={scale}",
        "about:blank",
    ]
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    wait_for_debug_port(proc, port=port, timeout_s=15.0)
    return proc


def wait_for_debug_port(proc: subprocess.Popen, port: int, timeout_s: float) -> int:
    """Poll /json/version on the given port until Chrome answers."""
    deadline = time.monotonic() + timeout_s
    last_err: Optional[Exception] = None
    url = f"http://127.0.0.1:{port}/json/version"
    while time.monotonic() < deadline:
        if proc.poll() is not None:
            raise RuntimeError(f"Chrome exited early with code {proc.returncode}")
        try:
            with urllib.request.urlopen(url, timeout=0.5) as r:
                data = json.loads(r.read().decode("utf-8"))
                if "Browser" in data:
                    return port
        except Exception as e:
            last_err = e
            time.sleep(0.15)
    raise RuntimeError(
        f"Chrome debug port {port} not ready in {timeout_s}s "
        f"(is another Chrome using it?): {last_err}"
    )


def fetch_page_ws(port: int) -> str:
    """Return the websocket URL of the first page target from Chrome /json listing."""
    with urllib.request.urlopen(f"http://127.0.0.1:{port}/json", timeout=5) as r:
        pages = json.loads(r.read().decode("utf-8"))
    for p in pages:
        if p.get("type") == "page":
            return p["webSocketDebuggerUrl"]
    raise RuntimeError("No page target found in Chrome /json")


# ---------------------------------------------------------------------------
# Minimal WebSocket client (RFC 6455) over raw socket
# ---------------------------------------------------------------------------

class WSClient:
    def __init__(self, url: str):
        # url: ws://host:port/path
        if not url.startswith("ws://"):
            raise ValueError(f"Only ws:// supported, got {url}")
        rest = url[len("ws://"):]
        host_port, _, path = rest.partition("/")
        self.host, _, self.port_str = host_port.partition(":")
        self.port = int(self.port_str) if self.port_str else 80
        self.path = "/" + path
        self.sock: Optional[socket.socket] = None
        self._msg_id = 0

    def connect(self) -> None:
        s = socket.create_connection((self.host, self.port), timeout=10)
        key = base64.b64encode(os.urandom(16)).decode("ascii")
        req = (
            f"GET {self.path} HTTP/1.1\r\n"
            f"Host: {self.host}:{self.port}\r\n"
            "Upgrade: websocket\r\n"
            "Connection: Upgrade\r\n"
            f"Sec-WebSocket-Key: {key}\r\n"
            "Sec-WebSocket-Version: 13\r\n"
            "\r\n"
        )
        s.sendall(req.encode("ascii"))
        # Read response headers
        buf = b""
        while b"\r\n\r\n" not in buf:
            chunk = s.recv(4096)
            if not chunk:
                raise ConnectionError("Chrome closed during WS handshake")
            buf += chunk
        head, _, _ = buf.partition(b"\r\n\r\n")
        if b" 101 " not in head.split(b"\r\n", 1)[0]:
            raise ConnectionError(f"WS handshake failed: {head[:200]!r}")
        # Drain any extra bytes (shouldn't be any for upgrade)
        self.sock = s

    def close(self) -> None:
        if self.sock is not None:
            try:
                self.sock.close()
            except Exception:
                pass
            self.sock = None

    def _send_frame(self, payload: bytes, opcode: int = 0x1) -> None:
        assert self.sock is not None
        # Client must mask. Frame header:
        # byte 0: FIN(1) RSV(3) opcode(4)
        # byte 1: MASK(1) payload_len(7); 126/127 for 16/64-bit extended len
        header = bytearray([0x80 | (opcode & 0x0F)])
        L = len(payload)
        if L < 126:
            header.append(0x80 | L)
        elif L < (1 << 16):
            header.append(0x80 | 126)
            header += struct.pack(">H", L)
        else:
            header.append(0x80 | 127)
            header += struct.pack(">Q", L)
        mask = os.urandom(4)
        header += mask
        masked = bytearray(b ^ mask[i % 4] for i, b in enumerate(payload))
        self.sock.sendall(bytes(header) + bytes(masked))

    def _recv_exact(self, n: int) -> bytes:
        assert self.sock is not None
        buf = b""
        while len(buf) < n:
            chunk = self.sock.recv(n - len(buf))
            if not chunk:
                raise ConnectionError("WS closed during recv")
            buf += chunk
        return buf

    def _recv_frame(self) -> Tuple[int, bytes]:
        """Return (opcode, payload)."""
        assert self.sock is not None
        b1, b2 = self._recv_exact(2)
        fin = b1 >> 7
        opcode = b1 & 0x0F
        masked = (b2 >> 7) & 1
        L = b2 & 0x7F
        if L == 126:
            L = struct.unpack(">H", self._recv_exact(2))[0]
        elif L == 127:
            L = struct.unpack(">Q", self._recv_exact(8))[0]
        if masked:
            mask_key = self._recv_exact(4)
        else:
            mask_key = None
        payload = self._recv_exact(L)
        if mask_key:
            payload = bytes(b ^ mask_key[i % 4] for i, b in enumerate(payload))
        if not fin:
            # Simple client: no fragmentation expected
            raise ConnectionError("Fragmented frame not supported")
        return opcode, payload

    def send_request(self, method: str, params: Optional[dict] = None) -> int:
        self._msg_id += 1
        msg = {"id": self._msg_id, "method": method, "params": params or {}}
        self._send_frame(json.dumps(msg).encode("utf-8"))
        return self._msg_id

    def recv_message(self) -> dict:
        """Receive frames until a JSON message is complete; return parsed dict."""
        while True:
            opcode, payload = self._recv_frame()
            if opcode == 0x8:  # close
                raise ConnectionError("Chrome closed the WS connection")
            if opcode == 0x9:  # ping
                self._send_frame(payload, opcode=0xA)  # pong
                continue
            if opcode == 0x1:  # text
                return json.loads(payload.decode("utf-8"))
            # Skip binary / continuation / etc.
            if opcode in (0x0, 0x2):
                continue

    def wait_for(self, msg_id: int, method_to_wait: Optional[str] = None, timeout_s: float = DEFAULT_NAV_TIMEOUT_S):
        """Block until we get a response for msg_id (or an event matching method_to_wait)."""
        deadline = time.monotonic() + timeout_s
        while time.monotonic() < deadline:
            msg = self.recv_message()
            if "id" in msg and msg["id"] == msg_id:
                if "error" in msg:
                    raise RuntimeError(f"CDP error: {msg['error']}")
                return msg.get("result")
            if method_to_wait and msg.get("method") == method_to_wait:
                return msg
        raise TimeoutError(f"Timed out waiting for id={msg_id} / method={method_to_wait}")


# ---------------------------------------------------------------------------
# Pipeline
# ---------------------------------------------------------------------------

def capture_png(
    html_path: Path,
    out_path: Path,
    viewport_width: int = DEFAULT_WIDTH,
    scale: int = DEFAULT_SCALE,
    port: int = DEFAULT_DEBUG_PORT,
) -> Path:
    proc = start_chrome(port=port, viewport_width=viewport_width, scale=scale)
    try:
        ws_url = fetch_page_ws(port)
        ws = WSClient(ws_url)
        ws.connect()
        try:
            ws.send_request("Page.enable")
            ws.wait_for(1, timeout_s=5.0)
            # Navigate to the HTML file; this triggers a fresh loadEventFired.
            nav_id = ws.send_request("Page.navigate", {"url": f"file://{html_path}"})
            nav_result = ws.wait_for(nav_id, method_to_wait="Page.loadEventFired", timeout_s=DEFAULT_NAV_TIMEOUT_S)
            # Give layout & web fonts a moment to settle.
            time.sleep(0.5)
            cap_id = ws.send_request(
                "Page.captureScreenshot",
                {
                    "format": "png",
                    "captureBeyondViewport": True,
                    "fromSurface": True,
                    "optimizeForSpeed": False,
                },
            )
            result = ws.wait_for(cap_id, timeout_s=DEFAULT_NAV_TIMEOUT_S)
            data = result.get("data")
            if not data:
                raise RuntimeError(f"captureScreenshot returned no data: {result}")
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_bytes(base64.b64decode(data))
            return out_path
        finally:
            ws.close()
    finally:
        try:
            proc.terminate()
            proc.wait(timeout=5)
        except Exception:
            try:
                proc.kill()
            except Exception:
                pass


def render_plan_to_png(
    plan_path: Path,
    out_path: Path,
    schema_path: Path,
    viewport_width: int = DEFAULT_WIDTH,
    scale: int = DEFAULT_SCALE,
) -> dict:
    plan = render_plan(plan_path, schema_path)
    html_doc = build_html(plan)
    with tempfile.TemporaryDirectory() as td:
        html_path = Path(td) / f"{plan.get('infographic_id', plan_path.stem)}.html"
        html_path.write_text(html_doc, encoding="utf-8")
        written = capture_png(html_path, out_path, viewport_width, scale)
    return {
        "ok": True,
        "plan_path": str(plan_path),
        "png_path": str(written),
        "width": viewport_width,
        "scale": scale,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Render an infographic plan JSON to a PNG image via headless Chrome CDP."
    )
    parser.add_argument("infographic_plans", nargs="+", help="Path(s) to infographic plan JSON")
    parser.add_argument("--schema", default=str(DEFAULT_SCHEMA_PATH), help="Path to infographic-plan schema")
    parser.add_argument("--out", default="/tmp/text-to-infographic-png", help="Output directory for PNG files")
    parser.add_argument("--width", type=int, default=DEFAULT_WIDTH, help="CSS viewport width (default 1000)")
    parser.add_argument("--scale", type=int, default=DEFAULT_SCALE, help="Device scale factor / DPR (default 2)")
    args = parser.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    schema_path = Path(args.schema)

    results = []
    for plan_path in args.infographic_plans:
        plan_path = Path(plan_path)
        plan = render_plan(plan_path, schema_path)
        slug = plan.get("infographic_id", plan_path.stem)
        out_file = out_dir / f"{slug}.png"
        try:
            render_plan_to_png(plan_path, out_file, schema_path, args.width, args.scale)
            results.append({"ok": True, "plan": str(plan_path), "png": str(out_file)})
        except Exception as e:
            results.append({"ok": False, "plan": str(plan_path), "error": str(e)})

    summary = {
        "out_dir": str(out_dir),
        "width": args.width,
        "scale": args.scale,
        "results": results,
        "ok": all(r["ok"] for r in results),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if summary["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
