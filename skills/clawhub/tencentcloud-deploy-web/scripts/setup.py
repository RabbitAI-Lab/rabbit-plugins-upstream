#!/usr/bin/env python3
"""腾讯云首次接入向导：在本机打开一个网页，带非技术用户完成「注册 → 建策略 → 建子用户 → 交密钥」。
纯标准库，Python 3.8+，Windows/macOS/Linux 通用。

为什么用网页：用户不需要打开终端；密钥只在用户浏览器 → 本机进程 → 本机文件之间流转，
不经过 agent 的对话，模型看不到。网页只监听 127.0.0.1，地址里带一次性 token，保存成功后自动退出。

用法（agent 来运行；它会阻塞到用户完成或超时，建议在后台运行）：
    python setup.py [--profile agent-ops] [--region ap-hongkong] [--no-browser] [--timeout 1800] [--force]

stderr 会先打印网页地址（浏览器没自动打开时，把地址发给用户）。
结束时 stdout 输出一行 JSON：
    {"ok": true,  "profile": "agent-ops", "uin": "...", "access": {...}}
    {"ok": false, "reason": "timeout|already_configured|..."}
stdout 里永远不会出现密钥。
"""
import argparse
import base64
import html
import json
import secrets
import sys
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import tcapi  # noqa: E402

POLICY = (HERE.parent / "references" / "agent-ops-policy.json").read_text(encoding="utf-8")

FRIENDLY = {
    "AuthFailure.SecretIdNotFound": "SecretId 不对：请检查是否完整复制（以 AKID 开头），或者这个密钥已经被删除。",
    "AuthFailure.SignatureFailure": "SecretKey 不对：请重新复制 SecretKey，注意不要多带空格。",
    "AuthFailure.SecretIdDisabled": "这个密钥已被禁用，请在子用户详情里启用它，或者新建一个。",
    "Local.NetworkError": "连不上腾讯云，请检查网络后重试。",
}

ASSETS = HERE.parent / "assets"
PAGE = (ASSETS / "setup.html").read_text(encoding="utf-8")
LOGO_B64 = base64.b64encode((ASSETS / "claw-school-logo.png").read_bytes()).decode("ascii")
# 本页面处理密钥：浏览器层面禁止加载任何外部脚本/样式/图片/字体，也禁止向本机以外发请求。
# 推广内容只是普通超链接（用户点击后在新标签页打开）。
CSP = ("default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; "
       "img-src data:; connect-src 'self'; form-action 'none'; base-uri 'none'; frame-ancestors 'none'")


def verify(sid: str, skey: str, region: str):
    """返回 (ok, 给用户看的文字, 给 agent 的结果字典)。"""
    sid, skey = sid.strip(), skey.strip()
    if not sid.startswith("AKID") or len(skey) < 20:
        return False, "格式不对：SecretId 应该以 AKID 开头，SecretKey 是一长串字母和数字。请重新复制。", None
    try:
        ident = tcapi.call_with((sid, skey), "sts", "GetCallerIdentity", region=region)
    except tcapi.TcError as e:
        return False, FRIENDLY.get(e.code, f"腾讯云没有通过验证（{e.code}）。请检查后重试。"), None
    if ident.get("Type") != "CAMUser":
        return False, ("这是主账号的密钥，权限太大，不能交给 AI 助手。\n"
                       "请按第 3 步创建子账号 agent-ops，然后用它的密钥。\n"
                       "（建议到「访问密钥」页面把刚才这个主账号密钥禁用。）"), None
    access = {}
    for svc, action, params in (("dnspod", "DescribeDomainList", {"Limit": 1}),
                                ("lighthouse", "DescribeInstances", {}),
                                ("teo", "DescribeZones", {})):
        try:
            tcapi.call_with((sid, skey), svc, action, params, region=region)
            access[svc] = "allowed"
        except tcapi.TcError as e:
            access[svc] = "allowed" if e.code.startswith("ResourceNotFound") else "denied"
    if "denied" in access.values():
        return False, ("密钥是对的，但这个子账号还没有权限。\n"
                       "请到「用户列表」→ agent-ops → 关联策略，勾选 agent-ops-web，然后再点一次「保存并验证」。"), None
    return True, "", {"uin": ident.get("UserId"), "owner_uin": ident.get("AccountId"), "access": access}


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--profile", default=tcapi.DEFAULT_PROFILE)
    ap.add_argument("--region", default="ap-hongkong")
    ap.add_argument("--port", type=int, default=0)
    ap.add_argument("--no-browser", action="store_true")
    ap.add_argument("--timeout", type=int, default=1800)
    ap.add_argument("--force", action="store_true", help="已有可用凭证时也重新设置")
    a = ap.parse_args()

    if not a.force and tcapi.load_credential(a.profile):
        try:
            ident = tcapi.call("sts", "GetCallerIdentity", profile=a.profile)
            print(json.dumps({"ok": True, "reason": "already_configured", "profile": a.profile,
                              "uin": ident.get("UserId")}, ensure_ascii=False))
            return 0
        except tcapi.TcError:
            pass  # 旧凭证失效 → 继续走向导

    token = secrets.token_urlsafe(16)
    page = (PAGE.replace("__POLICY__", html.escape(POLICY)).replace("__LOGO__", LOGO_B64)
            .replace("__TOKEN__", token).encode("utf-8"))
    result = {}
    done = threading.Event()

    class H(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass  # 不打印访问日志，以免误打出请求内容

        def _send(self, code, body, ctype):
            self.send_response(code)
            self.send_header("Content-Type", ctype)
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Security-Policy", CSP)
            self.send_header("Referrer-Policy", "no-referrer")
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self):
            q = parse_qs(urlparse(self.path).query)
            if q.get("t", [""])[0] != token:
                return self._send(403, "链接已失效，请让 AI 助手重新打开。".encode("utf-8"), "text/plain; charset=utf-8")
            self._send(200, page, "text/html; charset=utf-8")

        def do_POST(self):
            q = parse_qs(urlparse(self.path).query)
            if q.get("t", [""])[0] != token or not self.path.startswith("/save"):
                return self._send(403, b"{}", "application/json")
            n = int(self.headers.get("Content-Length", 0))
            try:
                d = json.loads(self.rfile.read(n).decode("utf-8"))
            except Exception:
                d = {}
            ok, text, info = verify(d.get("sid", ""), d.get("skey", ""), a.region)
            if ok:
                tcapi.save_credential(a.profile, d["sid"], d["skey"], a.region)
                result.update({"ok": True, "profile": a.profile, **info})
                text = ("✅ 连接成功！子账号编号 " + str(info["uin"]) + "\n"
                        "密钥已保存在这台电脑上。现在可以关掉这个页面，回到 AI 助手那里继续了。")
                threading.Timer(1.5, done.set).start()
            body = json.dumps({"ok": ok, "text": text}, ensure_ascii=False).encode("utf-8")
            self._send(200, body, "application/json; charset=utf-8")

    srv = ThreadingHTTPServer(("127.0.0.1", a.port), H)
    url = f"http://127.0.0.1:{srv.server_address[1]}/?t={token}"
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    print(f"SETUP_URL {url}", file=sys.stderr, flush=True)
    if not a.no_browser:
        try:
            webbrowser.open(url)
        except Exception:
            pass

    finished = done.wait(a.timeout)
    srv.shutdown()
    if not finished:
        result = {"ok": False, "reason": "timeout",
                  "say": "接入页面已超时关闭。需要时告诉我，我重新打开一个。"}
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    sys.exit(main())
