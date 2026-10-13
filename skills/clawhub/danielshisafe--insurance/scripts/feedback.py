#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
保险计划书分析大师 — 反馈收集器
=====================================================================
把「出错」和「改进意见」变成作者能收到、能复现、且不会泄露隐私的一封邮件。

设计前提
-------------------------------------------------------------------
技能内部**没有服务端**，反馈无法自动上报。所以链路是：

    出错 / 提意见  →  落盘成 md  →  打包 zip  →  生成预填好的 .eml
                                                  →  使用人双击、点发送

零凭据、零第三方依赖、零网络配置。

★ 隐私铁律（最重要的一条）
-------------------------------------------------------------------
保险计划书里有姓名、身份证号、保单号、保费金额，**一个字都不能进反馈**。
本脚本对所有写入内容强制脱敏：

  - 绝对路径      → `<路径>/<文件>.pdf`（路径里常带姓名，如 `桌面/张三的保单.pdf`）
  - 4 位以上数字  → `<数字>`（保费、身份证、保单号、金额一律抹掉）
  - 命令行参数    → 同样脱敏后才记录

脱敏是**保守**的：宁可多抹，不可漏抹。若你需要让作者看到具体数值，
请手工另建一个文件放进 feedback 目录并明确告知。

用法
-------------------------------------------------------------------
  # 手动提一条反馈（改进建议 / 数据问题 / 其他）
  python scripts/feedback.py report --type 建议 --content "压力测试表希望能加一档 10% 实现率"

  # 列出已收集的反馈
  python scripts/feedback.py list

  # 打包全部反馈 + 生成一封预填好的邮件，自动打开
  python scripts/feedback.py export

  # 只打包不打开
  python scripts/feedback.py export --no-open

  # 清空已导出的反馈（导出成功后才建议清）
  python scripts/feedback.py clear --yes

  # 打印「要不要告诉开发者」的标准文案（供模型转述，不写任何文件）
  python scripts/feedback.py invite --about "IRR 算出来和手算差很多"

放置位置
-------------------------------------------------------------------
反馈写到 `~/.workbuddypro/feedback/保险计划书分析大师/`，**不在技能目录内**。
原因有二：重装/升级技能不丢反馈；绝不会被打进分发包泄露给别人。

