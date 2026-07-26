#!/usr/bin/env python3
"""
folder-icon (方案B - MDI)：为子文件夹批量生成并应用彩色图标。

使用 Material Design Icons (MDI)，图标直接放在每个子文件夹内部（folder.ico），
而非集中存放在独立目录。适合简单扁平的目录结构。

用法:
    python folder_icon_mdi.py "D:\目标目录" [--force]
    python folder_icon_mdi.py "D:\目标目录" --map-only  # 仅显示映射表，不做任何操作

依赖: pip install Pillow cairosvg
"""

import io
import os
import struct
import subprocess
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw
except ImportError:
    print("请安装 Pillow: pip install Pillow")
    sys.exit(1)

try:
    import cairosvg
except ImportError:
    print("请安装 cairosvg: pip install cairosvg")
    sys.exit(1)


# =============================================================================
# MDI 图标映射配置
# 格式: "子文件夹名": ("mdi-icon-name", "HEXCOLOR")
# =============================================================================
ICON_MAP = {
    # 示例映射（使用时替换为你自己的文件夹名和图标）
    "ProjectA":                     ("shield-lock", "E84D39"),
    "ProjectB":                     ("application-braces", "0078D4"),
    "ProjectC":                     ("bug", "FF5722"),
    "ProjectD":                     ("calendar-clock", "2196F3"),
    "ProjectE":                     ("chat", "07C160"),
    "ProjectF":                     ("microsoft-windows", "0078D4"),
    "ProjectG":                     ("source-repository-multiple", "333333"),
    "ProjectH":                     ("bookmark-multiple", "E91E63"),
    "ProjectI":                     ("package-variant-closed", "009688"),
    "ProjectJ":                     ("book-open-variant", "607D8B"),
}

# 可以为其他项目添加新的映射块，注释说明目标路径
# 例如：
# MY_OTHER_PROJECT = {
#     "SubfolderA": ("icon-name", "HEXCOLOR"),
# }

# 将所有映射块合并
ALL_MAPS = {}
ALL_MAPS.update(ICON_MAP)

ICO_SIZES = [16, 24, 32, 48, 64, 128, 256]
MDI_BASE = "https://raw.githubusercontent.com/Templarian/MaterialDesign/master/svg"


# =============================================================================
def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def fetch_svg(icon_name):
    """从 MDI GitHub 仓库获取 SVG 内容"""
    import urllib.request
    url = f"{MDI_BASE}/{icon_name}.svg"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.read().decode("utf-8")
    except Exception as e:
        print(f"    ⚠ 无法获取 SVG '{icon_name}': {e}")
        return None


def svg_to_image(svg_content, size=512):
    """将 SVG 渲染为 PIL Image"""
    try:
        png_data = cairosvg.svg2png(
            bytestring=svg_content.encode("utf-8"),
            output_width=size,
            output_height=size
        )
        return Image.open(io.BytesIO(png_data)).convert("RGBA")
    except Exception as e:
        print(f"    ⚠ SVG 渲染错误: {e}")
        return None


def create_icon(svg_content, bg_hex):
    """
    生成 512x512 画布：彩色圆角背景 + 白色SVG图标居中。
    返回 PIL Image。
    """
    bg_rgb = hex_to_rgb(bg_hex)

    # 渲染 SVG 到 512x512 PNG
    icon_img = svg_to_image(svg_content, 512)
    if icon_img is None:
        return None

    # 画布
    canvas = Image.new("RGBA", (512, 512), bg_rgb)
    draw = ImageDraw.Draw(canvas)
    draw.rounded_rectangle([(6, 6), (505, 505)], radius=40, fill=bg_rgb)

    # 裁剪 SVG 实际内容区域并缩放至 62%
    bbox = icon_img.getbbox()
    icon = icon_img.crop(bbox) if bbox else icon_img

    target = int(512 * 0.62)
    scale = target / max(icon.size)
    new_size = (int(icon.width * scale), int(icon.height * scale))
    icon_resized = icon.resize(new_size, Image.LANCZOS)

    x = (512 - new_size[0]) // 2
    y = (512 - new_size[1]) // 2
    canvas.paste(icon_resized, (x, y), icon_resized)
    return canvas


