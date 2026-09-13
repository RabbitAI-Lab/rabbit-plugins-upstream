#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""打包双色球 SKILL 为可分发 zip（dist/ssq-probability-analyzer.zip）。

原则（沿用大乐透打包经验）：
- 顶层只留入口 run_ssq.py + README.md + 使用指南.txt + SKILL.md + references/
- lib/ 放全部模块与离线数据
- 排除：临时补丁(_*.py)、__pycache__、HTML 产物(*.html)、运行时产物(json)、状态/日志文件
        以及运行时可重建缓存 ssq_valid_combos.json（由 ssq_auto.exhaustive_combos 首跑自动重建）
        以及可选装饰图 assets/win_illustrations/（缺失时报告自动回退，不联网无法重算故不带）
- 保留离线数据：ssq_history.json / ssq_winner_stats.json / ssq_data_source.json（离线自洽基石）
"""
import os
import zipfile

SKILL_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = os.path.join(SKILL_ROOT, "scripts")
LIB = os.path.join(SCRIPTS, "lib")
DIST_DIR = os.path.join(SKILL_ROOT, "dist")
ZIP_PATH = os.path.join(DIST_DIR, "ssq-probability-analyzer.zip")

# scripts/ 顶层保留
TOP_KEEP = {"run_ssq.py", "README.md", "使用指南.txt"}

# lib/ 排除（临时 / 产物 / 状态）
LIB_EXCLUDE = {
    "_gen_baseline.py", "_patch_me.py",
    "ssq_eci_backtest_result.json",
    "ssq_method_explorer.json",
    "ssq_prediction_2026090_v8.json",
    "ssq_recommended_periods.json",
    # 运行时产物(每次运行再生, 不必随包发):
    "ssq_data_fetch_log.json",
    "ssq_ml_selfcheck.json",
    "ssq_power_baseline.json",
    "ssq_power_report.json",
    "ssq_winning_news_cache.json",
    # 运行时可重建缓存(首跑由 ssq_auto.exhaustive_combos() 自动生成, 8.6MB 体积大户, 必排除):
    "ssq_valid_combos.json",
    # 机器特定/运行时状态(绝不能随包污染新装用户缓存认知):
    "ssq_cache_manifest.json",      # 按目标期缓存清单, 机器相关
    "ssq_performance.json",         # 运行时性能追踪
    "ssq_ledger.json",              # 个人运行时诚实账本, 涉及隐私, 发布包排除
    "manifest.json",                # win_photos 缓存标记(真实图片未抓取时不应假装已缓存)
    # 机器/安装特定的哈希基线(由 ssq_self_integrity.py --init 生成本机哈希):
    # 若随包发出, 新装用户文件哈希与陈旧基线不符 -> #24 误报"代码被篡改". 必须排除.
    "ssq_integrity_manifest.json",
    # 运行时状态/告警(绝不能随包污染新装用户):
    "ssq_run_alert.txt",
    "REPORT_PATH.txt",
    "ssq_watchdog_status.txt",
    "ssq_watchdog_alerts.log",
}
LIB_EXCLUDE_SUFFIX = (".html", ".csv", ".log")
LIB_EXCLUDE_PREFIX = ("_", "ssq_prediction_", "ssq_performance_")

# 顶层 scripts 排除
TOP_EXCLUDE = {"health_history.csv", "health_latest.json"}


def allowed_lib(name):
    if name in LIB_EXCLUDE:
        return False
    if name.endswith(LIB_EXCLUDE_SUFFIX):
        return False
    if name.startswith(LIB_EXCLUDE_PREFIX):
        return False
    return True


def build():
    if os.path.exists(ZIP_PATH):
        try:
            os.remove(ZIP_PATH)
        except OSError:
            # 沙箱/回收站不可用时 os.remove 被拦截, 无所谓:
            # 下方 zipfile 以 "w" 模式打开会直接覆盖旧 zip
            pass
    os.makedirs(DIST_DIR, exist_ok=True)

    included = []

    def add_dir(src, arc_base):
        for root, dirs, files in os.walk(src):
            # 跳过 __pycache__ 与可选装饰图目录(缺失时报告自动回退, 不随包发)
            dirs[:] = [d for d in dirs
                       if d != "__pycache__" and d != "win_illustrations"]
            for fn in sorted(files):
                full = os.path.join(root, fn)
                rel = os.path.relpath(full, src).replace("\\", "/")
                arc = f"{arc_base}/{rel}"
                if "scripts/lib/" in arc:
                    if not allowed_lib(fn):
                        continue
                if os.path.basename(full) in TOP_EXCLUDE:
                    continue
                zf.write(full, arc)
                included.append(arc)

    def add_file(src, arc):
        zf.write(src, arc)
        included.append(arc)

    with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as zf:
        # 顶层 SKILL.md
        add_file(os.path.join(SKILL_ROOT, "SKILL.md"),
                 "ssq-probability-analyzer/SKILL.md")
        # references
        add_dir(os.path.join(SKILL_ROOT, "references"),
                "ssq-probability-analyzer/references")
        # scripts 顶层
        for fn in TOP_KEEP:
            p = os.path.join(SCRIPTS, fn)
            if os.path.exists(p):
                add_file(p, f"ssq-probability-analyzer/scripts/{fn}")
        # lib
        add_dir(LIB, "ssq-probability-analyzer/scripts/lib")

    print(f"打包完成: {ZIP_PATH}")
    print(f"包含文件数: {len(included)}")
    mods = [i for i in included if i.endswith(".py")]
    print(f"  .py 模块: {len(mods)}")
    data = [i for i in included if i.endswith(".json")]
    print(f"  .json 数据: {len(data)} -> {sorted(os.path.basename(d) for d in data)}")
    refs = [i for i in included if "/references/" in i]
    print(f"  references: {len(refs)}")
    pyc = [i for i in included if i.endswith(".pyc")]
    print(f"  __pycache__ 误打包: {len(pyc)}")


if __name__ == "__main__":
    build()
