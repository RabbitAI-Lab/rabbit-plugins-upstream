#!/usr/bin/env python3
"""环境自检：流水线开跑前先确认一切就绪。

只依赖标准库，因此在依赖缺失时也能正常运行。
用法：
    python scripts/check_env.py
退出码 0 = 全部就绪；1 = 存在阻塞项。
"""

from __future__ import annotations

import os
import shutil
import sys

MODULES = {
    "whisper": "openai-whisper",
    "edge_tts": "edge-tts",
    "pysrt": "pysrt",
    "pydub": "pydub",
}


def check_modules() -> tuple[list[str], list[str]]:
    """区分「没装」和「装了但导入崩溃」。

    这一点很关键：SSL 初始化失败之类的环境问题会让已安装的包在
    import 阶段抛异常，症状与「没装」一模一样。若不加区分就会给出
    「请 pip install」的错误指引，让人白费力气反复重装。
    """
    import importlib

    missing: list[str] = []
    broken: list[str] = []
    for mod, pkg in MODULES.items():
        try:
            importlib.import_module(mod)
            print(f"  OK    {mod}")
        except ModuleNotFoundError:
            print(f"  MISS  {mod}        -> pip install {pkg}")
            missing.append(pkg)
        except Exception as exc:  # noqa: BLE001 - 任何异常都说明是环境而非缺包
            print(f"  BROKEN {mod}       已安装，但导入时崩溃：{type(exc).__name__}: {exc}")
            broken.append(mod)
    return missing, broken


def check_ffmpeg() -> str | None:
    path = shutil.which("ffmpeg")
    if path:
        print(f"  OK    ffmpeg       {path}")
        return None
    print("  MISS  ffmpeg       -> 需加入 PATH（pydub / whisper 都要调用它）")
    return "ffmpeg"


def check_ffprobe() -> None:
    path = shutil.which("ffprobe")
    if path:
        print(f"  OK    ffprobe      {path}")
    else:
        print("  WARN  ffprobe      未找到（步骤 3 核验音频时长时需要，通常随 ffmpeg 一起安装）")


def check_sslkeylogfile() -> None:
    """Windows 上偶发的坑：SSLKEYLOGFILE 指向无法写入的路径。

    SSL 库初始化时会尝试写该文件，失败则报 PermissionError。
    症状极具迷惑性：pip list 看得到包、包也确实装好了，
    却 import 不进来，看起来就像没装一样。

    注意：不能用 os.access() 判断可写性，它在某些环境下会误报。
    必须真的打开一次文件。
    """
    value = os.environ.get("SSLKEYLOGFILE")
    if not value:
        print("  OK    SSLKEYLOGFILE 未设置")
        return

    try:
        with open(value, "a"):
            pass
        print(f"  OK    SSLKEYLOGFILE {value}（实测可写）")
        return
    except Exception as exc:  # noqa: BLE001
        reason = f"{type(exc).__name__}: {exc}"

    print(f"  WARN  SSLKEYLOGFILE={value}  实测无法写入（{reason}）")
    print("        这会导致 pip / edge_tts 在 SSL 初始化时崩溃，")
    print("        并伪装成“包没安装”。若上方出现 BROKEN 多半就是这个原因。")
    print("        修复：")
    print("          Git Bash/Linux/macOS : unset SSLKEYLOGFILE")
    print("          PowerShell           : Remove-Item Env:SSLKEYLOGFILE")
    print("          长久方案             : 从系统环境变量中删除它")


def main() -> int:
    print(f"Python  {sys.executable}")
    print(f"版本    {sys.version.split()[0]}\n")

    print("[ Python 依赖 ]")
    missing, broken = check_modules()

    print("\n[ 外部工具 ]")
    missing_bin = check_ffmpeg()
    check_ffprobe()

    print("\n[ 环境变量陷阱 ]")
    check_sslkeylogfile()

    blockers = missing + ([missing_bin] if missing_bin else [])
    print()
    if missing:
        print("缺失依赖，请安装：")
        for item in missing:
            print(f"  - {item}")
    if broken:
        print("以下包已安装但导入失败，通常是环境问题而非缺包：")
        for item in broken:
            print(f"  - {item}")
        print("  请先按上一节的提示处理环境变量，不要用重装来解决。")
    if blockers or broken:
        return 1
    print("结论：环境就绪，可以开始流水线。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
