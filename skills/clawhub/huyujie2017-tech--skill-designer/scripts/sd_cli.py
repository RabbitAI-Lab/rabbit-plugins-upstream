#!/usr/bin/env python3
"""
sd_cli.py — skill-designer 脚本统一入口

把 init_blueprint / draft_blueprint / check_blueprint / validate_skill /
export_brief / trace_patch / visualize_blueprint / b09_summary / infer_design /
deepen_blueprint / check_update
十一个脚本聚合到一个 CLI，减少记忆负担、统一路径与退出码。

用法：
    python scripts/sd_cli.py init   <蓝图目录> --name <skill名> [--channel full|light] [--entry create|improve]
    python scripts/sd_cli.py draft  <蓝图目录> --name <skill名> --answers '<JSON>'
    python scripts/sd_cli.py infer  --answers '<JSON>' [--archetype <id>] [--json]   # Step② 先看 AI 怎么设计，再决定出不出方案
    python scripts/sd_cli.py proto  <蓝图目录> --name <skill名> --answers '<JSON>' [--output <dir>] [--archetype <id>] [--force]   # 四步流 Step② 初步方案
    python scripts/sd_cli.py deepen <蓝图目录> --accept-all --set "B02.正交性=..." --tick B01,B02   # Step③ 深化设计
    python scripts/sd_cli.py deepen <蓝图目录>                                    # 只读扫描待决项，不改动
    python scripts/sd_cli.py check  <蓝图目录> [--json] [--write-iqs]
    python scripts/sd_cli.py validate <skill目录> [--json] [--fix] [--diag]
    python scripts/sd_cli.py export <蓝图目录> --output <产物目录> [--format all|md|json|sketch] [--allow-gap]
    python scripts/sd_cli.py patch  <反馈.json> --output patches.md [--threshold 4.5]
    python scripts/sd_cli.py visualize <蓝图目录> --output blueprint.svg [--mode completion|essence|dual-track] [--focus N] [--theme light|dark]
    python scripts/sd_cli.py b09-summary <蓝图目录> --output b09-summary.svg [--theme light|dark]
    python scripts/sd_cli.py structure <蓝图目录> --output structure.svg [--theme light|dark]
    python scripts/sd_cli.py session <蓝图目录> --output session.html [--theme light|dark]   # v3.10.1 合成大图聚合
    python scripts/sd_cli.py structure --archetype full --output full-example.svg
    python scripts/sd_cli.py evals   [--json]            # A 维触发证据自检
    python scripts/sd_cli.py selftest                    # C8 教训回流门槛自回归（改判据后必跑）
    python scripts/sd_cli.py package [skill目录] [--zip <包路径>]   # 打包硬门禁：validate → prepare_release(+--sync-dist) → 卫生扫描（fail-closed）；--zip 连跑包完整性校验
    python scripts/sd_cli.py update-check [--json]       # 查 SkillHub 是否有新版本（读 config.json 坐标）
    python scripts/sd_cli.py knowledge index --write     # 知识库索引（机器件）+ ID 编号空间
    python scripts/sd_cli.py knowledge search --block B07 --text 路由   # 按格/主题/标签/全文检索条目（只返 ID 与标题）
    python scripts/sd_cli.py knowledge get D-133         # 按 ID 取条目正文（从权威源实时切片，无第二份拷贝）
    python scripts/sd_cli.py knowledge verify            # 完整性核对：索引↔权威源 hash / ID 连续 / 条目库视图自洽
    python scripts/sd_cli.py knowledge stats             # 条目统计与存活度（遥测未启用时如实说明）
    python scripts/sd_cli.py knowledge selftest          # 契约层反向测试（改判据后必跑，L11）
    python scripts/sd_cli.py --self-check                # 校验 skill-designer 自身

全局选项：
    --root <路径>   skill-designer 根目录（默认：本脚本所在目录的父目录）
    --dry-run       只打印将要执行的命令，不真正运行
    --retries N     子进程环境/IO 失败时自动重试次数（默认 3）
    --backoff S     指数退避初始秒数（默认 0.5）
"""

import argparse
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path
from typing import Optional

from retry import RetryRunner


def find_root() -> Path:
    return Path(__file__).resolve().parent.parent


def script_path(root: Path, name: str) -> Path:
    return root / "scripts" / name


def add_common(ap):
    ap.add_argument("--root", default=None, help="skill-designer 根目录（默认自动推断）")
    ap.add_argument("--dry-run", action="store_true", help="只打印命令")
    ap.add_argument("--retries", type=int, default=3, help="环境/IO 失败自动重试次数（默认 3）")
    ap.add_argument("--backoff", type=float, default=0.5, help="指数退避初始秒数（默认 0.5）")


def _runner(args) -> RetryRunner:
    return RetryRunner(max_retries=args.retries, backoff=args.backoff, dry_run=args.dry_run)


