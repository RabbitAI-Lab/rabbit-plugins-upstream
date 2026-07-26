#!/usr/bin/env python3
"""
Smart Memory v3 CLI — 线索驱动的渐进式记忆系统。

命令：
  init-db           初始化数据库（幂等）
  validate          运行一致性校验
  rebuild-manifest  重建 manifest 注册表
  recall            召回记忆
  record            记录知识卡片
  decide            执行三步决策
  scan-round        扫描 docs/ 目录更新 manifest
  orphans           检测孤文档
  decay-report      衰减报告
  slim              文档瘦身
  signal            记录信号
  stale-detect      巡检过期卡片
  restore           恢复卡片
  gc                垃圾回收
  migrate           从 v2 迁移
  env-snapshot      环境快照
"""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Optional

# 支持 "python -m v3.memory" 和 "python memory.py" 两种运行方式。
# 使用 sys.path.append 而非 insert(0)，避免覆盖标准库路径中的同名包。
_PKG_DIR = str(Path(__file__).resolve().parent)
_PARENT_DIR = str(Path(_PKG_DIR).parent)
if _PARENT_DIR not in sys.path:
    sys.path.append(_PARENT_DIR)


def get_base_dir() -> str:
    return _PKG_DIR


# ======================================================================
# 命令处理函数
# ======================================================================

def cmd_init_db(args) -> int:
    """初始化数据库（幂等）。"""
    from v3.db import init_db, DB_PATH

    conn = init_db()
    conn.close()
    print(f"数据库已初始化: {DB_PATH}")
    print("所有表和索引已就绪（幂等操作）。")
    return 0


def cmd_validate(args) -> int:
    """运行一致性校验。"""
    from v3.validate import validate, print_report

    base = args.base_dir or get_base_dir()
    report = validate(base)
    print(print_report(report))
    return 0 if report.valid else 1


def cmd_rebuild_manifest(args) -> int:
    """扫描 docs/ 目录重建 manifest 表。"""
    from v3.manifest import ManifestStore

    base_dir = args.base_dir or get_base_dir()
    docs_dir = os.path.join(base_dir, "docs")
    store = ManifestStore()
    count = store.rebuild(docs_dir)
    print(f"Manifest 重建完成: {count} 个文档已注册")
    return 0


def _print_recall_json(result, verbose):
    """以 JSON 格式输出召回结果。"""
    output = {
        "query": result["query"],
        "mode": result["mode"],
        "max_docs": result.get("max_docs", 3),
        "l2_triggered": result["l2_triggered"],
        "l1_results": result["l1_results"],
    }
    if verbose:
        output["l1_results"] = [
            {**r, "_verbose": {
                "importance": r.get("importance"),
                "retention": r.get("retention"),
                "status": r.get("status"),
            }}
            for r in result["l1_results"]
        ]
    if result.get("l2_results"):
        output["l2_results"] = result["l2_results"]
    print(json.dumps(output, ensure_ascii=False, indent=2))


def _print_recall_l1(l1, verbose):
    """以表格形式打印 L1 召回结果。"""
    if verbose:
        print(f"{'排名':<4} {'ID':<38} {'得分':<8} {'Import':<7} {'Retention':<9} {'Status':<18} {'标题':<20}")
        print("-" * 120)
        for i, item in enumerate(l1, 1):
            cid = item.get("card_id", "")[:36]
            score = f"{item.get('score', 0):.4f}"
            imp = f"{item.get('importance', 0):.3f}"
            ret = f"{item.get('retention', 0):.3f}"
            status = item.get("status", "")
            title = item.get("title", "")[:18]
            print(f"{i:<4} {cid:<38} {score:<8} {imp:<7} {ret:<9} {status:<18} {title}")
    else:
        print(f"{'排名':<4} {'ID':<38} {'得分':<8} {'标题':<30} {'关键词'}")
        print("-" * 100)
        for i, item in enumerate(l1, 1):
            cid = item.get("card_id", "")[:36]
            score = f"{item.get('score', 0):.4f}"
            title = item.get("title", "")[:28]
            keywords = ", ".join(item.get("keywords", [])[:4])
            print(f"{i:<4} {cid:<38} {score:<8} {title:<30} {keywords}")


def _print_recall_l2(l2_results, max_docs):
    """打印 L2 全文展开结果。"""
    print(f"\n--- L2 全文展开 ({len(l2_results)} 条, max_docs={max_docs}) ---")
    for item in l2_results:
        print(f"\n[{item['card_id']}] {item['title']}")
        content = item.get("content", "")
        if content:
            print(content[:500])


