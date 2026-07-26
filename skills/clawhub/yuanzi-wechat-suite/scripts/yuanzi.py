#!/usr/bin/env python3
# yuanzi-wechat-suite 总调度（v2.0.0）
# 用法：
#   python3 yuanzi.py --help                # 命令总览
#   python3 yuanzi.py --check                # 4 站自检
#   python3 yuanzi.py extract --url <mp URL> # 读稿
#   python3 yuanzi.py image <subcmd> --args  # 配图
#   python3 yuanzi.py publish <input>        # 发布
#   python3 yuanzi.py check <article>        # v7 散文体校验
#   python3 yuanzi.py all --url <mp> --title "..."  # 全流程

import sys
import argparse
import subprocess
from pathlib import Path

SKILL_ROOT = Path(__file__).parent.parent.resolve()
SCRIPTS = SKILL_ROOT / "scripts"


def run(cmd, cwd=None, check=False):
    """执行子命令并返回 (returncode, stdout, stderr)"""
    try:
        r = subprocess.run(
            cmd, cwd=cwd, capture_output=True, text=True,
            encoding="utf-8", errors="replace",
        )
        return r.returncode, r.stdout, r.stderr
    except FileNotFoundError as e:
        return 127, "", str(e)


def cmd_check(_args):
    """4 站自检"""
    print("[1/4] 写作舵 (master / v7_check.py)...")
    rc, out, err = run(
        [sys.executable, str(SCRIPTS / "master" / "v7_check.py"), "--check"],
        cwd=str(SKILL_ROOT),
    )
    print(("  [OK] " if rc == 0 else "  [X] ") + (out.strip() or err.strip()))

    print("[2/4] 读稿锚 (extractor / extract.js)...")
    rc, out, err = run(["node", "--version"], cwd=str(SCRIPTS / "extractor"))
    if rc == 0:
        print(f"  [OK] node: {out.strip()}")
        if (SCRIPTS / "extractor" / "node_modules").exists():
            print("  [OK] node_modules 已装")
        else:
            print("  [!] node_modules 未装，请先 npm install")
    else:
        print("  [X] node 未装")

    print("[3/4] 配图帆 (image-gen / generate.py)...")
    rc, out, err = run(
        [sys.executable, str(SCRIPTS / "image-gen" / "generate.py"), "--help"],
        cwd=str(SCRIPTS / "image-gen"),
    )
    print("  [OK] generate.py 可用" if rc in (0, 2) else f"  [X] {err.strip()}")
    try:
        from PIL import Image  # noqa
        print("  [OK] Pillow 可用")
    except ImportError:
        print("  [!] Pillow 未装，请 pip install Pillow")

    print("[4/4] 发布桨 (publisher / publish_wechat.py)...")
    rc, out, err = run(
        [
            sys.executable,
            str(SCRIPTS / "publisher" / "publish_wechat.py"),
            "--help",
        ],
        cwd=str(SCRIPTS / "publisher"),
    )
    print("  [OK] publish_wechat.py 可用" if rc == 0 else f"  [X] {err.strip()}")
    try:
        import keyring  # noqa
        print("  [OK] keyring 可用")
    except ImportError:
        print("  [!] keyring 未装，请 pip install keyring")

    print("\n=== 自检完成 ===")
    return 0


def cmd_extract(args):
    """读稿"""
    if not args.url:
        print("[X] --url 必填（mp.weixin.qq.com URL）")
        return 1
    cmd = ["node", str(SCRIPTS / "extractor" / "extract.js"), "--url", args.url]
    if args.output:
        cmd += ["--output", args.output]
    print(f"$ {' '.join(cmd)}")
    rc, out, err = run(cmd, cwd=str(SCRIPTS / "extractor"))
    if out: print(out)
    if err: print(err, file=sys.stderr)
    return rc


def cmd_image(args):
    """配图"""
    cmd = [sys.executable, str(SCRIPTS / "image-gen" / "generate.py")] + args.rest
    print(f"$ {' '.join(cmd)}")
    rc, out, err = run(cmd, cwd=str(SCRIPTS / "image-gen"))
    if out: print(out)
    if err: print(err, file=sys.stderr)
    return rc


