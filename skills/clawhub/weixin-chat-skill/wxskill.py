"""通用 skill 的命令行入口：让任意 AI 读取/监听本机薇芯聊天记录。输出均为 JSON（或 NDJSON）。

子命令：
  status                     自检：账号 / 薇芯是否运行 / 密钥是否就绪 / 依赖
  list                       列出可导出的会话（JSON 数组）
  history <会话> [选项]       读取指定会话的【全量】聊天记录
  poll    <会话> [选项]       取指定会话【自上次以来的增量】（首次建基线，返回空）
  watch   <会话> [选项]       常驻监听，把新消息逐行 NDJSON 追加到文件并打印
  setup   [--seconds N]       抓取密钥（需真人在薇芯里点开会话/搜索触发）
  reset   [--yes]            清理所有生成物，还原初始状态

会话用显示名或 wxid 的子串/精确值指定。仅限本机本人账号、本地学习研究。
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import stat
import sys
import time
from pathlib import Path

import wxapi
import wxread

HERE = Path(__file__).resolve().parent


def _out(obj) -> None:
    print(json.dumps(obj, ensure_ascii=False))


def _fail(msg: str) -> None:
    print(json.dumps({"error": str(msg)}, ensure_ascii=False))
    sys.exit(1)


# --------------------------------------------------------------- status ----
def cmd_status(args) -> None:
    info = {"deps": {}, "weixin_running": False, "accounts": [], "account": None,
            "keys_ready": {}}
    for mod in ("Crypto", "zstandard", "psutil", "frida"):
        try:
            __import__(mod)
            info["deps"][mod] = True
        except Exception:
            info["deps"][mod] = False
    try:
        accts = wxread.find_accounts()
    except Exception as e:
        accts = []
        info["accounts_error"] = str(e)
    info["weixin_running"] = any(a.get("running") for a in accts)
    info["accounts"] = [{"wxid": a["wxid"], "running": a.get("running", False)} for a in accts]
    if accts:
        acct = next((a for a in accts if a.get("running")), accts[0])
        info["account"] = acct["wxid"]
        keys = wxread.load_keys(wxapi.KEYS_DIR / f"{acct['wxid']}.json")
        msg_ready = any(keys.get(r) for r in wxread.message_db_rels(acct["db_dir"]))
        info["keys_ready"] = {
            "contact": bool(keys.get("contact/contact.db")),
            "session": bool(keys.get("session/session.db")),
            "message": msg_ready,
        }
        info["ready"] = bool(keys.get("contact/contact.db")) and msg_ready
    else:
        info["ready"] = False
    _out(info)


# ----------------------------------------------------------------- list ----
def cmd_list(args) -> None:
    ctx = wxapi.open_account(args.account)
    _out({"account": ctx["wxid"], "conversations": wxapi.list_conversations(ctx)})


# -------------------------------------------------------------- history ----
def cmd_history(args) -> None:
    ctx = wxapi.open_account(args.account)
    conv = wxapi.resolve_conversation(ctx, args.conversation)
    recs = wxapi.read_history(ctx, conv["wxid"], media=args.media, limit=args.limit)
    result = {"account": ctx["wxid"], "conversation": conv, "count": len(recs), "messages": recs}
    if args.out:
        Path(args.out).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        _out({"account": ctx["wxid"], "conversation": conv, "count": len(recs), "out": str(args.out)})
    else:
        _out(result)


# ----------------------------------------------------------------- poll ----
def cmd_poll(args) -> None:
    ctx = wxapi.open_account(args.account)
    conv = wxapi.resolve_conversation(ctx, args.conversation)
    recs, baselined = wxapi.poll_increment(ctx, conv["wxid"], media=args.media, backlog=args.backlog)
    _out({"account": ctx["wxid"], "conversation": conv, "baselined": baselined,
          "new": len(recs), "messages": recs})


# ---------------------------------------------------------------- watch ----
def cmd_watch(args) -> None:
    ctx = wxapi.open_account(args.account)
    conv = wxapi.resolve_conversation(ctx, args.conversation)
    disp = wxapi.sanitize(conv["display"])
    out = Path(args.out) if args.out else (wxapi.EXPORT_DIR / ctx["wxid"] / f"{disp}_{conv['wxid'].split('@')[0][-8:]}.jsonl")
    out.parent.mkdir(parents=True, exist_ok=True)
    # 首次建基线（不回灌历史）
    wxapi.poll_increment(ctx, conv["wxid"], media=args.media, backlog=args.backlog)
    print(json.dumps({"watching": conv["display"], "wxid": conv["wxid"], "out": str(out),
                      "interval": args.interval}, ensure_ascii=False), flush=True)
    try:
        while True:
            time.sleep(args.interval)
            recs, _ = wxapi.poll_increment(ctx, conv["wxid"], media=args.media)
            if recs:
                with open(out, "a", encoding="utf-8") as f:
                    for r in recs:
                        line = json.dumps(r, ensure_ascii=False)
                        f.write(line + "\n")
                        print(line, flush=True)
    except KeyboardInterrupt:
        print(json.dumps({"stopped": True}, ensure_ascii=False), flush=True)


# ---------------------------------------------------------------- setup ----
def cmd_setup(args) -> None:
    import capture_keys
    ctx_accts = wxread.find_accounts()
    if not ctx_accts:
        _fail("未发现薇芯账号，请先启动并登录薇芯。")
    acct = next((a for a in ctx_accts if a.get("running")), ctx_accts[0])
    if args.account:
        acct = next((a for a in ctx_accts if a["wxid"] == args.account), acct)
    keys_file = wxapi.KEYS_DIR / f"{acct['wxid']}.json"
    sys.stderr.write(
        f"账号 {acct['wxid']}：开始抓密钥，约 {args.seconds}s。\n"
        "请在薇芯里多点开会话、搜索聊天内容、打开收藏/朋友圈/公众号（每个库首次打开连接才暴露密钥）。\n")
    sys.stderr.flush()

    def prog(done, total, rel):
        sys.stderr.write(f"  抓到 {rel} ({done}/{total})\n")
        sys.stderr.flush()

    try:
        cracked = capture_keys.capture(acct["db_dir"], keys_file, args.seconds, on_progress=prog)
    except Exception as e:
        _fail(f"抓取失败：{e}")
    _out({"account": acct["wxid"], "captured": len(cracked),
          "keys_file": str(keys_file), "keys": sorted(cracked.keys())})


# ---------------------------------------------------------------- reset ----
def _force_rm(p: Path) -> None:
    def onerr(func, path, _exc):
        try:
            os.chmod(path, stat.S_IWRITE); func(path)
        except Exception:
            pass
    if p.is_dir():
        try:
            shutil.rmtree(p, onexc=onerr)
        except TypeError:
            shutil.rmtree(p, onerror=lambda f, pth, ei: onerr(f, pth, None))
    else:
        try:
            p.unlink()
        except PermissionError:
            os.chmod(p, stat.S_IWRITE); p.unlink()


def cmd_reset(args) -> None:
    targets = [d for d in (HERE / "keys", HERE / "state", HERE / "export", HERE / "__pycache__") if d.is_dir()]
    targets += [HERE / n for n in ("keys.json", "captured_key.json", "imgkey.txt", "export_state.json")
                if (HERE / n).exists()]
    targets = [t for t in targets if t.resolve().parent == HERE or HERE in t.resolve().parents]
    if not targets:
        _out({"reset": True, "removed": [], "note": "已是初始状态"}); return
    if not args.yes:
        _out({"reset": False, "would_remove": [t.name for t in targets],
              "note": "加 --yes 以确认删除"}); return
    removed = []
    for t in targets:
        try:
            _force_rm(t); removed.append(t.name)
        except OSError as e:
            pass
    _out({"reset": True, "removed": removed})


def main() -> None:
    p = argparse.ArgumentParser(prog="wxskill", description="薇芯聊天记录 skill CLI（JSON 输出）")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("status").set_defaults(func=cmd_status)

    sp = sub.add_parser("list"); sp.add_argument("--account"); sp.set_defaults(func=cmd_list)

    sp = sub.add_parser("history")
    sp.add_argument("conversation"); sp.add_argument("--account")
    sp.add_argument("--limit", type=int); sp.add_argument("--media", action="store_true")
    sp.add_argument("--out"); sp.set_defaults(func=cmd_history)

    sp = sub.add_parser("poll")
    sp.add_argument("conversation"); sp.add_argument("--account")
    sp.add_argument("--media", action="store_true"); sp.add_argument("--backlog", action="store_true")
    sp.set_defaults(func=cmd_poll)

    sp = sub.add_parser("watch")
    sp.add_argument("conversation"); sp.add_argument("--account")
    sp.add_argument("--media", action="store_true"); sp.add_argument("--backlog", action="store_true")
    sp.add_argument("--interval", type=int, default=5); sp.add_argument("--out")
    sp.set_defaults(func=cmd_watch)

    sp = sub.add_parser("setup")
    sp.add_argument("--account"); sp.add_argument("--seconds", type=int, default=90)
    sp.set_defaults(func=cmd_setup)

    sp = sub.add_parser("reset"); sp.add_argument("--yes", action="store_true")
    sp.set_defaults(func=cmd_reset)

    args = p.parse_args()
    try:
        args.func(args)
    except SystemExit:
        raise
    except Exception as e:
        _fail(e)


if __name__ == "__main__":
    main()