def build_ico(canvas):
    """
    从画布生成 7 种尺寸（16/24/32/48/64/128/256）的 ICO 二进制数据。
    所有子图像以 PNG 格式内嵌。
    """
    # 生成各尺寸 PNG
    png_list = []
    for s in ICO_SIZES:
        resized = canvas.resize((s, s), Image.LANCZOS)
        buf = io.BytesIO()
        resized.save(buf, format="PNG")
        png_list.append(buf.getvalue())

    # 构建 ICO 二进制数据
    # ICO 文件结构：header + entries + [image data...]
    entry_fmt = "<BBBBHHII"
    header = struct.pack("<HHH", 0, 1, len(ICO_SIZES))
    entry_size = struct.calcsize(entry_fmt)

    data_start = len(header) + len(ICO_SIZES) * entry_size
    offset = data_start

    entries = b""
    for i, s in enumerate(ICO_SIZES):
        w = s if s < 256 else 0
        h = s if s < 256 else 0
        entries += struct.pack(
            entry_fmt,
            w, h,           # 宽高（256用0表示）
            0, 0,           # 调色板数、保留
            1, 32,          # 平面数、bpp
            len(png_list[i]),
            offset
        )
        offset += len(png_list[i])

    return header + entries + b"".join(png_list)


def write_desktop_ini(folder_path):
    """
    写入 desktop.ini，IconResource 使用同目录下的 folder.ico。
    编码必须为 ANSI。
    """
    ini_content = (
        "[.ShellClassInfo]\r\n"
        "IconResource=folder.ico,0\r\n"
        "[ViewState]\r\n"
        "Mode=\r\n"
        "Vid=\r\n"
        "FolderType=Generic\r\n"
    )
    ini_path = folder_path / "desktop.ini"
    ini_path.write_text(ini_content, encoding="ansi")
    return ini_path


def set_attributes_vbs(paths, use_readonly=True):
    """
    使用 VBScript 设置 Windows 文件属性。
    paths: list of (folder_path, ini_path)
    use_readonly: True=+R (方案B), False=+S (方案A)
    """
    attr_flag = "1" if use_readonly else "4"  # 1=R, 4=S
    attr_name = "R" if use_readonly else "S"

    lines = [
        'Dim fso: Set fso = CreateObject("Scripting.FileSystemObject")',
    ]
    for i, (folder_path, ini_path) in enumerate(paths):
        folder_str = str(folder_path).replace("\\", "\\\\")
        ini_str = str(ini_path).replace("\\", "\\\\")
        lines.append(f'Dim f{i}: Set f{i} = fso.GetFolder("{folder_str}")')
        lines.append(f'f{i}.Attributes = f{i}.Attributes Or {attr_flag}')
        lines.append(
            f'Dim i{i}: Set i{i} = fso.GetFile("{ini_str}")'
        )
        lines.append(f'i{i}.Attributes = i{i}.Attributes Or 2 Or 4')

    lines.append('WScript.Echo "Done"')

    vbs = "\n".join(lines)
    vbs_path = "/mnt/d/_set_attrs.vbs"
    with open(vbs_path, "w") as f:
        f.write(vbs)

    subprocess.run(
        ["/mnt/c/Windows/System32/cscript.exe", "/nologo", "D:\\_set_attrs.vbs"],
        capture_output=True, text=True, encoding="gbk", errors="replace"
    )
    os.remove(vbs_path)
    return True


def render_mapping_table():
    """返回 MDI 映射的 Markdown 表格"""
    lines = []
    lines.append("| 文件夹 | MDI 图标 | 背景色 |")
    lines.append("|---|---|---|")
    for folder in sorted(ALL_MAPS.keys()):
        icon, bg = ALL_MAPS[folder]
        lines.append(f"| {folder} | `{icon}` | `#{bg}` |")
    return "\n".join(lines)


