---
name: legionspace-version
description: >
  检查大群空间 (LegionSpace, package: com.tongfudun.legion) 在各大应用商店的最新版本号。
  This skill should be used when the user asks to check LegionSpace versions, 大群空间版本,
  query app store versions for LegionSpace, or any request about the version status of
  the LegionSpace app across Chinese app stores.
  Covers: Apple App Store, Tencent MyApp, Xiaomi, vivo, Honor, Huawei, OPPO.
disable-model-invocation: true
allowed-tools: Bash
---

# LegionSpace 大群空间版本查询

查询 LegionSpace（包名 `com.tongfudun.legion`）在 7 大应用商店的最新版本号。

## 执行步骤

将以下 Python 脚本写入临时文件并执行。

### 依赖检查（执行前）

```bash
python -c "import requests" 2>/dev/null || python -m pip install requests
python -c "from playwright.sync_api import sync_playwright" 2>/dev/null || { python -m pip install playwright && python -m playwright install chromium; }
```

### 查询脚本

将以下完整内容写入 `${TEMP}/legionspace_check.py` 然后执行 `python ${TEMP}/legionspace_check.py`：

```python
# -*- coding: utf-8 -*-
"""LegionSpace App Store Version Check"""

import re, os, sys
from datetime import datetime

os.environ['no_proxy'] = '*'
os.environ['NO_PROXY'] = '*'
os.environ['HTTP_PROXY'] = ''
os.environ['HTTPS_PROXY'] = ''

PKG = "com.tongfudun.legion"

import requests
from playwright.sync_api import sync_playwright

rs = requests.Session()
rs.trust_env = False
rs.proxies = {'http': None, 'https': None}

def ok(v):
    """Validate version string: must be X.Y.Z or X.Y.Z.W, first number 1-1999"""
    try:
        p = [int(x) for x in v.split(".")]
        return len(p) >= 3 and p[0] < 2000 and p[0] >= 1
    except:
        return False

def find_ver(html):
    """Extract version number from HTML using 4-layer fallback strategy"""
    t = html.lower()

    # Layer 1: JSON fields "versionName" / "version_name" / "version" near package name
    # Many app stores embed version in JSON-LD or inline script data
    for field in ['versionname', 'version_name', 'version']:
        for m in re.finditer(r'"%s"\s*:\s*"(\d+\.\d+\.\d+(?:\.\d+)?)"' % field, t):
            v = m.group(1)
            if not ok(v): continue
            ctx = t[max(0, m.start()-600):m.end()+100]
            if PKG in ctx or 'legion' in ctx:
                return v

    # Layer 2: Clean text - strip HTML tags, scripts, styles, then match
    # patterns like "版本: 5.7.2", "Version: 5.7.2", "ver 5.7.2", "软件版本：V5.7.2"
    cl = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
    cl = re.sub(r'<style[^>]*>.*?</style>', '', cl, flags=re.DOTALL)
    cl = re.sub(r'<[^>]+>', ' ', cl)
    cl = re.sub(r'&nbsp;', ' ', cl)
    cl = re.sub(r'\s+', ' ', cl)

    for m in re.finditer(
        r'(?:version|ver[^a-z]|版本[号]?|软件版本)'
        r'\s*[:：\s]*'
        r'[Vv]?(\d+\.\d+\.\d+(?:\.\d+)?)',
        cl, re.IGNORECASE):
        v = m.group(1)
        if ok(v) and 3 <= int(v.split('.')[0]) <= 10:
            return v

    # Layer 3: "V X.Y.Z" pattern near app keywords (legionspace/legion/tongfudun)
    for kw in ['legionspace', 'legion', 'tongfudun']:
        idx = cl.lower().find(kw)
        if idx < 0: continue
        chunk = cl[idx:idx+1500]
        for m in re.finditer(r'\b[Vv](\d+\.\d+\.\d+(?:\.\d+)?)\b', chunk):
            if ok(m.group(1)):
                return m.group(1)

    # Layer 4: Package name exists in page → search version-like patterns nearby
    if PKG in t[:20000]:
        for m in re.finditer(
            r'(?:version|ver|版本)\D{0,5}'
            r'(\d+\.\d+\.\d+(?:\.\d+)?)', cl, re.IGNORECASE):
            if ok(m.group(1)):
                return m.group(1)

    return None

def pw_fetch(url, wait_ms=8000):
    """Fetch page with headless Chromium via Playwright, then extract version"""
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=True,
                args=['--no-proxy-server', '--proxy-server=direct://',
                      '--no-sandbox', '--disable-gpu'])
            ctx = browser.new_context(
                ignore_https_errors=True,
                user_agent=('Mozilla/5.0 (Linux; Android 13; Pixel 7) '
                            'AppleWebKit/537.36 Chrome/125.0.0.0 Safari/537.36'))
            page = ctx.new_page()
            page.goto(url, wait_until='networkidle', timeout=30000)
            page.wait_for_timeout(wait_ms)
            v = find_ver(page.content())
            ctx.close()
            browser.close()
            return v
    except Exception:
        return None

now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
results = []

print("=" * 50)
print("  LegionSpace App Store Version Check")
print("  %s" % now)
print("  Package: %s" % PKG)
print("=" * 50)
print()

# ============================================================
# STORE 1: Apple App Store — iTunes Lookup API (simple HTTP GET)
# URL: https://itunes.apple.com/lookup?bundleId=com.tongfudun.legion&country=cn
# Response: JSON with "results"[0]["version"]
# ============================================================
sys.stdout.write("  [1/7] Apple App Store ........ ")
sys.stdout.flush()
try:
    r = rs.get("https://itunes.apple.com/lookup?bundleId=%s&country=cn" % PKG, timeout=15)
    d = r.json()
    v = d["results"][0]["version"]
    print("v%s" % v)
    results.append(("Apple App Store", v))
except:
    print("FAIL")
    results.append(("Apple App Store", "--"))

# ============================================================
# STORE 2: Tencent MyApp (应用宝)
# URL: https://a.app.qq.com/o/simple.jsp?pkgname=com.tongfudun.legion
# Rendered with Playwright (mobile UA, 6s wait)
# ============================================================
sys.stdout.write("  [2/7] MyApp (Tencent) ........ ")
sys.stdout.flush()
v = pw_fetch("https://a.app.qq.com/o/simple.jsp?pkgname=%s" % PKG, 6000)
print("v%s" % v if v else "N/A")
results.append(("MyApp(Tencent)", v or "--"))

# ============================================================
# STORE 3: Xiaomi App Store (小米应用商店)
# URL: https://app.mi.com/details?id=com.tongfudun.legion
# Rendered with Playwright (mobile UA, 6s wait)
# ============================================================
sys.stdout.write("  [3/7] Xiaomi App Store ....... ")
sys.stdout.flush()
v = pw_fetch("https://app.mi.com/details?id=%s" % PKG, 6000)
print("v%s" % v if v else "N/A")
results.append(("Xiaomi", v or "--"))

# ============================================================
# STORE 4: vivo App Store
# URL: https://h5.appstore.vivo.com.cn/period2/index.html#/details
#      ?search_word=大群空间 (URL-encoded)
#      &search_action=4
#      &app_id=4072610
#      &app_pos=1
#      &source=5
#      &appId=4072610
#      &frompage=searchResultApp
#      &listpos=1
# Rendered with Playwright (mobile UA, 8s wait — vivo pages are heavier)
# ============================================================
sys.stdout.write("  [4/7] vivo App Store ......... ")
sys.stdout.flush()
v = pw_fetch(
    "https://h5.appstore.vivo.com.cn/period2/index.html"
    "#/details"
    "?search_word=%E5%A4%A7%E7%BE%A4%E7%A9%BA%E9%97%B4"
    "&search_action=4&app_id=4072610&app_pos=1&source=5"
    "&appId=4072610&frompage=searchResultApp&listpos=1",
    8000)
print("v%s" % v if v else "N/A")
results.append(("vivo", v or "--"))

# ============================================================
# STORE 5: Honor App Store (荣耀应用市场)
# URL: https://appmarket-h5.cloud.honor.com/h5/share/latest/index.html
#      ?shareId=2074329936971526144
#      &shareTo=wechat
# Rendered with Playwright (mobile UA, 8s wait)
# ============================================================
sys.stdout.write("  [5/7] Honor App Store ........ ")
sys.stdout.flush()
v = pw_fetch(
    "https://appmarket-h5.cloud.honor.com/h5/share/latest/index.html"
    "?shareId=2074329936971526144&shareTo=wechat",
    8000)
print("v%s" % v if v else "N/A")
results.append(("Honor", v or "--"))

# ============================================================
# STORE 6: Huawei AppGallery (华为应用市场)
# URL: https://appgallery.huawei.com/app/C114551451
#      ?sharePrepath=ag
#      &locale=zh_CN
#      &source=appshare
#      &subsource=C114551451
#      &shareTo=weixin
#      &shareFrom=appmarket
#      &shareIds=958675a106bd4db490a7bb0bbb0e8462_1
#      &callType=SHARE
# Rendered with Playwright (mobile UA, 10s wait — Huawei pages are the slowest)
# ============================================================
sys.stdout.write("  [6/7] Huawei AppGallery ..... ")
sys.stdout.flush()
v = pw_fetch(
    "https://appgallery.huawei.com/app/C114551451"
    "?sharePrepath=ag&locale=zh_CN&source=appshare"
    "&subsource=C114551451&shareTo=weixin"
    "&shareFrom=appmarket"
    "&shareIds=958675a106bd4db490a7bb0bbb0e8462_1&callType=SHARE",
    10000)
print("v%s" % v if v else "N/A")
results.append(("Huawei", v or "--"))

# ============================================================
# STORE 7: OPPO App Store (软件商店)
# URL: https://store.oppo.com/cn/search?q=LegionSpace
# Rendered with Playwright (mobile UA, 6s wait)
# NOTE: OPPO store is phone-only; PC often gets redirected or blocked
#       → expect "N/A (phone only)" frequently
# ============================================================
sys.stdout.write("  [7/7] OPPO App Store ......... ")
sys.stdout.flush()
v = pw_fetch("https://store.oppo.com/cn/search?q=LegionSpace", 6000)
print("v%s" % v if v else "N/A (phone only)")
results.append(("OPPO", v or "--"))

print()
print("=" * 50)
print("  Results")
print("=" * 50)
for name, ver in results:
    print("  %-18s  %s" % (name, ver))

# Save report to current working directory
rf = os.path.join(os.getcwd(), "LegionSpace_versions.txt")
with open(rf, "w", encoding="utf-8") as f:
    f.write("LegionSpace App Store Versions\n")
    f.write("Time: %s\n" % now)
    f.write("=" * 50 + "\n\n")
    for name, ver in results:
        f.write("  %-18s  %s\n" % (name, ver))
print("\n  Report: %s" % rf)
print()
```

