#!/usr/bin/env python3
"""
chrome_manager.py — 多店铺 Chrome 会话层：注册表 + 按需拉起 + 优雅关闭。

设计（店群模式，支持 10+ 店铺）：
  - 每店独立 user-data-dir（登录态加密落盘，实例关闭不丢）+ 固定 CDP 端口
  - 按需轮转：用前 probe 端口，活着复用；没活才拉起。内存峰值 = 并发实例数
  - 优雅关闭：CDP Browser.close（cookie 落盘），绝不强杀
  - 幂等：重复 ensure_chrome() 无副作用

注册表 ~/.pdd-data/shops.yaml：
  shops:
    - name: shop-a         # 别名（agent 寻址用，"同步 A 店"）
      label: 某某旗舰店      # 显示名（可省）
      mall_id: 123456789    # 首次采集后自动回填
      cdp_port: 9222
      profile_dir: ~/.pdd-data/profiles/shop-a

用法（python import 或 CLI）:
  from chrome_manager import load_shops, ensure_chrome, shutdown_chrome
  python3 chrome_manager.py list
  python3 chrome_manager.py add <name> [--port 9223]   # 拉起 Chrome 等人登录，自动登记
"""
import os, sys, json, time, shutil, subprocess

import urllib.request

# 零第三方依赖：HTTP 走标准库 urllib；pyyaml 可选（没装用内置极简 fallback）。
# 原则：缺任何可选库，模块本身必须能 import 成功——否则上层守卫没机会给结构化提示。
try:
    import yaml  # 无 pyyaml 时用内置极简 fallback（见 _load_yaml/_dump_yaml）
except ImportError:
    yaml = None

DATA_DIR = os.path.expanduser(os.environ.get("PDD_DATA_DIR", "~/.pdd-data"))
SHOPS_FILE = os.path.join(DATA_DIR, "shops.yaml")
MMS_LOGIN = "https://mms.pinduoduo.com/login"
MMS_HOME = "https://mms.pinduoduo.com/home"
DEFAULT_FIRST_PORT = 9222
PROBE_TIMEOUT = 3

# ---------------- yaml（无 pyyaml 时的极简 fallback） ----------------

def _dump_yaml(obj):
    if yaml is not None:
        return yaml.safe_dump(obj, allow_unicode=True, sort_keys=False)
    else:
        lines = ["shops:"]
        for s in obj.get("shops", []):
            lines.append(f"  - name: {s['name']}")
            for k in ("label", "mall_id", "cdp_port", "profile_dir"):
                if s.get(k) is not None:
                    lines.append(f"    {k}: {s[k]}")
        return "\n".join(lines) + "\n"

def _load_yaml(text):
    if yaml is not None:
        return yaml.safe_load(text) or {}
    else:
        # 极简解析（缩进宽容）：同时兼容 pyyaml safe_dump 的顶格 "- name:" 和
        # 本文件 fallback dump 的 "  - name:"——注册表可能由任一环境写入
        shops, cur = [], None
        for ln in text.splitlines():
            s = ln.strip()
            if not s or s == "shops:" or s.startswith("#"):
                continue
            if s.startswith("- "):
                cur = {}
                shops.append(cur)
                s = s[2:].strip()
                if not s:
                    continue
            if cur is not None and ":" in s:
                k, v = s.split(":", 1)
                k, v = k.strip(), v.strip().strip("'\"")
                if k in ("mall_id", "cdp_port") and v:
                    try:
                        v = int(v)
                    except ValueError:
                        pass
                cur[k] = v
        return {"shops": shops}


# ---------------- 注册表 ----------------

def load_shops():
    if not os.path.exists(SHOPS_FILE):
        return []
    return (_load_yaml(open(SHOPS_FILE, encoding="utf-8").read()) or {}).get("shops", [])

def save_shops(shops):
    """就地截断写（非 原子替换）：os.replace 的 unlink 步骤会被 Agent 沙箱判成
    "删除文件"弹权限。fsync 把就地写的损坏窗口压到最小。"""
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(SHOPS_FILE, "w", encoding="utf-8") as f:
        f.write(_dump_yaml({"shops": shops}))
        f.flush()
        os.fsync(f.fileno())

def find_shop(name):
    """按 name/label/mall_id 模糊寻址（agent 说显示名的一部分也能命中别名）。"""
    name = str(name).strip().lower()
    for s in load_shops():
        if (name == s["name"].lower() or name == str(s.get("mall_id"))
                or (s.get("label") and name in s["label"].lower())
                or name in s["name"].lower()):
            return s
    return None

def _next_free_port(shops):
    used = {s["cdp_port"] for s in shops}
    p = DEFAULT_FIRST_PORT
    while p in used:
        p += 1
    return p


# ---------------- Chrome 实例管理 ----------------

