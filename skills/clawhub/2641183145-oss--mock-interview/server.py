#!/usr/bin/env python3
"""模拟面试答题页的本地 server。

只绑 127.0.0.1 —— data/ 里是用户的简历和面试回答,不能让同网段的人读到。
收满 5 个回答后进程自动退出(前端合约的一部分)。

标准库,零依赖。
"""

import json
import os
import re
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import console  # noqa: F401  — 修 Windows GBK 控制台

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT, "data")
WEB_DIR = os.path.join(ROOT, "web")
SESSION_PATH = os.path.join(DATA_DIR, "session.json")
INFO_PATH = os.path.join(DATA_DIR, "server-info.json")

HOST = "127.0.0.1"
DEFAULT_PORT = 8787
PORT_TRIES = 12

# 放行任意端口的 localhost,这样前端同事跑 Vite/CRA dev server 不用配代理
LOCALHOST_ORIGIN = re.compile(r"^http://(?:localhost|127\.0\.0\.1)(?::\d+)?$")

_lock = threading.Lock()


def load_session():
    with open(SESSION_PATH, encoding="utf-8") as f:
        return json.load(f)


def save_session(session):
    """先写临时文件再替换 —— 避免 wait.py 读到写一半的 JSON。"""
    tmp = SESSION_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(session, f, ensure_ascii=False, indent=2)
    os.replace(tmp, SESSION_PATH)


