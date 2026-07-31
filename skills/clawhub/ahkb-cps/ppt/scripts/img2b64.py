#!/usr/bin/env python3
"""AHKB-CPS :: img2b64.py — convert images to base64 data URIs for inline embedding.

Usage:
  img2b64.py <image-file> [image-file...]
  img2b64.py <image-file> [-o output.txt | --clip]

Converts one or more image files to base64 data URIs (data:image/...;base64,...)
and prints them to stdout. This is useful for embedding images directly into
self-contained HTML slides, since AHKB-CPS requires all images to be base64 inline.

Options:
  -o FILE       Write output to FILE instead of stdout
  --clip        Copy to clipboard (Windows: uses clip命令)

Examples:
  # Convert a single image and copy to clipboard
  python scripts/img2b64.py photo.jpg --clip

  # Convert multiple images, save to a text file
  python scripts/img2b64.py photo1.jpg photo2.png -o images.b64.txt

  # Pipe into a file (PowerShell)
  python scripts/img2b64.py photo.jpg > img_data.txt
"""

import os, sys, base64, subprocess, struct

SUPPORTED = {
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.png': 'image/png',
    '.gif': 'image/gif',
    '.webp': 'image/webp',
    '.svg': 'image/svg+xml',
    '.ico': 'image/x-icon',
    '.bmp': 'image/bmp',
}


# ── 常见图片格式魔数签名 ──
MAGIC_SIGNS = {
    b'\xff\xd8\xff': 'JPEG',
    b'\x89PNG\r\n\x1a\n': 'PNG',
    b'GIF87a': 'GIF',
    b'GIF89a': 'GIF',
    b'RIFF': 'WEBP',   # + 'WEBP' at offset 8
    b'<svg': 'SVG',
    b'\x00\x00\x01\x00': 'ICO',
    b'BM': 'BMP',
}


def validate_data_uri(data_uri, source_path):
    """验证 data URI 格式正确且可解码为有效图片。

    检查项：
      1. 没有双逗号（data:image/...;base64,,...）
      2. base64 段无空白字符
      3. base64 可正确解码
      4. 解码后的二进制匹配图片文件的魔数签名
    """
    errors = []

    # 检查双逗号
    if ',,' in data_uri:
        errors.append("数据 URI 中包含双逗号（,,），请检查拼接逻辑")

    # 提取 base64 段（data:image/...;base64,<数据>）
    m = data_uri.split(';base64,')
    if len(m) != 2:
        errors.append("数据 URI 格式错误：找不到 ;base64, 分隔符")
    else:
        b64_part = m[1]
        # 检查空白字符
        if b64_part.strip() != b64_part:
            errors.append("base64 数据段包含首尾空白字符，可能导致解析失败")
        # 尝试解码
        try:
            raw = base64.b64decode(b64_part, validate=True)
        except Exception as e:
            errors.append(f"base64 解码失败: {e}")
            raw = None

        # 检查空数据
        if raw is not None and len(raw) == 0:
            errors.append("解码后数据为空，文件可能已损坏")
        # 验证图片魔数
        if raw is not None and len(raw) > 0:
            ext = os.path.splitext(source_path)[1].lower()
            magic_ok = False
            detected_format = '未知'
            for magic, fmt in MAGIC_SIGNS.items():
                if raw[:len(magic)] == magic:
                    magic_ok = True
                    detected_format = fmt
                    break
            # WEBP 特殊处理：前 4 字节 RIFF，偏移 8 处为 WEBP
            if not magic_ok and ext in ('.webp',) and raw[:4] == b'RIFF' and raw[8:12] == b'WEBP':
                magic_ok = True
                detected_format = 'WEBP'
            if not magic_ok:
                errors.append(f"解码数据不匹配任何已知图片格式（前 16 字节: {raw[:16].hex()}）")
            else:
                # 格式与扩展名交叉检查
                ext_fmt_map = {
                    '.jpg': 'JPEG', '.jpeg': 'JPEG',
                    '.png': 'PNG', '.gif': 'GIF',
                    '.webp': 'WEBP', '.svg': 'SVG',
                    '.ico': 'ICO', '.bmp': 'BMP',
                }
                if ext in ext_fmt_map and ext_fmt_map[ext] != detected_format:
                    errors.append(
                        f"格式冲突：文件扩展名 {ext} 预期 {ext_fmt_map[ext]}，"
                        f"但魔数签名检测为 {detected_format}。文件可能已损坏或扩展名错误"
                    )

    if errors:
        for err in errors:
            print(f"  ✗ {err}", file=sys.stderr)
        return False
    return True


def img_to_data_uri(path):
    """Convert an image file to a base64 data URI string."""
    ext = os.path.splitext(path)[1].lower()
    if ext not in SUPPORTED:
        print(f"[WARN] Unknown extension '{ext}' for {path}, treating as image/png", file=sys.stderr)
        mime = 'image/png'
    else:
        mime = SUPPORTED[ext]

    with open(path, 'rb') as f:
        raw = f.read()

    if len(raw) == 0:
        print(f"[ERROR] {path} 是空文件，无法转换", file=sys.stderr)
        sys.exit(1)

    b64 = base64.b64encode(raw).decode('ascii')
    data_uri = f'data:{mime};base64,{b64}'

    # ── 输出前自动验证 ──
    if not validate_data_uri(data_uri, path):
        print(f"  [FATAL] {path} 转换后的 data URI 验证未通过，已中止输出", file=sys.stderr)
        sys.exit(1)

    size_kb = len(raw) / 1024
    print(f"[OK] {path} -> {size_kb:.0f} KB data URI（{mime}，已验证签名）", file=sys.stderr)
    return data_uri

def copy_to_clipboard(text):
    """Copy text to clipboard using Windows clip command."""
    try:
        proc = subprocess.Popen(['clip'], stdin=subprocess.PIPE, shell=True)
        proc.communicate(text.encode('utf-8'))
        print("[OK] Copied to clipboard!", file=sys.stderr)
    except Exception as e:
        print(f"[WARN] Clipboard copy failed: {e}", file=sys.stderr)

def main():
    args = sys.argv[1:]

    if not args:
        print(__doc__)
        sys.exit(1)

    # Parse options
    output_file = None
    do_clip = False
    files = []

    i = 0
    while i < len(args):
        if args[i] in ('-h', '--help'):
            print(__doc__)
            sys.exit(0)
        elif args[i] == '-o' and i + 1 < len(args):
            output_file = args[i + 1]
            i += 2
        elif args[i] == '--clip':
            do_clip = True
            i += 1
        elif args[i].startswith('-'):
            print(f"[ERROR] Unknown option: {args[i]}", file=sys.stderr)
            sys.exit(1)
        else:
            files.append(args[i])
            i += 1

    if not files:
        print("[ERROR] No image files specified.", file=sys.stderr)
        sys.exit(1)

    # Validate files
    for f in files:
        if not os.path.isfile(f):
            print(f"[ERROR] File not found: {f}", file=sys.stderr)
            sys.exit(1)

    # Convert all files
    results = []
    for f in files:
        data_uri = img_to_data_uri(f)
        results.append(data_uri)

    # Output
    output_text = '\n'.join(results)

    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(output_text)
        print(f"[OK] Written to {output_file}", file=sys.stderr)
    elif do_clip:
        copy_to_clipboard(output_text)
        # Also print to stdout so user can see it
        print(output_text)
    else:
        # Print to stdout (user can redirect to file)
        print(output_text)


if __name__ == '__main__':
    main()
