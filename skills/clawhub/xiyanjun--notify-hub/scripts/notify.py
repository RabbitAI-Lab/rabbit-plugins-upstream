#!/usr/bin/env python3
"""
notify-hub — 统一通知层 CLI

一个 skill 抽象掉所有消息通道：调用方定义"发什么"（text/card/file），
`--to` 指定"发到哪"（channel:target），内容定义一次、可广播到任意通道。

通道：feishu / wecom / dingtalk / slack / telegram / email

用法：
  notify config add feishu 我的群 --url https://open.feishu.cn/open-apis/bot/v2/hook/xxx
  notify send text "收盘提醒" --to feishu:我的群
  notify send card examples/card_report.json --to feishu:群1,wecom:群2   # 广播
  notify send file report.pdf --to email:老板
  notify test --to feishu:我的群

配置默认存于 ~/.notify-hub/config.json，可用 NOTIFY_CONFIG 覆盖。零第三方依赖。
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core import registry, router
from core import message as msgmod

DEFAULT_CONFIG = os.environ.get("NOTIFY_CONFIG") or os.path.expanduser(
    "~/.notify-hub/config.json"
)

# config add 支持的凭据字段（不同通道用不同子集）：(命令行 flag, 配置字段名)
CRED_FLAGS = [
    ("url", "url"), ("secret", "secret"), ("token", "token"),
    ("chat-id", "chat_id"), ("smtp-host", "smtp_host"), ("port", "port"),
    ("user", "user"), ("password", "password"), ("to", "to"), ("sender", "sender"),
]


def load_config():
    if not os.path.exists(DEFAULT_CONFIG):
        return {"channels": {}}
    with open(DEFAULT_CONFIG, "r", encoding="utf-8") as f:
        return json.load(f)


def save_config(cfg):
    os.makedirs(os.path.dirname(DEFAULT_CONFIG), exist_ok=True)
    with open(DEFAULT_CONFIG, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)
    try:
        os.chmod(DEFAULT_CONFIG, 0o600)  # 凭据敏感，仅本人可读
    except OSError:
        pass


def read_content(arg, use_stdin):
    if use_stdin:
        return sys.stdin.read()
    if arg and os.path.isfile(arg):
        with open(arg, "r", encoding="utf-8") as f:
            return f.read()
    return arg or ""


# ---------------------------------------------------------------- config ----

def cmd_config_add(args):
    cfg = load_config()
    cred = {}
    for flag, dest in CRED_FLAGS:
        val = getattr(args, dest, None)
        if val is not None:
            cred[dest] = int(val) if dest == "port" else val
    if not cred:
        sys.exit("错误：未提供任何凭据（--url/--token/--smtp-host 等）")
    ch_cfg = cfg.setdefault("channels", {}).setdefault(args.channel, {})
    ch_cfg.setdefault("targets", {})[args.target] = cred
    if ch_cfg.get("default") is None:
        ch_cfg["default"] = args.target
    save_config(cfg)
    print(f"已添加 {args.channel} 目标「{args.target}」"
          + ("（并设为该通道默认）" if ch_cfg["default"] == args.target else ""))


def cmd_config_list(args):
    registry.load_all()
    cfg = load_config()
    chs = cfg.get("channels", {})
    if not chs:
        print("尚未配置任何通道。")
        return
    for ch, c in chs.items():
        dflt = c.get("default")
        for tgt in c.get("targets", {}):
            mark = " *" if tgt == dflt else ""
            print(f"  {ch}:{tgt}{mark}")
    print(f"支持通道：{', '.join(registry.names())}")


def cmd_config_rm(args):
    cfg = load_config()
    ch_cfg = cfg.get("channels", {}).get(args.channel)
    if not ch_cfg or ch_cfg.get("targets", {}).pop(args.target, None) is None:
        sys.exit(f"错误：未找到 {args.channel}:{args.target}")
    if ch_cfg.get("default") == args.target:
        ch_cfg["default"] = next(iter(ch_cfg.get("targets", {})), None)
    save_config(cfg)
    print(f"已删除 {args.channel}:{args.target}")


def cmd_config_default(args):
    cfg = load_config()
    ch_cfg = cfg.get("channels", {}).get(args.channel)
    if not ch_cfg or args.target not in ch_cfg.get("targets", {}):
        sys.exit(f"错误：未找到 {args.channel}:{args.target}")
    ch_cfg["default"] = args.target
    save_config(cfg)
    print(f"{args.channel} 默认目标已设为「{args.target}」")


# ---------------------------------------------------------------- send ----

def build_message(args):
    if args.kind == "text":
        content = read_content(" ".join(args.content) if args.content else "", args.stdin).strip()
        if not content:
            sys.exit("错误：文本内容为空")
        return {"kind": "text", "text": content, "title": args.title or "通知"}
    if args.kind == "card":
        raw = read_content(args.content[0] if args.content else "", args.stdin).strip()
        if not raw:
            sys.exit("错误：卡片内容为空")
        try:
            data = json.loads(raw)
        except json.JSONDecodeError as e:
            sys.exit(f"错误：卡片 JSON 解析失败：{e}")
        if "kind" not in data:
            data = {"kind": "card", **data}
        return data
    if args.kind == "file":
        path = args.content[0] if args.content else ""
        if not path or not os.path.isfile(path):
            sys.exit(f"错误：文件不存在：{path}")
        return {"kind": "file", "path": path, "title": args.title or "文件", "caption": args.caption or ""}
    sys.exit(f"未知消息类型：{args.kind}")


def resolve_targets(args, cfg):
    if args.to == "all":
        return [(name, None) for name in registry.names() if name in cfg.get("channels", {})]
    targets = router.parse_targets(args.to)
    if not targets:
        targets = [(name, None) for name in registry.names() if name in cfg.get("channels", {})]
    return targets


def cmd_dry_run(args, message):
    """零配置预览：对目标通道（默认全部）渲染消息，打印 payload，不发送、无需凭据。"""
    spec = (args.to or "").strip()
    if spec and spec != "all":
        names = [name for name, _ in router.parse_targets(spec) if registry.get(name)]
    else:
        names = registry.names()
    if not names:
        sys.exit("错误：没有可预览的通道")
    print("== dry-run 预览（未发送，无需凭据）==\n")
    for name in names:
        cls = registry.get(name)
        payload = cls({}).render(message)
        print(f"--- {name}（{cls.label}） ---")
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        print()


def cmd_send(args):
    registry.load_all()
    cfg = load_config()
    message = build_message(args)
    if args.dry_run:
        cmd_dry_run(args, message)
        return
    targets = resolve_targets(args, cfg)

    if not targets:
        sys.exit("错误：未指定目标（--to），也没有已配置通道。先用 config add 添加。")

    all_ok = True
    for ch_name, tgt in targets:
        cls = registry.get(ch_name)
        if not cls:
            print(f"  ✗ {ch_name}:{tgt or '默认'} — 未知通道")
            all_ok = False
            continue
        ch = cls(cfg.get("channels", {}).get(ch_name, {}))
        try:
            r = ch.send(message, tgt)
        except Exception as e:
            r = {"ok": False, "code": -1, "msg": str(e)}
        mark = "✓" if r.get("ok") else "✗"
        print(f"  {mark} {ch_name}:{tgt or '默认'} — {r.get('msg', '')}")
        if not r.get("ok"):
            all_ok = False
    sys.exit(0 if all_ok else 1)


def cmd_test(args):
    registry.load_all()
    cfg = load_config()
    targets = resolve_targets(args, cfg)
    all_ok = True
    for ch_name, tgt in targets:
        cls = registry.get(ch_name)
        if not cls:
            print(f"  ✗ {ch_name} — 未知通道")
            all_ok = False
            continue
        ch = cls(cfg.get("channels", {}).get(ch_name, {}))
        try:
            r = ch.send({"kind": "text", "text": "notify-hub 连通性测试"}, tgt)
        except Exception as e:
            r = {"ok": False, "msg": str(e)}
        print(f"  {'✓' if r.get('ok') else '✗'} {ch_name}:{tgt or '默认'} — {r.get('msg', '')}")
        if not r.get("ok"):
            all_ok = False
    sys.exit(0 if all_ok else 1)


def cmd_channels(args):
    registry.load_all()
    print("支持通道：")
    for name in registry.names():
        cls = registry.get(name)
        print(f"  {name:10s} {cls.label}  (限流 {cls.rate_per_min}/分钟)")


# ------------------------------------------------------------------ main ----

def main():
    ap = argparse.ArgumentParser(prog="notify", description="统一通知层：定义一次内容，广播到任意通道")
    sub = ap.add_subparsers(dest="cmd", required=True)

    # config
    pc = sub.add_parser("config", help="管理通道与目标配置")
    pcc = pc.add_subparsers(dest="sub", required=True)
    a = pcc.add_parser("add", help="添加目标")
    a.add_argument("channel", help="通道名（feishu/wecom/dingtalk/slack/telegram/email）")
    a.add_argument("target", help="目标名（如群名/收件人）")
    for flag, dest in CRED_FLAGS:
        a.add_argument(f"--{flag}", dest=dest, default=None)
    a.set_defaults(func=cmd_config_add)
    a = pcc.add_parser("list", help="列出所有目标")
    a.set_defaults(func=cmd_config_list)
    a = pcc.add_parser("rm", help="删除目标")
    a.add_argument("channel")
    a.add_argument("target")
    a.set_defaults(func=cmd_config_rm)
    a = pcc.add_parser("default", help="设通道默认目标")
    a.add_argument("channel")
    a.add_argument("target")
    a.set_defaults(func=cmd_config_default)

    # send
    a = sub.add_parser("send", help="发送消息")
    a.add_argument("kind", choices=["text", "card", "file"])
    a.add_argument("content", nargs="*", help="内容（文本/卡片文件或JSON/文件路径）")
    a.add_argument("--to", default=None, help="目标，如 feishu:群名,wecom:群名；或 all 广播")
    a.add_argument("--stdin", action="store_true", help="从 stdin 读取内容")
    a.add_argument("--title", default=None, help="标题（text/file 用于邮件主题）")
    a.add_argument("--caption", default=None, help="文件说明")
    a.add_argument("--dry-run", action="store_true", help="预览各通道渲染结果，不发送（无需配置凭据）")
    a.set_defaults(func=cmd_send)

    # test
    a = sub.add_parser("test", help="连通性测试")
    a.add_argument("--to", default=None)
    a.set_defaults(func=cmd_test)

    # channels
    a = sub.add_parser("channels", help="列出支持的通道")
    a.set_defaults(func=cmd_channels)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
