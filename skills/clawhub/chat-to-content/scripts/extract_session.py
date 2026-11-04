#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
extract_session.py - 读取本机 WorkBuddy 会话记录（.jsonl），判定是否具备可总结的历史对话，
并把对话抽取为一份干净的 transcript.md 供后续写作使用。

用法:
    # 前置检查：当前会话是否已有足够可读取的历史对话
    python extract_session.py --check

    # 前置检查
    python extract_session.py --check

    # 抽取对话记录到指定目录（输出 transcript.md）
    python extract_session.py --out-dir ./_session_dump

    # 列出当前工作区的会话文件（仅文件名与时间，不含内容）
    python extract_session.py --list 10

本脚本只能读取运行环境指明的当前会话，没有指定其它会话的参数。

判断规则（--check）:
    ok=True  需要同时满足：找到会话文件 / 用户发言 >= 1 条 / 助手回复 >= 1 条 /
             有效正文字符数 >= --min-chars（默认 200）
    ok=False 时给出 reason，调用方（SKILL.md）应据此直接结束，不启动后续流程。
"""

import argparse
import io
import json
import os
import re
import sys
from datetime import datetime

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

# 同目录的净化模块：素材写入磁盘前先剥离凭据与个人标识
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from redact import scrub  # noqa: E402

PROJECTS_ROOT = os.path.join(os.path.expanduser("~"), ".workbuddy", "projects")

# 会话身份：运行环境注入的会话 ID，用来精确锁定"当前会话"这一个文件。
# 只读取这两个标识变量，不读取任何密钥类环境变量。
SESSION_ENV_KEYS = ("CODEBUDDY_SESSION_ID", "WORKBUDDY_SESSION_ID")


def _env(*keys):
    for k in keys:
        v = os.environ.get(k)
        if v and v.strip():
            return v.strip()
    return ""

NOISE_PREFIXES = (
    "<command-name>",
    "<local-command-stdout>",
    "<system-reminder>",
    "<user-prompt-submit-hook>",
)
TAG_RE = re.compile(
    r"<(system-reminder|command-name|local-command-stdout|user-prompt-submit-hook)"
    r"[\s\S]*?</\1>",
    re.I,
)


def slugify_path(path):
    """C:/Users/wzq/WorkBuddy/2026-10-26-16-38-03 -> c-users-wzq-WorkBuddy-2026-10-26-16-38-03"""
    p = os.path.abspath(path).replace("\\", "/")
    return p.replace(":", "").replace("/", "-").lower()


def clean_text(text):
    if not isinstance(text, str):
        return ""
    # <user_query> 只是外层包裹标签，内容要保留
    text = re.sub(r"</?user_query[^>]*>", "", text, flags=re.I)
    text = TAG_RE.sub("", text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text


def is_noise(text):
    t = text.lstrip()
    return any(t.startswith(p) for p in NOISE_PREFIXES)


def content_to_text(content):
    """jsonl 的 content 可能是 str 或 list[dict]，这里只保留纯文本部分。"""
    if isinstance(content, str):
        return content
    if not isinstance(content, list):
        return ""
    parts = []
    for item in content:
        if not isinstance(item, dict):
            continue
        itype = item.get("type")
        if itype in ("text", "input_text", "output_text"):
            parts.append(item.get("text", "") or "")
        elif itype == "thinking":
            continue  # 思维链不进入素材
        elif itype in ("tool_use", "tool_result", "image", "file"):
            continue
    return "\n".join(parts)


def parse_session(path):
    """返回 (meta, turns)。turns = [{'role','ts','text'}]"""
    meta = {
        "session_file": path,
        "session_id": os.path.splitext(os.path.basename(path))[0],
        "title": "",
        "cwd": "",
        "first_ts": None,
        "last_ts": None,
    }
    turns = []
    with io.open(path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except Exception:
                continue  # 会话正在写入，末尾可能有半行
            rtype = obj.get("type")
            if rtype == "ai-title":
                meta["title"] = obj.get("title") or meta["title"]
                continue
            if rtype == "session-meta":
                m = obj.get("meta") or {}
                meta["cwd"] = meta["cwd"] or m.get("cwd", "")
                meta["title"] = meta["title"] or m.get("title", "")
                continue
            if rtype != "message":
                continue
            role = obj.get("role")
            if role not in ("user", "assistant"):
                continue
            text = clean_text(content_to_text(obj.get("content")))
            if not text or is_noise(text):
                continue
            ts = obj.get("timestamp")
            if isinstance(ts, (int, float)):
                ts = ts / 1000 if ts > 1e11 else ts
            if meta["first_ts"] is None and ts:
                meta["first_ts"] = ts
            if ts:
                meta["last_ts"] = ts
            if not meta["cwd"]:
                meta["cwd"] = obj.get("cwd", "")
            turns.append({"role": role, "ts": ts, "text": text})
    return meta, turns


def find_session_files(project_slug, limit=None):
    """列出当前工作区目录下的会话文件，返回 [(mtime, path)]，按修改时间倒序。

    不接受"扫描全部工作区"的用法：跨目录读取等于读别人的对话。
    """
    hits = []
    pdir = _project_dir(project_slug) if project_slug else None
    if pdir:
        for name in os.listdir(pdir):
            if name.endswith(".jsonl"):
                fp = os.path.join(pdir, name)
                try:
                    hits.append((os.path.getmtime(fp), fp))
                except OSError:
                    pass
    hits.sort(reverse=True)
    return hits[:limit] if limit else hits


def _project_dir(proj_slug):
    """在 projects 根目录下找到实际目录。

    不同平台对目录名大小写的处理不一致，这里只做一次不区分大小写的匹配，
    避免因为大小写差异退回到「猜最近会话」的旧逻辑。
    """
    root = PROJECTS_ROOT
    if not os.path.isdir(root):
        return None
    direct = os.path.join(root, proj_slug)
    if os.path.isdir(direct):
        return direct
    try:
        target = proj_slug.lower()
        for name in os.listdir(root):
            if name.lower() == target and os.path.isdir(os.path.join(root, name)):
                return os.path.join(root, name)
    except OSError:
        pass
    return None


def valid_session_id(sid):
    """会话 ID 只允许字母、数字、连字符、下划线，杜绝路径穿越写法。"""
    return bool(sid) and bool(re.match(r"^[A-Za-z0-9][A-Za-z0-9_-]{5,79}$", sid))


def resolve_current_session():
    """定位当前会话文件，返回 (path, source)。

    唯一的定位依据是运行环境注入的会话 ID（CODEBUDDY_SESSION_ID）加上进程
    自身的当前工作目录。**不接受任何命令行选择器**：没有 --session-file、
    没有 --session-id、没有 --project-slug、也没有 --cwd。

    这样"只整理当前会话"才是可验证的：脚本根本没有表达"读另一个会话"的语法。
    无法确认身份时返回 (None, None)，由调用方停止。
    """
    sid = _env(*SESSION_ENV_KEYS)
    if not valid_session_id(sid):
        return None, None
    pdir = _project_dir(slugify_path(os.getcwd()))
    if not pdir:
        return None, None
    cand = os.path.join(pdir, "%s.jsonl" % sid)
    return (cand, "session_id") if os.path.isfile(cand) else (None, None)


def stats(turns):
    u = sum(1 for t in turns if t["role"] == "user")
    a = sum(1 for t in turns if t["role"] == "assistant")
    chars = sum(len(t["text"]) for t in turns)
    return u, a, chars


def fmt_ts(ts):
    if not ts:
        return ""
    try:
        return datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M")
    except Exception:
        return ""


def write_transcript(meta, turns, out_dir, per_message=1600, max_chars=24000, redact=True):
    os.makedirs(out_dir, exist_ok=True)
    lines = [
        "# 会话原始记录（自动抽取，已脱敏）" if redact else "# 会话原始记录（自动抽取）",
        "",
        "- 会话文件：`%s.jsonl`（仅记录文件名，不含本机完整路径）" % meta["session_id"],
        "- 会话 ID：`%s`" % meta["session_id"],
        "- 标题：%s" % (meta["title"] or "（未命名）"),
        "- 时间：%s ~ %s" % (fmt_ts(meta["first_ts"]), fmt_ts(meta["last_ts"])),
        "- 有效轮次：用户 %d 条 / 助手 %d 条"
        % (
            sum(1 for t in turns if t["role"] == "user"),
            sum(1 for t in turns if t["role"] == "assistant"),
        ),
        "",
        "---",
        "",
    ]
    total = 0
    redacted_hits = 0
    idx = {"user": 0, "assistant": 0}
    for t in turns:
        idx[t["role"]] += 1
        text = t["text"]
        if redact:
            text, hits = scrub(text)
            redacted_hits += hits
        truncated = False
        if len(text) > per_message:
            text = text[:per_message]
            truncated = True
        if total + len(text) > max_chars:
            lines.append("（后续内容已按字符上限截断，如需完整上下文请直接读取会话 jsonl）")
            break
        total += len(text)
        who = "用户" if t["role"] == "user" else "助手"
        lines.append("## %s #%d  %s" % (who, idx[t["role"]], fmt_ts(t["ts"])))
        lines.append("")
        lines.append(text)
        if truncated:
            lines.append("")
            lines.append("> （本条原文较长，已截断至 %d 字）" % per_message)
        lines.append("")
    out = os.path.join(out_dir, "transcript.md")
    with io.open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return out, total, redacted_hits


def main():
    ap = argparse.ArgumentParser(
        description="抽取当前会话记录。不接受指定其它会话的参数。"
    )
    ap.add_argument("--check", action="store_true", help="只做前置检查，输出 JSON")
    ap.add_argument("--out-dir", help="抽取 transcript.md 的输出目录")
    ap.add_argument("--min-chars", type=int, default=200)
    ap.add_argument("--min-user-turns", type=int, default=1)
    ap.add_argument("--min-assistant-turns", type=int, default=1)
    ap.add_argument("--per-message", type=int, default=1600)
    ap.add_argument("--max-chars", type=int, default=24000)
    ap.add_argument("--no-redact", action="store_true", help="关闭脱敏（默认开启，落盘前替换凭据/手机号/邮箱/本机路径）")
    ap.add_argument("--list", type=int, metavar="N", help="列出当前工作区的会话文件（只有文件名与时间，不含内容）")
    args = ap.parse_args()

    if args.list:
        # 只列当前工作区的文件清单，不解析内容，也不构成读取入口
        rows = []
        for mtime, fp in find_session_files(slugify_path(os.getcwd()), args.list):
            try:
                size = os.path.getsize(fp)
            except OSError:
                size = 0
            rows.append(
                {
                    "session_id": os.path.basename(fp)[: -len(".jsonl")],
                    "mtime": datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M:%S"),
                    "size": size,
                }
            )
        print(json.dumps(rows, ensure_ascii=False, indent=2))
        return 0

    path, source = resolve_current_session()
    if not path or not os.path.isfile(path):
        sid = _env(*SESSION_ENV_KEYS)
        if not sid:
            reason = (
                "运行环境未提供会话 ID（CODEBUDDY_SESSION_ID），无法确认哪个文件属于当前会话。"
                "已停止，未读取任何会话。"
            )
        elif not valid_session_id(sid):
            reason = "运行环境提供的会话 ID 格式不合法，已停止，未读取任何会话。"
        else:
            reason = (
                "已定位到会话 ID %s，但当前工作区（%s）下没有对应记录文件。已停止，未读取其它会话。"
                % (sid, slugify_path(os.getcwd()))
            )
        print(
            json.dumps(
                {
                    "ok": False,
                    "reason": reason,
                    "session_file": None,
                    "selection": {"source": None, "session_id": sid or None},
                },
                ensure_ascii=False,
            )
        )
        return 2

    meta, turns = parse_session(path)
    u, a, chars = stats(turns)

    result = {
        "ok": None,
        "session_file": path,
        "selection": {"source": source, "session_id": meta["session_id"]},
        "session_id": meta["session_id"],
        "title": meta["title"],
        "cwd": meta["cwd"],
        "started_at": fmt_ts(meta["first_ts"]),
        "ended_at": fmt_ts(meta["last_ts"]),
        "user_turns": u,
        "assistant_turns": a,
        "chars": chars,
    }

    if u < args.min_user_turns:
        result["ok"] = False
        result["reason"] = "会话中尚无用户提问（user_turns=%d），没有可总结的交互内容。" % u
    elif a < args.min_assistant_turns:
        result["ok"] = False
        result["reason"] = "会话中尚无助手回复（assistant_turns=%d），交互未成闭环，暂不总结。" % a
    elif chars < args.min_chars:
        result["ok"] = False
        result["reason"] = (
            "有效对话正文仅 %d 字（阈值 %d），内容过短，不足以提炼成文章/贴图。" % (chars, args.min_chars)
        )
    else:
        result["ok"] = True
        result["reason"] = "存在可读取的历史对话，可继续。"
        result["preview"] = [t["text"][:120] for t in turns[:4]]

    if args.out_dir:
        out, written, redacted_hits = write_transcript(
            meta, turns, args.out_dir, args.per_message, args.max_chars, redact=not args.no_redact
        )
        result["transcript"] = out
        result["transcript_chars"] = written
        result["redacted"] = not args.no_redact
        result["redacted_hits"] = redacted_hits

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
