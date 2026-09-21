"""邮件 SMTP 通道。text→纯文本邮件，card→HTML 邮件（表格转 HTML table），file→附件。

所有用户内容在写入 HTML 前均做转义，防止内容被当作 HTML 注入；
markdown section 用极简渲染（粗体/斜体/行内代码），button 的 url 限制 http/https。
"""
import html
import os
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.header import Header

from core import message as msg
from core.registry import register
from channels.base import Channel


def _md_to_html(text):
    """极简 markdown → HTML：先转义，再做粗体/斜体/行内代码。换行由容器 white-space 保留。"""
    t = html.escape(text or "")
    t = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    return t


def _safe_url(url):
    """仅放行 http/https 链接并转义，其余回退为 '#'。"""
    u = (url or "").strip()
    if re.match(r"^https?://", u, re.IGNORECASE):
        return html.escape(u)
    return "#"


@register
class EmailChannel(Channel):
    name = "email"
    label = "邮件"
    rate_per_min = 30

    def render_text(self, m):
        return {"subject": m.get("title", "通知"), "body": m.get("text", ""), "html": False,
                "attachments": []}

    def render_card(self, m):
        title = html.escape(m.get("title", ""))
        out = [f'<h2 style="font-family:sans-serif">{title}</h2>']
        for sec in m.get("sections", []):
            t = sec.get("type")
            if t == "markdown":
                out.append(
                    f'<div style="font-family:sans-serif;white-space:pre-wrap">{_md_to_html(sec.get("content", ""))}</div>')
            elif t == "table":
                headers = sec.get("headers", [])
                rows = sec.get("rows", [])
                th = "".join(
                    f"<th style='border:1px solid #ccc;padding:6px'>{html.escape(str(h))}</th>"
                    for h in headers)
                trs = ["<tr>" + th + "</tr>"]
                for r in rows:
                    trs.append("<tr>" + "".join(
                        f"<td style='border:1px solid #ccc;padding:6px'>{html.escape(str(c))}</td>"
                        for c in r) + "</tr>")
                out.append(
                    f"<table style='border-collapse:collapse;border:1px solid #ccc'>{''.join(trs)}</table>")
            elif t == "button":
                out.append(
                    f'<p><a href="{_safe_url(sec.get("url"))}" '
                    f'style="display:inline-block;padding:8px 16px;background:#2d7ff9;color:#fff;'
                    f'text-decoration:none;border-radius:4px">{html.escape(str(sec.get("text", "")))}</a></p>')
            elif t == "note":
                out.append(
                    f'<p style="color:#888;font-size:12px">{html.escape(sec.get("content", ""))}</p>')
        return {"subject": m.get("title", "通知"), "body": "".join(out), "html": True,
                "attachments": []}

    def render_file(self, m):
        path = m.get("path", "")
        return {"subject": m.get("title", "文件"), "body": m.get("caption", f"附件：{os.path.basename(path)}"),
                "html": False, "attachments": [path] if os.path.isfile(path) else []}

    def post(self, target, payload):
        t = self.resolve_target(target)
        self._throttle()
        em = MIMEMultipart()
        em["Subject"] = Header(payload.get("subject", "通知"), "utf-8")
        em["From"] = t.get("from") or t.get("user")
        em["To"] = t.get("to")
        body = MIMEText(payload.get("body", ""), "html" if payload.get("html") else "plain", "utf-8")
        em.attach(body)
        for path in payload.get("attachments", []):
            with open(path, "rb") as f:
                part = MIMEApplication(f.read(), Name=os.path.basename(path))
            part["Content-Disposition"] = f'attachment; filename="{os.path.basename(path)}"'
            em.attach(part)

        host, port = t.get("smtp_host"), int(t.get("port", 465))
        user, pwd = t.get("user"), t.get("password")
        try:
            if port == 465:
                srv = smtplib.SMTP_SSL(host, port, timeout=20)
            else:
                srv = smtplib.SMTP(host, port, timeout=20)
                srv.starttls()
            if user:
                srv.login(user, pwd)
            srv.sendmail(em["From"], [t.get("to")], em.as_string())
            srv.quit()
            return {"ok": True, "code": 0, "msg": "success"}
        except Exception as e:
            return {"ok": False, "code": -1, "msg": str(e)}
