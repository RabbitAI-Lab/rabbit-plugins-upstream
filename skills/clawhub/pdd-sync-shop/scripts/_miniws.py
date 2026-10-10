#!/usr/bin/env python3
"""_miniws.py — 纯 Python 标准库的极简 WebSocket 客户端（RFC 6455 客户端子集）。

存在理由：让本技能在"什么都没有"的业务电脑上零第三方依赖可跑——
有 websocket-client 时优先用它；没有时本模块兜底（接口兼容 create_connection）。
只为本机 CDP 设计：ws://localhost:PORT/devtools/...，无 TLS、无代理、无扩展协商。

能力边界（够 CDP 用，不做通用库）：
  - 客户端发送按规范加掩码；接收 text/binary/continuation 分片聚合
  - 7/16/64-bit 三档长度（goodsList 响应几百 KB 属 64-bit 档，已覆盖）
  - ping 自动回 pong；close 帧按规范回应
"""
import base64, json, os, socket, struct
from urllib.parse import urlparse


class MiniWS:
    def __init__(self, url, timeout=60):
        u = urlparse(url)
        host, port = u.hostname or "localhost", u.port or 80
        self.sock = socket.create_connection((host, port), timeout=timeout)
        self._buf = bytearray()
        key = base64.b64encode(os.urandom(16)).decode()
        path = (u.path or "/") + (("?" + u.query) if u.query else "")
        req = (f"GET {path} HTTP/1.1\r\nHost: {host}:{port}\r\n"
               "Upgrade: websocket\r\nConnection: Upgrade\r\n"
               f"Sec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n")
        self.sock.sendall(req.encode())
        raw = bytearray()
        while b"\r\n\r\n" not in raw:
            chunk = self.sock.recv(4096)
            if not chunk:
                raise ConnectionError("websocket 握手中断")
            raw += chunk
        head, _, rest = bytes(raw).partition(b"\r\n\r\n")
        status = head.split(b"\r\n", 1)[0]
        if b" 101" not in status:
            raise ConnectionError("websocket 握手失败: " + status.decode(errors="replace")[:80])
        self._buf += rest  # 握手响应后可能已粘了首帧数据

    # ---- 底层 ----
    def _read_exact(self, n):
        while len(self._buf) < n:
            chunk = self.sock.recv(65536)
            if not chunk:
                raise ConnectionError("连接被关闭")
            self._buf += chunk
        out = bytes(self._buf[:n])
        del self._buf[:n]
        return out

    def _send_frame(self, opcode, payload=b""):
        mask = os.urandom(4)
        masked = bytes(b ^ mask[i % 4] for i, b in enumerate(payload))
        n = len(payload)
        if n < 126:
            hdr = bytes([0x80 | opcode, 0x80 | n])
        elif n < 65536:
            hdr = bytes([0x80 | opcode, 0x80 | 126]) + struct.pack(">H", n)
        else:
            hdr = bytes([0x80 | opcode, 0x80 | 127]) + struct.pack(">Q", n)
        self.sock.sendall(hdr + mask + masked)

    # ---- websocket-client 兼容接口 ----
    def send(self, data):
        self._send_frame(0x1, data.encode() if isinstance(data, str) else bytes(data))

    def recv(self):
        msg = bytearray()
        while True:
            b1, b2 = self._read_exact(2)
            fin, op = b1 & 0x80, b1 & 0x0F
            ln = b2 & 0x7F
            if ln == 126:
                ln = struct.unpack(">H", self._read_exact(2))[0]
            elif ln == 127:
                ln = struct.unpack(">Q", self._read_exact(8))[0]
            if b2 & 0x80:  # 服务端帧按规范不掩码；容错处理
                mk = self._read_exact(4)
                data = bytes(c ^ mk[i % 4] for i, c in enumerate(self._read_exact(ln)))
            else:
                data = self._read_exact(ln)
            if op == 0x8:   # close
                try: self._send_frame(0x8)
                except Exception: pass
                raise ConnectionError("对端关闭连接")
            if op == 0x9:   # ping → pong
                self._send_frame(0xA, data)
                continue
            if op == 0xA:   # pong：忽略
                continue
            msg += data     # text/binary/continuation
            if fin:
                return msg.decode()

    def close(self):
        try: self._send_frame(0x8)
        except Exception: pass
        try: self.sock.close()
        except Exception: pass


def create_connection(url, timeout=60, **_ignored):
    """兼容 websocket.create_connection(url, timeout=, suppress_origin=, max_size=...)。
    多余参数静默忽略（本实现天然不发 Origin、无消息大小上限）。"""
    return MiniWS(url, timeout=timeout)