def _chrome_binary():
    # 手动指定出口（探测不到或想用特定浏览器时）：PDD_CHROME_PATH=完整可执行文件路径
    env = os.environ.get("PDD_CHROME_PATH")
    if env:
        env = os.path.expanduser(env)
        return env if os.path.exists(env) else None
    local = os.environ.get("LOCALAPPDATA", "")  # Windows 无管理员权限时 Chrome 默认装这里
    for c in ("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",       # macOS
              "/Applications/Chromium.app/Contents/MacOS/Chromium",
              "C:/Program Files/Google/Chrome/Application/chrome.exe",              # Windows 全局安装
              "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe",
              os.path.join(local, "Google", "Chrome", "Application", "chrome.exe") if local else "",
              # Edge 兜底：每台 Windows 都有，Chromium 内核，CDP 参数完全通用
              "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
              "C:/Program Files/Microsoft/Edge/Application/msedge.exe"):
        if c and os.path.exists(c):
            return c
    for c in ("google-chrome", "chromium", "chrome"):                               # Linux
        if shutil.which(c):
            return shutil.which(c)
    return None

def probe(port):
    """端口上有活着的 CDP 吗？活着返回 /json 列表，否则 None。（纯标准库）"""
    try:
        with urllib.request.urlopen(f"http://localhost:{port}/json", timeout=PROBE_TIMEOUT) as r:
            return json.loads(r.read().decode())
    except Exception:
        return None

def _has_mms_logged_in(port):
    """已登录的 mms 页（非登录页）存在 → True。"""
    pages = probe(port) or []
    for t in pages:
        if t.get("type") != "page":
            continue
        u = t.get("url", "")
        if "mms.pinduoduo.com" in u and "/login" not in u and not u.startswith("chrome"):
            return True
    return False

def ensure_chrome(shop, first_url=MMS_HOME, headless=False):
    """确保该店的 Chrome 实例活着并返回 (port, launched?)。已活直接复用（幂等）。"""
    port = shop["cdp_port"]
    if _has_mms_logged_in(port):
        return port, False
    exe = _chrome_binary()
    if not exe:
        raise RuntimeError("no_chrome")  # 上层转成 notify_user
    profile = os.path.expanduser(shop.get("profile_dir") or
                                 os.path.join(DATA_DIR, "profiles", shop["name"]))
    cmd = [exe, f"--remote-debugging-port={port}", f"--user-data-dir={profile}",
           "--no-first-run", "--no-default-browser-check", "--disable-session-crashed-bubble",
           first_url]
    if headless:
        cmd.insert(1, "--headless=new")  # 注意：登录操作不能 headless，仅已登录采集可选
    kw = {"stdout": subprocess.DEVNULL, "stderr": subprocess.DEVNULL}
    if os.name == "nt":
        # 脱离控制台进程树：否则 launcher（agent 的 shell）退出时 Windows 会连坐杀掉 Chrome
        kw["creationflags"] = 0x00000008 | 0x00000200  # DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP
    else:
        kw["start_new_session"] = True
    subprocess.Popen(cmd, **kw)
    for _ in range(30):  # 等最多 15s 起 CDP
        time.sleep(0.5)
        if probe(port):
            return port, True
    raise RuntimeError(f"chrome_start_timeout:{port}")

def shutdown_chrome(port):
    """CDP Browser.close 优雅关闭（cookie 落盘）。"""
    try:
        import websocket
    except ImportError:
        import _miniws as websocket  # 纯标准库兜底（create_connection 接口兼容）
    try:
        pages = probe(port)
        if not pages:
            return False
        bws = None
        for t in pages:
            if t.get("type") == "page":
                bws = t.get("webSocketDebuggerUrl")  # 任意 page 的 ws 都能发 Browser.close
                break
        if not bws:
            return False
        ws = websocket.create_connection(bws, timeout=10, suppress_origin=True)
        try:
            ws.send(json.dumps({"id": 1, "method": "Browser.close"}))
        finally:
            ws.close()
        for _ in range(10):
            time.sleep(0.5)
            if not probe(port):
                return True
        return False
    except Exception:
        return False


# ---------------- 登记新店（人登一次，自动回填） ----------------

def _ws_connect(url, timeout=10):
    try:
        from websocket import create_connection
    except ImportError:
        from _miniws import create_connection  # 纯标准库兜底
    return create_connection(url, timeout=timeout, suppress_origin=True)


def _get_cookie(port, name="PASS_ID"):
    """CDP Network.getCookies 读 mms 的 httpOnly cookie（任意 page 的 ws 都能发）。无→None。"""
    try:
        pages = probe(port) or []
        ws_url = next((t["webSocketDebuggerUrl"] for t in pages if t.get("type") == "page"), None)
        if not ws_url:
            return None
        ws = _ws_connect(ws_url)
        try:
            ws.send(json.dumps({"id": 1, "method": "Network.getCookies",
                                "params": {"urls": ["https://mms.pinduoduo.com"]}}))
            while True:
                msg = json.loads(ws.recv())
                if msg.get("id") == 1:
                    for c in msg.get("result", {}).get("cookies", []):
                        if c.get("name") == name:
                            return c
                    return None
        finally:
            ws.close()
    except Exception:
        return None


