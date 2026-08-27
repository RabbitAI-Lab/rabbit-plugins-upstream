"""Telegram Bot API 通道。卡片渲染为 HTML 文本 + inline keyboard；文件走 sendDocument。"""
import json
import os
import uuid
import urllib.error
import urllib.request

from core import message as msg
from core.registry import register
from channels.base import Channel


@register
class TelegramChannel(Channel):
    name = "telegram"
    label = "Telegram"
    rate_per_min = 30

    def _api(self, token, method):
        return f"https://api.telegram.org/bot{token}/{method}"

    def render_text(self, m):
        return {"method": "sendMessage", "data": {"text": m.get("text", "")}}

    def render_card(self, m):
        html = []
        title = m.get("title", "")
        if title:
            html.append(f"<b>{title}</b>")
        buttons = []
        for sec in m.get("sections", []):
            t = sec.get("type")
            if t == "markdown":
                html.append(sec.get("content", ""))
            elif t == "table":
                txt = msg.table_to_text(sec.get("headers", []), sec.get("rows", []))
                html.append(f"<pre>{txt}</pre>")
            elif t == "button":
                buttons.append([{"text": sec.get("text", ""), "url": sec.get("url", "")}])
            elif t == "note":
                html.append(f"<i>{sec.get('content', '')}</i>")
        data = {"text": "\n".join(html), "parse_mode": "HTML"}
        if buttons:
            data["reply_markup"] = {"inline_keyboard": buttons}
        return {"method": "sendMessage", "data": data}

    def render_file(self, m):
        return {"method": "sendDocument", "file": True, "data": {"caption": m.get("caption", "")}}

    def post(self, target, payload):
        t = self.resolve_target(target)
        token = t["token"]
        chat_id = t["chat_id"]
        method = payload["method"]
        data = dict(payload.get("data", {}))
        data["chat_id"] = chat_id

        if payload.get("file"):
            return self._send_document(token, data, payload.get("path", ""))
        return self._post_json(self._api(token, method), data)

    def _post_json(self, url, data):
        self._throttle()
        req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"),
                                     headers={"Content-Type": "application/json"}, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                body = json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            return {"ok": False, "code": e.code, "msg": e.read().decode("utf-8", "ignore")}
        except Exception as e:
            return {"ok": False, "code": -1, "msg": str(e)}
        if body.get("ok"):
            return {"ok": True, "code": 0, "msg": "success"}
        return {"ok": False, "code": body.get("error_code"), "msg": body.get("description", "")}

    def _send_document(self, token, data, path):
        if not path or not os.path.isfile(path):
            return {"ok": False, "code": -2, "msg": f"文件不存在：{path}"}
        self._throttle()
        boundary = "----notifyhub" + uuid.uuid4().hex
        parts = []
        for key, val in data.items():
            parts.append(f"--{boundary}\r\nContent-Disposition: form-data; name=\"{key}\"\r\n\r\n{val}\r\n".encode("utf-8"))
        fname = os.path.basename(path)
        parts.append(f"--{boundary}\r\nContent-Disposition: form-data; name=\"document\"; filename=\"{fname}\"\r\nContent-Type: application/octet-stream\r\n\r\n".encode("utf-8"))
        with open(path, "rb") as f:
            parts.append(f.read())
        parts.append(f"\r\n--{boundary}--\r\n".encode("utf-8"))
        body = b"".join(parts)
        req = urllib.request.Request(
            self._api(token, "sendDocument"), data=body,
            headers={"Content-Type": f"multipart/form-data; boundary={boundary}"}, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                result = json.loads(resp.read().decode("utf-8"))
        except Exception as e:
            return {"ok": False, "code": -1, "msg": str(e)}
        if result.get("ok"):
            return {"ok": True, "code": 0, "msg": "success"}
        return {"ok": False, "code": result.get("error_code"), "msg": result.get("description", "")}