def run(target_dir, force=False, dry_run=False):
    """主流程"""
    target_path = Path(target_dir)
    if not target_path.is_dir():
        print(f"[错误] 目录不存在: {target_dir}")
        return

    subfolders = sorted([d for d in target_path.iterdir() if d.is_dir()])

    # 找到与本映射匹配的子文件夹
    matching = []
    for folder in subfolders:
        if folder.name in ALL_MAPS:
            matching.append(folder)

    if not matching:
        print(f"[信息] 目录 '{target_dir}' 中没有与映射表中名称匹配的子文件夹。")
        print(f"    映射表包含: {', '.join(sorted(ALL_MAPS.keys()))}")
        print(f"    目录包含: {', '.join(f.name for f in subfolders)}")
        return

    print(f"[信息] 目标目录: {target_path}")
    print(f"[信息] 发现 {len(matching)} 个匹配的文件夹")
    print()

    # 存储路径供批量属性设置
    folder_paths = []

    for subfolder in matching:
        folder_name = subfolder.name
        icon_name, bg_hex = ALL_MAPS[folder_name]

        print(f"  [{folder_name}] icon={icon_name} bg=#{bg_hex}")

        if dry_run:
            print(f"    → (dry-run, skip)")
            continue

        # 1. 获取 SVG
        svg = fetch_svg(icon_name)
        if svg is None:
            print(f"    ✗ 获取 SVG 失败，跳过")
            continue

        # 2. 生成画布
        canvas = create_icon(svg, bg_hex)
        if canvas is None:
            print(f"    ✗ 生成画布失败，跳过")
            continue

        # 3. 生成 ICO
        ico_data = build_ico(canvas)
        ico_path = subfolder / "folder.ico"
        if ico_path.exists() and not force:
            print(f"    → folder.ico 已存在（--force 强制覆盖）")
        else:
            ico_path.write_bytes(ico_data)
            print(f"    ✓ folder.ico ({len(ico_data)} bytes)")

        # 4. 写入 desktop.ini
        ini_path = write_desktop_ini(subfolder)
        print(f"    ✓ desktop.ini")

        folder_paths.append((subfolder, ini_path))
        print()

    # 5. 批量设置属性
    if not dry_run and folder_paths:
        print("  [设置属性]")
        try:
            set_attributes_vbs(folder_paths, use_readonly=True)
            print(f"    ✓ 已为 {len(folder_paths)} 个文件夹设置 +R，desktop.ini 设置 +H+S")
        except Exception as e:
            print(f"    ✗ 设置属性失败: {e}")
            print("      替代方案：以管理员身份运行以下命令：")
            for folder, _ in folder_paths:
                print(f'      attrib +R "{folder}"')
                print(f'      attrib +H +S "{folder}\\desktop.ini"')

    print()
    print("[完成] 图标应用完成！按 F5 或重启 Explorer 查看效果。")
    print()
    print("如需刷新图标缓存：")
    print("  taskkill /f /im explorer.exe")
    print('  del /a /q "%localappdata%\\Microsoft\\Windows\\Explorer\\iconcache*"')
    print("  start explorer.exe")


def display_mapping():
    """显示映射表"""
    print("==============================================")
    print("  MDI 映射表（可用于 folder_icon_mdi.py）")
    print("==============================================")
    print()
    print("| 文件夹 | MDI 图标 | 背景色 |")
    print("|---|---|---|")
    for folder in sorted(ALL_MAPS.keys()):
        icon, bg = ALL_MAPS[folder]
        print(f"| {folder} | `{icon}` | `#{bg}` |")
    print()
    print(f"总计: {len(ALL_MAPS)} 个映射")
    print()


# =============================================================================
# CLI
# =============================================================================
def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="[方案B-MDI] 为子文件夹批量生成彩色图标（每个文件夹内部存放 folder.ico）"
    )
    parser.add_argument("target_dir", nargs="?",
                        help="目标目录（含子文件夹）")
    parser.add_argument("--force", action="store_true",
                        help="强制重新生成已有图标")
    parser.add_argument("--dry-run", action="store_true",
                        help="仅预览")
    parser.add_argument("--map-only", action="store_true",
                        help="仅显示当前映射表")
    parser.add_argument("--add", nargs=4, metavar=("FOLDER", "ICON", "HEX", "SOURCE_NAME"),
                        help="添加新映射项：文件夹名 图标名 十六进制色(无#) 源名称(如MY_PROJECT)")

    args = parser.parse_args()

    if args.map_only:
        display_mapping()
        return

    # 处理添加新映射
    if args.add:
        folder, icon, hex_color, source = args.add
        # 统一格式处理
        if hex_color.startswith("#"):
            hex_color = hex_color[1:]
        hex_color = hex_color.upper().replace("0X", "")

        target_dict = None
        # 目前已注册的映射块
        REGISTRY = {
            "CONFIG": ICON_MAP,
        }
        # 用户指定源
        source_key = source.upper()
        if source_key == "CONFIG":
            target_dict = ICON_MAP

        if target_dict is not None:
            target_dict[folder] = (icon, hex_color)
            print(f"[OK] 已添加: {folder} -> ({icon}, #{hex_color}) 到 {source}")
        else:
            print(f"[错误] 未找到源: {source}。可用的源: CONFIG")
            print("手动添加方法：")
            print(f'  1. 打开 scripts/folder_icon_mdi.py')
            print(f'  2. 在 ICON_MAP 字典中添加：')
            print(f'     "{folder}": ("{icon}", "{hex_color}"),')

            # 兼容新模式：直接在 ICON_MAP 中添加
            ICON_MAP[folder] = (icon, hex_color)
            print(f"[OK] 已直接添加到 ICON_MAP（非持久化，重启后丢失）")
        return

    if not args.target_dir:
        parser.print_help()
        return

    run(
        target_dir=args.target_dir,
        force=args.force,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    main()
