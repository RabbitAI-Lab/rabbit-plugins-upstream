#!/usr/bin/env python3
"""gen-site-themes.py — 由 config/themes/*.json 生成站点主题产物。

两份产物：
  1. docs/themes/index.html 的主题卡片（默认模式 / --check）
  2. docs/assets/t-live.css —— 「活终端」组件的每主题 CSS 变量（css 子命令）

用法：
  python3 scripts/gen-site-themes.py              # 原地重写 index.html 标记间内容
  python3 scripts/gen-site-themes.py --check      # 只检查主题卡 + t-live.css，不一致 exit 1
  python3 scripts/gen-site-themes.py css [路径]   # 生成 t-live.css（默认 docs/assets/t-live.css）

卡片生成逻辑：
  按固定顺序（catppuccin-mocha, tokyo-night, gruvbox-dark, ember, voltage,
  parchment, ledger）读各主题 JSON（判据同 scripts/theme.sh 的 is_theme_json：
  含 "Profiles" 键才是主题，names.json 这类边表自动跳过），换算 BG/FG/CURSOR
  chips + ANSI 0-15 十六色块（Red/Green/Blue Component 浮点 → #rrggbb），前 3 套
  标 free、其余标 paid，亮暗按背景亮度判定，生成与现有 tcard 结构完全一致的
  HTML 片段。显示名取 config/themes/names.json（en/zh）。

t-live.css 生成逻辑：
  每套主题两行 —— [data-tlive="<name>"] 挂 --t-bg/--t-fg/--t-cur/--t-sel 与
  --t-a0…--t-a15 共 20 个变量；.t-dot[data-theme="<name>"] 给主题圆点上底色
  （取 --t-bg 同值 hex）。Selection 取 "Selection Background"，旧文件只有
  "Selection Color" 时回退取之。

什么时候重跑（防漂移）：
  改了任何 config/themes/<主题>.json 的色值、names.json 的显示名，或主题增删
  之后，重跑一次让两份产物与色板真相源对齐：
      python3 scripts/gen-site-themes.py            # 原地重写标记间内容
      python3 scripts/gen-site-themes.py css        # 重写 t-live.css
      python3 scripts/gen-site-themes.py --check    # 只检查，不一致 exit 1
  ⛔ 标记不存在时直接报错退出，绝不盲写 —— 标记由 HTML 维护方负责插入。
"""

import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
THEMES_DIR = ROOT / "config" / "themes"
TARGET = ROOT / "docs" / "themes" / "index.html"
TLIVE_TARGET = ROOT / "docs" / "assets" / "t-live.css"

BEGIN = "<!-- BEGIN:GENERATED:THEMES -->"
END = "<!-- END:GENERATED:THEMES -->"

# 画廊固定顺序；前 3 套免费（社区色），其余付费（品牌色）
ORDER = ["catppuccin-mocha", "tokyo-night", "gruvbox-dark", "ember", "voltage", "parchment", "ledger"]
FREE_COUNT = 3

# 卡片之间/之后的固定文案（与现页逐字一致；改文案要同步这里）
PROSE_FREE = (
    '<h2><span class="en">Free · community</span><span class="zh">免费 · 社区</span></h2>\n'
    '<p><span class="en">These three ship in the lite build. Switch by name, or use the picker for a live preview.</span>'
    '<span class="zh">这三套随 Lite 版交付。按名切换，或用选肤器看实时预览。</span></p>'
)
PROSE_PAID = (
    '<h2><span class="en">Paid · brand</span><span class="zh">付费 · 品牌</span> <span class="tag tag-paid">paid</span></h2>\n'
    '<p><span class="en">Ember and Voltage are dark; Parchment and Ledger are light. They ship only with the Pro build '
    '— shown here for the look and the measured colors, not as a do-it-yourself recipe.</span>'
    '<span class="zh">Ember、Voltage 为暗色；Parchment、Ledger 为亮色。只在付费包内交付 —— '
    '这里展示观感与实测色值，不提供自制配方。</span></p>'
)


def is_theme_json(path: Path) -> bool:
    """判据与 scripts/theme.sh 的 is_theme_json 一致：含 "Profiles" 键才是主题。"""
    try:
        return "Profiles" in json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return False


def hex_of(color: dict) -> str:
    """iTerm2 的 Red/Green/Blue Component 浮点 → #rrggbb（小写）。"""
    chan = []
    for k in ("Red Component", "Green Component", "Blue Component"):
        v = round(float(color.get(k, 0.0)) * 255)
        chan.append(min(255, max(0, v)))
    return "#%02x%02x%02x" % tuple(chan)


