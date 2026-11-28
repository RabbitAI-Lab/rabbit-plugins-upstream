"""薇芯 4.x 解密库读取与消息格式化（仅本人数据，本地使用）。

职责：账号/数据目录探测、库解密打开、联系人与会话解析、发送人唯一标识、详细消息格式化。
数据流：加密 *.db --复制字节--> 临时副本 --decrypt_db--> 明文 sqlite --sqlite3 只读--> 解析。

依赖：pycryptodome(Crypto)、zstandard、psutil。密钥由 capture_keys.py 抓取（每库一把）。
"""
from __future__ import annotations

import hashlib
import json
import re
import sqlite3
import tempfile
import unicodedata
import xml.etree.ElementTree as ET
from pathlib import Path

import psutil
import zstandard

from decrypt import decrypt_db

_ZSTD = zstandard.ZstdDecompressor()
_ZSTD_MAGIC = b"\x28\xb5\x2f\xfd"

CONTACT_DB = "contact/contact.db"
SESSION_DB = "session/session.db"


# ============================================================ 小工具 ========
def _s(v) -> str:
    if v is None:
        return ""
    if isinstance(v, (bytes, bytearray)):
        return bytes(v).decode("utf-8", "replace")
    return str(v)


def make_tmp_dir() -> Path:
    return Path(tempfile.mkdtemp(prefix="wxexport_"))


# ---- 终端显示宽度（中文/全角算 2 列），用于表格对齐 ----
def disp_width(s: str) -> int:
    return sum(2 if unicodedata.east_asian_width(ch) in ("W", "F") else 1 for ch in s)


def trunc_width(s: str, width: int) -> str:
    out, cur = [], 0
    for ch in s:
        cw = 2 if unicodedata.east_asian_width(ch) in ("W", "F") else 1
        if cur + cw > width:
            break
        out.append(ch)
        cur += cw
    return "".join(out)


def pad_width(s: str, width: int, align: str = "left") -> str:
    """按显示宽度补空格对齐；超宽先截断。align: left / right。"""
    s = trunc_width(s, width)
    gap = max(0, width - disp_width(s))
    return (" " * gap + s) if align == "right" else (s + " " * gap)


def load_keys(keys_file: Path) -> dict[str, str]:
    p = Path(keys_file)
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return {}


# ============================================================ 账号探测 ======
_ACCT_FOLDER = re.compile(r"^(?P<wxid>.+)_\d+$")


def _wxid_from_dbdir(db_dir: Path) -> str:
    """db_storage 的上一级形如 'wxid_xxx_1034'，去掉结尾 _<数字> 得到 wxid。"""
    folder = db_dir.parent.name
    m = _ACCT_FOLDER.match(folder)
    return m.group("wxid") if m else folder


def find_accounts() -> list[dict]:
    """探测本机可用薇芯账号：返回 [{wxid, db_dir, running}]。

    先看运行中的 weixin.exe 打开的 .db 句柄里含 '\\db_storage\\' 的路径；
    再补扫常见根目录下的 */db_storage/session/session.db。
    """
    found: dict[str, dict] = {}

    # 1) 运行中的进程句柄
    for proc in psutil.process_iter(["pid", "name"]):
        if (proc.info["name"] or "").lower() != "weixin.exe":
            continue
        try:
            files = proc.open_files()
        except Exception:
            continue
        for f in files:
            low = f.path.lower().replace("/", "\\")
            idx = low.find("\\db_storage\\")
            if idx != -1:
                db_dir = Path(f.path[:idx + len("\\db_storage")])
                wxid = _wxid_from_dbdir(db_dir)
                found.setdefault(wxid, {"wxid": wxid, "db_dir": db_dir, "running": True})

    # 2) 常见根目录补扫（不做全盘递归，避免卡顿）
    roots = [
        Path.home() / "Documents" / "xwechat_files",
        Path.home() / "Documents" / "weixin Files",
    ]
    for root in roots:
        if not root.is_dir():
            continue
        for acct in root.iterdir():
            db_dir = acct / "db_storage"
            if (db_dir / "session" / "session.db").exists():
                wxid = _wxid_from_dbdir(db_dir)
                found.setdefault(wxid, {"wxid": wxid, "db_dir": db_dir, "running": False})

    return list(found.values())


