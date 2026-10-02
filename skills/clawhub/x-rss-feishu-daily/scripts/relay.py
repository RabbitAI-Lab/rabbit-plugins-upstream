"""飞书推送中转：接收 Miniflux Webhook(new_entries)，组装卡片发到飞书群。

仅用标准库。配置从同目录 feishu.env 读取（KEY=VALUE）。
"""
import base64
import datetime
import email.utils
import html
import json
import os
import threading
import time
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

BASE = os.path.dirname(os.path.abspath(__file__))
CONF = {}
with open(os.path.join(BASE, "feishu.env"), encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            CONF[k.strip()] = v.strip()

FEISHU_CHAT_ID = CONF["FEISHU_CHAT_ID"]
MINIFLUX_URL = CONF["MINIFLUX_URL"].rstrip("/")
REPORT_BOT_NAME = CONF.get("REPORT_BOT_NAME", "")
REPORT_BOT_OPEN_ID = CONF.get("REPORT_BOT_OPEN_ID", "")
REPORT_COOLDOWN_H = float(CONF.get("REPORT_TRIGGER_COOLDOWN_H", "20"))
_state_path = os.path.join(BASE, ".report_state.json")
BASIC = "Basic " + base64.b64encode(
    f'{CONF["MINIFLUX_ADMIN_USERNAME"]}:{CONF["MINIFLUX_ADMIN_PASSWORD"]}'.encode()
).decode()

FB_ENABLED = CONF.get("FOLLOW_BUILDERS", "") == "1"
FB_PROXY = CONF.get("FB_PROXY", "http://host.docker.internal:7891")
FB_SOURCES = [
    ("fb_x", "https://raw.githubusercontent.com/zarazhangrui/follow-builders/main/feed-x.json"),
    ("fb_podcasts", "https://raw.githubusercontent.com/zarazhangrui/follow-builders/main/feed-podcasts.json"),
    ("fb_blogs", "https://raw.githubusercontent.com/zarazhangrui/follow-builders/main/feed-blogs.json"),
]

_token = {"value": None, "expire_at": 0.0}
_lock = threading.Lock()
_titles = {"map": {}, "at": 0.0}


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


def get_token():
    with _lock:
        if _token["value"] and time.time() < _token["expire_at"] - 300:
            return _token["value"]
        req = urllib.request.Request(
            "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
            data=json.dumps(
                {"app_id": CONF["FEISHU_APP_ID"], "app_secret": CONF["FEISHU_APP_SECRET"]}
            ).encode(),
            headers={"Content-Type": "application/json"},
        )
        d = json.load(urllib.request.urlopen(req, timeout=15))
        if d.get("code") != 0:
            raise RuntimeError(f"get token failed: {d}")
        _token["value"] = d["tenant_access_token"]
        _token["expire_at"] = time.time() + d.get("expire", 7200)
        return _token["value"]


def send_card(card):
    payload = {
        "receive_id": FEISHU_CHAT_ID,
        "msg_type": "interactive",
        "content": json.dumps(card, ensure_ascii=False),
    }
    req = urllib.request.Request(
        "https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type=chat_id",
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer " + get_token(),
        },
    )
    d = json.load(urllib.request.urlopen(req, timeout=15))
    if d.get("code") != 0:
        raise RuntimeError(f"send card failed: {d}")
    return d


def feed_title_map():
    if time.time() - _titles["at"] > 3600:
        try:
            req = urllib.request.Request(
                MINIFLUX_URL + "/v1/feeds", headers={"Authorization": BASIC}
            )
            feeds = json.load(urllib.request.urlopen(req, timeout=10))
            _titles["map"] = {f["id"]: f["title"] for f in feeds}
            _titles["at"] = time.time()
            log("feed 标题已刷新:", _titles["map"])
        except Exception as e:
            log("刷新 feed 标题失败:", e)
    return _titles["map"]


