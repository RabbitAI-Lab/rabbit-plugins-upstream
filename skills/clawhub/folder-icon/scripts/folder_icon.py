#!/usr/bin/env python3
r"""
folder-icon: 为子文件夹批量生成并应用彩色图标

用法:
    python folder_icon.py "D:\目标目录" [--icon-dir "D:\Icon"] [--dry-run] [--force]

依赖: pip install svglib reportlab Pillow PyYAML requests
"""

import argparse
import os
import sys
import shutil
import subprocess
from pathlib import Path

import requests
import yaml
from PIL import Image
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

# =============================================================================
# 图标名 → Tabler SVG 名 映射表
# 命名规范: <功能>-<风格>.ico
#   -outline = 线框风格，无后缀 = 填充风格
# =============================================================================
ICON_TO_TABLER = {
    "book-outline.ico": "book",
    "folder-outline.ico": "folder",
    "file-document-outline.ico": "file-description",
    "file-word-outline.ico": "file-text",
    "file-excel-outline.ico": "file-spreadsheet",
    "image-outline.ico": "photo",
    "video-outline.ico": "video",
    "music-outline.ico": "music",
    "cloud-download-outline.ico": "cloud-download",
    "cloud-upload-outline.ico": "cloud-upload",
    "database-outline.ico": "database",
    "shield-check-outline.ico": "shield-check",
    "alert-outline.ico": "alert-circle",
    "school-outline.ico": "school",
    "cactus.ico": "cactus",
    "code-outline.ico": "code",
    "notebook-outline.ico": "notes",
    "account-search-outline.ico": "user-search",
    "settings-outline.ico": "settings",
    "download-outline.ico": "download",
    "upload-outline.ico": "upload",
    "link-outline.ico": "link",
    "lock-outline.ico": "lock",
    "mail-outline.ico": "mail",
    "star-outline.ico": "star",
    "heart-outline.ico": "heart",
    "trash-outline.ico": "trash",
    "edit-outline.ico": "edit",
    "search-outline.ico": "search",
    "tool-outline.ico": "tools",
    "chart-bar-outline.ico": "chart-bar",
    "gamepad-outline.ico": "device-gamepad",
    "archive-outline.ico": "archive",
    # === 扩展图标（Documents 专用）===
    "bug-outline.ico": "bug",
    "circle-outline.ico": "circle",
    "device-laptop-outline.ico": "device-laptop",
    "presentation-outline.ico": "presentation",
    "terminal-outline.ico": "terminal",
    "signal-outline.ico": "signal",
    "cpu-outline.ico": "cpu",
}

# Tabler Icons CDN 基础 URL (v3.x)
TABLER_CDN = "https://unpkg.com/@tabler/icons/icons/{name}.svg"


# =============================================================================
# SVG 获取
# =============================================================================
def get_svg(tabler_name: str, use_local: str = None) -> str:
    """从 CDN 或本地读取 SVG 内容。"""
    if use_local and Path(use_local).is_dir():
        local = Path(use_local) / f"{tabler_name}.svg"
        if local.exists():
            return local.read_text(encoding="utf-8")
    url = TABLER_CDN.format(name=tabler_name)
    resp = requests.get(url, timeout=15)
    resp.raise_for_status()
    return resp.text