### 输出

- 控制台打印每个商店的版本号
- 报告文件保存在当前工作目录：`./LegionSpace_versions.txt`

## URL 汇总

| # | 商店 | URL |
|---|------|-----|
| 1 | **Apple App Store** | `https://itunes.apple.com/lookup?bundleId=com.tongfudun.legion&country=cn` |
| 2 | **Tencent MyApp** | `https://a.app.qq.com/o/simple.jsp?pkgname=com.tongfudun.legion` |
| 3 | **Xiaomi** | `https://app.mi.com/details?id=com.tongfudun.legion` |
| 4 | **vivo** | `https://h5.appstore.vivo.com.cn/period2/index.html#/details?search_word=大群空间&search_action=4&app_id=4072610&app_pos=1&source=5&appId=4072610&frompage=searchResultApp&listpos=1` |
| 5 | **Honor** | `https://appmarket-h5.cloud.honor.com/h5/share/latest/index.html?shareId=2074329936971526144&shareTo=wechat` |
| 6 | **Huawei** | `https://appgallery.huawei.com/app/C114551451?sharePrepath=ag&locale=zh_CN&source=appshare&subsource=C114551451&shareTo=weixin&shareFrom=appmarket&shareIds=958675a106bd4db490a7bb0bbb0e8462_1&callType=SHARE` |
| 7 | **OPPO** | `https://store.oppo.com/cn/search?q=LegionSpace` |

