#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
跨平台 Chrome 远程调试端口启动工具 (start_chrome.py)
支持 macOS, Windows, Linux 全平台无缝启动 Chrome 调试模式 (默认 9222 端口)。
完全替代 .bat 和 .sh 脚本，符合 SkillHub 与跨平台安全规范。
"""

import sys
import os
import platform
import subprocess
import shutil
import socket
import argparse
from pathlib import Path


def is_port_in_use(port: int, host: str = "127.0.0.1") -> bool:
    """检查指定端口是否已被占用"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.8)
        try:
            s.connect((host, port))
            return True
        except (ConnectionRefusedError, socket.timeout, OSError):
            return False


def find_chrome_executable() -> str:
    """自动探测当前操作系统的 Google Chrome 可执行文件路径"""
    os_type = platform.system()

    if os_type == "Darwin":  # macOS
        candidates = [
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            os.path.expanduser("~/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"),
            "/Applications/Chromium.app/Contents/MacOS/Chromium",
        ]
        for path in candidates:
            if os.path.exists(path) and os.access(path, os.X_OK):
                return path
        # 尝试通过 which
        which_path = shutil.which("google-chrome") or shutil.which("chromium")
        if which_path:
            return which_path

    elif os_type == "Windows":  # Windows
        candidates = [
            os.path.join(os.environ.get("ProgramFiles", "C:\\Program Files"), "Google\\Chrome\\Application\\chrome.exe"),
            os.path.join(os.environ.get("ProgramFiles(x86)", "C:\\Program Files (x86)"), "Google\\Chrome\\Application\\chrome.exe"),
            os.path.join(os.environ.get("LOCALAPPDATA", ""), "Google\\Chrome\\Application\\chrome.exe"),
            os.path.join(os.environ.get("ProgramFiles", "C:\\Program Files"), "Microsoft\\Edge\\Application\\msedge.exe"),
        ]
        for path in candidates:
            if path and os.path.exists(path):
                return path
        which_path = shutil.which("chrome.exe") or shutil.which("chrome") or shutil.which("msedge.exe")
        if which_path:
            return which_path

    else:  # Linux / Unix
        candidates = [
            "google-chrome",
            "google-chrome-stable",
            "chromium-browser",
            "chromium",
        ]
        for name in candidates:
            which_path = shutil.which(name)
            if which_path:
                return which_path

    return ""


def launch_chrome(port: int = 9222, custom_path: str = None) -> bool:
    """以调试模式启动 Chrome 浏览器"""
    print(f"🔍 正在检测系统环境与 Google Chrome 安装路径...")
    
    if is_port_in_use(port):
        print(f"✨ 调试端口 {port} 已处于运行/监听状态！无需重复启动。")
        print(f"👉 您可以直接运行自动化关注脚本: python3 scripts/blogger_auto_follow.py -p <平台> -f <数据文件>")
        return True

    chrome_path = custom_path or find_chrome_executable()
    if not chrome_path:
        print(f"❌ 未在系统默认路径找到 Google Chrome 可执行文件。")
        print(f"💡 请确认已安装 Google Chrome，或通过参数指定路径: python3 scripts/start_chrome.py --path \"/path/to/chrome\"")
        return False

    print(f"🚀 找到 Chrome: {chrome_path}")
    print(f"🌐 正在启动 Chrome (调试端口: {port})...")

    args = [
        chrome_path,
        f"--remote-debugging-port={port}",
        "--no-first-run",
        "--no-default-browser-check"
    ]

    try:
        if platform.system() == "Windows":
            # Windows 后台脱离终端启动
            subprocess.Popen(args, creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP, close_fds=True)
        else:
            # macOS / Linux 后台无阻塞启动
            subprocess.Popen(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)

        print(f"✅ Google Chrome 已成功启动！(CDP 调试端口: {port})")
        print(f"💡 接下来您可以在打开的浏览器中完成平台登录，然后运行批量关注脚本。")
        return True
    except Exception as e:
        print(f"❌ 启动 Chrome 失败: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="跨平台 Chrome 调试端口启动器 (支持 macOS/Windows/Linux)")
    parser.add_argument("-p", "--port", type=int, default=9222, help="远程调试端口号 (默认: 9222)")
    parser.add_argument("--path", type=str, default=None, help="自定义 Chrome 可执行文件路径")
    
    args = parser.parse_args()
    success = launch_chrome(port=args.port, custom_path=args.path)
    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()