def is_light(bg: dict) -> bool:
    """背景是不是亮底：sRGB 线性化后按亮度加权，≥0.5 为亮。"""
    def lin(c: float) -> float:
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (float(bg.get(k, 0.0)) for k in ("Red Component", "Green Component", "Blue Component"))
    return (0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)) >= 0.5


def swatch(i: int, hx: str) -> str:
    return (
        f'<div class="sw" role="listitem" title="ANSI {i} · {hx}">'
        f'<i style="background:{hx}"></i>'
        f'<div class="sw-meta"><span class="n">{i:02d}</span><code>{hx}</code></div></div>'
    )


def card(name: str, idx: int, prof: dict, names: dict) -> str:
    free = idx < FREE_COUNT
    tier = "free" if free else "paid"
    mode = "light" if is_light(prof.get("Background Color", {})) else "dark"
    mode_zh = "亮色" if mode == "light" else "暗色"
    disp = names.get(name, {})
    en = html.escape(disp.get("en") or name)
    zh = html.escape(disp.get("zh") or name)

    bg = hex_of(prof.get("Background Color", {}))
    fg = hex_of(prof.get("Foreground Color", {}))
    cur = hex_of(prof.get("Cursor Color", prof.get("Foreground Color", {})))

    lines = [
        f'<article class="tcard {tier} {mode}" id="{html.escape(name)}">',
        '  <div class="tcard-hd">',
        '    <div class="tcard-id">',
        f'      <div class="tno">{idx + 1:02d} · {tier.upper()} · {mode.upper()}</div>',
        f'      <h3><span class="en">{en}</span><span class="zh">{zh}</span></h3>',
        f'      <div class="tslug"><code>{html.escape(name)}</code></div>',
        '    </div>',
        '    <div class="ttags">',
        f'      <span class="tag tag-{tier}">{tier}</span>',
        f'      <span class="tag tag-mode"><span class="en">{mode}</span><span class="zh">{mode_zh}</span></span>',
        '    </div>',
        '  </div>',
        '  <div class="tchips">',
        f'    <span class="tchip"><b>BG</b><i style="background:{bg}"></i><code>{bg}</code></span>',
        f'    <span class="tchip"><b>FG</b><i style="background:{fg}"></i><code>{fg}</code></span>',
        f'    <span class="tchip"><b>CURSOR</b><i style="background:{cur}"></i><code>{cur}</code></span>',
        '  </div>',
        '  <div class="swatches" role="list" aria-label="ANSI 0-15">',
    ]
    swatches = "".join(
        swatch(i, hex_of(prof.get(f"Ansi {i} Color", {}))) for i in range(16)
    )
    lines.append("    " + swatches)
    foot_tag = (
        '<span class="tag tag-free"><span class="en">free</span><span class="zh">免费</span></span>'
        if free
        else '<span class="tag tag-paid"><span class="en">paid</span><span class="zh">付费</span></span>'
    )
    lines += [
        '  </div>',
        f'  <div class="tfoot"><code>./scripts/theme.sh {html.escape(name)}</code>{foot_tag}</div>',
        '</article>',
    ]
    return "\n".join(lines)


def generate() -> str:
    names = json.loads((THEMES_DIR / "names.json").read_text(encoding="utf-8"))
    free_cards, paid_cards = [], []
    for name in ORDER:
        prof = load_profile(name)
        idx = ORDER.index(name)
        (free_cards if idx < FREE_COUNT else paid_cards).append(card(name, idx, prof, names))

    parts = [PROSE_FREE, '<div class="tgrid">', *free_cards, "</div>", "", PROSE_PAID, '<div class="tgrid">', *paid_cards, "</div>"]
    return "\n".join(parts)


def load_profile(name: str) -> dict:
    """读某主题的 Profiles[0]；缺文件或缺 Profiles 键直接退出。"""
    path = THEMES_DIR / f"{name}.json"
    if not is_theme_json(path):
        print(f"✗ 缺主题文件或不是主题（无 Profiles 键）：{path.relative_to(ROOT)}", file=sys.stderr)
        sys.exit(1)
    return json.loads(path.read_text(encoding="utf-8"))["Profiles"][0]


def tlive_vars(prof: dict) -> str:
    """Profiles[0] → 一串 CSS 自定义属性：--t-bg/--t-fg/--t-cur/--t-sel + --t-a0…15。"""
    sel = prof.get("Selection Background") or prof.get("Selection Color") or {}
    base = [
        ("--t-bg", prof.get("Background Color", {})),
        ("--t-fg", prof.get("Foreground Color", {})),
        ("--t-cur", prof.get("Cursor Color", {})),
        ("--t-sel", sel),
    ]
    parts = [f"{k}:{hex_of(v)}" for k, v in base]
    for i in range(16):
        ansi = prof.get(f"Ansi {i} Color", {})
        parts.append(f"--t-a{i}:{hex_of(ansi)}")
    return ";".join(parts)