def build_card(entries):
    titles = feed_title_map()
    lines = []
    for e in entries[:10]:
        name = titles.get(e.get("feed_id"), "X 博主")
        title = (e.get("title") or "(无标题)").strip().replace("\n", " ")[:120]
        url = e.get("url") or ""
        if url:
            lines.append(f"- **{name}**：[{title}]({url})")
        else:
            lines.append(f"- **{name}**：{title}")
    if len(entries) > 10:
        lines.append(f"…等共 {len(entries)} 条，其余去 Miniflux（http://localhost:8088）看")
    return {
        "config": {"wide_screen_mode": True},
        "header": {
            "title": {"tag": "plain_text", "content": f"X 更新 · {len(entries)} 条新推文"},
            "template": "blue",
        },
        "elements": [{"tag": "div", "text": {"tag": "lark_md", "content": "\n".join(lines)}}],
    }


def trigger_report(force=False):
    """推送完成后点名日报智能体。force=True 跳过冷却（如手动全量重发后）。"""
    if not REPORT_BOT_NAME:
        return
    last = 0.0
    try:
        last = json.load(open(_state_path, encoding="utf-8"))["last"]
    except Exception:
        pass
    if not force and time.time() - last < REPORT_COOLDOWN_H * 3600:
        log("日报点名冷却中，跳过")
        return
    if REPORT_BOT_OPEN_ID:
        at = f'<at user_id="{REPORT_BOT_OPEN_ID}"></at> '
        text = {"text": f"{at} 请根据本群最新推送整理一份今日日报"}
    else:
        at = "@"  # 退化：纯文本点名
        text = {"text": f"{at}{REPORT_BOT_NAME} 请根据本群最新推送整理一份今日日报"}
    payload = {
        "receive_id": FEISHU_CHAT_ID,
        "msg_type": "text",
        "content": json.dumps(text, ensure_ascii=False),
    }
    req = urllib.request.Request(
        "https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type=chat_id",
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer " + get_token(),
        },
    )
    d = json.load(urllib.request.urlopen(req, timeout=15))
    if d.get("code") != 0:
        raise RuntimeError(f"trigger report failed: {d}")
    json.dump({"last": time.time()}, open(_state_path, "w"))
    log("已发送日报点名")



# ===== Follow Builders：JSON → RSS 转换桥 =====
def _rfc822(iso):
    try:
        dt = datetime.datetime.fromisoformat(str(iso).replace("Z", "+00:00"))
        return email.utils.format_datetime(dt.astimezone(datetime.timezone.utc))
    except Exception:
        return ""

def _esc(s):
    return html.escape(str(s or ""), quote=True)

def _items_to_rss(title, link, items):
    rows = "".join(
        "<item><title>{t}</title><guid isPermaLink=\"false\">{g}</guid><link>{l}</link>"
        "<description>{d}</description><pubDate>{p}</pubDate></item>".format(
            t=_esc(i["title"]), g=_esc(i["guid"]), l=_esc(i["link"]),
            d=_esc(i["desc"]), p=_esc(i["pubDate"]))
        for i in items)
    return ("<?xml version=\"1.0\" encoding=\"UTF-8\"?><rss version=\"2.0\"><channel>"
            f"<title>{_esc(title)}</title><link>{_esc(link)}</link>"
            f"<description>{_esc(title)}</description>{rows}</channel></rss>")