# ============================================================ 解密打开 ======
def decrypt_to_temp(db_dir: Path, rel: str, key_hex: str, tmp_dir: Path) -> Path | None:
    """复制字节后解密到 tmp_dir，返回明文 sqlite 路径；失败返回 None。"""
    src = Path(db_dir) / rel
    if not src.exists() or not key_hex:
        return None
    try:
        raw = src.read_bytes()
    except OSError:
        return None
    copy = tmp_dir / (rel.replace("/", "_") + ".enc")
    copy.write_bytes(raw)
    dst = tmp_dir / (rel.replace("/", "_") + ".dec")
    try:
        decrypt_db(copy, dst, bytes.fromhex(key_hex))
    except Exception:
        return None
    return dst


def decrypt_open(db_dir: Path, rel: str, key_hex: str, tmp_dir: Path) -> sqlite3.Connection | None:
    dec = decrypt_to_temp(db_dir, rel, key_hex, tmp_dir)
    if not dec:
        return None
    try:
        con = sqlite3.connect(f"file:{dec}?mode=ro", uri=True)
        con.text_factory = bytes
        return con
    except sqlite3.Error:
        return None


# ============================================================ 内容解码 ======
def decode_content(blob) -> str:
    if blob is None:
        return ""
    if isinstance(blob, str):
        return blob
    if isinstance(blob, (bytes, bytearray)):
        b = bytes(blob)
        if b[:4] == _ZSTD_MAGIC:
            try:
                b = _ZSTD.decompress(b)
            except Exception:
                try:
                    b = _ZSTD.decompress(b, max_output_size=64 << 20)
                except Exception:
                    return "[无法解压的内容]"
        return b.decode("utf-8", "replace")
    return str(blob)


def strip_group_prefix(text: str) -> str:
    """群聊正文常带 '发送人id:\\n' 前缀，去掉它。"""
    if "\n" in text:
        head, rest = text.split("\n", 1)
        if head.endswith(":") or head.endswith("："):
            token = head[:-1]
            if token and (":" not in token) and (" " not in token) and len(token) < 80:
                return rest
    return text


# ============================================================ 联系人 ========
def build_contacts(db_dir: Path, keys: dict, tmp_dir: Path) -> dict[str, dict]:
    """username -> {display, nick, remark, alias}。display = 备注>昵称>别名>''。"""
    out: dict[str, dict] = {}
    con = decrypt_open(db_dir, CONTACT_DB, keys.get(CONTACT_DB, ""), tmp_dir)
    if not con:
        return out
    try:
        cur = con.cursor()
        for uname, remark, nick, alias in cur.execute(
            "SELECT username, remark, nick_name, alias FROM contact"
        ):
            u = _s(uname)
            if not u:
                continue
            remark, nick, alias = _s(remark), _s(nick), _s(alias)
            out[u] = {
                "display": remark or nick or alias or "",
                "nick": nick,
                "remark": remark,
                "alias": alias,
            }
    except sqlite3.Error:
        pass
    finally:
        con.close()
    return out


def display_of(contacts: dict, username: str) -> str:
    info = contacts.get(username)
    return info["display"] if info and info.get("display") else ""


def resolve_sender(username: str, contacts: dict, me: str, room_nicks: dict | None = None) -> str:
    """发送人带唯一标识：我(mywxid) / 显示名(wxid) / 仅 wxid（未知）。
       群聊里优先用群昵称（room_nicks[wxid]），其次联系人备注/昵称，再退回 wxid。"""
    if not username:
        return "系统"
    if username == me:
        return f"我({me})"
    disp = ""
    if room_nicks:
        disp = room_nicks.get(username, "")
    if not disp:
        disp = display_of(contacts, username)
    return f"{disp}({username})" if disp else username


# -------------------------------------------------- 群成员群昵称（protobuf）--
def _pb_varint(b, i):
    shift = val = 0
    while i < len(b):
        x = b[i]; i += 1
        val |= (x & 0x7F) << shift
        if not x & 0x80:
            break
        shift += 7
    return val, i


def _pb_fields(b):
    """极简 protobuf 解析，按需产出 (field_no, wire_type, value)。"""
    i, n = 0, len(b)
    while i < n:
        tag, i = _pb_varint(b, i)
        field, wt = tag >> 3, tag & 7
        if wt == 0:
            v, i = _pb_varint(b, i); yield field, wt, v
        elif wt == 2:
            ln, i = _pb_varint(b, i); yield field, wt, b[i:i + ln]; i += ln
        elif wt == 5:
            yield field, wt, b[i:i + 4]; i += 4
        elif wt == 1:
            yield field, wt, b[i:i + 8]; i += 8
        else:
            return


