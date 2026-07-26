#!/usr/bin/env python3
"""
AI Daily Briefing - 环境初始化与安装检查
运行一次即可，负责检测 OS/GUI 环境并安装缺失依赖
"""
import os, sys, subprocess, shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from common import has_gui, detect_os, load_env, ok, fail, warn

PASS = FAIL = WARN = 0

def _ok(msg):
    global PASS
    ok(msg); PASS += 1

def _fail(msg):
    global FAIL
    fail(msg); FAIL += 1

def _warn(msg):
    global WARN
    warn(msg); WARN += 1

def install_tool(name, install_cmd, check_cmd=None):
    """尝试自动安装工具，返回是否成功。"""
    print(f"   尝试自动安装 {name}...")
    try:
        subprocess.run(install_cmd, shell=True, check=True, capture_output=True)
        if check_cmd and not shutil.which(check_cmd):
            return False
        return True
    except Exception:
        return False

def main():
    load_env()
    OS = detect_os()
    has_gui_env = has_gui()

    print("=== AI Daily Briefing 环境初始化 ===")
    print(f"操作系统: {OS}")
    print(f"GUI 环境: {'是' if has_gui_env else '否（无 GUI 模式）'}")
    print()

    # ── 1. 环境变量检查 ──
    print("1. 环境变量检查")
    VARS = [
        ("FEISHU_APP_ID", "飞书应用 App ID", "飞书开放平台创建应用获取"),
        ("FEISHU_OPEN_ID", "飞书用户 Open ID（私信异常通知）", "飞书管理后台查看"),
        ("FEISHU_CHAT_ID", "飞书群聊 ID（简报发送目标）", "飞书群设置中查看"),
        ("PH_API_TOKEN", "Product Hunt API token", "https://api.producthunt.com/v2/oauth/applications 注册"),
        ("PROXY_URL", "SOCKS5 代理地址（用于被墙站点）", "自备代理服务"),
    ]
    for name, desc, hint in VARS:
        val = os.environ.get(name, "")
        if val:
            _ok(f"{name} 已设置")
        else:
            _fail(f"{name} 未设置")
            print(f"      用途: {desc}")
            print(f"      获取: {hint}")
    print()

    # ── 2. 工具依赖检查与自动安装 ──
    print("2. 工具依赖检查")

    # 2a. python3
    if shutil.which("python3"):
        v = subprocess.run(["python3", "--version"], capture_output=True, text=True).stdout.strip()
        _ok(f"python3 已安装 ({v})")
    else:
        _fail("python3 未安装")
        if install_tool("python3", "apt-get update -qq && apt-get install -y -qq python3 python3-pip", "python3"):
            _ok("python3 已自动安装")
        elif install_tool("python3", "yum install -y -q python3 python3-pip", "python3"):
            _ok("python3 已自动安装")
        elif install_tool("python3", "brew install python3", "python3"):
            _ok("python3 已自动安装")
        else:
            _fail("自动安装失败，请手动安装 python3")

    # 2b. curl
    if shutil.which("curl"):
        _ok("curl 已安装")
    else:
        _fail("curl 未安装")
        if install_tool("curl", "apt-get update -qq && apt-get install -y -qq curl", "curl"):
            _ok("curl 已自动安装")
        elif install_tool("curl", "yum install -y -q curl", "curl"):
            _ok("curl 已自动安装")
        else:
            _fail("自动安装失败，请手动安装 curl")

    # 2c. lark-cli
    if shutil.which("lark-cli"):
        _ok("lark-cli 已安装")
        out = subprocess.run(["lark-cli", "config", "show"], capture_output=True, text=True).stdout
        if '"appId"' in out:
            _ok("lark-cli 已绑定")
        else:
            _warn("lark-cli 未绑定")
            print("   运行: lark-cli config bind --source openclaw --app-id $FEISHU_APP_ID --identity bot-only --force")
    else:
        _fail("lark-cli 未安装")
        if install_tool("lark-cli", "npm install -g @larksuite/cli", "lark-cli"):
            _ok("lark-cli 已自动安装")
        else:
            _fail("npm 未安装，无法自动安装 lark-cli")
            print("   请先安装 Node.js: https://nodejs.org")

    # 2d. 可选依赖（GUI 已移除，仅保留基础检查）
    print()
    print("   依赖检查完成（所有采集均通过 API 实现，无需 GUI）")
    print()

    # ── 3. 配置指引 ──
    print(f"=== 检查完成: {PASS} 通过, {WARN} 警告, {FAIL} 失败 ===")

    if FAIL > 0:
        print()
        print("📋 配置步骤：")
        print("   1. 在 ~/.openclaw/.env 中设置缺失的环境变量")
        print("   2. 安装缺失的工具（已尝试自动安装）")
        print(f"   3. 运行 python3 {SCRIPT_DIR}/preflight_check.py 确认 API 可用性")
        print("   4. 运行技能：告诉 AI '生成今日 AI 简报'")
        return 1

    if not has_gui_env:
        print()
        print("ℹ️  无 GUI 环境提示：")
        print("   - 所有采集均通过 API 实现，无需 GUI 环境")

    return 0

if __name__ == "__main__":
    sys.exit(main())
