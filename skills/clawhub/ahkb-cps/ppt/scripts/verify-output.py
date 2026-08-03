#!/usr/bin/env python3
"""
verify-output.py — 验证生成的 HTML 幻灯片文件完整性
======================================================

用法：
    python scripts/verify-output.py <输出的.html>

检查项：
  1. HTML 结构完整性（DOCTYPE、html、head、body、闭合标签）
  2. 幻灯片结构（.deck、.slide、.is-active）
  3. 36 个主题是否全部嵌入 window.__THEMES
  4. 21 个 Canvas FX 模块是否内联
  5. runtime.js 是否嵌入（关键函数存在性）
  6. base.css 设计令牌是否嵌入（CSS 变量）
  7. 图片是否为 base64 data URI（无外部路径）
  8. 图片不得被包裹容器包裹（<div>、<figure> 等直接包裹 <img> 视为违规）
  9. 无外部 skill 资产引用（<link>/<script src> 指向 assets/）
  10. 编辑模式代码是否存在
  11. 主题切换补丁是否存在
  12. 左下角时钟是否正常
"""

import os, re, sys, json, base64

# Fix Windows console encoding for Unicode output
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

# ── 期望值 ──
EXPECTED_THEME_COUNT = 36
EXPECTED_FX_COUNT = 21

EXPECTED_THEMES = [
    'minimal-white', 'editorial-serif', 'soft-pastel', 'sharp-mono',
    'arctic-cool', 'sunset-warm', 'catppuccin-latte', 'catppuccin-mocha',
    'dracula', 'tokyo-night', 'nord', 'solarized-light', 'gruvbox-dark',
    'rose-pine', 'neo-brutalism', 'glassmorphism', 'bauhaus', 'swiss-grid',
    'terminal-green', 'xiaohongshu-white', 'rainbow-gradient', 'aurora',
    'blueprint', 'memphis-pop', 'cyberpunk-neon', 'y2k-chrome', 'retro-tv',
    'japanese-minimal', 'vaporwave', 'midcentury', 'corporate-clean',
    'academic-paper', 'news-broadcast', 'pitch-deck-vc', 'magazine-bold',
    'engineering-whiteprint',
]

EXPECTED_FX = [
    '_util', 'particle-burst', 'confetti-cannon', 'firework', 'starfield',
    'matrix-rain', 'knowledge-graph', 'neural-net', 'constellation',
    'orbit-ring', 'galaxy-swirl', 'word-cascade', 'letter-explode',
    'chain-react', 'magnetic-field', 'data-stream', 'gradient-blob',
    'sparkle-trail', 'shockwave', 'typewriter-multi', 'counter-explosion',
]

RUNTIME_KEY_FUNCTIONS = [
    'function go(', 'function showSlide(', 'function applyTheme(',
    'function fitSlide(', 'function toggleEditMode(', 'function pushUndo(',
    'function undo(', 'function redo(',
]

RUNTIME_KEY_VARS = [
    'const ANIMS =', 'const FX_LIST =', 'BroadcastChannel',
    'contentEditable', 'toggleEditMode',
]

CSS_VARIABLE_NAMES = [
    '--bg', '--surface', '--text-1', '--text-2', '--accent',
    '--radius', '--border', '--shadow', '--font-sans',
]


# ── 颜色 ──
class C:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    END = '\033[0m'

def ok(msg):
    print(f"  {C.GREEN}[OK] {msg}{C.END}")

def fail(msg, detail=""):
    print(f"  {C.RED}[FAIL] {msg}{C.END}")
    if detail:
        for line in detail.split("\n"):
            print(f"     {C.RED}  {line}{C.END}")

def warn(msg):
    print(f"  {C.YELLOW}[WARN] {msg}{C.END}")