def parse_room_members(ext: bytes) -> dict[str, str]:
    """解析 chat_room.ext_buffer，返回 {成员wxid: 群昵称}（群昵称可能为空串）。
       结构：顶层 field1 = 成员子消息；子消息 field1=wxid, field2=群昵称。"""
    out: dict[str, str] = {}
    if not ext:
        return out
    try:
        for f, wt, val in _pb_fields(bytes(ext)):
            if f == 1 and wt == 2:
                wxid = nick = ""
                for sf, swt, sval in _pb_fields(val):
                    if swt == 2 and sf == 1:
                        wxid = bytes(sval).decode("utf-8", "replace")
                    elif swt == 2 and sf == 2:
                        nick = bytes(sval).decode("utf-8", "replace")
                if wxid:
                    out[wxid] = nick
    except Exception:
        pass
    return out


def build_room_nicknames(db_dir: Path, keys: dict, tmp_dir: Path) -> dict[str, dict]:
    """{群username: {成员wxid: 群昵称}}。"""
    rooms: dict[str, dict] = {}
    con = decrypt_open(db_dir, CONTACT_DB, keys.get(CONTACT_DB, ""), tmp_dir)
    if not con:
        return rooms
    try:
        for uname, ext in con.execute("SELECT username, ext_buffer FROM chat_room"):
            u = _s(uname)
            if not u or ext is None:
                continue
            members = {w: n for w, n in parse_room_members(bytes(ext)).items() if n}
            if members:
                rooms[u] = members
    except sqlite3.Error:
        pass
    finally:
        con.close()
    return rooms


# ============================================================ 会话/消息库 ===
def msg_table_name(username: str) -> str:
    return "Msg_" + hashlib.md5(username.encode("utf-8")).hexdigest()


_SHARD = re.compile(r"message_\d+\.db$")


def message_db_rels(db_dir: Path) -> list[str]:
    """聊天消息分库（message_0.db / message_1.db …，不含 biz/fts/resource）。"""
    rels = []
    mdir = Path(db_dir) / "message"
    if mdir.is_dir():
        for p in sorted(mdir.glob("message_*.db")):
            if _SHARD.match(p.name):
                rels.append(f"message/{p.name}")
    return rels


def conversations_of(con: sqlite3.Connection) -> list[str]:
    """消息库里的会话（Name2Id.is_session=1）。"""
    try:
        return [
            _s(u)
            for u, iss in con.execute("SELECT user_name, is_session FROM Name2Id")
            if iss == 1 and _s(u)
        ]
    except sqlite3.Error:
        return []


def name2id_map(con: sqlite3.Connection) -> dict[int, str]:
    try:
        return {rid: _s(u) for rid, u in con.execute("SELECT rowid, user_name FROM Name2Id")}
    except sqlite3.Error:
        return {}


def table_exists(con: sqlite3.Connection, table: str) -> bool:
    try:
        return bool(con.execute(
            "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (table,)
        ).fetchone())
    except sqlite3.Error:
        return False


def msg_count(con: sqlite3.Connection, username: str) -> int:
    t = msg_table_name(username)
    if not table_exists(con, t):
        return 0
    try:
        return con.execute(f'SELECT COUNT(*) FROM "{t}"').fetchone()[0]
    except sqlite3.Error:
        return 0


def msg_count_last(con: sqlite3.Connection, username: str) -> tuple[int, int]:
    """返回 (消息数, 最近消息时间戳)。时间取自消息表 create_time，不依赖 session.db。"""
    t = msg_table_name(username)
    if not table_exists(con, t):
        return 0, 0
    try:
        cnt, last = con.execute(f'SELECT COUNT(*), MAX(create_time) FROM "{t}"').fetchone()
        return cnt or 0, last or 0
    except sqlite3.Error:
        return 0, 0


