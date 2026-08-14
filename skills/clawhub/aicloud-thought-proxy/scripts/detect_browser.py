#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
云思客 (AIcloud-thought-proxy) — 默认浏览器内核检测脚本

用途：判断系统默认浏览器是 Chromium 内核还是 Gecko 内核，
      以决定使用哪条操控通道（chrome-mcp/BrowserSkill 还是 GeckoDriver+Marionette）。

用法：
    python detect_browser.py                   # 自动检测
    python detect_browser.py --browser <路径>  # 手动指定浏览器可执行文件

输出（JSON）：
    {
      "engine":  "chromium" | "gecko" | "unknown",
      "browser": "品牌名",
      "path":    "可执行文件完整路径或 null",
      "method":  "manual | registry:ProgId | common-path | xdg-settings | lsregister | unknown",
      "hint":    "对应操控通道提示"
    }
"""

import json
import os
import sys

# ---------- Windows 下保证 stdout 为 UTF-8 ----------
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# ---------- 内核判定表：可执行文件名(小写) -> (内核, 品牌) ----------
CHROMIUM_EXES = {
    "chrome.exe": "Google Chrome",
    "chromium.exe": "Chromium",
    "msedge.exe": "Microsoft Edge",
    "brave.exe": "Brave",
    "vivaldi.exe": "Vivaldi",
    "opera.exe": "Opera",
    "360se.exe": "360 安全浏览器",
    "360chrome.exe": "360 极速浏览器",
    "qqbrowser.exe": "QQ 浏览器",
    "sogouexplorer.exe": "搜狗高速浏览器",
    "ucbrowser.exe": "UC 浏览器",
    "liebao.exe": "猎豹浏览器",
}
GECKO_EXES = {
    "firefox.exe": "Mozilla Firefox",
    "firefox": "Mozilla Firefox",
    "palemoon.exe": "Pale Moon",
    "waterfox.exe": "Waterfox",
}

# ---------- Windows: ProgId -> 可执行文件名 ----------
PROGID_TO_EXE = {
    "chromehtml": "chrome.exe",
    "msedgehtm": "msedge.exe",
    "bravehtml": "brave.exe",
    "vivaldihtm": "vivaldi.exe",
    "operastable": "opera.exe",
    "360se": "360se.exe",
}


def classify_exe(exe_name):
    """按可执行文件名返回 (engine, browser) 或 None。"""
    name = (exe_name or "").strip().lower()
    if not name:
        return None
    if name in CHROMIUM_EXES:
        return "chromium", CHROMIUM_EXES[name]
    if name in GECKO_EXES:
        return "gecko", GECKO_EXES[name]
    # 前缀匹配兜底：FirefoxURL-xxx / MSEdgeHTM-xxx 等
    if name.startswith("firefoxurl"):
        return "gecko", "Mozilla Firefox"
    if name.startswith("msedgehtm"):
        return "chromium", "Microsoft Edge"
    if name.startswith("chrome"):
        return "chromium", "Google Chrome"
    return None


# ---------- Windows 常见安装路径 ----------
WINDOWS_COMMON_PATHS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Mozilla Firefox\firefox.exe",
    r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe",
]


def detect_windows():
    """Windows：注册表 ProgId 优先，常见路径兜底。"""
    try:
        import winreg  # noqa: PLC0415

        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\Shell\Associations\UrlAssociations\http\UserChoice",
        )
        try:
            prog_id, _ = winreg.QueryValueEx(key, "ProgId")
        finally:
            winreg.CloseKey(key)

        exe = PROGID_TO_EXE.get((prog_id or "").lower())
        if exe:
            # 尝试定位完整路径（App Paths）
            full = find_exe_full_path(exe)
            if full:
                kind = classify_exe(os.path.basename(full))
                if kind:
                    return kind[0], kind[1], full, "registry:ProgId"
            kind = classify_exe(exe)
            if kind:
                return kind[0], kind[1], None, "registry:ProgId"
        if prog_id and prog_id.lower().startswith("firefoxurl"):
            return "gecko", "Mozilla Firefox", None, "registry:ProgId"
    except Exception:
        pass

    # 常见路径兜底
    for p in WINDOWS_COMMON_PATHS:
        if os.path.isfile(p):
            kind = classify_exe(os.path.basename(p))
            if kind:
                return kind[0], kind[1], p, "common-path"
    return None, None, None, "unknown"


def find_exe_full_path(exe):
    """通过注册表 App Paths 或 PATH 定位可执行文件完整路径。"""
    try:
        import winreg  # noqa: PLC0415

        key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\\" + exe,
        )
        try:
            val, _ = winreg.QueryValueEx(key, None)
            if val and os.path.isfile(val):
                return val
        finally:
            winreg.CloseKey(key)
    except Exception:
        pass
    for d in os.environ.get("PATH", "").split(os.pathsep):
        p = os.path.join(d, exe)
        if os.path.isfile(p):
            return p
    return None


def detect_macos():
    """macOS：常见 App 路径 + LaunchServices 简易探测。"""
    common = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        "/Applications/Firefox.app/Contents/MacOS/firefox",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
    ]
    for p in common:
        if os.path.isfile(p):
            kind = classify_exe(os.path.basename(p))
            if kind:
                return kind[0], kind[1], p, "common-path"
    # LaunchServices 查询默认 http handler（尽力而为）
    try:
        import subprocess  # noqa: PLC0415

        out = subprocess.run(
            [
                "/System/Library/Frameworks/CoreServices.framework/Frameworks/"
                "LaunchServices.framework/Support/lsregister",
                "-dump",
            ],
            capture_output=True,
            text=True,
            timeout=20,
        ).stdout
        for line in out.splitlines():
            if "http" in line.lower() and "handler" in line.lower():
                low = line.lower()
                if "firefox" in low:
                    return "gecko", "Mozilla Firefox", None, "lsregister"
                if any(k in low for k in ("chrome", "edge", "brave", "chromium")):
                    return "chromium", "Chromium-based", None, "lsregister"
    except Exception:
        pass
    return None, None, None, "unknown"


def detect_linux():
    """Linux：xdg-settings 读取默认浏览器 desktop 文件。"""
    try:
        import subprocess  # noqa: PLC0415

        out = subprocess.run(
            ["xdg-settings", "get", "default-web-browser"],
            capture_output=True,
            text=True,
            timeout=10,
        ).stdout.strip().lower()
        if "firefox" in out or "palemoon" in out:
            return "gecko", "Mozilla Firefox", None, "xdg-settings"
        if any(k in out for k in ("chrome", "chromium", "edge", "brave", "opera", "vivaldi")):
            return "chromium", "Chromium-based", None, "xdg-settings"
    except Exception:
        pass
    # 常见路径兜底
    for p in ("/usr/bin/firefox", "/usr/bin/google-chrome", "/usr/bin/microsoft-edge",
              "/usr/bin/chromium", "/snap/bin/firefox"):
        if os.path.isfile(p):
            kind = classify_exe(os.path.basename(p))
            if kind:
                return kind[0], kind[1], p, "common-path"
    return None, None, None, "unknown"


def main():
    # 手动指定路径优先
    browser_path = None
    if "--browser" in sys.argv:
        idx = sys.argv.index("--browser")
        if idx + 1 < len(sys.argv):
            browser_path = sys.argv[idx + 1].strip('"')
        else:
            print(json.dumps({"error": "--browser 缺少路径参数"}, ensure_ascii=False))
            sys.exit(2)

    if browser_path:
        if not os.path.isfile(browser_path):
            print(json.dumps({"error": f"浏览器路径不存在: {browser_path}"}, ensure_ascii=False))
            sys.exit(2)
        kind = classify_exe(os.path.basename(browser_path))
        if kind:
            engine, browser = kind
            method = "manual"
        else:
            engine, browser, method = "unknown", "无法识别", "manual"
    else:
        if sys.platform.startswith("win"):
            engine, browser, browser_path, method = detect_windows()
        elif sys.platform == "darwin":
            engine, browser, browser_path, method = detect_macos()
        else:
            engine, browser, browser_path, method = detect_linux()

    if engine == "chromium":
        hint = "Chromium 内核：使用 chrome-mcp 连接器，不可用时加载 BrowserSkill / agent-browser（见 references/chromium-automation.md）"
    elif engine == "gecko":
        hint = "Gecko 内核：使用 GeckoDriver + Marionette，需确保 geckodriver 可用（见 references/gecko-automation.md）"
    else:
        hint = "未能识别默认浏览器，请手动指定浏览器可执行文件路径（--browser <路径>）"

    result = {
        "engine": engine or "unknown",
        "browser": browser,
        "path": browser_path,
        "method": method,
        "hint": hint,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
