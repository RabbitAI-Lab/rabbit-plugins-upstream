"""南向本地 mock 服务：模拟平台 TCP 41032，用于离线验证 lib/south_client.py。

启动：python tests/mock_south.py [port]
"""
import json
import socket
import sys
import threading


class MockSouth(threading.Thread):
    def __init__(self, port=0):
        super().__init__(daemon=True)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(("127.0.0.1", port))
        self.port = self.sock.getsockname()[1]
        self.sock.listen(1)
        self.frames = []
        self.conn = None
        self._lock = threading.Lock()

    def run(self):
        conn, _ = self.sock.accept()
        self.conn = conn
        buf = b""
        while True:
            try:
                chunk = conn.recv(4096)
            except OSError:
                break
            if not chunk:
                break
            buf += chunk
            while b"\n" in buf:
                line, buf = buf.split(b"\n", 1)
                self._handle(line.decode("utf-8", "replace"))

    def _handle(self, text):
        if not text.strip():
            return
        msg = json.loads(text)
        item = msg["data"][0]
        func = item["func"]
        with self._lock:
            self.frames.append(msg)
        result = None
        if func == "lgn":
            result = "SESSION-1"
        elif func == "get_time":
            result = "2026-11-04 01:05:14"
        elif func == "gfinfo":
            result = {"version": "1.0", "total": 2, "size": 512}
        elif func == "gfcet":
            result = {"fmid": item["args"][0], "no": item["args"][1], "pro": 100, "data": "A8FF3C"}
        reply = {"top": "result", "ter": msg.get("ter"), "data": [
            {"func": func, "code": 0, "result": result, "fid": item.get("fid")}], "ack": ""}
        self.conn.sendall((json.dumps(reply, ensure_ascii=False) + "\n").encode("utf-8"))

    def push_order(self, tra, args, cmd="set"):
        payload = {"top": "order", "ter": "DEV", "data": [
            {"cmd": cmd, "args": args, "tra": tra}], "ack": "1"}
        self.conn.sendall((json.dumps(payload, ensure_ascii=False) + "\n").encode("utf-8"))

    def funcs(self):
        return [m["data"][0]["func"] for m in self.frames]


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 41032
    srv = MockSouth(port)
    srv.start()
    print("mock south on 127.0.0.1:%d" % srv.port)
    try:
        while True:
            srv.join(1)
    except KeyboardInterrupt:
        pass