def cmd_recall(args) -> int:
    """召回记忆（L1/L2 渐进披露）。"""
    from v3.recall import RecallEngine

    engine = RecallEngine()
    mode = "full" if getattr(args, "load", False) else args.mode
    max_docs = getattr(args, "max_docs", 3)
    include_stale = getattr(args, "include_stale", False)
    skip_precond_cache = getattr(args, "skip_precond_cache", False)
    verbose = getattr(args, "verbose", False)

    result = engine.recall(
        query=args.query, top=args.top,
        days=getattr(args, "days", 30), mode=mode,
        max_docs=max_docs, include_stale=include_stale,
        skip_precond_cache=skip_precond_cache,
    )

    if args.json:
        _print_recall_json(result, verbose)
        return 0

    l1 = result["l1_results"]
    print(f"查询: {result['query']}")
    print(f"模式: {result['mode']} | L2 触发: {result['l2_triggered']}")
    print(f"L1 命中: {len(l1)} 条\n")

    if not l1:
        print("未找到匹配线索。")
        return 0

    _print_recall_l1(l1, verbose)

    if result["l2_triggered"] and result.get("l2_results"):
        _print_recall_l2(result["l2_results"], max_docs)

    return 0


def cmd_record(args) -> int:
    """记录知识卡片。"""
    from v3.cues import CueStore

    store = CueStore()

    keywords = [k.strip() for k in args.keywords.split(",")] if args.keywords else []
    docs = [d.strip() for d in args.docs.split(",")] if args.docs else []
    preconditions = [p.strip() for p in args.preconditions.split(";;")] if args.preconditions else []

    card = {
        "id": args.id,
        "title": args.title,
        "keywords": keywords,
        "scene": args.scene or "",
        "docs": docs,
        "importance": args.importance,
        "retention": args.retention,
        "content": args.scene or "",
        "tags": keywords,
    }

    if preconditions:
        card["preconditions"] = preconditions

    try:
        card_id = store.add(card)
        print(f"线索卡已保存: {card_id}")
        if args.id:
            print(f"  ID: {args.id}")
        print(f"  标题: {args.title}")
        print(f"  关键词: {', '.join(keywords) if keywords else '(无)'}")
        if preconditions:
            print(f"  前置条件: {len(preconditions)} 条")
    except ValueError as e:
        print(f"错误: {e}")
        return 1

    # --capture-env: 同时采集环境快照
    if getattr(args, "capture_env", False):
        print()
        _do_env_snapshot(cue_id=card_id)

    return 0


def cmd_decide(args) -> int:
    """执行三步决策。"""
    from v3.recall import RecallEngine
    from v3.decide import DecideEngine

    recall_engine = RecallEngine()
    decide_engine = DecideEngine()

    query_text = args.message or args.query
    recall_result = recall_engine.recall(
        query=query_text,
        top=8,
        days=30,
        mode="l1",
    )
    decision = decide_engine.decide(query_text, recall_result)

    print(f"查询: {query_text}")
    print(f"决策: {decision['action']}")
    print(f"原因: {decision['reason']}")
    stats = decision.get("stats", {})
    print(f"L1 命中: {stats.get('l1_count', 0)} 条")
    print(f"L2 命中: {stats.get('l2_count', 0)} 条")
    if stats.get("avg_relevance"):
        print(f"平均相关度: {stats['avg_relevance']:.4f}")
    if stats.get("redundancy"):
        print(f"冗余率: {stats['redundancy']:.4f}")

    if decision.get("card_ids"):
        print(f"\n推荐卡片: {', '.join(decision['card_ids'][:5])}")

    return 0