def cmd_init(args) -> int:
    root = Path(args.root).resolve() if args.root else find_root()
    python = sys.executable
    cmd = [python, str(script_path(root, "init_blueprint.py")), args.target,
           "--name", args.name]
    if args.channel:
        cmd += ["--channel", args.channel]
    if args.entry:
        cmd += ["--entry", args.entry]
    if args.json:
        cmd += ["--json"]
    return _runner(args).run(cmd, cwd=root)


def cmd_draft(args) -> int:
    root = Path(args.root).resolve() if args.root else find_root()
    python = sys.executable
    cmd = [python, str(script_path(root, "draft_blueprint.py")), args.target,
           "--name", args.name, "--answers", args.answers]
    if args.json:
        cmd += ["--json"]
    return _runner(args).run(cmd, cwd=root)


def cmd_proto(args) -> int:
    root = Path(args.root).resolve() if args.root else find_root()
    python = sys.executable
    cmd = [python, str(script_path(root, "blueprint_proto.py")), args.target,
           "--name", args.name, "--answers", args.answers]
    if args.output:
        cmd += ["--output", args.output]
    if args.archetype:
        cmd += ["--archetype", args.archetype]
    # P0 修复：parser 有 --force 但此前没转发，blueprint_proto 侧永远收到 False；
    # 目录已存在时会走「跳过创建」分支并因 design_info 未初始化而 UnboundLocalError。
    if args.force:
        cmd += ["--force"]
    if args.json:
        cmd += ["--json"]
    return _runner(args).run(cmd, cwd=root)


def cmd_check(args) -> int:
    root = Path(args.root).resolve() if args.root else find_root()
    python = sys.executable
    cmd = [python, str(script_path(root, "check_blueprint.py")), args.target]
    if args.json:
        cmd += ["--json"]
    if args.write_iqs:
        cmd += ["--write-iqs"]
    if getattr(args, "tick_lesson", ""):
        cmd += ["--tick-lesson", args.tick_lesson]
    return _runner(args).run(cmd, cwd=root)


def cmd_validate(args) -> int:
    root = Path(args.root).resolve() if args.root else find_root()
    python = sys.executable
    target = "--self" if args.self_check else args.target
    cmd = [python, str(script_path(root, "validate_skill.py")), target]
    for flag in ("--json", "--fix", "--diag"):
        if getattr(args, flag.lstrip("-").replace("-", "_")):
            cmd.append(flag)
    return _runner(args).run(cmd, cwd=root)


def cmd_export(args) -> int:
    root = Path(args.root).resolve() if args.root else find_root()
    python = sys.executable
    cmd = [python, str(script_path(root, "export_brief.py")), args.target,
           "--format", args.format]
    if args.output:
        cmd += ["--output", args.output]
    if args.stdout:
        cmd.append("--stdout")
    # B08「真实场景跑过」必须等 skill 落地才有，硬等 10/10 会让④永远导不出来
    if args.allow_gap:
        cmd.append("--allow-gap")
        if args.min_iqs is not None:
            cmd += ["--min-iqs", str(args.min_iqs)]
    return _runner(args).run(cmd, cwd=root)


def cmd_deepen(args) -> int:
    """③深化设计：批量采纳 AI 建议 / 定向拍板 / 勾验收 checklist。"""
    root = Path(args.root).resolve() if args.root else find_root()
    python = sys.executable
    cmd = [python, str(script_path(root, "deepen_blueprint.py")), args.target]
    if args.accept_all:
        cmd.append("--accept-all")
    if args.accept:
        cmd += ["--accept", args.accept]
    for s in (args.set or []):
        cmd += ["--set", s]
    if args.tick:
        cmd += ["--tick", args.tick]
    if args.json:
        cmd.append("--json")
    return _runner(args).run(cmd, cwd=root)


def cmd_update_check(args) -> int:
    """检查 SkillHub 上是否有新版本（官方无 CLI 可消费的清单端点，走自研脚本）。"""
    root = Path(args.root).resolve() if args.root else find_root()
    python = sys.executable
    cmd = [python, str(script_path(root, "check_update.py"))]
    if args.json:
        cmd.append("--json")
    return _runner(args).run(cmd, cwd=root)


def cmd_patch(args) -> int:
    root = Path(args.root).resolve() if args.root else find_root()
    python = sys.executable
    cmd = [python, str(script_path(root, "trace_patch.py")), args.feedback]
    if args.output:
        cmd += ["--output", args.output]
    if args.threshold is not None:
        cmd += ["--threshold", str(args.threshold)]
    return _runner(args).run(cmd, cwd=root)