def fb_build(kind, data):
    items = []
    if kind == "fb_x":
        for acc in data.get("x", []):
            for tw in acc.get("tweets", []):
                text = (tw.get("text") or "").strip().replace(chr(10), " ")
                items.append({
                    "title": f"{acc.get('name','')}：{text[:80]}",
                    "guid": f"fbx-{tw.get('id')}",
                    "link": tw.get("url") or f"https://x.com/{acc.get('handle')}",
                    "desc": text,
                    "pubDate": _rfc822(tw.get("createdAt"))})
    elif kind == "fb_podcasts":
        for ep in data.get("podcasts", []):
            items.append({
                "title": f"{ep.get('name','')}｜{ep.get('title','')}",
                "guid": f"fbp-{ep.get('guid') or ep.get('url')}",
                "link": ep.get("url") or "",
                "desc": (ep.get("transcript") or "")[:800],
                "pubDate": _rfc822(ep.get("publishedAt"))})
    elif kind == "fb_blogs":
        for b in data.get("blogs", []):
            items.append({
                "title": f"{b.get('name','')}｜{b.get('title','')}",
                "guid": f"fbb-{b.get('url')}",
                "link": b.get("url") or "",
                "desc": (b.get("description") or b.get("content") or "")[:800],
                "pubDate": _rfc822(b.get("publishedAt"))})
    items.sort(key=lambda i: i["pubDate"], reverse=True)
    names = {"fb_x": "Follow Builders · X", "fb_podcasts": "Follow Builders · 播客",
             "fb_blogs": "Follow Builders · 博客"}
    caps = {"fb_x": 80, "fb_podcasts": 30, "fb_blogs": 30}
    return _items_to_rss(names[kind], "https://github.com/zarazhangrui/follow-builders",
                         items[:caps[kind]])

def fb_refresh_once():
    op = urllib.request.build_opener(urllib.request.ProxyHandler(
        {"http": FB_PROXY, "https": FB_PROXY}))
    op.addheaders = [("User-Agent", "Mozilla/5.0 rss-stack")]
    for kind, url in FB_SOURCES:
        d = json.load(op.open(url, timeout=90))
        xml = fb_build(kind, d)
        open(os.path.join(BASE, kind + ".xml"), "w", encoding="utf-8").write(xml)
        log(f"FB {kind} 已转换（{xml.count('<item>')} 条）")

def fb_loop():
    while True:
        try:
            fb_refresh_once()
        except Exception as e:
            log("FB 刷新失败:", e)
        time.sleep(4 * 3600)


class Handler(BaseHTTPRequestHandler):
    def _reply(self, code, body=b""):
        self.send_response(code)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path.startswith("/feeds/"):
            name = self.path.split("/feeds/", 1)[1].split("?")[0]
            p = os.path.join(BASE, name)
            if name in ("fb_x.xml", "fb_podcasts.xml", "fb_blogs.xml") and os.path.exists(p):
                data = open(p, "rb").read()
                self.send_response(200)
                self.send_header("Content-Type", "application/xml; charset=utf-8")
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)
                return
        self._reply(200, b"ok")

    def do_POST(self):
        try:
            n = int(self.headers.get("Content-Length") or 0)
            data = json.loads(self.rfile.read(n) or b"{}")
        except Exception as e:
            log("bad json:", e)
            return self._reply(400)
        entries = data.get("entries") or []
        if not entries:
            log("忽略无 entries 的事件:", data.get("type") or data.get("event"))
            return self._reply(200)
        skip_ids = {int(x) for x in CONF.get("SKIP_FEED_IDS", "").split(",") if x.strip().isdigit()}
        if skip_ids:
            filtered = [e for e in entries if e.get("feed_id") not in skip_ids]
            if len(filtered) < len(entries):
                log(f"跳过总览源条目 {len(entries)-len(filtered)} 条")
            entries = filtered
        if not entries:
            return self._reply(200)
        try:
            send_card(build_card(entries))
            log(f"已推送 {len(entries)} 条到飞书")
            self._reply(200)
            try:
                trigger_report()
            except Exception as e:
                log("日报点名失败:", e)
        except Exception as e:
            log("推送失败:", e)
            self._reply(500)


if __name__ == "__main__":
    log("feishu-relay 启动，目标群:", FEISHU_CHAT_ID)
    if FB_ENABLED:
        threading.Thread(target=fb_loop, daemon=True).start()
        log("Follow Builders 桥已启用")
    feed_title_map()
    ThreadingHTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
