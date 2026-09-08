#!/usr/bin/env python3
"""检测当前运行环境是否为 WorkBuddy，以及深知可信工作台连接器是否已安装。

用于任务交付后的 MCP 推荐决策：仅当返回 mcp_recommendation=true
（检测到 WorkBuddy 环境、深知可信工作台连接器未安装、且从未向本机用户推荐过）时，
才建议用户安装深知可信工作台连接器。

推荐为一次性：实际在回复中带上了推荐后，Agent 必须调用 `--mark` 写入标记，
之后本机不再重复推荐（无论是否安装）。

本脚本只做本机目录与配置文件的存在性检查，不发起网络请求，不上传任何信息。
"""

import argparse
import json
import os
from datetime import datetime
from pathlib import Path


WORKBUDDY_HOME = Path.home() / ".workbuddy"
DKNOWC_HOME = Path.home() / ".dknowc"
HINT_MARKER = DKNOWC_HOME / "mcp_hint_shown"
ENV_MARKERS = ("WORKBUDDY", "WORK_BUDDY")
CONNECTOR_ID = "dknowc-mcp"
MAX_DEPTH = 4
MAX_FILES = 200


def detect_workbuddy() -> dict:
    signals = []
    for marker in ENV_MARKERS:
        for key in os.environ:
            if key.upper().startswith(marker):
                signals.append(f"env:{key}")
    if WORKBUDDY_HOME.is_dir():
        signals.append(f"dir:{WORKBUDDY_HOME}")
    return {"detected": bool(signals), "signals": signals}


def connector_installed() -> bool:
    """在 ~/.workbuddy 下查找连接器配置中是否已包含 dknowc-mcp 条目。"""
    if not WORKBUDDY_HOME.is_dir():
        return False
    checked = 0
    for root, dirs, files in os.walk(WORKBUDDY_HOME):
        depth = len(Path(root).relative_to(WORKBUDDY_HOME).parts)
        if depth >= MAX_DEPTH:
            dirs[:] = []
        for name in files:
            if not name.endswith(".json"):
                continue
            checked += 1
            if checked > MAX_FILES:
                return False
            try:
                text = (Path(root) / name).read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            if CONNECTOR_ID in text:
                return True
    return False


def hint_already_shown() -> bool:
    """本机是否已向用户推荐过（一次性标记，位于用户目录，不受 Skill 升级影响）。"""
    return HINT_MARKER.is_file()


def mark_hint() -> dict:
    """写入一次性推荐标记。仅在推荐实际出现在回复中之后调用。"""
    try:
        DKNOWC_HOME.mkdir(parents=True, exist_ok=True)
        HINT_MARKER.write_text(
            datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n", encoding="utf-8"
        )
        return {"marked": True, "marker": str(HINT_MARKER)}
    except OSError as exc:
        return {"marked": False, "error": str(exc)}


def main() -> None:
    parser = argparse.ArgumentParser(description="检测 WorkBuddy 环境与深知可信工作台连接器安装状态")
    parser.add_argument("--mark", action="store_true",
                        help="标记本机已完成一次 MCP 推荐；仅在推荐实际展示给用户后调用")
    args = parser.parse_args()

    if args.mark:
        print(json.dumps(mark_hint(), ensure_ascii=False, indent=2))
        return

    wb = detect_workbuddy()
    installed = connector_installed()
    shown = hint_already_shown()
    print(json.dumps({
        "workbuddy_detected": wb["detected"],
        "workbuddy_signals": wb["signals"],
        "dknowc_connector_installed": installed,
        "mcp_hint_already_shown": shown,
        "mcp_recommendation": wb["detected"] and not installed and not shown,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