## 版本提取策略（4 层回退）

1. **JSON 字段匹配**: 在 HTML 中搜索 `"versionName"`, `"version_name"`, `"version"` 等 JSON 字段，要求在包名 `com.tongfudun.legion` 或关键词 `legion` 附近（600 字符内）
2. **清洗文本匹配**: 去除所有 HTML 标签、script、style 后，搜索 `版本/VERSION/ver/软件版本 : VX.Y.Z` 模式
3. **关键词附近匹配**: 搜索 `legionspace`/`legion`/`tongfudun` 关键词出现位置前后 1500 字符内的 `VX.Y.Z` 模式
4. **包名附近匹配**: 如果页面前 20000 字符包含包名，搜索附近 `version|ver|版本` + 版本号

## 依赖

- Python 3.x
- `requests` — Apple App Store API 查询
- `playwright` + Chromium — 其余 6 个商店的 JS 页面渲染

## 注意事项

- OPPO 应用商店仅限手机端访问，PC 端可能返回 `N/A`
- 部分商店（vivo、Honor、Huawei）页面加载较慢，超时 8-10s
- 整个过程约需 30-60 秒
- 代理已强制关闭（`no_proxy=*`, `trust_env=False`），确保直连
- 报告文件保存在当前工作目录：`./LegionSpace_versions.txt`