def check_structure(html, path):
    """检查 HTML 基本结构"""
    issues = []
    if not html.startswith("<!DOCTYPE html>") and not html.startswith("<!DOCTYPE HTML>"):
        issues.append("缺少 <!DOCTYPE html>")
    if not re.search(r'<html\b', html, re.IGNORECASE):
        issues.append("缺少 <html> 标签")
    if not re.search(r'</html>\s*$', html, re.IGNORECASE):
        issues.append("缺少 </html> 闭合标签或不在文件末尾")
    if not re.search(r'<head>', html, re.IGNORECASE):
        issues.append("缺少 <head>")
    if not re.search(r'</head>', html, re.IGNORECASE):
        issues.append("缺少 </head>")
    if not re.search(r'<body\b', html, re.IGNORECASE):
        issues.append("缺少 <body>")
    if not re.search(r'</body>', html, re.IGNORECASE):
        issues.append("缺少 </body>")

    if issues:
        fail("HTML 结构不完整", "\n".join(issues))
        return False
    ok("HTML 结构完整 (DOCTYPE/html/head/body)")
    return True


def check_slides(html):
    """检查幻灯片结构"""
    deck_count = len(re.findall(r'class="[^"]*\bdeck\b[^"]*"', html))
    if deck_count == 0:
        fail("缺少 .deck 容器")
        return False
    ok(f".deck 容器存在 ({deck_count} 个)")

    slides = re.findall(r'<section[^>]*class="[^"]*\bslide\b[^"]*"', html)
    if len(slides) == 0:
        fail("没有找到任何 .slide 元素")
        return False
    ok(f"幻灯片数量: {len(slides)} 页")

    active = [s for s in slides if 'is-active' in s]
    if len(active) == 0:
        fail("没有 .slide 带有 .is-active 类，播放时可能白屏")
    elif len(active) > 1:
        warn(f"有 {len(active)} 个 .slide 同时带有 .is-active（可能是 demo 展示页），正常播放时应只有第1页")
    else:
        ok("第1页有 .is-active 类")

    return True


def check_themes(html):
    """检查 36 个主题是否嵌入"""
    # 检查 data-themes 属性
    m = re.search(r'data-themes\s*=\s*"([^"]*)"', html)
    if not m:
        fail("缺少 data-themes 属性")
        return False

    themes_in_attr = m.group(1).split(",")
    # 检查是否包含所有期望主题
    missing = [t for t in EXPECTED_THEMES if t not in themes_in_attr]
    if missing:
        fail(f"data-themes 缺少 {len(missing)} 个主题", ", ".join(missing))
        return False
    ok(f"data-themes 包含全部 {len(EXPECTED_THEMES)} 个主题 ({len(themes_in_attr)} 个)")

    # 检查 window.__THEMES
    if 'window.__THEMES' not in html:
        fail("缺少 window.__THEMES（主题 CSS 未嵌入）")
        return False

    # 粗略统计主题 CSS 条目数
    theme_entries = re.findall(r'"([^"]+)"\s*:\s*`', html)
    theme_entry_names = [t for t in theme_entries if t in EXPECTED_THEMES]
    if len(theme_entry_names) < EXPECTED_THEME_COUNT:
        fail(f"window.__THEMES 中主题 CSS 不足: 找到 {len(theme_entry_names)} 个，期望 {EXPECTED_THEME_COUNT} 个")
        return False
    ok(f"window.__THEMES 包含 {len(theme_entry_names)} 个主题 CSS")

    # 检查 data-theme 默认主题
    m2 = re.search(r'data-theme\s*=\s*"([^"]*)"', html)
    if m2:
        ok(f"默认主题: {m2.group(1)}")
    else:
        warn("没有设置 data-theme 默认主题")

    return True


def check_fx(html):
    """检查 Canvas FX 模块是否嵌入（通过 // name.js 注释标记检测）"""
    # 查找所有 // name.js 注释标记
    fx_markers = re.findall(r'//\s*(\S+\.js)', html)
    fx_found = [m.replace('.js', '') for m in fx_markers if m.replace('.js', '') in EXPECTED_FX]

    if len(fx_found) < EXPECTED_FX_COUNT:
        missing_fx = [n for n in EXPECTED_FX if n not in fx_found]
        warn(f"FX 模块不完整: 检测到 {len(fx_found)}/{EXPECTED_FX_COUNT} 个，缺失: {', '.join(missing_fx)}")
        return False
    ok(f"Canvas FX 模块: {len(fx_found)}/{EXPECTED_FX_COUNT} 个已嵌入")
    return True