def cmd_scan_round(args) -> int:
    """扫描 docs/ 新文件 + 批量评估前置条件并写入缓存（SPEC §6.2）。"""
    import time as _time
    from v3.manifest import ManifestStore
    from v3.precondition import PreconditionEvaluator

    base_dir = args.base_dir or get_base_dir()
    docs_dir = os.path.join(base_dir, "docs")

    since_minutes = getattr(args, "since", None)
    prompt_mode = getattr(args, "prompt", False)
    min_mtime = _time.time() - since_minutes * 60 if since_minutes else 0

    # 1. 扫描 docs/ 新文件，更新 manifest
    manifest_store = ManifestStore()
    candidates = []  # (rel_path, abs_path, mtime)

    if os.path.isdir(docs_dir):
        new_count = 0
        for root, dirs, files in os.walk(docs_dir):
            for fname in files:
                abs_path = os.path.join(root, fname)
                mtime = os.path.getmtime(abs_path)

                # --since 过滤
                if since_minutes and mtime < min_mtime:
                    continue

                rel_path = os.path.relpath(abs_path, os.path.dirname(docs_dir))
                existing = manifest_store.get_by_path(rel_path)
                if existing is None:
                    doc_id = rel_path.replace("\\", "/").replace("/", "_").replace(".", "_")
                    checksum = ManifestStore.compute_checksum(abs_path) or ""
                    manifest_store.add_entry(doc_id, rel_path, checksum)
                    new_count += 1
                    candidates.append((rel_path, abs_path, mtime))
        print(f"扫描 docs/: 发现 {new_count} 个新文件"
              + (f"（最近 {since_minutes} 分钟内）" if since_minutes else ""))
    else:
        print(f"docs/ 目录不存在: {docs_dir}")
        new_count = 0

    # --prompt 模式：列出候选，等待用户确认
    if prompt_mode and candidates:
        from datetime import datetime
        print(f"\n可沉淀候选 ({len(candidates)} 个):")
        for rel_path, abs_path, mtime in candidates:
            mt_str = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M:%S")
            print(f"  {rel_path}  (修改时间: {mt_str})")

        # 等待确认
        resp = input("\n确认继续评估前置条件? (y/n): ").strip().lower()
        if resp not in ("y", "yes"):
            print("已取消。")
            return 0

    # 2. 批量评估前置条件并写入 precondition_cache
    evaluator = PreconditionEvaluator(base_dir=base_dir)
    result = evaluator.evaluate_all()

    print(f"前置条件评估: {result['total']} 条检查")
    print(f"  通过: {result['passed']}")
    print(f"  失败: {result['failed']}")

    if result["failed"] > 0:
        print("\n失败详情:")
        for item in result["details"]:
            if not item["all_passed"]:
                print(f"  [{item['cue_id']}] {item['title']}")
                for c in item["checks"]:
                    if not c.get("passed"):
                        print(f"    - {c.get('detail', '')}")

    return 0


def cmd_orphans(args) -> int:
    """检测孤文档和断引用。"""
    from v3.db import get_connection
    from v3.cues import CueStore
    from v3.manifest import ManifestStore

    base_dir = args.base_dir or get_base_dir()
    docs_dir = os.path.join(base_dir, "docs")
    conn = get_connection()

    orphans_found = 0

    # 1. manifest 中注册但 docs/ 文件不存在的文档
    print("=== manifest 注册但文件缺失 ===")
    store = ManifestStore()
    all_entries = store.list_all()
    for entry in all_entries:
        doc_path = os.path.join(base_dir, entry["rel_path"])
        if not os.path.isfile(doc_path):
            print(f"  [!] {entry['doc_id']} → {entry['rel_path']} (文件不存在)")
            orphans_found += 1
    if not any(not os.path.isfile(os.path.join(base_dir, e["rel_path"])) for e in all_entries):
        print("  无")

    # 2. signals 中 cue_id 对应的 cue 已被删除
    print("\n=== 信号记录的线索已删除 ===")
    rows = conn.execute(
        """SELECT s.id, s.cue_id, s.signal_type, s.recorded_at
           FROM signals s LEFT JOIN cues c ON s.cue_id = c.id
           WHERE c.id IS NULL""",
    ).fetchall()
    if rows:
        for r in rows:
            print(f"  [!] signal_id={r['id']} cue_id={r['cue_id']} "
                  f"type={r['signal_type']} at={r['recorded_at']}")
            orphans_found += len(rows)
    else:
        print("  无")

    # 3. env_snapshots 中 cue_id 为 NULL 的记录
    print("\n=== 环境快照孤儿 (cue_id=NULL) ===")
    snap_rows = conn.execute(
        "SELECT id, captured_at FROM env_snapshots WHERE cue_id IS NULL"
    ).fetchall()
    if snap_rows:
        for r in snap_rows:
            print(f"  [!] env_snapshot_id={r['id']} captured_at={r['captured_at']}")
        orphans_found += len(snap_rows)
    else:
        print("  无")

    print(f"\n共发现 {orphans_found} 个孤项。")
    if orphans_found > 0:
        print("建议: 手动检查后可安全删除这些记录。")
    return 0


