"""结构化读取 API：把一条消息转成 JSON 记录，并提供账号/会话解析、全量读取、增量轮询。

供 wxskill.py（通用 skill 的 CLI 入口）复用，底层完全依赖现有 wxread / wxmedia / capture_keys。
仅限本机本人账号数据、本地学习研究。
"""
from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path

import wxread
import wxmedia
from exporter import sanitize

HERE = Path(__file__).resolve().parent
KEYS_DIR = HERE / "keys"
STATE_DIR = HERE / "state"
EXPORT_DIR = HERE / "export"

_APPMSG_TYPE = {
    2: "image", 3: "music", 4: "link", 5: "link", 6: "file", 8: "sticker",
    17: "location", 19: "merged", 33: "miniapp", 36: "miniapp", 40: "merged",
    51: "channel", 57: "quote", 2000: "transfer", 2001: "redpacket",
}
_BASE_TYPE = {
    1: "text", 3: "image", 34: "voice", 43: "video", 42: "card",
    47: "sticker", 48: "location", 50: "call", 10000: "system", 10002: "system",
}


def type_name(local_type: int, text: str = "") -> str:
    t = int(local_type) & 0xFFFFFFFF
    if t in _BASE_TYPE:
        return _BASE_TYPE[t]
    if t == 49:
        m = re.search(r"<type>\s*(\d+)\s*</type>", text)
        sub = int(m.group(1)) if m else -1
        return _APPMSG_TYPE.get(sub, "app")
    return "unknown"


def _fmt_time(ct) -> str:
    try:
        return datetime.fromtimestamp(ct).strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        return ""


def message_record(lid, ct, sender_u, lt, mc, is_group, contacts, me, conv_nicks,
                    db_dir=None, media_dir=None) -> dict:
    """单条消息 → 结构化记录。media_dir 非空时复制文件/视频本体并给相对路径。"""
    text = wxread.decode_content(mc)
    if is_group:
        text = wxread.strip_group_prefix(text)

    if not sender_u:
        sender_disp, is_me = "系统", False
    elif sender_u == me:
        sender_disp, is_me = "我", True
    else:
        sender_disp = ((conv_nicks or {}).get(sender_u, "")
                       or wxread.display_of(contacts, sender_u) or sender_u)
        is_me = False

    rec = {
        "local_id": lid,
        "ts": ct or 0,
        "time": _fmt_time(ct),
        "sender": sender_disp,
        "sender_wxid": sender_u or "",
        "is_me": is_me,
        "type": type_name(lt, text),
        "content": wxread.format_message(lt, mc, is_group),
        "media": None,
    }
    if db_dir is not None and media_dir is not None:
        ref = wxmedia.media_ref(lt, text, is_group)
        if ref and ref["kind"] in ("file", "video"):
            name = wxmedia.export_media(db_dir, ref, media_dir)
            if name:
                rec["media"] = f"media/{Path(media_dir).name}/{name}"
    return rec


# ----------------------------------------------------------- 账号 / 会话 ----
def open_account(account: str | None = None) -> dict:
    """选账号并加载上下文。account 为 wxid；默认取第一个（优先运行中的）。"""
    accts = wxread.find_accounts()
    if not accts:
        raise RuntimeError("未发现薇芯账号，请确认薇芯已启动并登录。")
    acct = None
    if account:
        acct = next((a for a in accts if a["wxid"] == account), None)
        if acct is None:
            raise RuntimeError(f"未找到账号：{account}")
    else:
        acct = next((a for a in accts if a.get("running")), accts[0])
    keys = wxread.load_keys(KEYS_DIR / f"{acct['wxid']}.json")
    tmp = wxread.make_tmp_dir()
    return {
        "wxid": acct["wxid"], "db_dir": acct["db_dir"], "keys": keys, "tmp": tmp,
        "me": acct["wxid"],
        "contacts": wxread.build_contacts(acct["db_dir"], keys, tmp),
        "room_nicks": wxread.build_room_nicknames(acct["db_dir"], keys, tmp),
    }