def read_messages(con: sqlite3.Connection, username: str, after_local_id: int):
    """按时间序(sort_seq)读某会话 local_id>after 的消息。
       返回 [(local_id, create_time, sender_wxid, local_type, content_bytes)]。"""
    t = msg_table_name(username)
    if not table_exists(con, t):
        return []
    n2i = name2id_map(con)
    rows = []
    try:
        for lid, ct, rsid, lt, mc in con.execute(
            f'SELECT local_id, create_time, real_sender_id, local_type, message_content '
            f'FROM "{t}" WHERE local_id > ? ORDER BY sort_seq', (after_local_id,)
        ):
            rows.append((lid, ct, n2i.get(rsid, ""), lt, mc))
    except sqlite3.Error:
        return []
    return rows


def conv_kind(username: str) -> str:
    if username.endswith("@chatroom"):
        return "群聊"
    if username in ("filehelper",):
        return "文件传输助手"
    if username.startswith("gh_"):
        return "公众号"
    if username in ("weixin", "newsapp", "fmessage"):
        return "系统"
    return "单聊"


def list_sessions(db_dir: Path, keys: dict, tmp_dir: Path) -> dict[str, dict]:
    """session.db -> {username: {summary, last_time}}。"""
    out: dict[str, dict] = {}
    con = decrypt_open(db_dir, SESSION_DB, keys.get(SESSION_DB, ""), tmp_dir)
    if not con:
        return out
    try:
        for u, summ, ts in con.execute(
            "SELECT username, summary, sort_timestamp FROM SessionTable"
        ):
            out[_s(u)] = {"summary": _s(summ), "last_time": ts or 0}
    except sqlite3.Error:
        pass
    finally:
        con.close()
    return out


def scan_conversations(db_dir: Path, keys: dict, contacts: dict, tmp_dir: Path) -> list[dict]:
    """扫描所有可导出的会话。返回按最近时间排序的列表：
       {username, display, kind, count, last_time, rel, key_ready}。
       消息数与最近时间都取自消息表（不依赖 session.db）。"""
    convs: dict[str, dict] = {}
    for rel in message_db_rels(db_dir):
        key = keys.get(rel, "")
        con = decrypt_open(db_dir, rel, key, tmp_dir) if key else None
        if not con:
            continue
        try:
            for u in conversations_of(con):
                cnt, last = msg_count_last(con, u)
                if cnt == 0:
                    continue
                cur = convs.get(u)
                if cur:
                    cur["count"] += cnt
                    cur["last_time"] = max(cur["last_time"], last)
                else:
                    convs[u] = {
                        "username": u,
                        "display": display_of(contacts, u) or u,
                        "kind": conv_kind(u),
                        "count": cnt,
                        "last_time": last,
                        "rel": rel,
                        "key_ready": True,
                    }
        finally:
            con.close()
    rows = list(convs.values())
    rows.sort(key=lambda r: r["last_time"], reverse=True)
    return rows


# ============================================================ 消息格式化 ====
_VOICE_LEN = re.compile(r'voicelength="(\d+)"')
_VIDEO_LEN = re.compile(r'playlength="(\d+)"')


def _xml_root(text: str):
    start = text.find("<")
    if start < 0:
        return None
    try:
        return ET.fromstring(text[start:])
    except Exception:
        return None


def _fmt_appmsg(text: str) -> str:
    root = _xml_root(text)
    app = root.find("appmsg") if root is not None else None
    if app is None:
        return "[应用消息]"
    title = (app.findtext("title") or "").strip()
    try:
        sub = int((app.findtext("type") or "-1").strip())
    except ValueError:
        sub = -1

    if sub in (4, 5):  # 链接
        url = (app.findtext("url") or "").strip()
        s = f"[链接:{title}]" if title else "[链接]"
        return f"{s} {url}".strip() if url else s
    if sub == 6:  # 文件
        size = app.findtext("appattach/totallen")
        human = _human_size(size)
        return f"[文件:{title}{(' '+human) if human else ''}]" if title else "[文件]"
    if sub == 8:
        return "[动画表情]"
    if sub == 17:
        return "[实时位置共享]"
    if sub in (19, 40):  # 合并转发
        return f"[聊天记录:{title}]" if title else "[聊天记录]"
    if sub in (33, 36):  # 小程序
        name = (app.findtext("sourcedisplayname") or title).strip()
        return f"[小程序:{name}]" if name else "[小程序]"
    if sub == 51:  # 视频号
        return f"[视频号:{title}]" if title else "[视频号]"
    if sub == 57:  # 引用
        refer = app.find("refermsg")
        who = _s_el(refer, "displayname")
        quoted = _s_el(refer, "content")
        base = title or (app.findtext("des") or "").strip()
        ref = f"（引用 {who}:{quoted[:40]}）" if (who or quoted) else ""
        return f"[引用] {base}{ref}".strip()
    if sub == 2000:  # 转账
        pay = app.find("wcpayinfo")
        fee = _s_el(pay, "feedesc")
        memo = _s_el(pay, "pay_memo")
        return f"[转账 {fee}{(' '+memo) if memo else ''}]".strip() if fee else "[转账]"
    if sub == 2001:  # 红包
        pay = app.find("wcpayinfo")
        wishing = _s_el(pay, "sendertitle") or _s_el(pay, "receivertitle")
        return f"[红包 {wishing}]" if wishing else "[红包]"
    if sub == 3:
        return f"[音乐:{title}]" if title else "[音乐]"
    if sub == 2:
        return "[图片]"
    return f"[应用消息:{title}]" if title else "[应用消息]"


