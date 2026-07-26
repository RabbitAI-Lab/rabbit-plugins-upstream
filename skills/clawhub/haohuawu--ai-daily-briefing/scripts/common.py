#!/usr/bin/env python3
"""
AI Daily Briefing - 公共函数库
被 collect.py 和 verify.py 共用
"""
import os, subprocess, json

# ── 操作系统检测 ──

def detect_os():
    import platform
    s = platform.system()
    if s == "Linux":
        return "linux"
    elif s == "Darwin":
        return "macos"
    elif s in ("Windows", "CYGWIN", "MINGW", "MSYS"):
        return "windows"
    return "unknown"


# 默认日期和输出路径

def default_date():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d")


def default_output_dir(date=None):
    d = date or default_date()
    return f"/tmp/ai-daily-briefing/{d}"


# ── 环境检测 ──

def has_gui():
    """检测是否有 GUI 环境。"""
    if os.environ.get("DISPLAY") or os.environ.get("WAYLAND_DISPLAY"):
        return True
    if os.path.exists("/tmp/.X11-unix/X0") or os.path.exists("/tmp/.X11-unix/X1"):
        return True
    try:
        subprocess.run(["pgrep", "-x", "Xvfb"], capture_output=True, check=True)
        return True
    except subprocess.CalledProcessError:
        pass
    return False


def opencli_available():
    """检测 opencli 是否可用。"""
    try:
        subprocess.run(["which", "opencli"], capture_output=True, check=True)
        return True
    except subprocess.CalledProcessError:
        return False


def use_x_twitter():
    """判断是否应该使用 X/Twitter 采集。"""
    return has_gui() and opencli_available()


def load_env():
    """从 ~/.openclaw/.env 加载环境变量。"""
    env_file = os.path.expanduser("~/.openclaw/.env")
    if not os.path.exists(env_file):
        return
    
    allowed = {
        "FEISHU_APP_ID", "FEISHU_OPEN_ID", "FEISHU_CHAT_ID", "PH_API_TOKEN",
        "PROXY_URL", "HTTP_PROXY_URL", "X_COOKIES_PATH", "OPENCLI_CDP_ENDPOINT",
        "AI_DAILY_DB_PATH", "FIRECRAWL_API_KEY"
    }
    
    with open(env_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, val = line.split("=", 1)
            key = key.strip()
            val = val.strip()
            if key in allowed:
                os.environ[key] = val


# ── 代理 ──

def get_proxy():
    return os.environ.get("PROXY_URL", "")


def proxy_opt():
    p = get_proxy()
    return ["--proxy", p] if p else []


def curl_json(url, max_time=15):
    """GET JSON 并返回 dict 或 None。"""
    cmd = ["curl", "-s", "--max-time", str(max_time)]
    if get_proxy():
        cmd += ["--proxy", get_proxy()]
    cmd += [url]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=max_time + 5)
        if not r.stdout.strip():
            return None
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        return None
    except subprocess.TimeoutExpired:
        return None
    except Exception:
        return None

def curl_text(url, max_time=15):
    """GET 文本并返回 str 或 None。"""
    cmd = ["curl", "-s", "--max-time", str(max_time)]
    if get_proxy():
        cmd += ["--proxy", get_proxy()]
    cmd += [url]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=max_time + 5)
        return r.stdout
    except subprocess.TimeoutExpired:
        return None
    except Exception:
        return None


# ── 输出辅助 ──

def ok(msg):
    print(f"   ✅ {msg}")

def fail(msg):
    print(f"   ❌ {msg}")

def warn(msg):
    print(f"   ⚠️  {msg}")
