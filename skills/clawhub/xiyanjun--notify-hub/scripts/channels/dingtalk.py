"""钉钉群机器人通道。加签：标准 HMAC-SHA256（key=secret，message=timestamp\\nsecret），base64 后 urlencode 拼 URL。"""
import base64
import hashlib
import hmac
import time
import urllib.parse

from core import message as msg
from core.registry import register
from channels.base import Channel

DINGTALK_ERRORS = {0: "ok", 300001: "token 无效", 310000: "关键词不匹配", 130101: "限流"}


@register
class DingtalkChannel(Channel):
    name = "dingtalk"
    label = "钉钉"
    rate_per_min = 20

    def render_text(self, m):
        return {"msgtype": "text", "text": {"content": m.get("text", "")}}

    def render_card(self, m):
        parts = []
        title = m.get("title", "")
        for sec in m.get("sections", []):
            t = sec.get("type")
            if t == "markdown":
                parts.append(sec.get("content", ""))
            elif t == "table":
                parts.append(msg.table_to_text(sec.get("headers", []), sec.get("rows", [])))
            elif t == "button":
                parts.append(f"[{sec.get('text', '')}]({sec.get('url', '')})")
            elif t == "note":
                parts.append(f"> {sec.get('content', '')}")
        text = "\n\n".join(p for p in parts if p)
        return {"msgtype": "markdown", "markdown": {"title": title, "text": text}}

    @staticmethod
    def _sign(timestamp: str, secret: str) -> str:
        string_to_sign = "{}\n{}".format(timestamp, secret)
        h = hmac.new(secret.encode("utf-8"), string_to_sign.encode("utf-8"),
                     digestmod=hashlib.sha256).digest()
        return urllib.parse.quote_plus(base64.b64encode(h))

    def post(self, target, payload):
        t = self.resolve_target(target)
        url = t["url"]
        if t.get("secret"):
            ts = str(round(time.time() * 1000))
            sign = self._sign(ts, t["secret"])
            sep = "&" if "?" in url else "?"
            url = f"{url}{sep}timestamp={ts}&sign={sign}"
        r = self.http_json(url, payload)
        if r["ok"]:
            code = r["body"].get("errcode")
            if code == 0:
                return {"ok": True, "code": 0, "msg": "success"}
            return {"ok": False, "code": code, "msg": DINGTALK_ERRORS.get(code, r["body"].get("errmsg", ""))}
        return {"ok": False, "code": r["code"], "msg": r["body"]}