def cmd_visualize(args) -> int:
    root = Path(args.root).resolve() if args.root else find_root()
    python = sys.executable
    cmd = [python, str(script_path(root, "visualize_blueprint.py")), args.target]
    if args.output:
        cmd += ["--output", args.output]
    if args.theme:
        cmd += ["--theme", args.theme]
    # P1 修复：统一入口此前漏了 --mode，出不了 Step② 要的 essence 总览图
    if args.mode:
        cmd += ["--mode", args.mode]
    # v3.10.1：dual-track 模式的当前选中格索引
    if args.focus is not None and getattr(args, "mode", "") == "dual-track":
        cmd += ["--focus", str(args.focus)]
    return _runner(args).run(cmd, cwd=root)


def cmd_evals(args) -> int:
    """A 维（触发可辨）的机器可验证证据：跑 scripts/evals.json 里的真实说法用例。

    为什么放进统一入口：证据必须"随手可跑"才叫证据——藏在一个冷门脚本里没人跑，
    等于没有。发布前 `sd_cli package` 与回归套件都会调它。
    """
    root = Path(args.root).resolve() if args.root else find_root()
    python = sys.executable
    cmd = [python, str(script_path(root, "run_evals.py")), str(root)]
    if args.json:
        cmd += ["--json"]
    return _runner(args).run(cmd, cwd=root)


def cmd_infer(args) -> int:
    """②初步方案的推断引擎：先看 AI 打算怎么设计，再决定要不要出方案。"""
    root = Path(args.root).resolve() if args.root else find_root()
    python = sys.executable
    cmd = [python, str(script_path(root, "infer_design.py")), "--answers", args.answers]
    if args.archetype:
        cmd += ["--archetype", args.archetype]
    if args.json:
        cmd += ["--json"]
    return _runner(args).run(cmd, cwd=root)


def cmd_b09_summary(args) -> int:
    root = Path(args.root).resolve() if args.root else find_root()
    python = sys.executable
    cmd = [python, str(script_path(root, "b09_summary.py")), args.target]
    if args.json:
        cmd += ["--json"]
    if args.output:
        cmd += ["--output", args.output]
    if args.theme:
        cmd += ["--theme", args.theme]
    return _runner(args).run(cmd, cwd=root)


def cmd_session(args) -> int:
    """v3.10.1：合成大图聚合入口——调三件套产出同屏 HTML（综合分 + BR-5 + 结构 + 评分 + 行动按钮）。

    数据流：visual_session.py 直接 import 三件套的数据收集函数，单次解析出全部数据。
    """
    root = Path(args.root).resolve() if args.root else find_root()
    python = sys.executable
    cmd = [python, str(script_path(root, "visual_session.py")), args.target]
    if args.output:
        cmd += ["--output", args.output]
    if args.theme:
        cmd += ["--theme", args.theme]
    if args.focus is not None:
        cmd += ["--focus", str(args.focus)]
    if args.json:
        cmd += ["--json"]
    return _runner(args).run(cmd, cwd=root)


def cmd_structure(args) -> int:
    root = Path(args.root).resolve() if args.root else find_root()
    python = sys.executable
    cmd = [python, str(script_path(root, "render_structure.py"))]
    if args.target:
        cmd.append(args.target)
    if args.output:
        cmd += ["--output", args.output]
    if args.archetype:
        cmd += ["--archetype", args.archetype]
    if args.format:
        cmd += ["--format", args.format]
    if args.theme:
        cmd += ["--theme", args.theme]
    if args.list:
        cmd.append("--list")
    if args.json:
        cmd.append("--json")
    return _runner(args).run(cmd, cwd=root)


# 打包违禁品清单（P2-9，A-006 收尾）：skillhub publish 对二进制文件直接拒收，
# __pycache__/*.pyc 夹带是真实事故（v2.20.8 前 dist 曾混入 export_brief 的 pyc）。
_BANNED_DIR_NAMES = {"__pycache__"}
_BANNED_EXTS = {".pyc", ".pyo", ".bak"}


def _hygiene_scan(scan_root: Path):
    """产物卫生扫描：返回违禁产物路径列表（目录带尾斜杠）。"""
    offenders = []
    if not scan_root.exists():
        return offenders
    for p in sorted(scan_root.rglob("*")):
        if p.is_dir() and p.name in _BANNED_DIR_NAMES:
            offenders.append(str(p) + "/")
        elif p.is_file() and p.suffix.lower() in _BANNED_EXTS:
            offenders.append(str(p))
    return offenders


# ── D-131 发布包完整性校验（v3.15.0 移植自姊妹分支 v4.4.0）──────────────
ARCHIVE_EXCLUDE = {"__pycache__", ".git", ".DS_Store", "node_modules"}


