"""Slack incoming webhook 通道。卡片渲染为 blocks，表格降级为文本。"""
import json
import urllib.error
import urllib.request

from core import message as msg
from core.registry import register
from channels.base import Channel


@register
class SlackChannel(Channel):
    name = "slack"
    label = "Slack"
    rate_per_min = 60

    def render_text(self, m):
        return {"text": m.get("text", "")}

    def render_card(self, m):
        blocks = []
        title = m.get("title", "")
        if title:
            blocks.append({"type": "section", "text": {"type": "mrkdwn", "text": f"*{title}*"}})
        for sec in m.get("sections", []):
            t = sec.get("type")
            if t == "markdown":
                blocks.append({"type": "section", "text": {"type": "mrkdwn", "text": sec.get("content", "")}})
            elif t == "table":
                txt = msg.table_to_text(sec.get("headers", []), sec.get("rows", []))
                blocks.append({"type": "section", "text": {"type": "mrkdwn", "text": f"```{txt}```"}})
            elif t == "button":
                blocks.append({"type": "actions", "elements": [{
                    "type": "button",
                    "text": {"type": "plain_text", "text": sec.get("text", ""), "emoji": True},
                    "url": sec.get("url", ""),
                }]})
            elif t == "note":
                blocks.append({"type": "context", "elements": [{
                    "type": "mrkdwn", "text": sec.get("content", "")}]})
        if blocks:
            blocks.append({"type": "divider"})
        return {"blocks": blocks}

    def post(self, target, payload):
        t = self.resolve_target(target)
        self._throttle()
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        req = urllib.request.Request(t["url"], data=data,
                                     headers={"Content-Type": "application/json"}, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                body = resp.read().decode("utf-8")
                return {"ok": body.strip() == "ok", "code": 0 if body.strip() == "ok" else -1, "msg": body}
        except urllib.error.HTTPError as e:
            return {"ok": False, "code": e.code, "msg": e.read().decode("utf-8", "ignore")}
        except Exception as e:
            return {"ok": False, "code": -1, "msg": str(e)}
