#!/usr/bin/env python3
"""Markdown to WeChat public account HTML converter using mdnice.

Usage:
    python convert.py <markdown_file> [--theme orangeHeart] [--output_dir ./output]

Dependencies:
    pip install mdnice requests
    playwright install chromium
"""

import argparse
import sys
from pathlib import Path


def convert_markdown_to_wechat(
    markdown_path: str,
    theme: str = "orangeHeart",
    output_dir: str | None = None,
    code_theme: str = "wechat",
    mac_style: bool = True,
) -> str:
    """Convert markdown file to WeChat formatted HTML.

    Args:
        markdown_path: Path to markdown file
        theme: Theme name (see AVAILABLE_THEMES below)
        output_dir: Output directory for HTML file
        code_theme: Code highlight theme
        mac_style: Enable Mac style rendering

    Returns:
        Path to generated HTML file
    """
    from mdnice import MarkdownConverter

    md_path = Path(markdown_path).resolve()
    if not md_path.exists():
        raise FileNotFoundError(f"Markdown file not found: {markdown_path}")

    if output_dir is None:
        output_dir = str(md_path.parent)
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    converter = MarkdownConverter(
        headless=True,
        code_theme=code_theme,
        mac_style=mac_style,
        clean_html=True,
    )

    result = converter.convert(
        str(md_path),
        theme=theme,
        platform="wechat",
        output_dir=output_dir,
        return_html=False,
        wrap_full_html=False,
    )

    if isinstance(result, list):
        output_path = result[0]
    else:
        output_path = str(result)

    # Fix fonts: mdnice uses light-weight fonts that are hard to read on mobile.
    # Replace with proper Chinese reading font stack.
    _fix_fonts(output_path)

    return output_path


def _fix_fonts(html_path: str) -> None:
    """Replace mdnice's default light-weight fonts with readable Chinese fonts.

    mdnice uses PingFangSC-Light / PingFangSC-light / STHeitiSC-Light which
    are too thin for comfortable reading, especially on mobile devices.
    """
    FONT_STACK = (
        "'PingFang SC', 'Hiragino Sans GB', "
        "'Microsoft YaHei', 'Noto Sans CJK SC', sans-serif"
    )
    replacements = [
        # orangeHeart / themes with Optima-based font
        (
            "font-family: Optima-Regular, Optima, PingFangSC-light, PingFangTC-light, "
            "'PingFang SC', Cambria, Cochin, Georgia, Times, 'Times New Roman', serif",
            f"font-family: {FONT_STACK}",
        ),
        # Standard light font used in many themes (capital L)
        ("font-family: PingFangSC-Light", f"font-family: {FONT_STACK}"),
        # Heading light font
        ("font-family: STHeitiSC-Light", f"font-family: {FONT_STACK}"),
    ]

    path = Path(html_path)
    if not path.exists():
        return

    content = path.read_text(encoding="utf-8")
    for old, new in replacements:
        content = content.replace(old, new)
    path.write_text(content, encoding="utf-8")

    print(f"🔤 字体已优化: {path.name}")


AVAILABLE_THEMES = {
    "normal": "默认主题",
    "shanchui": "山吹",
    "rose": "蔷薇紫",
    "fullStackBlue": "全栈蓝",
    "nightPurple": "凝夜紫",
    "cuteGreen": "萌绿",
    "extremeBlack": "极简黑",
    "orangeHeart": "橙心",
    "ink": "墨黑",
    "purple": "姹紫",
    "green": "绿意",
    "cyan": "嫩青",
    "wechatFormat": "WeChat-Format",
    "blueCyan": "兰青",
    "blueMountain": "前端之巅同款",
    "geekBlack": "极客黑",
    "red": "红绯",
    "blue": "蓝莹",
    "scienceBlue": "科技蓝",
    "simple": "简",
}

AVAILABLE_CODE_THEMES = [
    "wechat",
    "atom-one-dark",
    "atom-one-light",
    "monokai",
    "github",
    "vs2015",
    "xcode",
]


def list_themes():
    """Print available themes."""
    print("Available themes:")
    for key, name in AVAILABLE_THEMES.items():
        print(f"  {key:20s} {name}")
    print()
    print("Available code themes:")
    for t in AVAILABLE_CODE_THEMES:
        print(f"  {t}")


def main():
    parser = argparse.ArgumentParser(
        description="Convert Markdown to WeChat public account HTML"
    )
    parser.add_argument("markdown", nargs="?", help="Path to markdown file")
    parser.add_argument(
        "--theme",
        default="orangeHeart",
        help="Theme name (default: orangeHeart)",
    )
    parser.add_argument(
        "--code-theme",
        default="wechat",
        help="Code highlight theme (default: wechat)",
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Output directory (default: same as markdown file)",
    )
    parser.add_argument(
        "--mac-style",
        type=bool,
        default=True,
        help="Enable Mac style (default: True)",
    )
    parser.add_argument(
        "--list-themes",
        action="store_true",
        help="List available themes and exit",
    )

    args = parser.parse_args()

    if args.list_themes:
        list_themes()
        return

    if not args.markdown:
        parser.print_help()
        print("\nError: markdown file path is required")
        sys.exit(1)

    try:
        output_path = convert_markdown_to_wechat(
            args.markdown,
            theme=args.theme,
            output_dir=args.output_dir,
            code_theme=args.code_theme,
            mac_style=args.mac_style,
        )
        print(f"✅ Converted: {output_path}")
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