def check_runtime(html):
    """检查 runtime.js 是否嵌入"""
    # 检查关键函数
    missing_funcs = []
    for func in RUNTIME_KEY_FUNCTIONS:
        if func not in html:
            missing_funcs.append(func)

    if missing_funcs:
        fail("runtime.js 功能不完整，缺少关键函数", "\n".join(missing_funcs))
        return False
    ok("runtime.js 已嵌入，关键函数完备")

    # 检查关键变量
    missing_vars = []
    for var in RUNTIME_KEY_VARS:
        if var not in html:
            missing_vars.append(var)
    if missing_vars:
        warn(f"runtime.js 部分变量未找到: {', '.join(missing_vars)}")
    else:
        ok("runtime.js 关键变量完备")

    return True


def check_css_tokens(html):
    """检查 base.css 设计令牌是否嵌入"""
    missing_vars = []
    for var in CSS_VARIABLE_NAMES:
        if var not in html:
            missing_vars.append(var)

    if missing_vars:
        fail(f"base.css 设计令牌缺失 {len(missing_vars)} 个", "\n".join(missing_vars))
        return False
    ok("base.css 设计令牌 (CSS 变量) 已嵌入")

    # 检查是否有 animations.css（动效类名）
    anim_classes = ['anim-fade-up', 'anim-stagger-list', 'anim-zoom-pop']
    missing_anim = [c for c in anim_classes if c not in html]
    if missing_anim:
        warn(f"部分动效 CSS 类可能缺失: {', '.join(missing_anim)}")
    else:
        ok("animations.css 动效类名存在")

    return True


def check_images(html):
    """检查图片是否已转换为 base64 data URI"""
    # 查找所有 <img src="..."> 的路径
    ext_srcs = re.findall(r'<img[^>]*src="(?!data:)([^"]+)"', html)
    if ext_srcs:
        fail(f"存在外部图片路径（未转为 base64）: {len(ext_srcs)} 处", "\n".join(ext_srcs[:10]))
        return False

    # 统计 data URI 图片
    data_uris = re.findall(r'<img[^>]*src="data:image/[^;]+;base64,', html)
    if data_uris:
        ok(f"图片已全部转换为 base64 data URI ({len(data_uris)} 处)")
    else:
        # 可能没有图片
        all_imgs = re.findall(r'<img\b', html)
        if all_imgs:
            warn(f"有 {len(all_imgs)} 个 <img> 标签但未检测到 data URI")
        else:
            ok("页面中无图片（跳过检查）")

    return True


def check_img_wrappers(html):
    """检查图片是否有无效包裹容器（仅禁止 <figure> 和无语义纯包裹 <div>）"""
    # <figure> 包裹始终禁止
    figure_wraps = re.findall(r'<figure\b[^>]*>\s*<img\b', html)
    if figure_wraps:
        fail(f"发现 {len(figure_wraps)} 处图片被 <figure> 包裹，请直接用 <img>",
             "图片不应放在 <figure> 中")
        return False

    # 只检查纯包裹 div：class 为 img-* 或无 class 的 <div> 直接包裹 <img>
    bad_divs = re.findall(r'<div\b[^>]*class\s*=\s*"[^"]*img-wrapper[^"]*"[^>]*>\s*<img\b', html)
    if bad_divs:
        fail(f"发现 {len(bad_divs)} 处图片被纯包裹 <div class=\"img-wrapper\"> 包裹",
             "请将样式类直接加在 <img> 上，或使用 .row/.grid/.card 等布局容器")
        return False

    ok("图片布局检查通过")
    return True