def build_archive(src: Path, zip_path: Path) -> int:
    """把 src 打成 zip。**保留顶层目录名**——否则解包后目录名与 frontmatter `name`
    对不上，第 ② 查的 validate 会被 name/目录一致性误判（不是真缺陷）。"""
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    n = 0
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(src.rglob("*")):
            if any(part in ARCHIVE_EXCLUDE for part in p.parts):
                continue
            if p.is_file():
                z.write(p, Path(src.name) / p.relative_to(src))
                n += 1
    return n


def cmd_selftest(args) -> int:
    """C8 教训回流门槛自回归（v3.15.0）。

    背景即动机：姊妹分支 C8 上线时"实现完毕"，实则被三个缺陷同时废掉（错误 gate /
    泛词判据 / 同行口径），一次警都没报过。此类缺陷唯有**样例回归**能拦——故把修复时的
    验收样本固化成一条必然可跑的命令，改动判据后跑它，全绿才算没退化（教训见 lessons L11）。
    """
    python = sys.executable
    root = Path(args.root).resolve() if args.root else find_root()
    return subprocess.call([python, str(script_path(root, "check_blueprint.py")), "--self-test"])


def cmd_package(args) -> int:
    """package 子命令（P2-9）：打包硬门禁，三段 fail-closed（加 --zip 则四段）——

      ① validate 硬门禁：不过即拦截（退出码 2），杜绝「带病打包」；
      ② prepare_release（仅 skill-designer 自身）：重生成 dist 发布版 SKILL.md **+ 同步源目录**；
      ③ 产物卫生扫描：dist/目标目录含 __pycache__/*.pyc/*.bak 即拦截（退出码 3）；
      ④ （可选）发布包完整性校验：打 zip → testzip → 解包重跑 validate → 解包卫生扫描，
         失败退出码 4。**验产物不验源**（D-131）。

    全部通过（退出码 0）才允许进入 skillhub publish 流程。
    """
    root = Path(args.root).resolve() if args.root else find_root()
    python = sys.executable
    target = Path(args.target).resolve() if args.target else root
    is_self = target == root

    # ① validate 硬门禁
    val_cmd = [python, str(script_path(root, "validate_skill.py"))]
    val_cmd += ["--self"] if is_self else [str(target)]
    print(f"[package 1/3] validate 硬门禁：{' '.join(val_cmd[2:])}")
    rc = _runner(args).run(val_cmd, cwd=root)
    if rc != 0:
        print(f"[package] ❌ 打包拦截：validate 未通过（退出码 {rc}）——fail-closed，不进入打包")
        return 2

    # ② prepare_release（发布版 frontmatter 转换，只服务 skill-designer 自身）
    if is_self:
        # v3.15.0：补 --sync-dist。原因：此前只重生成 SKILL.md，不同步 references/scripts，
        # 导致「门禁全绿但 dist 内容仍停留在上个版本」的假绿——姊妹分支 v4.4.0 发布时就撞上：
        # dist SKILL.md 已标 4.4.0，包内 references 却还是旧版。
        # 这正踩中自家 D-131「验产物不验源」：门禁验的是源，发布用的是包。
        prep_cmd = [python, str(script_path(root, "prepare_release.py")), "--sync-dist"]
        print("[package 2/3] prepare_release：重生成 dist 发布版 SKILL.md + 同步源目录（--sync-dist）")
        rc = _runner(args).run(prep_cmd, cwd=root)
        if rc != 0:
            print("[package] ❌ prepare_release 失败——fail-closed")
            return 2
    else:
        print("[package 2/3] 非 skill-designer 自身目录，跳过 prepare_release（它只服务自身发布）")

    # ③ 产物卫生扫描
    scan_root = (root / "dist" / "skill-designer") if is_self else target
    print(f"[package 3/3] 产物卫生扫描：{scan_root}")
    offenders = _hygiene_scan(scan_root)
    if offenders:
        print(f"[package] ❌ 卫生扫描拦截（fail-closed）：{len(offenders)} 项违禁产物：")
        for o in offenders[:20]:
            print(f"  - {o}")
        if len(offenders) > 20:
            print(f"  - …共 {len(offenders)} 项")
        print("  处置：删除 __pycache__ 与 *.pyc/*.bak 后重跑 package（skillhub publish 拒收二进制）")
        return 3

    # ④ 发布包完整性校验（D-131）：**验产物，不验源**
    if getattr(args, "zip", ""):
        zip_path = Path(args.zip).resolve()
        n_files = build_archive(scan_root, zip_path)
        print(f"[package 4/4] 发布包完整性校验（D-131 三查）：{zip_path}（{n_files} 个文件）")
        with zipfile.ZipFile(zip_path) as z:
            bad = z.testzip()
        if bad:
            print(f"[package] ❌ ① 包损坏，首个损坏文件：{bad}")
            return 4
        print("  ✅ ① testzip()：包完整，无损坏条目")
        tmp = Path(tempfile.mkdtemp(prefix="sd_verify_"))
        try:
            with zipfile.ZipFile(zip_path) as z:
                z.extractall(tmp)
            cands = [d for d in (tmp, *tmp.iterdir()) if (d / "SKILL.md").is_file()]
            if not cands:
                print("[package] ❌ ② 解包后未找到 SKILL.md——打包内容不完整")
                return 4
            skill_dir = cands[0]
            rc = _runner(args).run(
                [python, str(script_path(root, "validate_skill.py")), str(skill_dir)], cwd=root)
            if rc != 0:
                print(f"[package] ❌ ② 解包后重跑 validate 未通过（退出码 {rc}）——产物与源不一致或漏文件")
                return 4
            print("  ✅ ② 解包后重跑 validate：通过（产物即源，无漏文件）")
            off2 = _hygiene_scan(skill_dir)
            if off2:
                print(f"[package] ❌ ③ 解包后卫生扫描：{len(off2)} 项违禁产物（打包过程引入）")
                for o in off2[:10]:
                    print(f"  - {o}")
                return 4
            print("  ✅ ③ 解包后卫生扫描：无 __pycache__ / *.pyc / *.bak")
        finally:
            shutil.rmtree(tmp, ignore_errors=True)  # 沙箱可能拦截安全删除，忽略即可
        print("[package] ✅ 门禁四段全过（validate / prepare_release / 卫生扫描 / 包完整性）"
              "——可进入 publish；同版本重发前记得 bump version")
        return 0

    print("[package] ✅ 门禁三段全过（validate / prepare_release / 卫生扫描）——可进入 publish；"
          "加 --zip <路径> 可连跑第④段 D-131 发布包完整性校验；同版本重发前记得 bump version")
    return 0


