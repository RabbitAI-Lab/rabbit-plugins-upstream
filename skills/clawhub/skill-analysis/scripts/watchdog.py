#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Skill Watchdog —— 跨平台 Skill 自动扫描与变动监控。

功能：
  1. 首次运行 `--check`：全量扫描全部已安装 Skill 目录，输出安全体检报告并建档。
  2. 后续每日运行 `--check`：仅扫描新安装或版本更新后的 Skill（跳过无变化的 Skill）。
  3. 安装新 Skill 后运行 `--check <path>`：只扫描该 Skill（启用前静默扫描）。
  4. `--daemon` 模式（可选）：按每日间隔轮询，自动增量重扫。

跨平台支持（自动发现 Skill 目录）：
  - WorkBuddy   : ~/.workbuddy/skills/
  - Claude Code : ~/.claude/skills/、CLAUDE.md、AGENTS.md
  - OpenClaw    : ~/.claw/skills/、~/.claw/config/
  - Cursor      : .cursorrules、.cursor/config/

状态文件：~/.workbuddy/skills/skill-analysis/state/watchdog.json
  - 记录每个已知 Skill 的最后审查状态（路径/名称/评分/扫描时间/文件哈希/信号快照）
  - v2.5.0：记录 signals 信号快照，版本更新后比对「新增的高危信号」→ UPDATE_POISONING 告警
    （防更新投毒：首次安装良性、更新后悄悄加入窃密/外传逻辑的延迟武器化手法）
  - 状态文件设计为机器可读，不包含自然语言指令，防日志投毒

用法：
  python watchdog.py                          # 自动扫描全部已知目录
  python watchdog.py --check                  # 同上
  python watchdog.py --check <path>           # 只扫描指定 Skill
  python watchdog.py --daemon [--interval 3600] # 后台轮询（秒）
  python watchdog.py --report                 # 输出最近状态报告
  python watchdog.py --platform               # 列出检测到的平台与目录
