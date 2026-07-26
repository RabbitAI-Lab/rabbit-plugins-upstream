#!/usr/bin/env python3
"""
Logo颜色提取工具
用法: python extract_colors.py <logo_image_path> [--top N]
输出: JSON格式的主色调列表和建议主题配置
"""

import sys
import json
import math

def extract_colors(image_path, top_n=3):
    """从图片提取主色调，返回HEX列表"""
    try:
        from PIL import Image
    except ImportError:
        print("安装 Pillow: pip install pillow --break-system-packages", file=sys.stderr)
        sys.exit(1)
    
    img = Image.open(image_path).convert('RGB').resize((200, 200), Image.LANCZOS)
    pixels = list(img.getdata())
    
    # 过滤背景色（白/黑/浅灰）
    def is_background(r, g, b):
        brightness = (r + g + b) / 3
        saturation = max(r, g, b) - min(r, g, b)
        return brightness > 235 or brightness < 20 or saturation < 25
    
    filtered = [(r, g, b) for r, g, b in pixels if not is_background(r, g, b)]
    
    if not filtered:
        return ['#4A7C59', '#C97040']  # 默认橙绿主题
    
    # 颜色量化（32色桶）
    from collections import Counter
    quantized = [(r // 32 * 32 + 16, g // 32 * 32 + 16, b // 32 * 32 + 16)
                 for r, g, b in filtered]
    counter = Counter(quantized)
    
    # 取最常见的颜色
    top_colors = counter.most_common(top_n * 3)
    
    # 去重（颜色距离过近则合并）
    def color_distance(c1, c2):
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(c1, c2)))
    
    deduplicated = []
    for color, count in top_colors:
        if all(color_distance(color, c) > 60 for c in deduplicated):
            deduplicated.append(color)
        if len(deduplicated) >= top_n:
            break
    
    return [f"#{r:02X}{g:02X}{b:02X}" for r, g, b in deduplicated]


def rgb_to_hsl(hex_color):
    """HEX转HSL"""
    r, g, b = int(hex_color[1:3], 16)/255, int(hex_color[3:5], 16)/255, int(hex_color[5:7], 16)/255
    max_c, min_c = max(r, g, b), min(r, g, b)
    l = (max_c + min_c) / 2
    if max_c == min_c:
        h = s = 0
    else:
        d = max_c - min_c
        s = d / (2 - max_c - min_c) if l > 0.5 else d / (max_c + min_c)
        if max_c == r:   h = (g - b) / d + (6 if g < b else 0)
        elif max_c == g: h = (b - r) / d + 2
        else:            h = (r - g) / d + 4
        h /= 6
    return h * 360, s * 100, l * 100


def hsl_to_hex(h, s, l):
    """HSL转HEX"""
    h, s, l = h / 360, s / 100, l / 100
    if s == 0:
        r = g = b = l
    else:
        def hue2rgb(p, q, t):
            if t < 0: t += 1
            if t > 1: t -= 1
            if t < 1/6: return p + (q - p) * 6 * t
            if t < 1/2: return q
            if t < 2/3: return p + (q - p) * (2/3 - t) * 6
            return p
        q = l * (1 + s) if l < 0.5 else l + s - l * s
        p = 2 * l - q
        r, g, b = hue2rgb(p, q, h + 1/3), hue2rgb(p, q, h), hue2rgb(p, q, h - 1/3)
    return f"#{int(r*255):02X}{int(g*255):02X}{int(b*255):02X}"


def adjust_color(hex_color, lightness_delta=0, saturation_delta=0):
    """调整颜色明度/饱和度"""
    h, s, l = rgb_to_hsl(hex_color)
    l = max(0, min(100, l + lightness_delta))
    s = max(0, min(100, s + saturation_delta))
    return hsl_to_hex(h, s, l)


def build_theme_from_colors(primary, accent=None):
    """从主色辅色生成完整CSS主题"""
    
    if not accent:
        # 辅色：主色色相+150度
        h, s, l = rgb_to_hsl(primary)
        accent = hsl_to_hex((h + 150) % 360, s, l)
    
    # 判断主色亮暗
    _, _, l = rgb_to_hsl(primary)
    is_light_primary = l > 50
    
    # 生成配色变量
    theme = {
        'css_vars': {
            '--bg': adjust_color(primary, lightness_delta=45, saturation_delta=-30),
            '--s1': '#FFFFFF',
            '--s2': adjust_color(primary, lightness_delta=40, saturation_delta=-20),
            '--bd': adjust_color(primary, lightness_delta=30, saturation_delta=-15),
            '--c1': primary,
            '--c2': accent,
            '--c3': adjust_color(accent, lightness_delta=10),
            '--c4': adjust_color(primary, lightness_delta=8),
            '--red': '#B04848',
            '--t': '#1A1A1A',
            '--mu': '#666666',
            '--mu2': '#CCCCCC',
            '--tx': '#333333',
        },
        'hero_bg': f"linear-gradient(135deg,{adjust_color(primary, -5)} 0%,{adjust_color(primary, -15)} 50%,{adjust_color(primary, -25)} 100%)",
        'tab_bg': adjust_color(primary, -20) if is_light_primary else adjust_color(primary, -10),
        'tab_border': adjust_color(primary, -30),
        'hero_border': adjust_color(primary, -35),
        'chart_colors': {
            'C1': primary,
            'C2': accent,
            'C3': adjust_color(accent, 10),
            'C4': adjust_color(primary, 8),
            'RED': '#B04848',
        }
    }
    return theme


def generate_css(theme):
    """生成可直接嵌入HTML的CSS片段"""
    vars_css = '\n'.join(f"  {k}:{v};" for k, v in theme['css_vars'].items())
    
    return f""":root {{
{vars_css}
  --hero-bg: {theme['hero_bg']};
  --tab-bg: {theme['tab_bg']};
  --tab-border: {theme['tab_border']};
  --hero-border: {theme['hero_border']};
}}"""


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='从Logo图片提取配色主题')
    parser.add_argument('image', help='Logo图片路径')
    parser.add_argument('--top', type=int, default=2, help='提取颜色数量（默认2）')
    parser.add_argument('--accent', help='手动指定辅色HEX（如 #E8631A）')
    parser.add_argument('--output', choices=['json', 'css', 'both'], default='both')
    args = parser.parse_args()
    
    colors = extract_colors(args.image, args.top)
    primary = colors[0]
    accent = args.accent or (colors[1] if len(colors) > 1 else None)
    
    theme = build_theme_from_colors(primary, accent)
    
    if args.output in ('json', 'both'):
        print("=== 提取的颜色 ===")
        print(f"主色: {primary}")
        print(f"辅色: {accent}")
        print(f"\n=== 完整主题 ===")
        print(json.dumps(theme, ensure_ascii=False, indent=2))
    
    if args.output in ('css', 'both'):
        print("\n=== CSS变量（直接粘贴到HTML）===")
        print(generate_css(theme))