def tlive_css() -> str:
    """7 套主题 ×（变量组 + 圆点底色）→ t-live.css 全文。"""
    lines = [
        "/* t-live.css — 由 scripts/gen-site-themes.py 产出，勿手改。",
        "   重生成：python3 scripts/gen-site-themes.py css",
        "   校验：  python3 scripts/gen-site-themes.py --check */",
        "",
    ]
    for name in ORDER:
        prof = load_profile(name)
        bg = hex_of(prof.get("Background Color", {}))
        lines.append(f'[data-tlive="{name}"]{{{tlive_vars(prof)}}}')
        lines.append(f'.t-dot[data-theme="{name}"]{{background:{bg}}}')
    return "\n".join(lines) + "\n"


def check_tlive() -> bool:
    """--check 的 t-live.css 部分：与生成结果逐字一致才算过。"""
    if not TLIVE_TARGET.exists():
        print(f"✗ {TLIVE_TARGET.relative_to(ROOT)} 不存在 —— 先跑 python3 scripts/gen-site-themes.py css")
        return False
    current = TLIVE_TARGET.read_text(encoding="utf-8")
    if current == tlive_css():
        print(f"✓ {TLIVE_TARGET.relative_to(ROOT)} 与 config/themes 一致")
        return True
    print(f"✗ {TLIVE_TARGET.relative_to(ROOT)} 与 config/themes 不一致 —— 重跑 scripts/gen-site-themes.py css")
    cur_lines, gen_lines = current.splitlines(), tlive_css().splitlines()
    for i, (a, b2) in enumerate(zip(cur_lines, gen_lines)):
        if a != b2:
            print(f"  首个差异在第 {i + 1} 行：")
            print(f"    现有: {a[:160]}")
            print(f"    生成: {b2[:160]}")
            break
    else:
        print(f"  行数不同：现有 {len(cur_lines)} 行 vs 生成 {len(gen_lines)} 行")
    return False


def locate(src: str) -> tuple[int, int] | None:
    """返回标记间内容的 (start, end)；标记缺失返回 None。"""
    b = src.find(BEGIN)
    if b == -1:
        return None
    b += len(BEGIN)
    e = src.find(END, b)
    if e == -1:
        return None
    return b, e


def main() -> int:
    argv = sys.argv[1:]

    # css 子命令：生成 t-live.css（默认 docs/assets/t-live.css，可传自定义路径）
    if argv and argv[0] == "css":
        out = Path(argv[1]) if len(argv) > 1 else TLIVE_TARGET
        try:
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(tlive_css(), encoding="utf-8")
        except OSError as exc:
            print(f"✗ 写 {out} 失败：{exc}", file=sys.stderr)
            return 1
        print(f"✓ 已生成 {out}（{len(ORDER)} 套主题 ×（变量组 + 圆点配色））")
        return 0

    check = "--check" in argv
    src = TARGET.read_text(encoding="utf-8")
    block = generate()
    span = locate(src)
    ok_html: bool
    if check:
        if span is None:
            print(f"✗ {TARGET.relative_to(ROOT)} 缺少 {BEGIN} / {END} 标记 —— 先插标记再跑 --check")
            ok_html = False
        else:
            current = src[span[0]:span[1]].strip()
            if current == block.strip():
                print(f"✓ {TARGET.relative_to(ROOT)} 主题卡与 config/themes 一致")
                ok_html = True
            else:
                print(f"✗ {TARGET.relative_to(ROOT)} 主题卡与 config/themes 不一致 —— 重跑 scripts/gen-site-themes.py 重写")
                cur_lines, gen_lines = current.splitlines(), block.strip().splitlines()
                for i, (a, b2) in enumerate(zip(cur_lines, gen_lines)):
                    if a != b2:
                        print(f"  首个差异在第 {i + 1} 行：")
                        print(f"    现有: {a[:160]}")
                        print(f"    生成: {b2[:160]}")
                        break
                else:
                    print(f"  行数不同：现有 {len(cur_lines)} 行 vs 生成 {len(gen_lines)} 行")
                ok_html = False
        ok_css = check_tlive()
        return 0 if (ok_html and ok_css) else 1

    # 默认模式：原地重写标记间内容；标记不存在则报错退出，不盲写
    if span is None:
        print(f"✗ {TARGET.relative_to(ROOT)} 缺少 {BEGIN} / {END} 标记，拒绝盲写 —— 标记由 HTML 维护方插入", file=sys.stderr)
        return 1
    out = src[:span[0]] + "\n" + block + "\n" + src[span[1]:]
    TARGET.write_text(out, encoding="utf-8")
    print(f"✓ 已重写 {TARGET.relative_to(ROOT)} 标记间内容（{len(ORDER)} 套主题卡）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
