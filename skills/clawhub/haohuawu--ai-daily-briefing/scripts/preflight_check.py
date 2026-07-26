#!/usr/bin/env python3
"""
AI Daily Briefing - 执行前 Preflight 检查
每次运行前执行，确认运行时环境就绪
"""
import os, sys, subprocess, json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from common import has_gui, load_env, get_proxy, ok, fail, warn

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

def curl_check(url, proxy=False, timeout=10, extra_headers=None):
    """GET URL 返回 (success: bool, response_text: str)"""
    cmd = ["curl", "-s", "--max-time", str(timeout)]
    if proxy:
        p = get_proxy()
        if p:
            cmd += ["--proxy", p]
    if extra_headers:
        for k, v in extra_headers.items():
            cmd += ["-H", f"{k}: {v}"]
    cmd += [url]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 5)
        return r.returncode == 0 and bool(r.stdout.strip()), r.stdout
    except Exception:
        return False, ""

def main():
    load_env()
    has_gui_env = has_gui()

    print("=== AI Daily Briefing Preflight 检查 ===")
    print(f"GUI 环境: {'是' if has_gui_env else '否'}")
    print()

    # ── 1. 环境变量 ──
    print("1. 环境变量检查")
    required = ["FEISHU_APP_ID", "FEISHU_OPEN_ID", "FEISHU_CHAT_ID", "PH_API_TOKEN"]
    for var in required:
        if os.environ.get(var, ""):
            _ok(f"{var} 已设置")
        else:
            _fail(f"{var} 未设置")
    print()

    # ── 2. 工具运行时检查 ──
    print("2. 工具运行时检查")
    if shutil.which("lark-cli"):
        _ok("lark-cli 可用")
        out = subprocess.run(["lark-cli", "config", "show"], capture_output=True, text=True).stdout
        if '"appId"' in out:
            _ok("lark-cli 已绑定")
        else:
            _fail("lark-cli 未绑定")
            print(f"   运行: lark-cli config bind --source openclaw --app-id {os.environ.get('FEISHU_APP_ID', 'YOUR_APP_ID')} --identity bot-only --force")
    else:
        _fail("lark-cli 不可用")
        print("   请先运行 setup.py 完成初始化安装")
    print()

    # ── 3. GUI 环境特有检查（X/Twitter）──
    if has_gui_env:
        print("3. 浏览器自动化检查（GUI 环境）")

        # 3a. Chrome 远程调试端口
        ok_port, _ = curl_check("http://127.0.0.1:9222/json/version", timeout=3)
        if ok_port:
            _ok("Chrome 远程调试端口 9222 运行中")
        else:
            _fail("Chrome 远程调试端口 9222 不可用")
            print()
            print("""   启动命令:
   export DISPLAY=:99
   nohup /opt/cloakbrowser/chrome \\
       --no-sandbox \\
       --load-extension=/home/browser/opencli-extension \\
       --user-data-dir=<chrome-profile-dir> \\
       --profile-directory=Default \\
       --no-first-run --no-default-browser-check \\
       --disable-gpu --disable-dev-shm-usage \\
       --proxy-server=\"{os.environ.get('PROXY_URL', '')}\" \\
       --remote-debugging-port=9222 \\
       "https://x.com/home" > /tmp/chrome.log 2>&1 &""")
            print()
            print("⚠️  Chrome 不可用，X/Twitter 板块将跳过。")

        # 3b. opencli 扩展
        if shutil.which("opencli"):
            out = subprocess.run(
                ["opencli", "doctor"],
                capture_output=True, text=True, env={**os.environ, "OPENCLI_CDP_ENDPOINT": "http://127.0.0.1:9222"}
            ).stdout
            if "Extension: connected" in out:
                _ok("opencli 扩展已连接")
            else:
                _fail("opencli 扩展未连接")
                print("   尝试: opencli daemon stop && opencli doctor")
        else:
            _fail("opencli 不可用")
            print("   请先运行 setup.py 完成初始化安装")

        # 3c. x.com 登录态
        if ok_port:
            print()
            print("   检查 x.com 登录态...")
            out = subprocess.run(
                ["opencli", "web", "fetch", "https://x.com/home"],
                capture_output=True, text=True, env={**os.environ, "OPENCLI_CDP_ENDPOINT": "http://127.0.0.1:9222"}
            ).stdout
            if "Home" in out:
                _ok("x.com 已登录")
            else:
                _warn("x.com 登录态异常或无法访问")
                print("   请通过远程桌面登录 x.com")
    else:
        print("3. 无 GUI 环境，跳过浏览器自动化检查")
        print("   X/Twitter 将使用 HN 或 GitHub Topics 替代数据源")
    print()

    # ── 4. API 可用性检查 ──
    print("4. API 可用性检查")

    # 4a. GitHub Search API
    print("   检查 GitHub Search API...")
    ok_api, text = curl_check("https://api.github.com/search/repositories?q=test&per_page=1", timeout=10)
    if ok_api and '"total_count"' in text:
        _ok("GitHub Search API 可用")
    else:
        _fail("GitHub Search API 不可用（可能被限流或网络问题）")

    # 4b. Hacker News API
    print("   检查 Hacker News API...")
    ok_hn, text = curl_check("https://hacker-news.firebaseio.com/v0/topstories.json", proxy=True, timeout=10)
    if ok_hn and text.startswith("["):
        _ok("Hacker News API 可用")
    else:
        _fail("Hacker News API 不可用（国内可能被墙，需配置 PROXY_URL）")

    # 4c. Product Hunt API
    print("   检查 Product Hunt API...")
    ph_token = os.environ.get("PH_API_TOKEN", "")
    ok_ph, text = curl_check(
        "https://api.producthunt.com/v2/api/graphql",
        timeout=10,
        extra_headers={
            "Authorization": f"Bearer {ph_token}",
            "Content-Type": "application/json"
        }
    )
    # GraphQL 需要 POST，curl_check 是 GET，这里单独处理
    try:
        r = subprocess.run([
            "curl", "-s", "--max-time", "10", "-X", "POST",
            "https://api.producthunt.com/v2/api/graphql",
            "-H", f"Authorization: Bearer {ph_token}",
            "-H", "Content-Type: application/json",
            "-d", '{"query":"{ posts(first: 1) { edges { node { name } } } }"}'
        ], capture_output=True, text=True, timeout=15)
        if r.returncode == 0 and '"name"' in r.stdout:
            _ok("Product Hunt GraphQL API 可用")
        else:
            _fail("Product Hunt API 不可用（PH_API_TOKEN 可能无效或已过期）")
    except Exception:
        _fail("Product Hunt API 检查异常")
    print()

    # ── 5. 可选：Firecrawl API Key 检查 ──
    print("5. 可选依赖检查")
    if os.environ.get("FIRECRAWL_API_KEY", ""):
        _ok("FIRECRAWL_API_KEY 已设置（Anthropic 等无 RSS 博客抓取）")
    else:
        _warn("FIRECRAWL_API_KEY 未设置（Anthropic 新闻将跳过）")
    print()

    # ── 6. 代理检查 ──
    print("6. 代理检查（可选）")
    if os.environ.get("PROXY_URL", ""):
        _ok("PROXY_URL 已配置（SOCKS5 代理）")
    else:
        _warn("PROXY_URL 未配置（Hacker News 在国内可能无法访问）")
    print()

    # ── 汇总 ──
    print(f"=== Preflight 完成: {PASS} 通过, {WARN} 警告, {FAIL} 失败 ===")

    if FAIL > 0:
        print()
        print("⚠️  存在失败项，请按指引修复后再运行。")
        print("   如果 Hacker News API 被墙，配置 PROXY_URL 环境变量。")
        if not has_gui_env:
            print("   无 GUI 环境，X/Twitter 相关失败可忽略。")
        return 1
    return 0

if __name__ == "__main__":
    import shutil
    sys.exit(main())
