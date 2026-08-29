"""企业微信群机器人通道。markdown 不支持表格，卡片降级为 markdown（表格→文本对齐）。"""
from core import message as msg
from core.registry import register
from channels.base import Channel

WECOM_ERRORS = {0: "ok", 93000: "参数格式错误", 45009: "限流(20条/分钟)", 93004: "机器人已停用"}

# 统一 color → 企业微信 font color（只支持 3 种内置色）
_COLOR = {"green": "info", "grey": "comment", "orange": "warning", "red": "warning"}


@register
class WecomChannel(Channel):
    name = "wecom"
    label = "企业微信"
    rate_per_min = 20

    def render_text(self, m):
        return {"msgtype": "text", "text": {"content": m.get("text", "")}}

    def render_card(self, m):
        lines = [f"**{m.get('title', '')}**", ""]
        for sec in m.get("sections", []):
            t = sec.get("type")
            if t == "markdown":
                lines.append(sec.get("content", ""))
            elif t == "table":
                lines.append(msg.table_to_text(sec.get("headers", []), sec.get("rows", [])))
            elif t == "button":
                lines.append(f"[{sec.get('text', '')}]({sec.get('url', '')})")
            elif t == "note":
                color = _COLOR.get(m.get("color", ""), "comment")
                lines.append(f'<font color="{color}">{sec.get("content", "")}</font>')
            lines.append("")
        content = "\n".join(lines).strip()
        if len(content.encode("utf-8")) > 4096:
            content = content.encode("utf-8")[:4090].decode("utf-8", "ignore") + "…"
        return {"msgtype": "markdown", "markdown": {"content": content}}

    def post(self, target, payload):
        t = self.resolve_target(target)
        r = self.http_json(t["url"], payload)
        if r["ok"]:
            code = r["body"].get("errcode")
            if code == 0:
                return {"ok": True, "code": 0, "msg": "success"}
            return {"ok": False, "code": code, "msg": WECOM_ERRORS.get(code, r["body"].get("errmsg", ""))}
        return {"ok": False, "code": r["code"], "msg": r["body"]}