def detect_mall_id(port, timeout_s=300):
    """轮询直到该端口出现已登录 mms 页，返回其 mall_id（从页面 URL/DOM 拿不到时返回 None）。"""
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        pages = probe(port) or []
        target = None
        for t in pages:
            if t.get("type") == "page" and "mms.pinduoduo.com" in t.get("url", "") \
                    and "/login" not in t.get("url", ""):
                target = t
                break
        if target:
            try:
                ws = _ws_connect(target["webSocketDebuggerUrl"])
                try:
                    js = ("(() => {const m = document.cookie.match(/mall_id=(\\d+)/);"
                          " if (m) return m[1];"
                          " const u = location.href.match(/mall_id=(\\d+)/);"
                          " return u ? u[1] : (window.__mms_info && String(window.__mms_info.mall_id)) || null;})()")
                    ws.send(json.dumps({"id": 1, "method": "Runtime.evaluate",
                                        "params": {"expression": js, "returnByValue": True}}))
                    while True:
                        msg = json.loads(ws.recv())
                        if msg.get("id") == 1:
                            return msg["result"]["result"].get("value")
                finally:
                    ws.close()
            except Exception:
                pass
        time.sleep(2)
    return None


def add_shop(name, port=None, label=None):
    """登记/重登流程（幂等：同名重跑 = 重新登录模式，3 天票过期后也用这条命令续）。

    全自动收尾——⚠️ agent 绝不要自己关闭/杀掉浏览器窗口，本函数会按安全顺序处理：
      1. 拉起该店专属 Chrome 到登录页，等人扫码/登录（最长 10 分钟）
      2. 检测到登录后缓冲 3 秒（让登录后的 Set-Cookie / 跳转收尾）
      3. 确认 httpOnly 登录票（PASS_ID）确已签发 → CDP Browser.close 优雅关闭（凭据落盘）
      4. 重新拉起一次复核：磁盘档案真能恢复登录态 → 再优雅关闭
    返回 login_persisted=true 才算登记成功闭环；false 时浏览器保持打开，提示继续登录。
    （背景：实测曾发生"登录完立刻强杀 Chrome → cookie 没落盘 → 被迫二次登录"）"""
    shops = load_shops()
    existing = next((s for s in shops if s["name"] == name), None)
    if existing:
        shop, is_new = existing, False      # 重登模式：复用登记信息
        if label:
            shop["label"] = label
    else:
        shop = {"name": name, "label": label or name,
                "cdp_port": int(port) if port else _next_free_port(shops),
                "profile_dir": os.path.join(DATA_DIR, "profiles", name)}
        is_new = True
    ensure_chrome(shop, first_url=MMS_LOGIN)          # 已登录态下会直接复用
    mall_id = detect_mall_id(shop["cdp_port"], timeout_s=600)
    if mall_id and not shop.get("mall_id"):
        shop["mall_id"] = int(mall_id)

    # —— 凭据落盘三部曲（防"登录完立刻关 → cookie 丢失 → 二次登录"）——
    persisted = False
    if _get_cookie(shop["cdp_port"]) or mall_id:
        time.sleep(3)
        if _get_cookie(shop["cdp_port"]):
            shutdown_chrome(shop["cdp_port"])         # 优雅关闭 = Chrome flush cookie 落盘
            time.sleep(1)
            ensure_chrome(shop, first_url=MMS_HOME)   # 重启复核：磁盘档案能恢复登录吗
            for _ in range(10):
                if _get_cookie(shop["cdp_port"]):
                    persisted = True
                    break
                time.sleep(1)
            shutdown_chrome(shop["cdp_port"])

    save_shops(shops + ([shop] if is_new else []))
    out = {"ok": True, "registered": True, "mall_id": shop.get("mall_id"),
           "login_persisted": persisted, "shop": shop}
    if persisted:
        out["note"] = ("登录凭据已确认保存并通过重启复核，该店后续采集会自动拉起浏览器，"
                       "无需再登录（登录票约 3 天有效，过期重跑本命令即可）。")
    else:
        out["keep_open"] = True
        out["action"] = {"type": "notify_user",
                         "message": f"店铺 {shop.get('label') or name} 的登录还未完成或未确认保存。"
                                    "浏览器窗口已保持打开，请完成登录后重跑登记命令；"
                                    "期间不要手动关闭该浏览器窗口。"}
    return out


# ---------------- CLI ----------------

if __name__ == "__main__":
    a = sys.argv
    if len(a) < 2 or a[1] == "list":
        rows = load_shops()
        print(json.dumps({"ok": True, "shops": rows}, ensure_ascii=False, indent=1))
    elif a[1] == "add" and len(a) > 2:
        port = a[a.index("--port") + 1] if "--port" in a else None
        label = a[a.index("--label") + 1] if "--label" in a else None
        print(json.dumps(add_shop(a[2], port=port, label=label), ensure_ascii=False))
    elif a[1] == "remove" and len(a) > 2:
        shops = load_shops()
        shops2 = [s for s in shops if s["name"] != a[2]]
        save_shops(shops2)
        print(json.dumps({"ok": True, "removed": len(shops) - len(shops2)}, ensure_ascii=False))
    else:
        print(__doc__)