# =============================================================================
# SVG 着色
# =============================================================================
def svg_colorize(svg_text: str, rgb: tuple[int, int, int]) -> str:
    """将 SVG 中的 currentColor / stroke / fill 替换为目标 RGB 色。保留 stop-color（渐变）和 stroke=\"none\"（透明）。"""
    r, g, b = rgb
    hex_color = f"#{r:02X}{g:02X}{b:02X}"

    import re
    svg = svg_text

    # 替换 currentColor
    svg = re.sub(r'\bcurrentColor\b', hex_color, svg)

    # 替换未加引号的纯色值 (stroke="..." 或 fill="...")
    # 跳过 stroke="none" 和 fill="none"
    def replace_color(m):
        attr = m.group(1)
        val = m.group(2)
        if val.lower() in ("none", "transparent"):
            return m.group(0)
        # 跳过渐变 stop-color
        if attr == "stop-color":
            return m.group(0)
        # 跳过含 # 或 rgb() 的已格式化的值
        if val.startswith("#") or val.startswith("rgb"):
            return m.group(0)
        # 替换命名颜色（white, black 等）和 hex（3位）
        return f'{attr}="{hex_color}"'

    svg = re.sub(r'(stroke|fill)="([^"]*)"', replace_color, svg)

    # 替换 stroke/fill 属性值（不带引号）
    def replace_attr_val(m):
        prefix = m.group(1)
        val = m.group(2)
        if val.lower() in ("none", "transparent"):
            return m.group(0)
        return f'{prefix}="{hex_color}"'

    svg = re.sub(r'\b(stroke|fill)\s*=\s*"([^"]+)"', replace_attr_val, svg)

    return svg


# =============================================================================
# SVG → PNG 渲染
# =============================================================================
def render_svg(svg_text: str, sizes: list[int] = None) -> dict[int, Image.Image]:
    """将 SVG 渲染为多尺寸 PNG。返回 {size: PIL.Image}。"""
    if sizes is None:
        sizes = [16, 32, 48, 256]

    import io
    from svglib.svglib import svg2rlg
    from reportlab.graphics import renderPM

    drawing = svg2rlg(io.StringIO(svg_text))
    if drawing is None:
        raise ValueError("Failed to parse SVG")

    # 统一到 512x512 基准，再缩放
    base_size = 512
    orig_w = drawing.width
    orig_h = drawing.height
    if orig_w and orig_h:
        scale = base_size / max(orig_w, orig_h)
        drawing.width = orig_w * scale
        drawing.height = orig_h * scale
        drawing.scale(scale, scale)

    images = {}
    for size in sizes:
        buf = io.BytesIO()
        renderPM.drawToFile(drawing, buf, fmt="PNG", dpi=144 * size / 256)
        buf.seek(0)
        img = Image.open(buf).resize((size, size), Image.LANCZOS)
        images[size] = img

    return images


# =============================================================================
# 多尺寸 PNG → ICO
# =============================================================================
def build_ico(images: dict[int, Image.Image], output_path: Path) -> None:
    """将多尺寸 PNG 打包为 Windows .ico 文件（保存为带透明 PNG 的 ICO）。"""
    sizes_ico = [16, 32, 48, 256]
    png_data_list = []
    for size in sizes_ico:
        img = images.get(size, images[max(images)])
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        png_data_list.append((size, buf.getvalue()))

    # ICO 文件格式：头部 + 目录项 + PNG 数据
    import struct

    with open(output_path, "wb") as f:
        # ICO 头
        f.write(struct.pack("<HHH", 0, 1, len(png_data_list)))
        offset = 6 + 16 * len(png_data_list)
        entries = []
        for size, png_bytes in png_data_list:
            w = 0 if size >= 256 else size
            h = 0 if size >= 256 else size
            entry = struct.pack("<BBBBHHII",
                               w,          # width
                               h,          # height
                               0,          # color palette
                               0,          # reserved
                               1,          # color planes
                               32,         # bits per pixel
                               len(png_bytes),
                               offset)
            entries.append(entry)
            offset += len(png_bytes)
        for entry in entries:
            f.write(entry)
        for _, png_bytes in png_data_list:
            f.write(png_bytes)


# =============================================================================
# 完整生成单个 .ico
# =============================================================================
def make_icon(icon_name: str, rgb: tuple, output_dir: Path,
              svg_source: str = None) -> Path:
    """生成一个彩色 .ico 文件并返回路径。"""
    if icon_name not in ICON_TO_TABLER:
        raise ValueError(f"未知图标名: {icon_name}，请先在 ICON_TO_TABLER 中注册")

    tabler_name = ICON_TO_TABLER[icon_name]
    svg_text = get_svg(tabler_name, use_local=svg_source)
    colored_svg = svg_colorize(svg_text, rgb)
    images = render_svg(colored_svg)

    output_path = output_dir / icon_name
    import io
    build_ico(images, output_path)
    return output_path