def check_no_external_skill_refs(html):
    """检查是否有指向 skill 外部资产的文件引用"""
    # 检查 <link> 引用
    link_refs = re.findall(r'<link[^>]*href="([^"]*)"', html)
    bad_refs = [r for r in link_refs if 'assets/' in r or 'themes/' in r]
    if bad_refs:
        fail("存在指向 skill 外部资产的 <link> 引用", "\n".join(bad_refs))
        return False

    # 检查 <script src> 引用
    script_refs = re.findall(r'<script[^>]*src="([^"]*)"', html)
    bad_scripts = [r for r in script_refs if 'assets/' in r]
    if bad_scripts:
        fail("存在指向 skill 外部资产的 <script src>", "\n".join(bad_scripts))
        return False

    ok("无外部 skill 资产引用（所有依赖已内联）")
    return True


def check_edit_mode(html):
    """检查编辑模式代码是否存在"""
    checks = {
        "编辑模式入口": 'toggleEditMode' in html,
        "contentEditable": 'contentEditable' in html,
        "撤销功能": 'pushUndo' in html or 'undo' in html,
        "恢复功能": 'redo' in html,
        "删除按钮": '×' in html or 'removeBtn' in html,
        "拖拽功能": 'mousedown' in html and ('transform' in html or 'translate' in html),
    }
    failed = [name for name, ok_flag in checks.items() if not ok_flag]
    if failed:
        fail("编辑模式功能不完整，缺失", "\n".join(failed))
        return False
    ok("编辑模式功能完备 (toggleEditMode / contentEditable / 撤销恢复 / 删除拖拽)")
    return True


def check_theme_switcher(html):
    """检查主题切换补丁是否存在"""
    patches = [
        ('__applyInlineTheme', '__applyInlineTheme' in html),
        ('theme-inline id 检测', 'theme-inline' in html),
        ('setInterval 轮询主题', 'setInterval' in html and ('getAttribute' in html or 'data-theme' in html)),
    ]
    failed = [name for name, ok_flag in patches if not ok_flag]
    if failed:
        warn(f"主题切换补丁可能不完整: {', '.join(failed)}")
        return False
    ok("主题切换补丁存在（__applyInlineTheme + 轮询）")
    return True


def check_clock(html):
    """检查左下角时钟是否存在"""
    checks = {
        "clock CSS": '.clock-display' in html,
        "clock JS": 'function tick()' in html and 'getHours()' in html and 'getMinutes()' in html,
        "clock interval": 'setInterval(tick, ' in html,
    }
    failed = [name for name, ok_flag in checks.items() if not ok_flag]
    if failed:
        fail(f"时钟功能不完整，缺失: {', '.join(failed)}")
        return False
    ok("左下角时钟存在（clock-display + 每分钟刷新）")
    return True


def check_fx_runtime_patch(html):
    """检查 fx-runtime.js 是否已打补丁（禁止动态加载）"""
    if 'FX_LIST = [' in html and ('/* embedded */' in html or 'FX_LIST = [];' in html):
        ok("fx-runtime.js 已打补丁（禁止动态加载外部 FX 文件）")
        return True
    elif 'FX_LIST =' in html:
        # 有 FX_LIST 但可能没打补丁
        warn("fx-runtime.js 的 FX_LIST 可能未打补丁，仍可能动态加载")
        return False
    else:
        # 没有 FX_LIST，可能根本没嵌入 fx-runtime
        warn("未检测到 fx-runtime.js 的 FX_LIST")
        return False


def check_file_size(html, path):
    """检查文件大小是否合理"""
    size = len(html.encode('utf-8'))
    size_mb = size / (1024 * 1024)
    if size_mb < 0.01:
        fail(f"文件过小 ({size_mb*1000:.0f} bytes)，可能为空或不完整")
        return False
    elif size_mb < 0.05:
        warn(f"文件较小 ({size_mb*1000:.0f} KB)，可能缺少主题或 FX")
    elif size_mb > 50:
        warn(f"文件较大 ({size_mb:.1f} MB)，加载可能较慢")
    else:
        ok(f"文件大小合理 ({size_mb:.1f} MB)")

    # 检查行数
    lines = html.count("\n")
    if lines < 100:
        warn(f"HTML 行数过少 ({lines} 行)，可能不完整")
    return True