def list_conversations(ctx: dict) -> list[dict]:
    rows = wxread.scan_conversations(ctx["db_dir"], ctx["keys"], ctx["contacts"], ctx["tmp"])
    return [
        {"display": r["display"], "wxid": r["username"], "kind": r["kind"],
         "count": r["count"], "last_time": r["last_time"],
         "last": _fmt_time(r["last_time"]) if r["last_time"] else ""}
        for r in rows
    ]


def resolve_conversation(ctx: dict, name_or_wxid: str) -> dict:
    rows = list_conversations(ctx)
    for r in rows:                                   # 先 wxid 精确
        if r["wxid"] == name_or_wxid:
            return r
    q = name_or_wxid.lower()
    hits = [r for r in rows if q in r["wxid"].lower() or q in r["display"].lower()]
    if not hits:
        raise RuntimeError(f"没有匹配的会话：{name_or_wxid}")
    if len(hits) > 1:
        names = ", ".join(f"{h['display']}({h['wxid']})" for h in hits[:8])
        raise RuntimeError(f"'{name_or_wxid}' 匹配到多个会话，请更精确或用 wxid：{names}")
    return hits[0]


# ----------------------------------------------------------- 读取 ----
def _read(ctx: dict, conv: str, after_local_id: int, media: bool):
    """读某会话 local_id>after 的消息（跨分库定位其所在表），返回 (records, max_local_id)。"""
    is_group = conv.endswith("@chatroom")
    conv_nicks = ctx["room_nicks"].get(conv) if is_group else None
    display = wxread.display_of(ctx["contacts"], conv) or conv
    media_dir = (EXPORT_DIR / ctx["wxid"] / "media" / sanitize(display)) if media else None
    out, maxid = [], after_local_id
    for rel in wxread.message_db_rels(ctx["db_dir"]):
        key = ctx["keys"].get(rel, "")
        con = wxread.decrypt_open(ctx["db_dir"], rel, key, ctx["tmp"]) if key else None
        if not con:
            continue
        try:
            if not wxread.table_exists(con, wxread.msg_table_name(conv)):
                continue
            for lid, ct, sender_u, lt, mc in wxread.read_messages(con, conv, after_local_id):
                maxid = max(maxid, lid)
                out.append(message_record(lid, ct, sender_u, lt, mc, is_group,
                                          ctx["contacts"], ctx["me"], conv_nicks,
                                          ctx["db_dir"], media_dir))
            return out, maxid        # 会话只在一个分库里
        finally:
            con.close()
    return out, maxid


def read_history(ctx: dict, conv: str, media: bool = False, limit: int | None = None) -> list[dict]:
    recs, _ = _read(ctx, conv, 0, media)
    if limit and limit > 0:
        recs = recs[-limit:]         # 最近 limit 条
    return recs


def _cursor_file(ctx: dict) -> Path:
    return STATE_DIR / f"{ctx['wxid']}.poll.json"


def _load_cursor(ctx: dict) -> dict:
    p = _cursor_file(ctx)
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def _save_cursor(ctx: dict, cursor: dict) -> None:
    p = _cursor_file(ctx)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(cursor, ensure_ascii=False, indent=2), encoding="utf-8")


def poll_increment(ctx: dict, conv: str, media: bool = False, backlog: bool = False):
    """自上次以来的新消息。首次调用默认建基线（返回 [] 且 baselined=True），
       之后只返回新增；backlog=True 时首次直接返回全部历史。
       返回 (records, baselined)。"""
    cursor = _load_cursor(ctx)
    first = conv not in cursor
    if first and not backlog:
        _, maxid = _read(ctx, conv, 0, media=False)      # 只取当前最大 local_id 作基线
        cursor[conv] = maxid
        _save_cursor(ctx, cursor)
        return [], True
    recs, maxid = _read(ctx, conv, cursor.get(conv, 0), media)
    cursor[conv] = maxid
    _save_cursor(ctx, cursor)
    return recs, False