# =============================================================================
# desktop.ini 写入（ANSI 编码 + 相对路径 IconResource）
# =============================================================================
def write_desktop_ini(folder_path: Path, icon_rel_path: Path,
                      config_path: Path = None) -> None:
    """
    为文件夹写入 desktop.ini，包含:
    - IconResource（相对路径，从 desktop.ini 所在文件夹出发）
    - [.ShellClassInfo] 节
    必须 ANSI 编码，否则 Windows Explorer 无法正确读取。
    """
    # 计算从目标文件夹到 icon 文件的相对路径
    # desktop.ini 位于目标文件夹内，所以相对路径以目标文件夹为起点
    # icon_path 如 D:\Icon\book-outline.ico，folder_path 如 D:\游戏\文档
    try:
        # 转为相对路径：以 desktop.ini 所在目录为起点
        rel = os.path.relpath(icon_rel_path, folder_path)
        # Windows 路径分隔符统一为反斜杠
        rel = rel.replace("/", "\\")
    except ValueError:
        # 跨驱动器等情况，使用绝对路径兜底
        rel = str(icon_rel_path).replace("/", "\\")

    ini_content = (
        "[.ShellClassInfo]\r\n"
        f"IconResource={rel}\r\n"
    )

    desktop_ini = folder_path / "desktop.ini"
    # 必须 ANSI 编码（cp1252 或直接让 Windows 默认使用系统代码页）
    # Python on Windows: encoding='ansi' 映射到系统默认代码页（通常 cp936 中文系统 / cp1252 西文）
    desktop_ini.write_text(ini_content, encoding="ansi")

    # 设置属性：+S（系统文件）+H（隐藏）
    _set_attributes(desktop_ini, "+S", "+H")


# =============================================================================
# 文件夹属性设置（空格路径必须加引号）
# =============================================================================
def set_folder_system_attr(folder_path: Path) -> None:
    """为文件夹设置 +S System 属性，使其能识别 desktop.ini。"""
    _set_attributes(folder_path, "+S")


def _set_attributes(path: Path, *attrs: str) -> None:
    """调用 attrib 命令。路径含空格时自动加引号。"""
    result = subprocess.run(
        ["attrib"] + list(attrs), str(path),
        capture_output=True, text=True
    )
    if result.returncode != 0:
        import warnings
        warnings.warn(f"attrib 失败: {result.stderr.strip()}")


# =============================================================================
# 刷新 Explorer
# =============================================================================
def refresh_explorer() -> None:
    """通知 Windows 刷新 Explorer 以显示新图标。"""
    try:
        subprocess.run(
            ["powershell", "-Command",
             "Rundll32 user32.dll,UpdatePerUserSystemParameters"],
            capture_output=True
        )
    except Exception:
        pass


# =============================================================================
# 加载配置
# =============================================================================
def load_config(skill_dir: Path, cli_icon_dir: str = None,
               cli_config: str = None) -> dict:
    """加载 icon_config.yaml。优先使用 CLI 参数。"""
    if cli_config and Path(cli_config).exists():
        return yaml.safe_load(Path(cli_config).read_text(encoding="utf-8"))

    default_config = skill_dir / "scripts" / "icon_config.yaml"
    if default_config.exists():
        return yaml.safe_load(default_config.read_text(encoding="utf-8"))

    # 无配置文件时使用默认值
    return {
        "icon_dir": ".folder-icons",
        "svg_source": "tabler",
        "explicit_mappings": []
    }


