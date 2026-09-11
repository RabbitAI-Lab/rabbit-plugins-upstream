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
  python3 bidhunter.py compliance scan <标书.pdf>       # v3.5 合规红线扫描
  python3 bidhunter.py compliance checklist            # v3.5 交标前自查清单
  python3 bidhunter.py feedback [--platform skillhub|clawhub] [--no-open]
                                                      # 零成本反馈：格式化+剪贴板+开评论页
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


def cmd_compliance(args):
    """v3.5 合规红线扫描（本地规则库，零 API 成本）"""
    sc = "compliance/compliance_scanner.py"
    if args.action == "scan":
        if not args.file:
            print("用法: bidhunter.py compliance scan <文件> [--mode tender|bid|both] [--json] [--llm]")
            return 1
        a = [args.file, "--mode", args.mode]
        if args.json:
            a.append("--json")
        if args.llm:
            a.append("--llm")
        r = _run(sc, args=a)
        print(r.stdout or r.stderr)
        return r.returncode
    if args.action == "checklist":
        r = _run(sc, args=["--checklist"])
        print(r.stdout or r.stderr)
        return r.returncode
    if args.action == "list":
        r = _run(sc, args=["--list"])
        print(r.stdout or r.stderr)
        return r.returncode
    print("用法:")
    print("  bidhunter.py compliance scan <文件> [--mode tender|bid|both] [--json] [--llm]")
    print("  bidhunter.py compliance checklist    # 交标前自查清单（31条）")
    print("  bidhunter.py compliance list         # 全部法定红线")
    print("")
    print("  --mode tender = 扫招标文件找埋雷；bid = 扫投标文件找致命项")
    print("  --llm = 附加 LLM 智能补充扫描（需配置 MiniMax Key，会消耗余额）")
    return 1


def cmd_feedback(args):
    """零成本反馈：本地格式化 -> 剪贴板 -> 打开平台评论页（无后端、无云服务）"""
    extra = []
    if args.platform:
        extra += ["--platform", args.platform]
    if args.no_open:
        extra.append("--no-open")
    if args.type:
        extra += ["--type", args.type]
    if args.scenario:
        extra += ["--scenario", args.scenario]
    if args.detail:
        extra += ["--detail", args.detail]
    r = _run("feedback.py", args=extra)
    return r.returncode


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
    pcomp = sub.add_parser("compliance"); pcomp.add_argument("action", nargs="?"); pcomp.add_argument("file", nargs="?")
    pcomp.add_argument("--mode", default="both", choices=["tender", "bid", "both"])
    pcomp.add_argument("--json", action="store_true"); pcomp.add_argument("--llm", action="store_true")
    pcomp.set_defaults(func=cmd_compliance)
    pfb = sub.add_parser("feedback", help="发送反馈到社区（零成本，无后端）")
    pfb.add_argument("--platform", choices=["skillhub", "clawhub"], default="skillhub")
    pfb.add_argument("--no-open", action="store_true", help="只生成文本，不打开浏览器")
    pfb.add_argument("--type", help="反馈类型编号 0-5（非交互直填）")
    pfb.add_argument("--scenario", help="使用场景（非交互直填）")
    pfb.add_argument("--detail", help="具体描述（非交互直填）")
    pfb.set_defaults(func=cmd_feedback)
    sub.add_parser("help").set_defaults(func=cmd_help)

    if len(sys.argv) < 2:
        cmd_help(None)
        return 0
    args = p.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