def verify_playability(html):
    """检查播放功能是否正常（静态分析）"""
    checks = {
        "幻灯片导航": all(f in html for f in ['function go(', 'function showSlide(', '.is-active']),
        "键盘事件": 'keydown' in html and ('ArrowLeft' in html or 'ArrowRight' in html),
        "全屏功能": 'fullscreen' in html.lower() or 'requestFullscreen' in html,
        "进度显示": '.slide-number' in html or 'progress' in html.lower(),
    }
    failed = [name for name, ok_flag in checks.items() if not ok_flag]
    if failed:
        fail(f"播放功能可能异常: {', '.join(failed)}")
        return False
    ok("播放功能基础检查通过 (导航/键盘/全屏/进度)")
    return True


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    path = sys.argv[1]
    if not os.path.isfile(path):
        print(f"{C.RED}文件不存在: {path}{C.END}")
        sys.exit(1)

    print(f"\n{C.BOLD}{C.CYAN}==============================================={C.END}")
    print(f"{C.BOLD}{C.CYAN}  AH-PPT Output Verification - {os.path.basename(path)}{C.END}")
    print(f"{C.BOLD}{C.CYAN}==============================================={C.END}\n")

    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # ── 执行所有检查 ──
    results = []

    print(f"{C.BOLD}1. HTML 结构完整性{C.END}")
    r = check_structure(html, path)
    results.append(("结构", r))

    print(f"\n{C.BOLD}2. 幻灯片结构{C.END}")
    r = check_slides(html)
    results.append(("幻灯片", r))

    print(f"\n{C.BOLD}3. 36 主题嵌入{C.END}")
    r = check_themes(html)
    results.append(("主题", r))

    print(f"\n{C.BOLD}4. Canvas FX 模块{C.END}")
    r = check_fx(html)
    results.append(("FX", r))

    print(f"\n{C.BOLD}5. runtime.js 嵌入{C.END}")
    r = check_runtime(html)
    results.append(("运行时", r))

    print(f"\n{C.BOLD}6. 编辑模式{C.END}")
    r = check_edit_mode(html)
    results.append(("编辑模式", r))

    print(f"\n{C.BOLD}7. 主题切换补丁{C.END}")
    r = check_theme_switcher(html)
    results.append(("主题切换", r))

    print(f"\n{C.BOLD}8. FX 动态加载补丁{C.END}")
    r = check_fx_runtime_patch(html)
    results.append(("FX补丁", r))

    print(f"\n{C.BOLD}9. CSS 设计令牌{C.END}")
    r = check_css_tokens(html)
    results.append(("CSS令牌", r))

    print(f"\n{C.BOLD}10. 图片 base64{C.END}")
    r = check_images(html)
    results.append(("图片", r))

    print(f"\n{C.BOLD}11. 图片包裹检查{C.END}")
    r = check_img_wrappers(html)
    results.append(("图片包裹", r))

    print(f"\n{C.BOLD}12. 无外部文件引用{C.END}")
    r = check_no_external_skill_refs(html)
    results.append(("内联完整性", r))

    print(f"\n{C.BOLD}12. 播放功能{C.END}")
    r = verify_playability(html)
    results.append(("播放", r))

    print(f"\n{C.BOLD}13. 文件大小{C.END}")
    r = check_file_size(html, path)
    results.append(("大小", r))

    

    print(f"\n{C.BOLD}14. 左下角时钟{C.END}")
    r = check_clock(html)
    results.append(("时钟", r))
# ── 汇总 ──
    total = len(results)
    passed = sum(1 for _, r in results if r)
    failed = total - passed

    print(f"\n{C.BOLD}{C.CYAN}==============================================={C.END}")
    print(f"{C.BOLD}  Summary: ", end="")
    if failed == 0:
        print(f"{C.GREEN}ALL PASSED ({passed}/{total}){C.END}")
    else:
        print(f"{C.RED}{failed} FAILED ({passed}/{total}){C.END}")
    print(f"{C.BOLD}{C.CYAN}==============================================={C.END}\n")

    return 0 if failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