# =============================================================================
# 主流程
# =============================================================================
def run(target_dir: str,
        icon_dir: str = None,
        config_path: str = None,
        dry_run: bool = False,
        force: bool = False) -> None:

    target_path = Path(target_dir)
    if not target_path.is_dir():
        print(f"[ERROR] 目录不存在: {target_dir}")
        return

    skill_dir = Path(__file__).parent.resolve()
    cfg = load_config(skill_dir, icon_dir, config_path)

    # 图标目录：相对于目标目录（允许 --icon-dir 传目录名或绝对路径）
    icon_dir_name = cfg.get("icon_dir", ".folder-icons")
    if os.path.isabs(icon_dir_name):
        icon_output_dir = Path(icon_dir_name)
    else:
        icon_output_dir = target_path / icon_dir_name
    svg_source = cfg.get("svg_source", "tabler")
    if svg_source == "local":
        svg_source = cfg.get("svg_local_dir")

    # 确保图标输出目录存在
    if not dry_run:
        icon_output_dir.mkdir(parents=True, exist_ok=True)

    print(f"[INFO] 目标目录: {target_path}")
    print(f"[INFO] 图标输出目录: {icon_output_dir}")
    print(f"[INFO] SVG 来源: {svg_source or 'CDN'}")
    print()

    mappings = cfg.get("explicit_mappings", [])
    if not mappings:
        print("[WARN] icon_config.yaml 中没有配置 explicit_mappings，什么都不做")
        return

    # 建立 folder_name → config 的字典便于快速查找
    mapping_dict = {m["folder"]: m for m in mappings}

    subfolders = sorted([d for d in target_path.iterdir() if d.is_dir()])

    for subfolder in subfolders:
        folder_name = subfolder.name
        if folder_name not in mapping_dict:
            continue

        m = mapping_dict[folder_name]
        icon_name = m["icon"]
        rgb = tuple(m["rgb"])
        color_desc = m.get("color", "")

        print(f"  {'[DRY]  ' if dry_run else ''}[{folder_name}] → {icon_name} {rgb} {color_desc}")

        if dry_run:
            continue

        # 1. 生成 .ico
        icon_path = icon_output_dir / icon_name
        if not icon_path.exists() or force:
            try:
                make_icon(icon_name, rgb, icon_output_dir, svg_source)
                print(f"    ✓ 生成图标: {icon_path}")
            except Exception as e:
                print(f"    ✗ 图标生成失败: {e}")
                continue
        else:
            print(f"    → 已有图标，跳过生成（用 --force 强制重建）")

        # 2. 写入 desktop.ini（含相对路径）
        try:
            write_desktop_ini(subfolder, icon_path, config_path)
            print(f"    ✓ desktop.ini 已写入（相对路径）")
        except Exception as e:
            print(f"    ✗ desktop.ini 写入失败: {e}")

        # 3. 设置文件夹 +S 属性
        try:
            set_folder_system_attr(subfolder)
            print(f"    ✓ 文件夹 +S 属性已设置")
        except Exception as e:
            print(f"    ✗ 文件夹属性设置失败: {e}")

        print()

    print("[DONE] 图标应用完成，按 F5 刷新 Explorer 查看效果")


# =============================================================================
# CLI 入口
# =============================================================================
def main() -> None:
    parser = argparse.ArgumentParser(
        description="为子文件夹批量生成并应用彩色图标（基于 Tabler Icons）"
    )
    parser.add_argument("target_dir", help="目标目录（含子文件夹）")
    parser.add_argument("--icon-dir", help="图标输出目录（覆盖配置文件）")
    parser.add_argument("--config", help="icon_config.yaml 路径（覆盖默认）")
    parser.add_argument("--dry-run", action="store_true",
                        help="仅预览，不实际修改")
    parser.add_argument("--force", action="store_true",
                        help="强制重新生成已有图标")
    args = parser.parse_args()

    run(
        target_dir=args.target_dir,
        icon_dir=args.icon_dir,
        config_path=args.config,
        dry_run=args.dry_run,
        force=args.force,
    )


if __name__ == "__main__":
    main()