def _build_decay_report(cues, now):
    """根据 Ebbinghaus 公式构建衰减报告列表。"""
    import math
    from datetime import datetime as _datetime

    report = []
    for cue in cues:
        current_retention = cue.get("retention", 1.0)
        importance = cue.get("importance", 0.5)
        updated_str = cue.get("updated", "")
        hours_elapsed = 0.0
        if updated_str:
            try:
                dt = _datetime.strptime(updated_str[:19], "%Y-%m-%d %H:%M:%S")
                hours_elapsed = (now - dt).total_seconds() / 3600
            except ValueError:
                continue

        S = importance * 720
        if S < 1:
            S = 1
        decayed_retention = current_retention * math.exp(-hours_elapsed / S)

        report.append({
            "card_id": cue.get("id"),
            "title": cue.get("title", ""),
            "status": cue.get("status"),
            "current_retention": round(current_retention, 4),
            "decayed_retention": round(decayed_retention, 4),
            "importance": round(importance, 4),
            "hours_since_update": round(hours_elapsed, 1),
        })
    return report


def _print_decay_table(report):
    """打印衰减报告表格。"""
    print(f"{'卡ID':<16} {'标题':<24} {'状态':<18} {'当前R':>8} {'衰减R':>8} {'重要性':>7} {'更新距今(时)':>14}  {'警告'}")
    print("-" * 120)

    for item in report:
        warning = "⚠ 即将 stale" if item["decayed_retention"] < 0.2 else ""
        print(f"{item['card_id']:<16} {item['title'][:23]:<24} {item['status']:<18} "
              f"{item['current_retention']:>8.4f} {item['decayed_retention']:>8.4f} "
              f"{item['importance']:>7.4f} {item['hours_since_update']:>14.1f}  {warning}")


def cmd_decay_report(args) -> int:
    """生成衰减报告，按 retention 排序（SPEC Ebbinghaus 公式）。"""
    from v3.cues import CueStore
    from v3.db import utcnow_dt

    store = CueStore()
    all_cues = store.list_all()
    eligible = [c for c in all_cues if c.get("status") in ("active", "stale_observed")]

    if not eligible:
        print("无 active/stale_observed 线索可供分析")
        return 0

    now = utcnow_dt()
    report = _build_decay_report(eligible, now)

    show_stale_only = getattr(args, "stale", False)
    if show_stale_only:
        report = [r for r in report if r["decayed_retention"] < 0.3]
        if not report:
            print("无 retention < 0.3 的即将失效卡片")
            return 0

    report.sort(key=lambda x: x["decayed_retention"])
    _print_decay_table(report)

    if show_stale_only:
        print(f"\n(已过滤: 仅显示 retention < 0.3 的即将失效卡片，共 {len(report)} 条)")

    return 0