def cmd_self_check(args) -> int:
    """sd --self-check：跑 validate_skill.py --self。"""
    args.self_check = True
    args.target = ""
    args.json = False
    args.fix = False
    args.diag = False
    # 顶层调用（不经过 validate 子解析器）时补齐缺失属性
    for attr, val in (("root", None), ("dry_run", False), ("retries", 3), ("backoff", 0.5)):
        if not hasattr(args, attr):
            setattr(args, attr, val)
    return cmd_validate(args)


def cmd_knowledge(args) -> int:
    """knowledge：知识库统一门面（ADR-001 阶段0 · 契约层）。

    转发给 knowledge.py（与其余 22 个脚本一致，由 sd_cli 统一路径/退出码/重试），
    不做二次实现——knowledge.py 是知识接口的唯一事实源（DP-209）。
    """
    root = Path(args.root).resolve() if args.root else find_root()
    cmd = [sys.executable, str(script_path(root, "knowledge.py")), args.knowledge_action]
    if args.knowledge_action == "index":
        if getattr(args, "write", False):
            cmd.append("--write")
        if getattr(args, "compact", False):
            cmd.append("--compact")
        if getattr(args, "out", ""):
            cmd += ["--out", args.out]
        if getattr(args, "json", False):
            cmd.append("--json")
    elif args.knowledge_action == "get":
        cmd.append(args.eid)
        if getattr(args, "format", ""):
            cmd += ["--format", args.format]
    elif args.knowledge_action == "search":
        for flag in ("block", "theme", "tag", "text"):
            v = getattr(args, flag, "")
            if v:
                cmd += [f"--{flag}", v]
        if getattr(args, "limit", None) is not None:
            cmd += ["--limit", str(args.limit)]
        if getattr(args, "ids_only", False):
            cmd.append("--ids-only")
        if getattr(args, "json", False):
            cmd.append("--json")
    elif args.knowledge_action == "verify":
        if getattr(args, "strict", False):
            cmd.append("--strict")
        if getattr(args, "json", False):
            cmd.append("--json")
    elif args.knowledge_action == "stats":
        cmd += ["--dead-after", str(getattr(args, "dead_after", 10))]
        if getattr(args, "tiers", False):
            cmd.append("--tiers")
        if getattr(args, "json", False):
            cmd.append("--json")
    elif args.knowledge_action == "selftest":
        if getattr(args, "json", False):
            cmd.append("--json")
    # --backend（阶段1 · 远程增强服务衔接位）：local（默认）/ remote / auto
    be = getattr(args, "backend", "")
    if be:
        cmd += ["--backend", be]
    return _runner(args).run(cmd, cwd=root)