class Handler(BaseHTTPRequestHandler):
    server_version = "MockInterview/1.0"
    protocol_version = "HTTP/1.1"

    # ---------- 基础设施 ----------

    def log_message(self, fmt, *args):
        sys.stderr.write("  %s\n" % (fmt % args))

    def _cors(self):
        origin = self.headers.get("Origin")
        if origin and LOCALHOST_ORIGIN.match(origin):
            self.send_header("Access-Control-Allow-Origin", origin)
            self.send_header("Vary", "Origin")

    def _send_json(self, obj, status=200):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self._cors()
        self.end_headers()
        self.wfile.write(body)

    def _err(self, code, message, status=400):
        self._send_json({"error": {"code": code, "message": message}}, status)

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Max-Age", "3600")
        self.send_header("Content-Length", "0")
        self.end_headers()

    # ---------- 路由 ----------

    def do_GET(self):
        path = self.path.split("?")[0]
        if path == "/api/session":
            return self._get_session()
        if path == "/api/health":
            return self._get_health()
        return self._serve_static(path)

    def do_POST(self):
        if self.path.split("?")[0] != "/api/answer":
            return self._err("not_found", "未知接口", 404)
        return self._post_answer()

    # ---------- 接口 ----------

    def _get_session(self):
        with _lock:
            s = load_session()
        # 刻意不返回 raw_material —— 答题页不需要用户的原始简历
        self._send_json({
            "session_id": s.get("session_id"),
            "status": s.get("status"),
            "context": s.get("context", {}),
            "questions": s.get("questions", []),
            "answered": [a["qid"] for a in s.get("answers", [])],
            "total": len(s.get("questions", [])),
        })

    def _get_health(self):
        with _lock:
            s = load_session()
        self._send_json({
            "ok": True,
            "status": s.get("status"),
            "answered": len(s.get("answers", [])),
            "total": len(s.get("questions", [])),
        })

    def _post_answer(self):
        try:
            length = int(self.headers.get("Content-Length") or 0)
        except ValueError:
            return self._err("bad_json", "Content-Length 不合法")
        if length <= 0:
            return self._err("bad_json", "请求体为空")

        try:
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
            if not isinstance(payload, dict):
                raise ValueError
        except (ValueError, UnicodeDecodeError):
            return self._err("bad_json", "请求体不是合法 JSON 对象")

        qid = payload.get("qid")
        text = (payload.get("text") or "").strip()

        with _lock:
            s = load_session()

            if s.get("status") != "awaiting_answers":
                return self._err("session_closed", "本轮已收集完成,不再接受提交", 409)

            qids = [q["id"] for q in s.get("questions", [])]
            if qid not in qids:
                return self._err("unknown_qid", f"未知题目 id: {qid!r}")
            if not text:
                return self._err("empty_answer", "回答内容为空")

            mode = payload.get("input_mode")
            if mode not in ("voice", "text"):
                mode = "text"
            dur = payload.get("duration_sec")
            dur = dur if isinstance(dur, (int, float)) and dur >= 0 else None

            record = {
                "qid": qid,
                "text": text,
                "input_mode": mode,
                "duration_sec": dur,
                "submitted_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            }

            answers = [a for a in s.get("answers", []) if a["qid"] != qid]  # 重提=覆盖
            answers.append(record)
            answers.sort(key=lambda a: qids.index(a["qid"]))
            s["answers"] = answers

            done = len(answers) == len(qids)
            if done:
                s["status"] = "collected"
            save_session(s)

        resp = {"ok": True, "answered": len(answers), "total": len(qids), "all_done": done}
        if done:
            resp["message"] = "回答已全部收集,请回到 Claude Code 查看评分"
        self._send_json(resp)

        if done:
            # 响应已写完,给 socket 一点时间 flush 再退。
            # 前端合约:收到 all_done 后不要再发请求。
            threading.Thread(target=self._shutdown_soon, daemon=True).start()

    def _shutdown_soon(self):
        time.sleep(1.0)
        print("\n✓ 5 个回答已收集完毕,server 退出。")
        print("  回到 Claude Code,让它给你打分。")
        sys.stdout.flush()
        self.server.shutdown()

        # 兜底:万一有 keep-alive 连接吊着 serve_forever 不返回,硬退。
        # 前端合约写明「收到 all_done 后 server 就没了」,不能让它半死不活。
        def force_exit():
            time.sleep(3.0)
            os._exit(0)

        threading.Thread(target=force_exit, daemon=True).start()

    # ---------- 静态文件 ----------

    def _serve_static(self, path):
        rel = "index.html" if path == "/" else path.lstrip("/")
        full = os.path.normpath(os.path.join(WEB_DIR, rel))
        if not full.startswith(WEB_DIR):  # 目录穿越
            return self._err("not_found", "路径不合法", 404)
        if not os.path.isfile(full):
            return self._err("not_found", f"文件不存在: {rel}", 404)

        ctypes = {
            ".html": "text/html; charset=utf-8",
            ".js": "text/javascript; charset=utf-8",
            ".css": "text/css; charset=utf-8",
            ".json": "application/json; charset=utf-8",
            ".svg": "image/svg+xml",
            ".png": "image/png",
            ".ico": "image/x-icon",
            ".woff2": "font/woff2",
        }
        ext = os.path.splitext(full)[1].lower()
        with open(full, "rb") as f:
            body = f.read()
        self.send_response(200)
        self.send_header("Content-Type", ctypes.get(ext, "application/octet-stream"))
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")  # 别缓存,前端改完刷新就生效
        self._cors()
        self.end_headers()
        self.wfile.write(body)


class ExclusiveServer(ThreadingHTTPServer):
    """独占端口。

    ThreadingHTTPServer 默认 allow_reuse_address = True,在 Windows 上会映射成
    SO_REUSEADDR —— 那意味着**多个进程能同时绑同一个端口**,bind 不报错,
    请求随机落到其中一个。上一个 server 没退干净时,用户会对着旧 session 答题。

    关掉复用,让端口冲突老老实实抛 OSError,下面的 bind_server 才能往上找端口。
    """

    allow_reuse_address = False

    def server_bind(self):
        if sys.platform == "win32":
            # Windows 独有:真正的独占绑定,比关掉 SO_REUSEADDR 更硬
            import socket
            try:
                self.socket.setsockopt(socket.SOL_SOCKET,
                                       socket.SO_EXCLUSIVEADDRUSE, 1)
            except (AttributeError, OSError):
                pass
        super().server_bind()


def port_in_use(port):
    """已经有 server 在这个端口服务了吗?

    绑定检测在某些平台上不可靠,所以直接发个请求探一下。
    """
    import urllib.request
    try:
        with urllib.request.urlopen(
            f"http://{HOST}:{port}/api/health", timeout=0.6
        ) as r:
            return r.status == 200
    except Exception:
        return False


def bind_server():
    """端口占用就往上找,别让演示卡在端口冲突。"""
    last = None
    for port in range(DEFAULT_PORT, DEFAULT_PORT + PORT_TRIES):
        if port_in_use(port):
            print(f"  端口 {port} 已有 server 在跑,换下一个")
            continue
        try:
            return ExclusiveServer((HOST, port), Handler), port
        except OSError as e:
            last = e
    raise SystemExit(
        f"端口 {DEFAULT_PORT}-{DEFAULT_PORT + PORT_TRIES - 1} 都不可用: {last}\n"
        f"可能有上一轮的 server 没退干净 —— 检查一下 python 进程。"
    )


def main():
    if not os.path.exists(SESSION_PATH):
        raise SystemExit(
            "找不到 data/session.json。\n"
            "先在 Claude Code 里录入经历、生成题目,再起 server。\n"
            "(想单独联调:复制 data/session.example.json 为 data/session.json)"
        )

    s = load_session()
    n_q = len(s.get("questions", []))
    n_a = len(s.get("answers", []))

    if s.get("status") != "awaiting_answers":
        print(f"⚠ session 状态是 {s.get('status')!r},不是 awaiting_answers。")
        if s.get("status") == "collected":
            raise SystemExit("这轮回答已经收完了 —— 回 Claude Code 打分,或重开一轮。")

    httpd, port = bind_server()
    url = f"http://{HOST}:{port}"

    with open(INFO_PATH, "w", encoding="utf-8") as f:
        json.dump({"url": url, "port": port, "pid": os.getpid()}, f, indent=2)

    print(f"\n  模拟面试答题页  →  {url}\n")
    print(f"  {n_q} 道题,已答 {n_a} 道")
    print("  答完最后一题后 server 会自动退出\n")
    if s.get("context", {}).get("density_note"):
        print(f"  提示:{s['context']['density_note']}\n")
    # 后台运行时 stdout 是管道,不 flush 的话这段横幅(含 URL)看不见
    sys.stdout.flush()

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n已中断。答过的题都存好了,重新起 server 可以接着答。")
    finally:
        httpd.server_close()
        if os.path.exists(INFO_PATH):
            os.remove(INFO_PATH)


if __name__ == "__main__":
    main()