def _s_el(el, tag: str) -> str:
    if el is None:
        return ""
    return (el.findtext(tag) or "").strip()


def _human_size(size) -> str:
    try:
        n = int(size)
    except (TypeError, ValueError):
        return ""
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.0f}{unit}" if unit == "B" else f"{n:.1f}{unit}"
        n /= 1024
    return f"{n:.1f}TB"


def _fmt_system(text: str) -> str:
    """系统消息：尽量还原可读文字。"""
    t = text.strip()
    if t.startswith("<sysmsg"):
        root = _xml_root(t)
        if root is not None:
            typ = root.get("type", "")
            if typ == "revokemsg":
                rep = root.findtext("revokemsg/replacemsg") or "撤回了一条消息"
                return f"[系统] {_strip_tags(rep)}"
            if typ == "pat":
                tpl = root.findtext("pat/template") or ""
                tpl = re.sub(r"\$\{[^}]*\}", "", tpl).strip() or "拍了拍"
                return f"[拍一拍] {_strip_tags(tpl)}"
            if typ == "sysmsgtemplate":
                tpl = root.findtext("sysmsgtemplate/content_template/template") or ""
                return f"[系统] {_strip_tags(tpl)}".strip()
            # 其它 sysmsg：取所有文本
            txt = _strip_tags(t)
            return f"[系统] {txt}" if txt else "[系统消息]"
    # 纯文本或带少量标签
    txt = _strip_tags(t)
    return f"[系统] {txt}" if txt else "[系统消息]"


def _strip_tags(text: str) -> str:
    text = re.sub(r"<!\[CDATA\[(.*?)\]\]>", r"\1", text, flags=re.S)
    text = re.sub(r"<[^>]+>", "", text)
    return re.sub(r"\s+", " ", text).strip()


# local_type 低 32 位 -> 简单占位（文本/应用/系统单独处理）
def format_message(local_type: int, content_raw, is_group: bool) -> str:
    """返回这条消息的内容文本：文本原样，其余尽量带细节的占位。解析出错一律降级，不抛异常。"""
    try:
        t = int(local_type) & 0xFFFFFFFF
        text = decode_content(content_raw)
        if is_group:
            text = strip_group_prefix(text)

        if t == 1:
            return text
        if t == 3:
            return "[图片]"
        if t == 34:
            m = _VOICE_LEN.search(text)
            return f"[语音 {int(int(m.group(1))/1000)}s]" if m else "[语音]"
        if t == 43:
            m = _VIDEO_LEN.search(text)
            return f"[视频 {m.group(1)}s]" if m else "[视频]"
        if t == 42:
            root = _xml_root(text)
            nick = root.get("nickname") if root is not None else ""
            return f"[名片:{nick}]" if nick else "[名片]"
        if t == 47:
            return "[动画表情]"
        if t == 48:
            root = _xml_root(text)
            loc = root.find("location") if root is not None else None
            poi = (loc.get("poiname") or loc.get("label")) if loc is not None else ""
            return f"[位置:{poi}]" if poi else "[位置]"
        if t == 50:
            return "[音视频通话]"
        if t == 49:
            return _fmt_appmsg(text)
        if t in (10000, 10002):
            return _fmt_system(text)
        snippet = re.sub(r"\s+", " ", text).strip()[:80]
        return f"[未知消息 type={t}]" + (f" {snippet}" if snippet else "")
    except Exception:
        return f"[无法解析的消息 type={local_type}]"