作者的收件邮箱在 `feedback_config.json` 的 `author_email` 字段。
=====================================================================
"""
import argparse
import json
import os
import re
import subprocess
import sys
import traceback
from datetime import datetime

SKILL_NAME = "保险计划书分析大师"
SKILL_VERSION = "1.5.3"

# ★ 反馈目录放在技能外：重装不丢，且绝不会被打进分发 zip
ROOT = os.path.join(os.path.expanduser("~"), ".workbuddypro", "feedback", SKILL_NAME)
CONFIG_PATH = os.path.join(ROOT, "feedback_config.json")
EXPORT_DIR = os.path.join(ROOT, "已导出")

DEFAULT_CONFIG = {
    # ★ 作者（本技能维护者）的收件邮箱。
    #   注意：这个值会**明文写进技能包** —— 分发后每个使用人 export 时都会看到它。
    #   只改本机的 feedback_config.json 是不够的：使用人机器上的配置是首次运行时
    #   用这里的默认值生成的，所以**默认值本身**必须是对的。
    "author_email": "zhenwei-shi@qq.com",
    # 是否在反馈里附带 Python 版本 / 系统信息（不含任何路径）
    "include_env": True,
}

PLACEHOLDER_EMAIL = "TODO@example.com"


# ---------------------------------------------------------------- 脱敏
_LONG_NUM = re.compile(r"\d[\d,]*(?:\.\d+)?")
_WIN_PATH = re.compile(r"[A-Za-z]:[\\/][^\s\"'|<>]+")
_POSIX_PATH = re.compile(r"(?:/[\w.\-一-鿿]+){3,}")


def _mask_numbers(s):
    """抹掉保费 / 身份证 / 保单号这类大数，但**保留 IRR 与利率**。

    ★ 为什么不能「一律抹掉 4 位以上数字」：
      初版就是这么做的，结果 `1.298`、`-0.188`、`3.5` 全被抹成 `<数字>`。
      而 IRR 与利率恰恰是判断「到底算错没算错」最关键的诊断信息 ——
      抹掉它们，反馈就只剩一句「IRR 不对」，作者无从下手。
      保费是整数（200000）、IRR 是小数（1.298），两者形态不同，可以分开处理。

    规则：
      - 整数（含千分位）  → 位数 ≥4 才抹：200000、1,000,000、身份证号、保单号
      - 小数              → 只看**整数部分**位数 ≥4 才抹：
                            1.298 / 0.188 / 3.5 保留；12345.67 这类大额抹掉
      - 1~3 位整数        → 保留（列号、数组下标、年份，丢了就没法定位）
    """
    def rep(m):
        t = m.group(0)
        if "." in t:
            intpart = re.sub(r"[^\d]", "", t.split(".")[0])
            return "<数字>" if len(intpart) >= 4 else t
        digits = re.sub(r"[^\d]", "", t)
        return "<数字>" if len(digits) >= 4 else t
    return _LONG_NUM.sub(rep, s)


def _mask_paths(s):
    """绝对路径只留扩展名 —— 路径里常带真实姓名（`桌面/张三的保单.pdf`）。"""
    def rep(m):
        ext = os.path.splitext(m.group(0))[1]
        return f"<路径>/<文件>{ext}" if ext else "<路径>"
    s = _WIN_PATH.sub(rep, s)
    s = _POSIX_PATH.sub(rep, s)
    return s


def sanitize(text):
    """强制脱敏：路径 → 数字 → 收尾。任何写盘内容都必须先过这一层。"""
    if text is None:
        return ""
    s = str(text)
    s = _mask_paths(s)
    s = _mask_numbers(s)
    return s


def sanitize_argv(argv):
    """命令行参数脱敏：参数里几乎必然含文件路径（也就可能含姓名）。"""
    if not argv:
        return ""
    out = []
    for i, a in enumerate(argv):
        if i == 0:
            # 脚本自身路径同样要脱敏（路径里有系统用户名）
            out.append(sanitize(os.path.basename(str(a))))
        else:
            out.append(sanitize(a))
    return " ".join(out)


# ---------------------------------------------------------------- 配置
def load_config():
    cfg = dict(DEFAULT_CONFIG)
    try:
        if os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH, encoding="utf-8") as f:
                cfg.update(json.load(f))
    except Exception:
        pass
    return cfg


def ensure_root():
    os.makedirs(ROOT, exist_ok=True)
    if not os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_CONFIG, f, ensure_ascii=False, indent=2)
    return ROOT


# ---------------------------------------------------------------- 写盘
def _stamp():
    return datetime.now().strftime("%Y%m%d-%H%M%S")


def _env_block(cfg):
    if not cfg.get("include_env", True):
        return ""
    return (f"- Python：{sys.version.split()[0]}\n"
            f"- 系统：{sys.platform}\n")


def write_feedback(kind, title, body, meta=None, filename=None, dedup=True):
    """写一条反馈到 ROOT，返回 `(文件路径, 是否命中重复)`。

    kind 用于文件名前缀。`dedup=True`（默认）时，若已存在正文完全相同的反馈，
    直接返回那条的路径并把第二项置 True，**不新建文件**。
    """
    ensure_root()
    cfg = load_config()
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = [
        f"# 【{kind}】{sanitize(title)}",
        "",
        f"- 提交时间：{stamp}",
        f"- 技能版本：{SKILL_VERSION}",
        f"- 反馈类型：{kind}",
    ]
    for k, v in (meta or {}).items():
        lines.append(f"- {k}：{sanitize(v)}")
    env = _env_block(cfg)
    if env:
        lines += ["", "## 环境", env.rstrip()]
    lines += ["", "## 内容", "", sanitize(body).strip() or "（空）", ""]
    text = "\n".join(lines)

    # ★ 去重：内容完全相同的反馈不记第二条。
    #   实测场景：同一条命令被重试执行（沙箱绕过、模型重复调用、使用人连点两次），
    #   会产生两条一模一样的反馈 —— 作者收到后既困惑（以为两个人提了同一件事），
    #   又无法判断这个问题到底有多普遍。宁可记一条，也不要重复刷屏。
    if dedup:
        dup = find_duplicate(body)
        if dup:
            return dup, True

    fn = filename or f"{_stamp()}-{kind}.md"
    path = os.path.join(ROOT, fn)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path, False


def find_duplicate(body):
    """已存在「正文完全相同」的反馈则返回其路径，否则返回 None。

    只比对 `## 内容` 之后的部分，忽略时间戳与环境信息 ——
    同一条意见换个时间再提，本质上还是同一条。
    """
    body_s = sanitize(body).strip()
    if not body_s or not os.path.isdir(ROOT):
        return None
    try:
        for fn in sorted(os.listdir(ROOT)):
            if not fn.endswith(".md"):
                continue
            try:
                t = open(os.path.join(ROOT, fn), encoding="utf-8").read()
            except Exception:
                continue
            i = t.find("## 内容")
            if i < 0:
                continue
            if t[i + len("## 内容"):].strip() == body_s:
                return os.path.join(ROOT, fn)
    except Exception:
        pass
    return None


def record_crash(etype, value, tb, argv=None):
    """供 _feedback_hook 调用：把未捕获异常写成脱敏故障快照。"""
    try:
        raw_tb = "".join(traceback.format_exception(etype, value, tb))
        body = (
            "## 异常\n\n"
            f"- 类型：`{sanitize(getattr(etype, '__name__', str(etype)))}`\n"
            f"- 消息：{sanitize(value)}\n\n"
            "## 调用栈（已脱敏）\n\n```\n"
            f"{sanitize(raw_tb)}\n```\n"
        )
        meta = {"触发命令": sanitize_argv(argv or sys.argv)}
        # 同一个崩溃反复发生 = 同一个 bug，去重后只留一份快照
        path, _dup = write_feedback("自动捕获", f"{etype.__name__}: {str(value)[:60]}",
                                    body, meta=meta,
                                    filename=f"{_stamp()}-crash.md")
        return path
    except Exception:
        return None


# ---------------------------------------------------------------- 子命令
def cmd_report(args):
    meta = {}
    if getattr(args, "context", None):
        # 「当时在做什么」—— 这是作者复现问题最需要、又最容易被漏掉的信息
        meta["当时场景"] = args.context
    path, dup = write_feedback(args.type, args.title or args.type,
                               args.content, meta=meta)
    if dup:
        print(f"这条反馈之前已经记过了，跳过重复：\n  {path}")
        print("\n（内容完全相同。作者收到两条一样的反而困惑，"
              "也会看不出这个问题到底有多普遍。）")
        return 0
    print(f"已记录反馈：{path}")
    print("提示：内容已脱敏（长数字与文件路径已被替换）。"
          "若需让作者看到具体数值，请另建文件说明。")
    print(f"\n下一步：python {os.path.basename(__file__)} export   # 打包并生成邮件")
    return 0


def cmd_list(args):
    if not os.path.isdir(ROOT):
        print("还没有任何反馈。")
        return 0
    files = sorted(f for f in os.listdir(ROOT)
                   if f.endswith(".md") and f != "README.md")
    if not files:
        print("还没有任何反馈。")
        return 0
    print(f"反馈目录：{ROOT}\n")
    for f in files:
        full = os.path.join(ROOT, f)
        with open(full, encoding="utf-8") as fh:
            head = ""
            for ln in fh:
                if ln.startswith("# "):
                    head = ln[2:].strip()
                    break
        print(f"  {f}  ({os.path.getsize(full)} 字节)  {head[:60]}")
    print(f"\n共 {len(files)} 条。导出：python {os.path.basename(__file__)} export")
    return 0


def cmd_invite(args):
    """打印「邀请反馈」的标准文案。

    ★ 为什么不直接弹窗、而要模型来转述：
      SKILL.md 没有运行时监听能力，识别「使用人不满」只能靠模型读规则后判断。
      本命令不写任何文件，只负责把邀请话术统一成一段克制、不打扰的文案，
      避免模型每次自己组织语言时越写越长、变成骚扰。

    ★ 文案设计原则：一句话、非阻塞、给明确退路。
      不说「请您提出宝贵建议」这类空话，直接说清楚「要说什么、要不要说、不说也没事」。
    """
    about = sanitize(args.about) if args.about else "刚才这个问题"
    line = "─" * 58
    print(line)
    print(f"  要不要把这条意见告诉开发者？（关于：{about[:26]}）")
    print()
    print("  如果刚才的过程让你觉得别扭，可以让我记一句话发给作者。")
    print("  内容会自动脱敏，不包含你的姓名、金额和文件信息。")
    print()
    print("  回「好」我就记下来；也可以直接说你想提什么。")
    print("  不想提完全没关系，我们继续。")
    print(line)
    return 0


def _zip_all(zip_path):
    import zipfile
    files = sorted(f for f in os.listdir(ROOT) if f.endswith(".md"))
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for f in files:
            z.write(os.path.join(ROOT, f), f)
    return files


def _build_eml(to, subject, body, zip_path):
    """构造一封带附件的 .eml。零依赖（email 是标准库）。"""
    from email.message import EmailMessage
    msg = EmailMessage()
    msg["To"] = to
    msg["Subject"] = subject
    msg["From"] = to
    msg.set_content(body)
    if zip_path and os.path.exists(zip_path):
        with open(zip_path, "rb") as f:
            data = f.read()
        msg.add_attachment(data, maintype="application", subtype="zip",
                           filename=os.path.basename(zip_path))
    return msg.as_bytes()


def cmd_export(args):
    if not os.path.isdir(ROOT):
        print("还没有任何反馈。")
        return 0
    files = sorted(f for f in os.listdir(ROOT) if f.endswith(".md"))
    if not files:
        print("还没有任何反馈。")
        return 0

    cfg = load_config()
    to = args.email or cfg.get("author_email") or PLACEHOLDER_EMAIL
    os.makedirs(EXPORT_DIR, exist_ok=True)
    stamp = _stamp()
    zip_path = os.path.join(EXPORT_DIR, f"{SKILL_NAME}-反馈-{stamp}.zip")
    _zip_all(zip_path)

    subject = f"[{SKILL_NAME}] 使用反馈 {len(files)} 条 · {stamp}"
    body = (
        f"你好，\n\n"
        f"这是「{SKILL_NAME}」（v{SKILL_VERSION}）的使用反馈，共 {len(files)} 条，"
        f"详见附件 zip。\n\n"
        f"反馈已于生成前自动脱敏：文件路径与 4 位以上数字均被替换，\n"
        f"不含姓名、身份证号、保单号或具体保费金额。\n\n"
        f"如需作者复现问题，请在正文中补充：\n"
        f"  1. 当时执行的命令\n"
        f"  2. 输入文件的类型（PDF / xlsx / docx）\n"
        f"  3. 产品类型与缴费方式（如「增额寿，年交 ×5 年」）\n"
        f"  4. 期望结果 vs 实际结果\n\n"
        f"（本邮件由 scripts/feedback.py 自动生成）\n"
    )
    eml_path = os.path.join(EXPORT_DIR, f"反馈邮件-{stamp}.eml")
    with open(eml_path, "wb") as f:
        f.write(_build_eml(to, subject, body, zip_path))

    print(f"已打包 {len(files)} 条反馈：{zip_path}  ({os.path.getsize(zip_path):,} 字节)")
    print(f"已生成邮件：{eml_path}")
    if to == PLACEHOLDER_EMAIL:
        print(f"\n⚠ 收件邮箱还是占位符 {PLACEHOLDER_EMAIL}，请先在下面这个文件里改成你的邮箱：\n"
              f"    {CONFIG_PATH}\n")
    else:
        print(f"收件人：{to}")
    if not args.no_open:
        opened = open_with_default(eml_path)
        print("已尝试用系统默认邮件客户端打开；若没弹出，请手动双击上面的 .eml 文件。") if opened \
            else print("无法自动打开，请手动双击上面的 .eml 文件。")
    return 0


def cmd_clear(args):
    if not os.path.isdir(ROOT):
        print("没有可清理的反馈。")
        return 0
    files = sorted(f for f in os.listdir(ROOT) if f.endswith(".md"))
    if not files:
        print("没有可清理的反馈。")
        return 0
    if not args.yes:
        print(f"将删除 {len(files)} 条反馈（已导出的 zip 不受影响）。"
              f"确认请加 --yes。")
        return 0
    n = 0
    for f in files:
        try:
            os.remove(os.path.join(ROOT, f))
            n += 1
        except Exception as e:
            print(f"  跳过 {f}：{e}")
    print(f"已清理 {n} 条反馈。")
    return 0


def open_with_default(path):
    """用系统默认程序打开（.eml 会唤起邮件客户端）。任何异常都不外抛。"""
    try:
        if sys.platform.startswith("win"):
            os.startfile(path)  # noqa: S606
        elif sys.platform == "darwin":
            subprocess.run(["open", path], check=False)
        else:
            subprocess.run(["xdg-open", path], check=False)
        return True
    except Exception:
        return False


# ---------------------------------------------------------------- CLI
def main():
    ap = argparse.ArgumentParser(
        description="反馈收集器：记录问题与建议，打包并生成一封预填好的邮件")
    sub = ap.add_subparsers(dest="cmd")

    p1 = sub.add_parser("report", help="手动提交一条反馈")
    p1.add_argument("--type", default="建议",
                    choices=["错误", "建议", "数据问题", "其他"],
                    help="反馈类型，默认「建议」")
    p1.add_argument("--title", help="一句话标题（默认用类型名）")
    p1.add_argument("--content", required=True, help="具体描述")
    p1.add_argument("--context", help="当时在做什么（如「在给年金做压力测试」），"
                                      "帮作者复现，可选")
    p1.set_defaults(func=cmd_report)

    p5 = sub.add_parser("invite", help="打印「邀请反馈」的标准文案（不写文件）")
    p5.add_argument("--about", help="这次是关于什么（会做脱敏），可选")
    p5.set_defaults(func=cmd_invite)

    p2 = sub.add_parser("list", help="列出已收集的反馈")
    p2.set_defaults(func=cmd_list)

    p3 = sub.add_parser("export", help="打包成 zip 并生成预填好的 .eml")
    p3.add_argument("--email", help="覆盖配置里的作者收件邮箱")
    p3.add_argument("--no-open", action="store_true", help="不自动打开邮件客户端")
    p3.set_defaults(func=cmd_export)

    p4 = sub.add_parser("clear", help="清空已收集的反馈（导出后使用）")
    p4.add_argument("--yes", action="store_true", help="确认删除")
    p4.set_defaults(func=cmd_clear)

    args = ap.parse_args()
    if not getattr(args, "func", None):
        ap.print_help()
        return 0
    try:
        return args.func(args)
    except Exception as e:
        # ★ 反馈机制自身绝不抛 traceback 干扰使用者
        print(f"[反馈模块异常] {type(e).__name__}: {e}", file=sys.stderr)
        print("反馈功能未能完成，但这不影响分析本身。", file=sys.stderr)
        return 0


if __name__ == "__main__":
    sys.exit(main())
