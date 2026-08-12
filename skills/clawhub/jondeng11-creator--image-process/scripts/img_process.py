#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
图片处理小工具 img_process.py
基于 Pillow，功能：改尺寸 / 转格式 / 裁白边 / 缩略图 / 压缩优化 / 生成分享图 / 批量处理 / 去背景
普通用户只需要先执行一次  pip install Pillow  就能用。
（去背景功能需要额外执行一次  pip install rembg，首次运行会联网下载约 176MB 模型，之后离线可用。）
"""

import os
import sys
import argparse
from PIL import Image, ImageDraw, ImageFont, ImageOps


# ---------- 基础工具函数 ----------

def open_img(path):
    """打开图片，出错时给普通人能看懂的提示。"""
    if not os.path.exists(path):
        sys.exit(f"找不到文件：{path}\n请检查路径是否写对（Windows 路径用 \\ 或 / 都可以）。")
    return Image.open(path)


def save_img(img, out_path, quality=None):
    """保存图片，自动处理不同格式的保存参数；JPG 不支持透明，自动垫白底。"""
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    ext = out_path.lower().rsplit(".", 1)[-1]
    kwargs = {}
    if ext == "webp":
        kwargs = {"quality": quality or 85, "method": 6}
    elif ext in ("jpg", "jpeg"):
        kwargs = {"quality": quality or 90, "optimize": True}
        if img.mode == "RGBA":  # JPG 没有透明通道，先垫白底
            bg = Image.new("RGB", img.size, (255, 255, 255))
            bg.paste(img, mask=img.split()[3])
            img = bg
    elif ext == "png":
        kwargs = {"optimize": True}
    img.save(out_path, **kwargs)
    return out_path


def resize_keep_ratio(img, width=None, height=None):
    """只给一边时，按比例算另一边；保证不变形。"""
    if width and height:
        return img.resize((width, height), Image.LANCZOS)
    if width:
        ratio = width / img.width
        return img.resize((width, int(img.height * ratio)), Image.LANCZOS)
    if height:
        ratio = height / img.height
        return img.resize((int(img.width * ratio), height), Image.LANCZOS)
    return img


def auto_trim(img, padding=0):
    """自动裁掉四周空白/透明边；padding 可留一点边距。"""
    if img.mode != "RGBA":
        img = img.convert("RGBA")
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
    if padding > 0:
        img = ImageOps.expand(img, border=padding, fill=(255, 255, 255, 0))
    return img


def get_font(size):
    """跨平台找系统中文字体，找不到就用默认字体（不报错）。"""
    candidates = [
        # Windows
        "C:/Windows/Fonts/msyh.ttc",        # 微软雅黑
        "C:/Windows/Fonts/simhei.ttf",       # 黑体
        "C:/Windows/Fonts/arial.ttf",
        # macOS
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/Helvetica.ttc",
        # Linux
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for p in candidates:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue
    return ImageFont.load_default()


def file_size(path):
    return os.path.getsize(path)


def size_text(bytes_):
    if bytes_ < 1024:
        return f"{bytes_} B"
    if bytes_ < 1024 * 1024:
        return f"{bytes_ / 1024:.0f} KB"
    return f"{bytes_ / 1024 / 1024:.2f} MB"


def default_out(input_path, suffix, ext=None):
    """没指定输出名时，自动起一个不覆盖原图的名字。"""
    stem, old = os.path.splitext(input_path)
    return stem + suffix + (ext or old)


def report(out_path, src_size=None):
    new_size = file_size(out_path)
    msg = f"✓ 已生成：{out_path}（{size_text(new_size)}）"
    if src_size is not None:
        if new_size < src_size:
            msg += f"  体积从 {size_text(src_size)} 降到 {size_text(new_size)}，省了 {100 * (1 - new_size / src_size):.0f}%"
        else:
            msg += f"  原体积 {size_text(src_size)}"
    print(msg)


# ---------- 各功能 ----------

def cmd_resize(args):
    img = open_img(args.input)
    out = args.output or default_out(args.input, "_resized")
    src = file_size(args.input)
    result = resize_keep_ratio(img, args.width, args.height)
    save_img(result, out)
    report(out, src)


def cmd_convert(args):
    img = open_img(args.input)
    out = args.output or default_out(args.input, "", "." + args.format)
    src = file_size(args.input)
    save_img(img, out, quality=args.quality)
    report(out, src)


def cmd_trim(args):
    img = open_img(args.input)
    out = args.output or default_out(args.input, "_trimmed")
    src = file_size(args.input)
    result = auto_trim(img, padding=args.padding)
    save_img(result, out)
    report(out, src)


def cmd_thumbnail(args):
    img = open_img(args.input)
    out = args.output or default_out(args.input, "_thumb")
    src = file_size(args.input)
    img.thumbnail((args.size, args.size), Image.LANCZOS)
    save_img(img, out)
    report(out, src)


def cmd_optimise(args):
    img = open_img(args.input)
    out = args.output or default_out(args.input, "_opt", ".webp")
    src = file_size(args.input)
    if args.max_width and img.width > args.max_width:
        img = resize_keep_ratio(img, width=args.max_width)
    save_img(img, out, quality=args.quality)
    report(out, src)


def cmd_og_card(args):
    w, h = 1200, 630
    if args.background and os.path.exists(args.background):
        bg = Image.open(args.background).convert("RGB").resize((w, h), Image.LANCZOS)
        base = Image.new("RGBA", (w, h), (255, 255, 255, 0))
        base = Image.alpha_composite(base, bg.convert("RGBA"))
    else:
        base = Image.new("RGBA", (w, h), args.bg_color or "#1a1a2e")
    # 半透明黑底，让文字更清楚
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 140))
    base = Image.alpha_composite(base, overlay)
    draw = ImageDraw.Draw(base)
    if args.title:
        f_title = get_font(56)
        b = draw.textbbox((0, 0), args.title, font=f_title)
        tw = b[2] - b[0]
        draw.text(((w - tw) // 2, h // 2 - 70), args.title, fill="white", font=f_title)
    if args.subtitle:
        f_sub = get_font(28)
        b = draw.textbbox((0, 0), args.subtitle, font=f_sub)
        sw = b[2] - b[0]
        draw.text(((w - sw) // 2, h // 2 + 10), args.subtitle, fill="#dddddd", font=f_sub)
    out = args.output or "og-card.png"
    save_img(base.convert("RGB"), out)
    report(out)


def cmd_batch(args):
    if not os.path.isdir(args.input):
        sys.exit(f"找不到文件夹：{args.input}")
    os.makedirs(args.output, exist_ok=True)
    count = 0
    for name in os.listdir(args.input):
        if not name.lower().endswith((".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tiff", ".gif")):
            continue
        src_path = os.path.join(args.input, name)
        dst_path = os.path.join(args.output, name)
        img = Image.open(src_path)
        if args.action == "resize":
            img = resize_keep_ratio(img, args.width, args.height)
        elif args.action == "convert":
            dst_path = os.path.splitext(dst_path)[0] + "." + args.format
            save_img(img, dst_path, quality=args.quality)
            count += 1
            print(f"  ✓ {name} -> {os.path.basename(dst_path)}")
            continue
        elif args.action == "trim":
            img = auto_trim(img, padding=args.padding)
        elif args.action == "thumbnail":
            img.thumbnail((args.size, args.size), Image.LANCZOS)
        elif args.action == "optimise":
            if args.max_width and img.width > args.max_width:
                img = resize_keep_ratio(img, width=args.max_width)
            dst_path = os.path.splitext(dst_path)[0] + ".webp"
            save_img(img, dst_path, quality=args.quality)
            count += 1
            print(f"  ✓ {name} -> {os.path.basename(dst_path)}")
            continue
        save_img(img, dst_path, quality=args.quality)
        count += 1
        print(f"  ✓ {name} -> {os.path.basename(dst_path)}")
    print(f"批量处理完成，共处理 {count} 张图片，输出到：{args.output}")


def cmd_remove_bg(args):
    try:
        from rembg import remove
    except ImportError:
        sys.exit("去背景功能需要先安装 rembg，请执行：\n  pip install rembg\n安装完成后再试一次。")
    img = open_img(args.input).convert("RGBA")
    src = file_size(args.input)
    print("正在去背景…（首次运行会联网下载模型，约 176MB，请稍候）")
    out_img = remove(img)
    out = args.output or default_out(args.input, "_nobg", ".png")
    save_img(out_img, out)
    report(out, src)


# ---------- 命令行入口 ----------

def build_parser():
    p = argparse.ArgumentParser(
        description="图片处理小工具：改尺寸 / 转格式 / 裁白边 / 缩略图 / 压缩 / 分享图 / 批量",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("resize", help="改尺寸（只给一边会自动按比例）")
    sp.add_argument("input")
    sp.add_argument("--width", type=int)
    sp.add_argument("--height", type=int)
    sp.add_argument("--output", "-o")
    sp.set_defaults(func=cmd_resize)

    sp = sub.add_parser("convert", help="转换格式（如 webp / png / jpg）")
    sp.add_argument("input")
    sp.add_argument("--format", required=True, choices=["webp", "png", "jpg", "jpeg"])
    sp.add_argument("--quality", type=int)
    sp.add_argument("--output", "-o")
    sp.set_defaults(func=cmd_convert)

    sp = sub.add_parser("trim", help="自动裁掉四周空白/透明边")
    sp.add_argument("input")
    sp.add_argument("--padding", type=int, default=0, help="裁剪后留的边距像素")
    sp.add_argument("--output", "-o")
    sp.set_defaults(func=cmd_trim)

    sp = sub.add_parser("thumbnail", help="生成缩略图（限制最长边）")
    sp.add_argument("input")
    sp.add_argument("--size", type=int, required=True, help="最长边像素，如 200")
    sp.add_argument("--output", "-o")
    sp.set_defaults(func=cmd_thumbnail)

    sp = sub.add_parser("optimise", help="压缩优化（默认转 WebP）")
    sp.add_argument("input")
    sp.add_argument("--max-width", type=int, help="超过此宽度则缩小")
    sp.add_argument("--quality", type=int, default=85)
    sp.add_argument("--output", "-o")
    sp.set_defaults(func=cmd_optimise)

    sp = sub.add_parser("og-card", help="生成 1200x630 社交分享图")
    sp.add_argument("--title", default="")
    sp.add_argument("--subtitle", default="")
    sp.add_argument("--bg-color", default="#1a1a2e")
    sp.add_argument("--background", default=None, help="可选：用一张图片做底图")
    sp.add_argument("--output", "-o", default="og-card.png")
    sp.set_defaults(func=cmd_og_card)

    sp = sub.add_parser("batch", help="批量处理整个文件夹")
    sp.add_argument("input", help="源文件夹")
    sp.add_argument("--action", required=True, choices=["resize", "convert", "trim", "thumbnail", "optimise"])
    sp.add_argument("--output", required=True, help="输出文件夹")
    sp.add_argument("--format", choices=["webp", "png", "jpg", "jpeg"])
    sp.add_argument("--width", type=int)
    sp.add_argument("--height", type=int)
    sp.add_argument("--size", type=int)
    sp.add_argument("--max-width", type=int)
    sp.add_argument("--quality", type=int, default=85)
    sp.add_argument("--padding", type=int, default=0)
    sp.set_defaults(func=cmd_batch)

    sp = sub.add_parser("remove-bg", help="去掉背景，输出带透明的 PNG（需先 pip install rembg）")
    sp.add_argument("input")
    sp.add_argument("--output", "-o")
    sp.set_defaults(func=cmd_remove_bg)

    return p


if __name__ == "__main__":
    args = build_parser().parse_args()
    args.func(args)