def cmd_slim(args) -> int:
    """文档瘦身规则检测：扫描 docs/ 检测 frontmatter 缺失、空标题等问题。"""
    import os as _os
    from pathlib import Path as _Path

    base_dir = args.base_dir or get_base_dir()
    docs_dir = _os.path.join(base_dir, "docs")

    if not _os.path.isdir(docs_dir):
        print(f"docs/ 目录不存在: {docs_dir}")
        return 1

    md_files = []
    for root, dirs, files in _os.walk(docs_dir):
        for fname in files:
            if fname.endswith(".md"):
                md_files.append(_os.path.join(root, fname))

    issues = {}
    total = len(md_files)

    for abs_path in md_files:
        rel_path = _os.path.relpath(abs_path, base_dir)
        file_issues = []

        try:
            with open(abs_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception:
            file_issues.append("无法读取文件")
            issues[rel_path] = file_issues
            continue

        # 1. frontmatter 缺失：文件不以 --- 开头
        if not content.startswith("---"):
            file_issues.append("frontmatter 缺失")

        # 2. 空标题：有 # ... 标题但内容为空或仅有空格
        for line in content.split("\n"):
            stripped = line.strip()
            if stripped.startswith("#"):
                title_text = stripped.lstrip("#").strip()
                if not title_text:
                    file_issues.append("空标题")
                break  # 只检查第一个标题

        # 3. 空文件：内容少于 10 字符
        if len(content) < 10:
            file_issues.append("空文件（少于 10 字符）")

        # 4. 无实质内容：去除标题和空行后少于 50 字符
        lines = content.split("\n")
        substantive = [l for l in lines if l.strip() and not l.strip().startswith("#")]
        substantive_text = "".join(substantive)
        if len(substantive_text) < 50 and not file_issues:
            file_issues.append(f"无实质内容（仅 {len(substantive_text)} 字符）")

        if file_issues:
            issues[rel_path] = file_issues

    print("文档瘦身检测报告")
    print("================")
    print(f"扫描文件数: {total}")

    if not issues:
        print("\n未发现问题。")
        return 0

    print(f"\n发现问题:")
    for path, path_issues in sorted(issues.items()):
        print(f"\n  {path}:")
        for issue in path_issues:
            print(f"    - {issue}")

    return 0


def _collect_env_info():
    """采集系统环境指纹，返回 (os_info, python_info, shell_info, git_info) 元组。"""
    import platform
    import subprocess as _subprocess

    os_info = f"{platform.system()} {platform.version()}"
    python_info = sys.version.split()[0]
    shell_info = os.environ.get("SHELL", os.environ.get("COMSPEC", "cmd"))

    # Git 信息（优雅降级）
    git_info = None
    try:
        result = _subprocess.run(
            ["git", "--version"], capture_output=True, text=True, timeout=5
        )
        if result.returncode == 0:
            git_info = result.stdout.strip()
    except Exception:
        pass

    return os_info, python_info, shell_info, git_info


def _do_env_snapshot(cue_id: Optional[str] = None):
    """采集系统环境指纹并写入 env_snapshots 表（内部复用）。"""
    from v3.db import get_connection

    os_info, python_info, shell_info, git_info = _collect_env_info()

    conn = get_connection()
    conn.execute(
        """INSERT INTO env_snapshots (cue_id, os, python, shell, git)
           VALUES (?, ?, ?, ?, ?)""",
        (cue_id, os_info, python_info, shell_info, git_info),
    )
    conn.commit()

    print(f"环境快照已写入")
    print(f"  OS:       {os_info}")
    print(f"  Python:   {python_info}")
    print(f"  Shell:    {shell_info}")
    print(f"  Git:      {git_info or '不可用'}")
    if cue_id:
        print(f"  关联 cue: {cue_id}")


def cmd_env_snapshot(args) -> int:
    """采集系统环境指纹并写入 env_snapshots 表。"""
    cue_id = getattr(args, "cue_id", None)
    _do_env_snapshot(cue_id=cue_id)
    return 0


def cmd_signal(args) -> int:
    """记录信号。"""
    from v3.signals import SignalStore
    from v3.cues import CueStore

    cue_store = CueStore()
    card = cue_store.get(args.cue_id)
    if card is None:
        print(f"错误: 线索卡 '{args.cue_id}' 不存在")
        return 1

    signal_store = SignalStore()
    try:
        signal_id = signal_store.record(
            card_id=args.cue_id,
            signal_type=args.signal_type,
        )
        # 读取更新后的 retention
        updated = cue_store.get(args.cue_id)
        new_ret = updated.get("retention", 0.0) if updated else 0.0

        print(f"信号已记录: id={signal_id}")
        print(f"  卡片: {args.cue_id} ({card.get('title', '')})")
        print(f"  类型: {args.signal_type}")
        print(f"  更新后 retention: {new_ret:.4f}")
    except ValueError as e:
        print(f"错误: {e}")
        return 1
    return 0


def _print_stale_mark_result(result):
    """打印 stale-detect --mark 的标记结果。"""
    new_stale = result.get("new_stale", [])
    confirmed = result.get("confirmed", [])
    print(f"\n巡检结果:")
    print(f"  新标记 stale_observed: {len(new_stale)} 条")
    for card in new_stale:
        print(f"    [{card['id']}] {card.get('title', '')} "
              f"(retention={card.get('retention', 0):.4f}, stale_count={card.get('stale_count', 0)})")
    print(f"  推进到 stale_confirmed: {len(confirmed)} 条")
    for card in confirmed:
        print(f"    [{card['id']}] {card.get('title', '')} "
              f"(stale_count={card.get('stale_count', 0)})")


def _print_stale_purge_result(gc_result):
    """打印 --purge 物理删除结果。"""
    deleted = gc_result.get("deleted", [])
    orphan_count = gc_result.get("orphan_snapshots_cleaned", 0)
    print(f"已删除: {len(deleted)} 条")
    for card in deleted:
        print(f"  [{card['id']}] {card.get('title', '')} — 成功")
    if orphan_count > 0:
        print(f"清理孤儿 env_snapshots: {orphan_count} 条")
    print("\n关联 signals 和 precondition_cache 已级联删除。")
    print("docs/ 文件未受影响。")


def _print_stale_dry_run_result(result):
    """打印 stale-detect 默认 dry-run 检测结果。"""
    detected = result.get("detected", [])
    would_confirm = result.get("would_confirm", [])
    print(f"\n巡检结果 (仅检测，未标记):")
    print(f"  检测到 stale 候选项: {len(detected)} 条")
    for card in detected:
        print(f"    [{card['id']}] {card.get('title', '')} "
              f"(retention={card.get('retention', 0):.4f}, status={card.get('status', '')})")
    print(f"  将推进到 stale_confirmed: {len(would_confirm)} 条")
    for card in would_confirm:
        print(f"    [{card['id']}] {card.get('title', '')} "
              f"(stale_count={card.get('stale_count', 0)}, 再检测1次即确认)")
    if detected or would_confirm:
        print("\n(使用 --mark 执行自动标记，--purge 标记后物理删除)")


def cmd_stale_detect(args) -> int:
    """巡检过期卡片。"""
    from v3.gc import GarbageCollector

    gc = GarbageCollector()
    mark_mode = getattr(args, "mark", False)
    purge_mode = getattr(args, "purge", False)
    refresh_cache = getattr(args, "refresh_cache", False)

    if refresh_cache:
        from v3.precondition import PreconditionEvaluator
        base_dir = args.base_dir or get_base_dir()
        evaluator = PreconditionEvaluator(base_dir=base_dir)
        cache_result = evaluator.evaluate_all()
        print(f"precondition_cache 已刷新: {cache_result['total']} 条检查 "
              f"(通过 {cache_result['passed']}, 失败 {cache_result['failed']})")

    print("正在巡检所有 active 和 stale_observed 卡片...")
    result = gc.scan_stale(dry_run=not mark_mode)

    if mark_mode:
        _print_stale_mark_result(result)
        if purge_mode:
            print("\n--- 执行 gc --confirm ---")
            gc_result = gc.gc(dry_run=False, force=True)
            _print_stale_purge_result(gc_result)
    else:
        _print_stale_dry_run_result(result)

    return 0


def cmd_delete(args) -> int:
    """标记线索卡片为已删除。"""
    from v3.cues import CueStore

    store = CueStore()
    card = store.get(args.cue_id)
    if card is None:
        print(f"错误: 线索卡 '{args.cue_id}' 不存在")
        return 1

    ok = store.mark_deleted(args.cue_id)
    if ok:
        title = card.get("title", "")
        print(f"已标记删除: {args.cue_id} — \"{title}\"")
        print("docs/ 文件未受影响")
    else:
        print(f"标记删除失败: {args.cue_id}")
        return 1
    return 0


def cmd_restore(args) -> int:
    """恢复卡片到 active。"""
    from v3.gc import GarbageCollector
    from v3.cues import CueStore

    cue_store = CueStore()
    card = cue_store.get(args.cue_id)
    if card is None:
        print(f"错误: 线索卡 '{args.cue_id}' 不存在")
        return 1

    gc = GarbageCollector()
    ok = gc.restore(args.cue_id)

    if ok:
        updated = cue_store.get(args.cue_id)
        print(f"已恢复: {args.cue_id}")
        if updated:
            print(f"  状态: {updated.get('status')}")
            print(f"  stale_count: {updated.get('stale_count')}")
            print(f"  retention: {updated.get('retention')}")
    else:
        print(f"恢复失败: {args.cue_id}")
        return 1
    return 0


def cmd_gc(args) -> int:
    """垃圾回收。"""
    from v3.gc import GarbageCollector

    gc = GarbageCollector()
    cleanup_signals = getattr(args, "cleanup_signals", False)
    signal_max_age = getattr(args, "signal_max_age", 180)

    # --cleanup-signals：先清理信号（确认模式在 gc 物理删除前执行）
    if cleanup_signals:
        signal_dry_run = not args.confirm
        signal_result = gc.cleanup_signals(
            max_age_days=signal_max_age,
            dry_run=signal_dry_run,
        )
        print(f"信号老化清理{' (预览)' if signal_dry_run else ''}: "
              f"{signal_result['deleted_count']} 条过期信号 "
              f"({signal_result['affected_cards']} 张卡片受影响) "
              f"[总信号 {signal_result['total_signals_before']} → {signal_result['total_signals_after']}]")

    if not args.confirm:
        result = gc.gc(dry_run=True, force=False)
        pending = result.get("pending", [])
        excluded = result.get("excluded_by_interval", [])

        print(f"\n待删除 (stale_confirmed,deleted): {len(pending)} 条")
        if excluded:
            print(f"巡检间隔未到 (stale_confirmed < 24h): {len(excluded)} 条")
            for card in excluded:
                print(f"  [{card['id']}] {card.get('title', '')} "
                      f"— stale_detected_at={card.get('stale_detected_at', 'N/A')}")
        if not pending:
            print("没有满足删除条件的卡片。")
            return 0

        for card in pending:
            print(f"  [{card['id']}] {card.get('title', '')} "
                  f"— stale {card.get('stale_count', 0)} 次"
                  f"{', 首次检测 ' + card.get('stale_detected_at', '') if card.get('stale_detected_at') else ''}")

        print("\n(仅预览，未执行删除。使用 --confirm 执行物理删除)")
        return 0

    # confirm 模式
    result = gc.gc(dry_run=False, force=True)
    deleted = result.get("deleted", [])
    orphan_count = result.get("orphan_snapshots_cleaned", 0)

    print(f"\n物理删除: {len(deleted)} 条")
    for card in deleted:
        print(f"  [{card['id']}] {card.get('title', '')} — 成功")
    if orphan_count > 0:
        print(f"清理孤儿 env_snapshots: {orphan_count} 条")
    print("\n关联 signals 和 precondition_cache 已级联删除。")
    print("docs/ 文件未受影响。")
    return 0


def cmd_migrate(args) -> int:
    """从 v2 迁移到 v3。"""
    from v3.migrate import Migrator

    base = args.base_dir or get_base_dir()
    migrator = Migrator(
        v2_dir=args.v2_dir,
        db_path=args.db_path,
    )

    if args.dry_run:
        report = migrator.run(dry_run=True)
        print("=== 迁移预览 (dry-run) ===")
        print(f"  cues: {report['cues']} 条")
        print(f"  signals: {report['signals']} 条")
        print(f"  manifest: {report['manifest']} 条")
        print(f"  docs: {report['docs']} 个文件")
        if report["errors"]:
            print(f"  错误: {', '.join(report['errors'])}")
    else:
        report = migrator.run(dry_run=False)
        print("=== 迁移完成 ===")
        print(f"  cues: {report['cues']} 条")
        print(f"  signals: {report['signals']} 条")
        print(f"  manifest: {report['manifest']} 条")
        print(f"  docs: {report['docs']} 个文件")
        if report["errors"]:
            print(f"  错误: {', '.join(report['errors'])}")

        # 迁移后自动校验
        print("\n正在校验...")
        migrator2 = Migrator(v2_dir=args.v2_dir, db_path=args.db_path)
        verify_result = migrator2.verify()
        v = verify_result
        print(f"  cues 数量一致: {v['cues_match']}")
        print(f"  manifest 数量一致: {v['manifest_match']}")
        if v["errors"]:
            for e in v["errors"]:
                print(f"  ! {e}")
        if not v["cues_match"] or not v["manifest_match"]:
            print("\n警告: 校验发现不一致，请检查。")
            return 1

    return 0


# ======================================================================
# 参数解析器构建
# ======================================================================

def _build_argument_parser():
    """构建 argparse 解析器，返回配置好的 ArgumentParser 对象。"""
    parser = argparse.ArgumentParser(
        description="Smart Memory v3 CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--base-dir", default=None, help="v3 根目录（默认脚本所在目录）")
    parser.add_argument("--db-path", default=None, help="SQLite 数据库路径")

    subparsers = parser.add_subparsers(dest="command", help="可用命令")

    # ---- init-db ----
    p = subparsers.add_parser("init-db", help="初始化数据库（幂等）")
    p.set_defaults(func=cmd_init_db)

    # ---- validate ----
    p = subparsers.add_parser("validate", help="运行一致性校验")
    p.set_defaults(func=cmd_validate)

    # ---- rebuild-manifest ----
    p = subparsers.add_parser("rebuild-manifest", help="重建 manifest 注册表")
    p.set_defaults(func=cmd_rebuild_manifest)

    # ---- recall ----
    p = subparsers.add_parser("recall", help="召回记忆")
    p.add_argument("-q", "--query", required=True, help="查询文本")
    p.add_argument("--top", type=int, default=8, help="返回最多 N 条（默认 8）")
    p.add_argument("--days", type=int, default=30, help="时间窗口（天，默认 30）")
    p.add_argument("--mode", choices=["l1", "l2", "full"], default="l1",
                   help="召回模式（默认 l1）")
    p.add_argument("--load", action="store_true",
                   help="自动展开 L2 文档全文（等同 --mode full）")
    p.add_argument("--max-docs", type=int, default=3,
                   help="L2 最多展开文档数（默认 3）")
    p.add_argument("--verbose", "-v", action="store_true",
                   help="详细输出（含 importance/retention/status）")
    p.add_argument("--include-stale", action="store_true",
                   help="包含 stale_observed 线索")
    p.add_argument("--skip-precond-cache", action="store_true",
                   help="跳过前置条件缓存，实时检查")
    p.add_argument("--json", action="store_true", help="JSON 格式输出")
    p.set_defaults(func=cmd_recall)

    # ---- record ----
    p = subparsers.add_parser("record", help="记录知识卡片")
    p.add_argument("--id", default=None, help="线索 ID（不指定则自动生成）")
    p.add_argument("--title", required=True, help="标题")
    p.add_argument("--keywords", default="", help="关键词（逗号分隔）")
    p.add_argument("--scene", default="", help="适用场景/内容")
    p.add_argument("--docs", default="", help="关联文档 ID（逗号分隔）")
    p.add_argument("--importance", type=float, default=0.5, help="重要性 0~1")
    p.add_argument("--retention", type=float, default=1.0, help="保留强度 0~1")
    p.add_argument("--preconditions", default="", help="前置条件（;; 分隔多条）")
    p.add_argument("--capture-env", action="store_true",
                   help="同时采集并关联环境指纹")
    p.set_defaults(func=cmd_record)

    # ---- decide ----
    p = subparsers.add_parser("decide", help="执行三步决策")
    p.add_argument("message", nargs="?", default="", help="用户消息/查询")
    p.add_argument("-q", "--query", default="", help="用户消息/查询（兼容旧接口）")
    p.set_defaults(func=cmd_decide)

    # ---- scan-round ----
    p = subparsers.add_parser("scan-round", help="扫描 docs/ 目录更新 manifest")
    p.add_argument("--since", type=int, default=None,
                   help="仅扫描最近 N 分钟内修改的文件")
    p.add_argument("--prompt", action="store_true",
                   help="列出可沉淀候选后等待用户确认再评估前置条件")
    p.set_defaults(func=cmd_scan_round)

    # ---- orphans ----
    p = subparsers.add_parser("orphans", help="检测孤文档")
    p.set_defaults(func=cmd_orphans)

    # ---- decay-report ----
    p = subparsers.add_parser("decay-report", help="衰减报告")
    p.add_argument("--stale", action="store_true",
                   help="仅显示 retention < 0.3 即将失效卡片")
    p.set_defaults(func=cmd_decay_report)

    # ---- slim ----
    p = subparsers.add_parser("slim", help="文档瘦身")
    p.set_defaults(func=cmd_slim)

    # ---- signal ----
    p = subparsers.add_parser("signal", help="记录信号")
    p.add_argument("cue_id", help="线索卡 ID")
    p.add_argument("signal_type", choices=["recall", "used", "failed", "confirmed",
                                           "ignored", "contradicted"],
                   help="信号类型")
    p.set_defaults(func=cmd_signal)

    # ---- stale-detect ----
    p = subparsers.add_parser("stale-detect", help="巡检过期卡片")
    p.add_argument("--mark", action="store_true",
                   help="自动标记失效线索为 stale_observed（默认仅检测报告）")
    p.add_argument("--purge", action="store_true",
                   help="标记后自动执行 gc --confirm 物理删除 stale_confirmed 项")
    p.add_argument("--refresh-cache", action="store_true",
                   help="强制刷新 precondition_cache")
    p.set_defaults(func=cmd_stale_detect)

    # ---- restore ----
    p = subparsers.add_parser("restore", help="恢复卡片")
    p.add_argument("cue_id", help="线索卡 ID")
    p.set_defaults(func=cmd_restore)

    # ---- delete ----
    p = subparsers.add_parser("delete", help="标记线索卡片为已删除")
    p.add_argument("cue_id", help="线索卡 ID")
    p.set_defaults(func=cmd_delete)

    # ---- gc ----
    p = subparsers.add_parser("gc", help="垃圾回收")
    p.add_argument("--confirm", action="store_true", default=False,
                   help="执行物理删除（默认仅预览）")
    p.add_argument("--cleanup-signals", action="store_true",
                   help="清理 active/stale_observed 卡片的过期信号")
    p.add_argument("--signal-max-age", type=int, default=180,
                   help="信号最大保留天数（默认 180）")
    p.set_defaults(func=cmd_gc)

    # ---- migrate ----
    p = subparsers.add_parser("migrate", help="从 v2 迁移")
    p.add_argument("--from", dest="v2_dir", required=True,
                   help="v2 数据目录路径")
    p.add_argument("--to", dest="db_path", default=None,
                   help="v3 数据库路径")
    p.add_argument("--dry-run", action="store_true", help="仅校验不写入")
    p.set_defaults(func=cmd_migrate)

    # ---- env-snapshot ----
    p = subparsers.add_parser("env-snapshot", help="环境快照")
    p.add_argument("--cue-id", help="关联的线索卡 ID（可选）")
    p.set_defaults(func=cmd_env_snapshot)

    return parser


# ======================================================================
# main — CLI 入口
# ======================================================================

def main():
    parser = _build_argument_parser()
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return 0

    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