def main() -> int:
    # Windows 控制台/管道统一 UTF-8，避免向 pipe 输出中文时按 GBK 编码导致下游解码崩溃
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    ap = argparse.ArgumentParser(
        description="skill-designer 统一 CLI（含自动重试：环境/IO 类失败默认重试 3 次）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="示例：\n  python scripts/sd_cli.py init ./bp/my-skill --name my-skill\n"
               "  python scripts/sd_cli.py check ./bp/my-skill\n"
               "  python scripts/sd_cli.py export ./bp/my-skill --format all\n"
               "  python scripts/sd_cli.py validate --self --retries 2 --backoff 1.0"
    )
    add_common(ap)
    ap.add_argument("--self-check", dest="self_check", action="store_true",
                    help="校验 skill-designer 自身（等价于 validate --self）")
    sub = ap.add_subparsers(dest="command", required=False)

    # init
    p_init = sub.add_parser("init", help="生成蓝图骨架（init_blueprint.py）")
    add_common(p_init)
    p_init.add_argument("target", help="目标蓝图目录")
    p_init.add_argument("--name", required=True, help="skill 名称")
    p_init.add_argument("--channel", choices=("light", "full"), help="轻量/完整通道")
    p_init.add_argument("--entry", choices=("create", "improve"), help="创建/改进入口")
    p_init.add_argument("--json", action="store_true", help="JSON 输出")

    # draft
    p_draft = sub.add_parser("draft", help="生成我拟草稿（draft_blueprint.py）")
    add_common(p_draft)
    p_draft.add_argument("target", help="目标蓝图目录")
    p_draft.add_argument("--name", required=True, help="skill 名称")
    p_draft.add_argument("--answers", required=True,
                         help='Phase 0 答案 JSON，如 {"problem":"...","scenario":"..."}')
    p_draft.add_argument("--json", action="store_true", help="JSON 输出")

    # proto（四步流 Step② 初步方案）
    p_proto = sub.add_parser("proto", help="四步流 Step② 初步方案：一键出有主张的设计稿（blueprint_proto.py）")
    add_common(p_proto)
    p_proto.add_argument("target", help="目标蓝图目录")
    p_proto.add_argument("--name", required=True, help="skill 名称")
    p_proto.add_argument("--answers", required=True,
                         help='概念讨论最低标准 JSON：{"problem":..,"audience":..,"platform":..,"entry":..,"priority":..,"flow":..,"example":..}')
    p_proto.add_argument("--output", "-o", help="可视化产物输出目录（默认=蓝图目录）")
    p_proto.add_argument("--archetype", "-a", help="结构框架 id（不给则由 infer_design 自动推断）")
    p_proto.add_argument("--force", action="store_true", help="目标目录非空时先备份再重建（默认跳过创建只出图）")
    p_proto.add_argument("--json", action="store_true", help="JSON 输出（stdout 纯净，便于机器解析）")

    # infer（②初步方案的推断引擎，可单独先跑）
    p_infer = sub.add_parser("infer", help="推断设计模式与结构框架（infer_design.py），出方案前先看 AI 怎么想")
    add_common(p_infer)
    p_infer.add_argument("--answers", required=True,
                         help='概念讨论 JSON 或文件路径：{"problem":..,"audience":..,"priority":..,"flow":..,"example":..}')
    p_infer.add_argument("--archetype", "-a",
                         choices=("minimal", "pipeline", "tool", "knowledge", "template", "full", "suite"),
                         help="显式指定结构框架（覆盖推断）")
    p_infer.add_argument("--json", action="store_true", help="输出完整推断 JSON")

    # check
    p_check = sub.add_parser("check", help="蓝图完成度检查（check_blueprint.py）")
    add_common(p_check)
    p_check.add_argument("target", help="蓝图目录")
    p_check.add_argument("--json", action="store_true", help="JSON 输出")
    p_check.add_argument("--write-iqs", action="store_true",
                         help="把机器算出的 IQS 蓝图完备度回填进 09-结果.md")
    p_check.add_argument("--tick-lesson", default="",
                         help="F6 机器钩子：本任务实际用到的经验规则 ID（逗号分隔，如 L01,L03），"
                              "写回 references/lessons.md 引用计数")

    # validate
    p_val = sub.add_parser("validate", help="skill 静态验证（validate_skill.py）")
    add_common(p_val)
    p_val.add_argument("target", nargs="?", default="", help="skill 目录（--self 时省略）")
    p_val.add_argument("--self", dest="self_check", action="store_true", help="验证 skill-designer 自身")
    p_val.add_argument("--json", action="store_true", help="JSON 输出")
    p_val.add_argument("--fix", action="store_true", help="自动修复可修复项")
    p_val.add_argument("--diag", action="store_true", help="软性项诊断")

    # export
    p_exp = sub.add_parser("export", help="导出交接产物（export_brief.py）")
    add_common(p_exp)
    p_exp.add_argument("target", help="蓝图目录")
    p_exp.add_argument("--output", "-o", help="产物输出目录（默认：蓝图目录/brief/）")
    p_exp.add_argument("--format", choices=("all", "md", "json", "sketch"), default="all", help="产物格式")
    p_exp.add_argument("--stdout", action="store_true", help="仅 --format json 时输出到 stdout")
    p_exp.add_argument("--allow-gap", dest="allow_gap", action="store_true",
                       help="IQS ≥ --min-iqs 时允许带缺口导出（B08 实证项需 skill 落地后才有）")
    p_exp.add_argument("--min-iqs", dest="min_iqs", type=int, default=None,
                       help="--allow-gap 的放行阈值（默认 90）")

    # deepen（③深化设计）
    p_dep = sub.add_parser("deepen", help="③深化设计：批量采纳 AI 建议 / 定向拍板 / 勾验收（deepen_blueprint.py）")
    add_common(p_dep)
    p_dep.add_argument("target", help="蓝图目录")
    p_dep.add_argument("--accept-all", dest="accept_all", action="store_true",
                       help="采纳全部格的【AI 建议】（等价于用户回「按建议」）")
    p_dep.add_argument("--accept", help="只采纳指定格，逗号分隔（如 B01,B03）")
    p_dep.add_argument("--set", action="append", default=[], metavar="B02.字段=值",
                       help='给【需用户拍板】/【待回填】字段定向赋值，可重复，如 --set "B02.正交性=..."')
    p_dep.add_argument("--tick", help="勾验收 checklist 的指定格，逗号分隔（如 B01,B02）")
    p_dep.add_argument("--json", action="store_true", help="JSON 输出")

    # patch
    p_patch = sub.add_parser("patch", help="外部平台返评补丁清单（trace_patch.py）")
    add_common(p_patch)
    p_patch.add_argument("feedback", help="反馈 JSON 文件路径或 JSON 字符串")
    p_patch.add_argument("--output", "-o", help="输出文件路径（默认 stdout）")
    p_patch.add_argument("--threshold", type=float, default=None, help="低于此分数视为需修复（默认 4.5）")

    # visualize
    p_vis = sub.add_parser("visualize", help="生成蓝图可视化 SVG（visualize_blueprint.py）")
    p_evals = sub.add_parser("evals", help="A 维触发证据：跑 evals.json 真实说法用例（run_evals.py）")
    add_common(p_evals)
    p_evals.add_argument("--json", action="store_true", help="输出 JSON 而非人类可读报告")
    add_common(p_vis)
    p_vis.add_argument("target", help="蓝图目录")
    p_vis.add_argument("--output", "-o", help="输出 SVG 文件路径")
    p_vis.add_argument("--theme", choices=("light", "dark"), default="light", help="主题")
    p_vis.add_argument("--mode", choices=("completion", "essence", "dual-track"), default=None,
                       help="completion=10 格完成度进度图（默认）｜essence=内容要点总览图（②初步方案用）｜dual-track=双轨进度图（左轨完成度 + 右轨当前格实质内容）")
    p_vis.add_argument("--focus", type=int, default=2,
                       help="dual-track 模式当前选中格索引（0-based，默认 2=B03 观点）")

    # b09-summary
    p_b09 = sub.add_parser("b09-summary", help="生成 B09 结果摘要图（b09_summary.py）")
    add_common(p_b09)
    p_b09.add_argument("target", help="蓝图目录")
    p_b09.add_argument("--json", action="store_true", help="输出结构化 JSON 摘要（含各分数来源）")
    p_b09.add_argument("--output", "-o", help="输出 SVG 文件路径")
    p_b09.add_argument("--theme", choices=("light", "dark"), default="light", help="主题")

    # structure
    p_st = sub.add_parser("structure", help="生成文件结构图 SVG（render_structure.py）")
    add_common(p_st)
    p_st.add_argument("target", nargs="?", default="", help="蓝图目录（省略则只出空白框架范例）")
    p_st.add_argument("--output", "-o", help="输出文件路径")
    p_st.add_argument("--archetype", "-a",
                      help="结构框架 id（minimal/pipeline/tool/knowledge/template/full/suite）")
    p_st.add_argument("--format", "-f", choices=("svg", "md", "all"), default="svg", help="输出格式")
    p_st.add_argument("--theme", choices=("light", "dark"), default="light", help="主题")
    p_st.add_argument("--list", action="store_true", help="列出所有结构框架")
    p_st.add_argument("--json", action="store_true", help="JSON 输出")

    # package（P2-9 打包硬门禁）
    p_pkg = sub.add_parser("package", help="打包硬门禁：validate → prepare_release(+--sync-dist) → 卫生扫描（fail-closed）；加 --zip 连跑包完整性校验")
    add_common(p_pkg)
    p_pkg.add_argument("target", nargs="?", default="", help="skill 目录（默认 skill-designer 自身）")
    p_pkg.add_argument("--zip", default="", metavar="路径",
                       help="额外执行第④段「发布包完整性校验」（D-131）：打 zip → testzip() → 解包重跑 validate → 解包卫生扫描。"
                            "失败退出码 4。")

    # selftest（v3.15.0）：C8 教训回流门槛自回归——改判据后必跑，防止"功能实现却从未生效"
    p_selftest = sub.add_parser("selftest", help="C8 教训回流门槛自回归（内置 6 档样例 + 回流提取）")
    add_common(p_selftest)

    # session（v3.10.1 合成大图聚合入口）
    p_ses = sub.add_parser("session", help="合成大图：调三件套产出同屏 HTML（综合分 + BR-5 + 结构 + 评分 + 行动按钮）")
    add_common(p_ses)
    p_ses.add_argument("target", help="蓝图目录")
    p_ses.add_argument("--output", "-o", help="输出 HTML 文件路径")
    p_ses.add_argument("--theme", choices=("light", "dark"), default="light", help="主题")
    p_ses.add_argument("--focus", type=int, default=2, help="10 格进度高亮索引（0-based，默认 2=B03）")
    p_ses.add_argument("--json", action="store_true", help="输出结构化 JSON 摘要，不生成 HTML")

    # update-check（SkillHub 版本检查；官方无 CLI 可消费的清单端点，故自研）
    p_up = sub.add_parser("update-check", help="检查 SkillHub 上是否有新版本（check_update.py）")
    add_common(p_up)
    p_up.add_argument("--json", action="store_true", help="机器可消费输出")

    # knowledge（ADR-001 阶段0）：知识库统一门面——ID/Manifest/检索/完整性 四件契约
    p_kn = sub.add_parser("knowledge", help="知识库统一门面：index/get/search/verify/stats（knowledge.py）")
    add_common(p_kn)
    kn = p_kn.add_subparsers(dest="knowledge_action", required=True)

    def _add_backend(pp):
        """给需要切后端的动作统一挂 --backend（阶段1 预留 · 远程增强服务衔接位）。"""
        pp.add_argument("--backend", choices=("local", "remote", "auto"), default="",
                        help="知识后端：local（默认，离线完备）/ remote（远程增强）/ auto（远程优先+本地兜底）")

    k = kn.add_parser("index", help="重建条目粒度索引（含 ID 编号空间）")
    k.add_argument("--write", action="store_true", help="写入 scripts/library_manifest.json（机器件）")
    k.add_argument("--compact", action="store_true", help="输出紧凑索引（上下文件）")
    k.add_argument("--out", default="", help="紧凑索引落盘路径（一般不必）")
    k.add_argument("--json", action="store_true")
    _add_backend(k)
    k = kn.add_parser("get", help="按 ID 取条目正文（从权威源实时切片）")
    k.add_argument("eid", help="条目 ID：D-133 / DP-209 / L12")
    k.add_argument("--format", choices=("md", "json"), default="md")
    _add_backend(k)
    k = kn.add_parser("search", help="检索条目（只返轻量元数据，不返正文）")
    k.add_argument("--block", default="", help="按积木格，如 B07")
    k.add_argument("--theme", default="", help="按主题，如 T4")
    k.add_argument("--tag", default="", help="按标签（子串）")
    k.add_argument("--text", default="", help="全文关键词（空格=AND）")
    k.add_argument("--limit", type=int, default=5, help="最多返回条数")
    k.add_argument("--ids-only", action="store_true", help="机器消费：只输出 ID")
    k.add_argument("--json", action="store_true")
    _add_backend(k)
    k = kn.add_parser("verify", help="完整性核对：索引↔权威源 / ID 编号 / 条目库视图一致性")
    k.add_argument("--strict", action="store_true", help="警告升级为失败")
    k.add_argument("--json", action="store_true")
    _add_backend(k)
    k = kn.add_parser("stats", help="知识库统计与存活度")
    k.add_argument("--dead-after", type=int, default=10, dest="dead_after")
    k.add_argument("--tiers", action="store_true", help="显示免费/付费分层策略")
    k.add_argument("--json", action="store_true")
    k = kn.add_parser("selftest", help="契约层反向测试：5 种坏样本是否被分别拦住（改判据后必跑）")
    k.add_argument("--json", action="store_true")

    args = ap.parse_args()

    # 顶层 --self-check（不带子命令）
    if not args.command:
        if getattr(args, "self_check", False):
            return cmd_self_check(args)
        ap.print_help()
        return 1

    handlers = {
        "init": cmd_init,
        "draft": cmd_draft,
        "proto": cmd_proto,
        "deepen": cmd_deepen,
        "infer": cmd_infer,
        "check": cmd_check,
        "validate": cmd_validate,
        "export": cmd_export,
        "patch": cmd_patch,
        "visualize": cmd_visualize,
        "b09-summary": cmd_b09_summary,
        "structure": cmd_structure,
        "session": cmd_session,
        "evals": cmd_evals,
        "selftest": cmd_selftest,
        "package": cmd_package,
        "update-check": cmd_update_check,
        "knowledge": cmd_knowledge,
    }
    return handlers[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
