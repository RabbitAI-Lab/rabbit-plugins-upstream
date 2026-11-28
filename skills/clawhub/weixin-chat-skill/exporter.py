"""导出引擎：把所选会话的聊天记录写成 TXT（已存在则追加），并支持实时轮询监听。

行格式： [YYYY-MM-DD HH:MM:SS] 发送人(wxid): 内容
增量：state[rel::username] = 已导出的最大 local_id；每次只追加更大的，文件已存在就续写。
"""
from __future__ import annotations

import json
import re
import time
from datetime import datetime
from pathlib import Path

import wxread
import wxmedia

_INVALID = re.compile(r'[\\/:*?"<>|\r\n]+')


def sanitize(name: str) -> str:
    return _INVALID.sub("_", name).strip() or "unknown"


def conversation_file(out_dir: Path, display: str, username: str) -> Path:
    tail = username.split("@")[0][-8:]
    return Path(out_dir) / f"{sanitize(display)}_{tail}.txt"


def load_state(state_file: Path) -> dict:
    p = Path(state_file)
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def save_state(state_file: Path, state: dict) -> None:
    Path(state_file).parent.mkdir(parents=True, exist_ok=True)
    Path(state_file).write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def _media_suffix(db_dir, local_type, content_raw, is_group, media_dir, display) -> str:
    """文件/视频：复制本体并在行尾标出相对路径；图片：标注未解密。"""
    t = int(local_type) & 0xFFFFFFFF
    if t not in (3, 43, 49):
        return ""
    text = wxread.decode_content(content_raw)
    if is_group:
        text = wxread.strip_group_prefix(text)
    ref = wxmedia.media_ref(local_type, text, is_group)
    if not ref:
        return ""
    if ref["kind"] in ("file", "video"):
        name = wxmedia.export_media(db_dir, ref, media_dir)
        if name:
            return f"  -> media/{sanitize(display)}/{name}"
        return f"  ({ref['kind']}本体未找到)"
    if ref["kind"] == "image":
        return "  (图片本体需图片密钥，暂未导出)"
    return ""


def _fmt_time(ct) -> str:
    try:
        return datetime.fromtimestamp(ct).strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        return "????-??-?? ??:??:??"


def export_once(db_dir, keys, out_dir, selected, contacts, me, state, tmp_dir,
                on_conv=None) -> int:
    """把所选会话(usernames 集合)的新消息追加到 TXT。返回新增条数。
       on_conv(display, n, path): 某会话本轮新增回调。"""
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    selected = set(selected)
    added = 0
    room_nicks = wxread.build_room_nicknames(db_dir, keys, tmp_dir)

    for rel in wxread.message_db_rels(db_dir):
        key = keys.get(rel, "")
        con = wxread.decrypt_open(db_dir, rel, key, tmp_dir) if key else None
        if not con:
            continue
        try:
            convs = [u for u in wxread.conversations_of(con) if u in selected]
            for conv in convs:
                skey = f"{rel}::{conv}"
                last = state.get(skey, 0)
                is_group = conv.endswith("@chatroom")
                rows = wxread.read_messages(con, conv, last)
                if not rows:
                    continue
                display = wxread.display_of(contacts, conv) or conv
                conv_nicks = room_nicks.get(conv) if is_group else None
                media_dir = out_dir / "media" / sanitize(display)
                lines, maxid = [], last
                for lid, ct, sender_u, lt, mc in rows:
                    maxid = max(maxid, lid)
                    sender = wxread.resolve_sender(sender_u, contacts, me, conv_nicks)
                    body = wxread.format_message(lt, mc, is_group)
                    body += _media_suffix(db_dir, lt, mc, is_group, media_dir, display)
                    lines.append(f"[{_fmt_time(ct)}] {sender}: {body}")
                fp = conversation_file(out_dir, display, conv)
                new_file = not fp.exists()
                with open(fp, "a", encoding="utf-8") as f:
                    if new_file:
                        f.write(f"===== 会话：{display}（{conv}）=====\n")
                    f.write("\n".join(lines) + "\n")
                state[skey] = maxid
                added += len(lines)
                if on_conv:
                    on_conv(display, len(lines), fp)
        finally:
            con.close()
    return added


def monitor(db_dir, keys, out_dir, selected, contacts, me, state_file, tmp_dir,
            interval=5) -> None:
    """先全量导出一次，再每 interval 秒追加新消息，Ctrl+C 退出。"""
    state = load_state(state_file)

    def first(display, n, path):
        print(f"  {display}: +{n} 条 -> {path.name}")

    n = export_once(db_dir, keys, out_dir, selected, contacts, me, state, tmp_dir, on_conv=first)
    save_state(state_file, state)
    print(f"首轮导出 {n} 条。进入实时监听，每 {interval}s 检查（Ctrl+C 退出）…")
    try:
        while True:
            time.sleep(interval)

            def live(display, k, path):
                print(f"[{datetime.now():%H:%M:%S}] {display} +{k} 条")

            n = export_once(db_dir, keys, out_dir, selected, contacts, me, state, tmp_dir, on_conv=live)
            if n:
                save_state(state_file, state)
    except KeyboardInterrupt:
        save_state(state_file, state)
        print("\n已停止监听。")