"""

import argparse
import datetime
import hashlib
import json
import os
import sys
import time
from pathlib import Path

# 确保同目录的 analyze_skill 可导入
SCRIPT_DIR = Path(os.path.abspath(__file__)).parent
sys.path.insert(0, str(SCRIPT_DIR))

from logger import ScanLogger, LOG_ROOT as LOG_DIR


# ── 状态文件 ────────────────────────────────────────────────
STATE_DIR = Path(os.path.expanduser("~")) / ".workbuddy" / "skills" / "skill-analysis" / "state"
STATE_FILE = STATE_DIR / "watchdog.json"


def load_state() -> dict:
    """加载已知 Skill 状态。"""
    if STATE_FILE.exists():
        try:
            return json.loads(open(STATE_FILE, encoding="utf-8").read())
        except Exception:
            pass
    return {"skills": {}, "last_full_scan": ""}


def save_state(state: dict):
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


def file_hash(path: Path) -> str:
    """快速文件哈希（SHA256，仅读前 64KB 用于性能）。"""
    try:
        h = hashlib.sha256()
        with open(path, "rb") as f:
            h.update(f.read(65536))
        return f"SHA256:{h.hexdigest()[:16]}"
    except Exception:
        return "ERROR"


def dir_fingerprint(directory: Path) -> str:
    """目录指纹：文件名列表 + 关键文件的哈希。"""
    if not directory.is_dir():
        return ""
    parts = []
    for f in sorted(directory.rglob("*")):
        if f.is_file() and f.suffix.lower() in (".md", ".py", ".sh", ".json", ".yaml", ".yml",
                                                  ".txt", ".js", ".ts", ".toml", ".cfg"):
            parts.append(f"{f.relative_to(directory)}:{file_hash(f)}")
    return "|".join(parts)


def discover_platforms() -> dict:
    """自动发现跨平台 Skill 目录。
    返回 {platform_name: [skill_dir_paths]}
    """
    home = Path(os.path.expanduser("~"))
    platforms = {}

    # WorkBuddy
    wb = home / ".workbuddy"
    if wb.exists():
        paths = []
        skills_d = wb / "skills"
        if skills_d.is_dir():
            paths.append(str(skills_d))
        if paths:
            platforms["WorkBuddy"] = paths

    # Claude Code
    cl = home / ".claude"
    if cl.exists():
        paths = []
        skills_d = cl / "skills"
        if skills_d.is_dir():
            paths.append(str(skills_d))
        for f in (cl / "CLAUDE.md", cl / "AGENTS.md", cl / "CLAUDE.local.md"):
            if f.is_file():
                paths.append(str(f))
        if paths:
            platforms["Claude Code"] = paths

    # OpenClaw
    claw = home / ".claw"
    if claw.exists():
        paths = []
        for d in (claw / "skills", claw / "config"):
            if d.is_dir():
                paths.append(str(d))
        if paths:
            platforms["OpenClaw"] = paths

    # Cursor
    if (home / ".cursor").exists():
        paths = []
        for pattern in ["**/*.cursorrules", "**/.cursorrules"]:
            for f in home.rglob(pattern):
                if ".workbuddy" not in str(f) and ".cursor" in str(f.parent):
                    paths.append(str(f))
                    break
        if paths:
            platforms["Cursor"] = paths[:5]  # 限制数量

    return platforms


def find_skills(base_dir: str) -> list:
    """在给定目录中找到所有可扫描的 Skill（含 SKILL.md 或独立脚本）。"""
    base = Path(base_dir)
    skills = []
    if base.is_file():
        if base.suffix.lower() in (".md", ".py", ".sh", ".json"):
            skills.append(str(base))
    elif base.is_dir():
        # 含 SKILL.md 子目录
        for sm in base.rglob("SKILL.md"):
            skills.append(str(sm.parent))
        # 独立 SKILL.md
        if (base / "SKILL.md").is_file():
            if str(base) not in skills:
                skills.append(str(base))
    return sorted(set(skills))


def detect_changes(known: dict, platforms: dict) -> dict:
    """检测新增/修改/删除的 Skill。"""
    changes = {"added": [], "modified": [], "removed": [], "same": []}
    current = {}  # slug_or_name → {path, fingerprint}

    for platform, dirs in platforms.items():
        for d in dirs:
            for skill_path in find_skills(d):
                slug = _slug(skill_path)
                fp = dir_fingerprint(Path(skill_path)) if Path(skill_path).is_dir() else file_hash(Path(skill_path))
                current[slug] = {"path": skill_path, "fingerprint": fp, "platform": platform}

    known_skills = known.get("skills", {})

    # 新增/修改
    for slug, info in current.items():
        if slug not in known_skills:
            changes["added"].append(info)
        elif known_skills[slug].get("fingerprint") != info["fingerprint"]:
            changes["modified"].append(info)
        else:
            changes["same"].append(info)

    # 删除
    for slug in known_skills:
        if slug not in current:
            changes["removed"].append({"slug": slug, "path": known_skills[slug].get("path", slug)})

    return changes


def _slug(skill_path: str) -> str:
    """从 Skill 路径生成稳定标识符。"""
    return Path(skill_path).name.lower()


def update_state_after_scan(state: dict, skill_path: str, result: dict):
    """扫描后更新状态文件。"""
    slug = _slug(skill_path)
    fp = dir_fingerprint(Path(skill_path)) if Path(skill_path).is_dir() else file_hash(Path(skill_path))
    state.setdefault("skills", {})[slug] = {
        "path": skill_path,
        "fingerprint": fp,
        "verdict": result.get("verdict", "?")[:120],
        "score": result.get("risk_score", {}).get("score", 0),
        "gate": result.get("admission_gate", "?"),
        "signals": list(result.get("signals", [])),  # v2.5.0 信号快照（更新投毒 Diff 依据）
        "last_scan": datetime.datetime.now().isoformat(),
    }


def diff_poisoning_signals(old_signals, new_signals):
    """比对信号快照，返回版本更新后『新增』的高危信号（P0/P1）。

    用途：防『更新投毒』（postmark-mcp / Orca Delayed Weaponization 教训）——
    一个 Skill 首次安装时可能是良性的，更新后悄悄加入窃密/外传逻辑。
    只对「变更后新增」的高危信号告警，不重复已有的发现。
    """
    old = set(old_signals or [])
    fresh = [s for s in (new_signals or []) if s not in old and s.startswith(("P0:", "P1:"))]
    return fresh


# ── 主入口 ──────────────────────────────────────────────────

def do_check(skill_path: str = None, auto_alert: bool = True):
    """执行扫描检查。
    若 skill_path 为 None，首次运行全量扫描所有已知平台的 Skill；
    后续运行仅扫描新增(added)或版本更新(modified)的 Skill（每日增量）。
    """
    # v3.0.1 沙箱模式：统一经 _load_engine 加载引擎（常规 import 或 engine.zip）
    from _load_engine import load as _load_engine
    _eng = _load_engine()
    analyze, analyze_dir, verdict_label, render_summary_table = (
        _eng.analyze, _eng.analyze_dir, _eng.verdict_label, _eng.render_summary_table)

    log = ScanLogger()
    platforms = discover_platforms()
    state = load_state()

    log.scan_start()
    start = time.time()

    if skill_path:
        # 单 Skill 扫描
        p = Path(skill_path)
        if p.is_dir() and (p / "SKILL.md").exists():
            result = analyze(p)
        elif p.is_dir() and any(p.rglob("SKILL.md")):
            results = analyze_dir(p)
            result = results[0] if results else {"error": "no skills found"}
        elif p.is_file() and p.suffix.lower() == ".md":
            result = analyze(p)
        else:
            log.error(str(p), "不是有效的 Skill 路径")
            log.scan_end(0, time.time() - start)
            return False

        name = result.get("basic_info", {}).get("name", p.name) if "basic_info" in result else p.name
        verdict = result.get("verdict", "?") if isinstance(result, dict) else str(result)
        score = result.get("risk_score", {}).get("score", 0) if isinstance(result, dict) else 0
        log.skill_scanned(name, str(verdict)[:120], score, str(skill_path))
        # v2.5.0 更新投毒 Diff：仅对「已有记录且本次变更」的 Skill 比对信号快照
        slug = _slug(str(p))
        had_prior = slug in state.get("skills", {})
        old_signals = set((state.get("skills", {}).get(slug) or {}).get("signals", [])) if had_prior else set()
        update_state_after_scan(state, skill_path, result if isinstance(result, dict) else {})
        if had_prior and isinstance(result, dict):
            fresh = diff_poisoning_signals(old_signals, result.get("signals", []))
            if fresh:
                log.update_poisoning(name, fresh)
                print(f"\n🚨 更新投毒告警：{name} 本次更新新增 {len(fresh)} 个高危信号："
                      f"{', '.join(fresh[:5])}")

        # 告警
        if isinstance(result, dict):
            hits = result.get("security_risks", {}).get("hits", [])
            for h in hits:
                log.finding(name, h["sev"], h["label"], h.get("line", 0), h.get("snippet", ""))
            if result.get("admission_gate", "").startswith("BLOCK"):
                log.alert(name, "准入卡点判定为 BLOCK")
                print(f"\n🚨 安全告警：{name} 被判定为 BLOCK！")
                print(f"   评级：{result.get('risks_summary',{}).get('verdict','?')}")
                print(f"   路径：{skill_path}")
            elif result.get("admission_gate", "").startswith("NEED_REVIEW"):
                log.alert(name, "准入卡点判定为 NEED_REVIEW")
                print(f"\n⚠️  需人工复核：{name}（NEED_REVIEW）")

    else:
        # 全平台扫描：首次运行全量，后续每日仅增量（新装 / 版本更新）
        first_run = not state.get("skills")
        changes = detect_changes(state, platforms)
        # 新规则：仅扫描新增(added)与版本更新/变更(modified)，跳过无变化的 Skill
        all_skills = changes["added"] + changes["modified"]

        if not all_skills:
            state["last_full_scan"] = datetime.datetime.now().isoformat()
            save_state(state)
            log.scan_end(0, time.time() - start)
            if first_run:
                print("未发现任何 Skill（已扫描全部已知目录），无可审计对象。")
            else:
                print("无新增或版本更新的 Skill，本次无需扫描。")
            return True

        if first_run:
            print(f"首次全量扫描：共 {len(all_skills)} 个 Skill（全部为新发现）...")
        else:
            print(f"每日增量扫描：检测到 {len(changes['added'])} 个新增 / "
                  f"{len(changes['modified'])} 个版本更新或变更 Skill，开始扫描...")

        results_list = []
        for info in all_skills:
            sp = Path(info["path"])
            if sp.is_dir():
                result = analyze(sp) if (sp / "SKILL.md").exists() else {}
            else:
                result = analyze(sp)
            results_list.append({"path": str(sp), "result": result, "info": info})

            name = result.get("basic_info", {}).get("name", sp.name) if isinstance(result, dict) and "basic_info" in result else sp.name
            verdict = result.get("verdict", "?") if isinstance(result, dict) else "?"
            score = result.get("risk_score", {}).get("score", 0) if isinstance(result, dict) else 0
            is_new = info in changes["added"]
            is_mod = info in changes["modified"]
            log.skill_scanned(name, str(verdict)[:120], score, str(sp),
                            new=is_new, modified=is_mod)

            # findings
            if isinstance(result, dict):
                for h in result.get("security_risks", {}).get("hits", []):
                    log.finding(name, h["sev"], h["label"], h.get("line", 0), h.get("snippet", ""))
                gate = result.get("admission_gate", "")
                if gate.startswith("BLOCK"):
                    log.alert(name, "BLOCK")
                    print(f"\n🚨 {name} → BLOCK（禁止准入）")
                elif gate.startswith("NEED_REVIEW"):
                    log.alert(name, "NEED_REVIEW")
                    print(f"\n⚠️  {name} → NEED_REVIEW")

            # v2.5.0 更新投毒 Diff：仅对「版本更新」的 Skill 比对信号快照
            slug = _slug(str(sp))
            old_signals = set((state.get("skills", {}).get(slug) or {}).get("signals", [])) if slug in state.get("skills", {}) else set()
            update_state_after_scan(state, str(sp), result if isinstance(result, dict) else {})
            if is_mod and isinstance(result, dict):
                fresh = diff_poisoning_signals(old_signals, result.get("signals", []))
                if fresh:
                    log.update_poisoning(name, fresh)
                    print(f"\n🚨 更新投毒告警：{name} 本次更新新增 {len(fresh)} 个高危信号："
                          f"{', '.join(fresh[:5])}")
            if is_new:
                log.skill_added(name, str(sp))
            if is_mod:
                log.skill_modified(name, str(sp))

        # 移除
        for r in changes["removed"]:
            slug = r["slug"]
            if slug in state.get("skills", {}):
                del state["skills"][slug]

        # 汇总表
        valid = [r for r in results_list if "error" not in r.get("result", {})]
        if valid:
            print("\n" + render_summary_table(valid))
        flagged = [r for r in valid if verdict_label(r["result"]) != "✅ 未发现风险"]
        if flagged:
            print(f"\n⚠️  共 {len(flagged)} 个 Skill 需关注，详见日志：{LOG_DIR}")

    state["last_full_scan"] = datetime.datetime.now().isoformat()
    save_state(state)
    log.scan_end(len(all_skills) if not skill_path else 1, time.time() - start)
    log.rotate()
    return True


def do_report():
    """输出最近状态报告。"""
    from logger import ScanLogger as SL
    log = SL()
    history = log.get_history(30)
    state = load_state()

    print("═" * 60)
    print("Skill Analysis · 安全状态报告")
    print("═" * 60)
    print(f"最近一次扫描：{state.get('last_full_scan', '从未')[:19]}")
    print(f"已追踪 Skill 数量：{len(state.get('skills', {}))}")

    ratings = {"safe": 0, "warning": 0, "danger": 0}
    for slug, info in state.get("skills", {}).items():
        g = info.get("gate", "")
        if g.startswith("BLOCK"):
            ratings["danger"] += 1
        elif g.startswith("NEED_REVIEW"):
            ratings["warning"] += 1
        else:
            ratings["safe"] += 1

    print(f"当前状态：🟢安全 {ratings['safe']}  🟡需关注 {ratings['warning']}  🔴危险 {ratings['danger']}")
    print()

    if ratings["danger"] > 0:
        print("🔴 危险 Skill（建议立即审查）：")
        for slug, info in state.get("skills", {}).items():
            if info.get("gate", "").startswith("BLOCK"):
                print(f"  - {info.get('path', slug)}")
        print()

    print(f"扫描历史（最近 {len(history)} 次）：")
    for rec in history[:10]:
        ts = rec.get("ts", "?")[:19]
        print(f"  {ts} | 共 {rec.get('total', 0)} Skill | "
              f"安全 {rec.get('safe', 0)} · 警告 {rec.get('warn', 0)} · 危险 {rec.get('danger', 0)}")
    print()
    print(f"日志目录：{LOG_DIR}")


def main():
    ap = argparse.ArgumentParser(description="Skill Analysis Watchdog — 跨平台自动扫描")
    ap.add_argument("--check", nargs="?", const="__ALL__",
                    help="执行检查（不指定路径则扫描全部平台，指定路径则只扫描该 Skill）")
    ap.add_argument("--daemon", action="store_true", help="后台轮询模式")
    ap.add_argument("--interval", type=int, default=86400,
                    help="轮询间隔（秒），默认 86400（1 天）")
    ap.add_argument("--report", action="store_true", help="输出安全状态报告")
    ap.add_argument("--platform", action="store_true",
                    help="列出检测到的平台与 Skill 目录")
    args = ap.parse_args()

    if args.platform:
        platforms = discover_platforms()
        for platform, dirs in platforms.items():
            print(f"\n📂 {platform}：")
            for d in dirs:
                skills = find_skills(d)
                print(f"   {d}  ({len(skills)} 个 Skill)")
        return

    if args.report:
        do_report()
        return

    if args.daemon:
        print(f"Watchdog 后台模式启动（间隔 {args.interval}s）...")
        try:
            while True:
                do_check()
                time.sleep(args.interval)
        except KeyboardInterrupt:
            print("\nWatchdog 已退出。")
        return

    # 默认：--check
    skill_path = None if args.check == "__ALL__" else args.check
    if args.check and skill_path:
        do_check(skill_path)
    else:
        do_check()


if __name__ == "__main__":
    main()
