#!/usr/bin/env python3
"""YZL-AIoT 南向设备客户端（Python，标准库实现）。

一个协议功能一个方法，加载技能后可直接 import：

    from south_client import SouthDevice
    d = SouthDevice(device_id="WANCD1-0000000007", password="123456")
    d.connect()                       # TCP 41032
    d.login()                         # lgn
    d.report(wd="25.3")               # facs
    d.heartbeat()                     # hear
    d.order_conf(tra)                 # order_conf
    d.order_reply(tra, sw="1")        # facs_reply

支持 TCP（41032）与 UDP（40501）；MQTT（1883）见 SKILL.md 的 topic 与 payload 说明。
帧格式来自 docs/01-协议说明.md（2026-11-04 实测）。
"""

import json
import socket
import time

DEFAULT_HOST = "ciot.yzlkj.com"
TCP_PORT = 41032
UDP_PORT = 40501

ERRORS = {
    0: "成功",
    1: "参数错误",
    2: "对象不存在",
    3: "认证失败",
    4: "未登录",
    9: "未知函数/服务器错误",
}


class SouthError(Exception):
    def __init__(self, message, code=None, payload=None):
        super().__init__(message)
        self.code = code
        self.payload = payload


class SouthDevice:
    def __init__(self, device_id, password, host=DEFAULT_HOST, port=None,
                 mode="tcp", timeout=8.0, product_id=None):
        self.device_id = device_id
        self.password = password
        self.host = host
        self.mode = mode
        self.port = port or (UDP_PORT if mode == "udp" else TCP_PORT)
        self.timeout = timeout
        self.product_id = product_id
        self.sock = None
        self._buf = b""
        self._fid = 0

    # ------------------------------------------------------------- 连接/关闭
    def connect(self, host=None, port=None):
        self.host = host or self.host
        self.port = port or self.port
        kind = socket.SOCK_DGRAM if self.mode == "udp" else socket.SOCK_STREAM
        self.sock = socket.socket(socket.AF_INET, kind)
        self.sock.settimeout(self.timeout)
        if self.mode == "udp":
            self.sock.connect((self.host, self.port))
        else:
            self.sock.connect((self.host, self.port))
        return self

    def close(self):
        if self.sock:
            try:
                self.sock.close()
            finally:
                self.sock = None

    # ------------------------------------------------------------- 帧构造/收发
    def _next_fid(self, prefix="F"):
        self._fid += 1
        return "%s%d" % (prefix, self._fid)

    def frame(self, func, args, fid=None):
        return json.dumps({"top": "func", "ter": self.device_id,
                           "data": [{"func": func, "args": list(args), "fid": fid or self._next_fid()}]},
                          ensure_ascii=False, separators=(",", ":"))

    def send_raw(self, text):
        if not self.sock:
            raise SouthError("未连接，先 connect()")
        self.sock.sendall((text + "\n").encode("utf-8") if self.mode == "tcp" else text.encode("utf-8"))

    def recv(self, timeout=None):
        """读一帧（TCP 按 \\n 拆；UDP 一个数据报），返回 dict。"""
        if not self.sock:
            raise SouthError("未连接，先 connect()")
        if timeout is not None:
            self.sock.settimeout(timeout)
        if self.mode == "udp":
            data, _ = self.sock.recvfrom(65535)
            return json.loads(data.decode("utf-8", "replace"))
        while b"\n" not in self._buf:
            chunk = self.sock.recv(4096)
            if not chunk:
                raise SouthError("连接已关闭")
            self._buf += chunk
        line, self._buf = self._buf.split(b"\n", 1)
        text = line.decode("utf-8", "replace").strip()
        if not text:
            return self.recv()
        return json.loads(text)

    def call(self, func, args, fid=None):
        """发一个功能帧并等它对应的 result。"""
        self.send_raw(self.frame(func, args, fid))
        return self.recv()

    @staticmethod
    def result_of(reply, func=None):
        """从 result 帧里取 data[0]。"""
        for item in (reply or {}).get("data", []):
            if func is None or item.get("func") == func:
                return item
        return None

    def check(self, reply, func):
        item = self.result_of(reply, func)
        code = None if item is None else item.get("code")
        if code != 0:
            raise SouthError("%s 失败：%s (code=%s)" % (func, ERRORS.get(code, "未知"), code),
                             code=code, payload=reply)
        return item

    # ------------------------------------------------------------- 协议功能
    def login(self):
        """lgn：登录，返回会话 token。"""
        return self.check(self.call("lgn", [self.password], "L1"), "lgn")

    def report(self, **values):
        """facs：实时上报（args 为扁平键值对）。"""
        args = []
        for k, v in values.items():
            args.extend([k, str(v)])
        return self.check(self.call("facs", args), "facs")

    def report_pairs(self, pairs):
        """facs：以 [(key, value), ...] 形式上报。"""
        args = []
        for k, v in pairs:
            args.extend([str(k), str(v)])
        return self.check(self.call("facs", args), "facs")

    def heartbeat(self):
        """hear：心跳。"""
        return self.check(self.call("hear", [], "H1"), "hear")

    def get_time(self):
        """get_time：校时（返回字符串或 Unix 秒，两种都可能）。"""
        item = self.check(self.call("get_time", ["1"], "T1"), "get_time")
        return item.get("result")

    def order_conf(self, tra):
        """order_conf：确认收到指令。"""
        return self.check(self.call("order_conf", [tra], "C1"), "order_conf")

    def order_reply(self, tra, **values):
        """facs_reply：执行结果 + 实际值。"""
        args = [tra, self.device_id]
        for k, v in values.items():
            args.extend([k, str(v)])
        return self.check(self.call("facs_reply", args), "facs_reply")

    def backfill(self, points):
        """facs_his：历史补传。

        points = [{"ts": 1792714948, "values": {"kk1": "11"}}, ...]
        单包 ≤ 1000 点；时间戳必须是 Unix 秒数字。
        """
        args = []
        for p in points:
            args.append(int(p["ts"]))
            for k, v in p.get("values", {}).items():
                args.extend([k, str(v)])
        if len(points) > 1000:
            raise ValueError("单包最多 1000 个数据点")
        return self.check(self.call("facs_his", args), "facs_his")

    def ota_info(self, firmware_id):
        """gfinfo：查固件信息。"""
        return self.check(self.call("gfinfo", [firmware_id], "I1"), "gfinfo")

    def ota_get(self, firmware_id, index):
        """gfcet：取第 index 个固件分片。"""
        return self.check(self.call("gfcet", [firmware_id, int(index)], "I2"), "gfcet")

    def pull_order(self):
        """get_order（UDP）：拉取挂起指令，无指令时 result 为 null。"""
        return self.check(self.call("get_order", [], "G1"), "get_order")

    def wakeup(self, **values):
        """lgn_facs（UDP）：唤醒 + 数据一体上报，args=[密码, 设备ID, k,v,...]。"""
        args = [self.password, self.device_id]
        for k, v in values.items():
            args.extend([k, str(v)])
        return self.check(self.call("lgn_facs", args, "L1"), "lgn_facs")

    # ------------------------------------------------------------- 指令循环
    def serve_forever(self, on_order=None, heartbeat_every=60, sleep=0.2):
        """简单设备循环：收 order → 确认 → 回调执行 → 回 facs_reply。"""
        last_beat = 0.0
        while True:
            if time.time() - last_beat >= heartbeat_every:
                self.heartbeat()
                last_beat = time.time()
            try:
                msg = self.recv(timeout=sleep)
            except socket.timeout:
                continue
            if msg.get("top") != "order":
                continue
            for item in msg.get("data", []):
                tra = item.get("tra", "")
                cmd = item.get("cmd")
                args = item.get("args", [])
                self.order_conf(tra)
                values = on_order(cmd, args) if on_order else {}
                self.order_reply(tra, **(values or {}))