def cmd_publish(args):
    """发布"""
    cmd = [
        sys.executable,
        str(SCRIPTS / "publisher" / "publish_wechat.py"),
    ]
    if args.input:
        cmd.append(args.input)
    cmd += args.rest
    print(f"$ {' '.join(cmd)}")
    rc, out, err = run(cmd, cwd=str(SCRIPTS / "publisher"))
    if out: print(out)
    if err: print(err, file=sys.stderr)
    return rc


def cmd_check_article(args):
    """v7 散文体校验"""
    if not args.input:
        print("[X] <article> 必填")
        return 1
    cmd = [
        sys.executable,
        str(SCRIPTS / "master" / "v7_check.py"),
        args.input,
    ]
    rc, out, err = run(cmd, cwd=str(SKILL_ROOT))
    if out: print(out)
    if err: print(err, file=sys.stderr)
    return rc


def cmd_all(args):
    """全流程：extract → check → image → publish --dry-run"""
    print("=== yuanzi 全流程 ===")
    print("[1/4] 读稿...")
    rc = cmd_extract(argparse.Namespace(url=args.url, output=None))
    if rc != 0:
        print(f"[X] 读稿失败 (rc={rc})")
        return rc

    print("\n[2/4] 散文体校验...")
    # 默认找最新 .md
    md_files = sorted(SKILL_ROOT.glob("**/*.md"), key=lambda p: p.stat().st_mtime, reverse=True)
    article = md_files[0] if md_files else None
    if article:
        rc = cmd_check_article(argparse.Namespace(input=str(article)))
        if rc != 0:
            print(f"[!] 散文体校验未通过 (rc={rc})，仍继续下游...")
    else:
        print("[!] 未找到 .md 文章，跳过散文体校验")

    print("\n[3/4] 配图（占位：请单独调 yuanzi image cover/compare/chart）")
    print("$ python3 scripts/image-gen/generate.py cover --help")

    print("\n[4/4] 发布（占位：请单独调 yuanzi publish <HTML>）")
    print(f"$ python3 scripts/publisher/publish_wechat.py <html> --dry-run --title '{args.title or '...'}'")

    print("\n=== 全流程终止于半自动节点（配图 + 发布需手动确认） ===")
    return 0


def main():
    parser = argparse.ArgumentParser(
        description="yuanzi-wechat-suite v2.0.0 总调度",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例：
  python3 yuanzi.py --check                                  # 4 站自检
  python3 yuanzi.py extract --url "https://mp.weixin.qq.com/s/..."
  python3 yuanzi.py image cover --title "标题" --output cover.png
  python3 yuanzi.py publish article.html --dry-run
  python3 yuanzi.py check article.md
  python3 yuanzi.py all --url "..." --title "..."
""",
    )
    parser.add_argument("--check", action="store_true", help="4 站自检")
    sub = parser.add_subparsers(dest="cmd")

    p_extract = sub.add_parser("extract", help="读稿锚 — mp.weixin.qq.com 解析")
    p_extract.add_argument("--url", help="公众号 URL")
    p_extract.add_argument("--output", help="输出文件")

    p_image = sub.add_parser("image", help="配图帆 — cover/compare/chart")
    p_image.add_argument("rest", nargs=argparse.REMAINDER, help="透传给 generate.py")

    p_publish = sub.add_parser("publish", help="发布桨 — Markdown/HTML → 草稿箱")
    p_publish.add_argument("input", nargs="?", help="Markdown 或 HTML 文件")
    p_publish.add_argument("rest", nargs=argparse.REMAINDER, help="透传给 publish_wechat.py")

    p_check = sub.add_parser("check", help="v7 散文体自动校验")
    p_check.add_argument("input", help=".md 或 .txt")

    p_all = sub.add_parser("all", help="全流程（半自动）")
    p_all.add_argument("--url", required=True, help="公众号 URL")
    p_all.add_argument("--title", help="文章标题")

    args = parser.parse_args()

    if args.check or args.cmd is None:
        return cmd_check(args)
    if args.cmd == "extract":
        return cmd_extract(args)
    if args.cmd == "image":
        return cmd_image(args)
    if args.cmd == "publish":
        return cmd_publish(args)
    if args.cmd == "check":
        return cmd_check_article(args)
    if args.cmd == "all":
        return cmd_all(args)
    return 0


if __name__ == "__main__":
    sys.exit(main())
