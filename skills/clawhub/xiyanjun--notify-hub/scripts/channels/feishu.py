"""飞书群机器人通道。签名：HMAC-SHA256，key=timestamp\\nsecret，加密空字节，base64。"""
import base64
import hashlib
import hmac
import time

from core import message as msg
from core.registry import register
from channels.base import Channel

FEISHU_ERRORS = {
    0: "success", 19021: "签名失败/时间戳超时", 19022: "IP白名单拦截",
    19024: "关键词校验失败", 9499: "请求体格式错误", 19001: "webhook token 无效",
}

# 飞书卡片 2.0 header template 支持的颜色枚举，非法值回退 blue
_TEMPLATE_COLORS = frozenset({
    "blue", "wathet", "turquoise", "green", "yellow",
    "orange", "red", "carmine", "violet", "purple", "indigo", "grey",
})


@register
class FeishuChannel(Channel):
    name = "feishu"
    label = "飞书"
    rate_per_min = 100

    @staticmethod
    def _sign(timestamp: str, secret: str) -> str:
        string_to_sign = "{}\n{}".format(timestamp, secret)
        h = hmac.new(string_to_sign.encode("utf-8"), digestmod=hashlib.sha256).digest()
        return base64.b64encode(h).decode("utf-8")

    def render_text(self, m):
        return {"msg_type": "text", "content": {"text": m.get("text", "")}}

    def render_card(self, m):
        color = m.get("color", "blue")
        if color not in _TEMPLATE_COLORS:
            color = "blue"
        elements = []
        for sec in m.get("sections", []):
            t = sec.get("type")
            if t == "markdown":
                elements.append({"tag": "markdown", "content": sec.get("content", "")})
            elif t == "table":
                md = msg.table_to_markdown(sec.get("headers", []), sec.get("rows", []))
                elements.append({"tag": "markdown", "content": md})
            elif t == "button":
                elements.append({
                    "tag": "button",
                    "text": {"tag": "plain_text", "content": sec.get("text", "")},
                    "type": "default",
                    "behaviors": [{"type": "open_url", "default_url": sec.get("url", "")}],
                })
            elif t == "note":
                # schema 2.0 已移除 note 元素，降级为 markdown 斜体
                elements.append({"tag": "markdown", "content": f"*{sec.get('content', '')}*"})
        return {
            "msg_type": "interactive",
            "card": {
                "schema": "2.0",
                "header": {
                    "title": {"tag": "plain_text", "content": m.get("title", "")},
                    "template": color,
                },
                "body": {"elements": elements},
            },
        }

    def post(self, target, payload):
        t = self.resolve_target(target)
        body = dict(payload)
        if t.get("secret"):
            ts = str(int(time.time()))
            body["timestamp"] = ts
            body["sign"] = self._sign(ts, t["secret"])
        r = self.http_json(t["url"], body)
        if r["ok"]:
            code = r["body"].get("code")
            if code == 0:
                return {"ok": True, "code": 0, "msg": "success"}
            return {"ok": False, "code": code, "msg": FEISHU_ERRORS.get(code, r["body"].get("msg", ""))}
        return {"ok": False, "code": r["code"], "msg": r["body"]}
