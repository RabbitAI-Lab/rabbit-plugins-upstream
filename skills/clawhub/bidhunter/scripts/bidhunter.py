#!/usr/bin/env python3
"""
bidhunter.py - Unified zero-friction entry point (BidHunter v1.5, A9).

Wraps the most common operations behind one memorable command so non-technical
users don't need to remember pipeline.sh / qual_check.py flags.

Usage:
  python3 bidhunter.py run [--fresh] [--summary]      # 采集+比对+报告+推送
  python3 bidhunter.py status                          # 今日采集状态
  python3 bidhunter.py doctor                          # 一键诊断
  python3 bidhunter.py demo                            # 看示例效果
  python3 bidhunter.py calendar [--days 7]             # 投标日历
  python3 bidhunter.py faq [关键词]                     # 查常见问题
  python3 bidhunter.py rules edit [--port 8080]        # 打开规则编辑器
  python3 bidhunter.py ai read <招标文件.pdf>          # v2.0 AI 速读
  python3 bidhunter.py ai advise <招标文件.pdf>        # v2.5 投标建议
  python3 bidhunter.py api serve [--port 8765]         # v3.0 本地查询API
  python3 bidhunter.py help                            # 全部命令
"""
import os
import sys
import subprocess
import argparse

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PY = sys.executable


def _run(cmd, **kw):
    return subprocess.run([PY, "-u", os.path.join(SCRIPT_DIR, cmd)] + kw.get("args", []),
                          capture_output=kw.get("capture", False), text=True)


def cmd_run(args):
    extra = []
    if args.fresh:
        extra.append("--fresh")
    if args.summary:
        extra.append("--summary")
    r = subprocess.run(["bash", os.path.join(SCRIPT_DIR, "pipeline.sh")] + extra)
    return r.returncode


def cmd_status(args):
    r = _run("status.py", capture=True)
    print(r.stdout or r.stderr)
    return 0


def cmd_doctor(args):
    r = _run("doctor.py")
    return r.returncode


def cmd_demo(args):
    r = _run("demo.py", args=(["--summary", "--calendar"] if args.calendar else []))
    print(r.stdout)
    return 0


def cmd_calendar(args):
    # use today's qual file if present
    import glob
    files = sorted(glob.glob(os.path.join(SCRIPT_DIR, "bid_cache", "qual_*.jsonl")))
    target = files[-1] if files else None
    if not target:
        print("尚无 qual 数据，请先运行: python3 bidhunter.py run")
        return 1
    r = _run("calendar.py", args=[target, "--days", str(args.days)])
    print(r.stdout)
    return 0


def cmd_faq(args):
    r = _run("faq.py", args=(args.terms if args.terms else []), capture=True)
    print(r.stdout or r.stderr)
    return 0


def cmd_rules(args):
    if args.action == "edit":
        port = args.port
        print(f"启动规则编辑器 → http://localhost:{port}  (Ctrl+C 退出)")
        r = _run("rule_editor.py", args=["--port", str(port)])
        return r.returncode
    print("用法: python3 bidhunter.py rules edit [--port 8080]")
    return 1


def cmd_ai(args):
    if args.action == "read":
        r = _run("ai/doc_reader.py", args=[args.file])
        print(r.stdout or r.stderr)
        return r.returncode
    if args.action == "advise":
        r = _run("ai/bid_advisor.py", args=[args.file])
        print(r.stdout or r.stderr)
        return r.returncode
    print("用法: bidhunter.py ai read <文件> | ai advise <文件>")
    return 1


def cmd_api(args):
    if args.action == "serve":
        r = _run("api_server.py", args=["--port", str(args.port)])
        return r.returncode
    print("用法: bidhunter.py api serve [--port 8765]")
    return 1


def cmd_help(args):
    print(__doc__)
    return 0


def main():
    p = argparse.ArgumentParser(prog="bidhunter", description="标讯猎手 统一入口")
    sub = p.add_subparsers(dest="cmd")

    sp = sub.add_parser("run"); sp.add_argument("--fresh", action="store_true"); sp.add_argument("--summary", action="store_true"); sp.set_defaults(func=cmd_run)
    sub.add_parser("status").set_defaults(func=cmd_status)
    sub.add_parser("doctor").set_defaults(func=cmd_doctor)
    pd = sub.add_parser("demo"); pd.add_argument("--calendar", action="store_true"); pd.set_defaults(func=cmd_demo)
    pc = sub.add_parser("calendar"); pc.add_argument("--days", type=int, default=7); pc.set_defaults(func=cmd_calendar)
    pf = sub.add_parser("faq"); pf.add_argument("terms", nargs="*"); pf.set_defaults(func=cmd_faq)
    pr = sub.add_parser("rules"); pr.add_argument("action", nargs="?"); pr.add_argument("--port", type=int, default=8080); pr.set_defaults(func=cmd_rules)
    pa = sub.add_parser("ai"); pa.add_argument("action", nargs="?"); pa.add_argument("file", nargs="?"); pa.set_defaults(func=cmd_ai)
    pap = sub.add_parser("api"); pap.add_argument("action", nargs="?"); pap.add_argument("--port", type=int, default=8765); pap.set_defaults(func=cmd_api)
    sub.add_parser("help").set_defaults(func=cmd_help)

    if len(sys.argv) < 2:
        cmd_help(None)
        return 0
    args = p.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
