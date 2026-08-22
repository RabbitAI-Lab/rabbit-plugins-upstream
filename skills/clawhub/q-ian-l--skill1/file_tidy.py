#!/usr/bin/env python3
"""File Tidy · 纯本地文件整理工具

零第三方依赖、跨平台（Windows / macOS / Linux）。所有破坏性操作默认仅预览，
加上 --apply 才真正执行。

子命令：organize / rename / clean / flatten / duplicates
"""
import argparse
import hashlib
import os
import shutil
import sys
from datetime import datetime
from pathlib import Path

# 扩展名 -> 分类目录
EXT_MAP = {
    "Images": {"jpg", "jpeg", "png", "gif", "bmp", "tiff", "webp", "svg",
               "heic", "ico", "avif"},
    "Documents": {"pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "txt",
                  "md", "markdown", "csv", "rtf", "odt", "pages", "key",
                  "numbers", "epub", "tex"},
    "Videos": {"mp4", "mov", "avi", "mkv", "webm", "flv", "wmv", "m4v"},
    "Audio": {"mp3", "wav", "ogg", "flac", "aac", "m4a", "wma", "opus"},
    "Archives": {"zip", "rar", "7z", "tar", "gz", "bz2", "xz", "tgz", "zst"},
    "Code": {"py", "js", "ts", "jsx", "tsx", "html", "htm", "css", "json",
             "yaml", "yml", "sh", "bash", "c", "cpp", "h", "hpp", "go", "rs",
             "java", "rb", "php", "sql", "lua", "vim"},
}


def category_for(ext: str) -> str:
    ext = ext.lower().lstrip(".")
    for cat, exts in EXT_MAP.items():
        if ext in exts:
            return cat
    return "Others"


def unique_target(dst: Path) -> Path:
    """若目标已存在，追加 (1)/(2) 后缀，绝不静默覆盖。"""
    if not dst.exists():
        return dst
    stem, suffix = dst.stem, dst.suffix
    i = 1
    while True:
        cand = dst.with_name(f"{stem} ({i}){suffix}")
        if not cand.exists():
            return cand
        i += 1


def resolve_path(p: str) -> Path:
    path = Path(p).expanduser().resolve()
    if not path.exists():
        sys.exit(f"[错误] 路径不存在 -> {path}")
    return path


def mode_label(apply: bool) -> str:
    return "APPLY (真正执行)" if apply else "DRY-RUN (加 --apply 才真正执行)"


def do_move(src: Path, dst_parent: Path, apply: bool) -> None:
    dst = unique_target(dst_parent / src.name)
    if apply:
        dst_parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(src), str(dst))
        print(f"  moved   {src.name}  ->  {dst}")
    else:
        print(f"  [DRY]   {src.name}  ->  {dst}")


def do_remove(path: Path, apply: bool, verb: str = "delete") -> None:
    if apply:
        if path.is_dir():
            shutil.rmtree(path)
        else:
            path.unlink()
        print(f"  {verb}  {path}")
    else:
        print(f"  [DRY]   {verb}  {path}")


# --------------------------------------------------------------------------- #
# organize
# --------------------------------------------------------------------------- #
def cmd_organize(args):
    root = resolve_path(args.path)
    if not root.is_dir():
        sys.exit("[错误] 目标必须是目录")
    print(f"# organize | by={args.by} depth={args.depth} | {mode_label(args.apply)}")
    print(f"# 目录: {root}\n")

    files = [p for p in root.iterdir() if p.is_file() and not p.name.startswith(".")]
    if not files:
        print("  没有可整理的文件。")
        return

    for f in files:
        if args.by == "ext":
            target_dir = root / category_for(f.suffix)
        else:  # date
            mtime = datetime.fromtimestamp(f.stat().st_mtime)
            if args.depth == "year":
                target_dir = root / mtime.strftime("%Y")
            else:
                target_dir = root / mtime.strftime("%Y") / mtime.strftime("%Y-%m")
        do_move(f, target_dir, args.apply)
    print(f"\n完成。共处理 {len(files)} 个文件。")


# --------------------------------------------------------------------------- #
# rename
# --------------------------------------------------------------------------- #
def build_new_name(name: str, args, idx: int) -> str:
    p = Path(name)
    stem, suffix = p.stem, p.suffix
    if args.lowercase:
        stem, suffix = stem.lower(), suffix.lower()
    if args.spaces_to_dash:
        stem = stem.replace(" ", "-")
    if args.prefix:
        stem = f"{args.prefix}-{stem}" if stem else args.prefix
    if args.suffix:
        stem = f"{stem}-{args.suffix}" if stem else args.suffix
    if args.sequence:
        stem = f"{idx:02d}-{stem}"
    return stem + suffix


def cmd_rename(args):
    root = resolve_path(args.path)
    print(f"# rename | prefix={args.prefix} suffix={args.suffix} "
          f"seq={args.sequence} lower={args.lowercase} dash={args.spaces_to_dash} "
          f"rec={args.recursive} | {mode_label(args.apply)}")
    print(f"# 目录: {root}\n")

    items = root.rglob("*") if args.recursive else root.iterdir()
    files = [p for p in items if p.is_file() and not p.name.startswith(".")]
    changed = 0
    for idx, f in enumerate(files, 1):
        new_name = build_new_name(f.name, args, idx)
        if new_name == f.name:
            continue
        dst = unique_target(f.parent / new_name)
        if args.apply:
            shutil.move(str(f), str(dst))
            print(f"  rename  {f.name}  ->  {dst.name}")
        else:
            print(f"  [DRY]   {f.name}  ->  {dst.name}")
        changed += 1
    print(f"\n完成。{changed} 个文件将改名。" if not args.apply
          else f"\n完成。已改名 {changed} 个文件。")


# --------------------------------------------------------------------------- #
# clean
# --------------------------------------------------------------------------- #
def find_empty_dirs(root: Path):
    result = []
    for dirpath, dirnames, filenames in os.walk(root, topdown=False):
        d = Path(dirpath)
        if d == root:
            continue
        rel = d.relative_to(root).parts
        if d.name.startswith(".") or any(part.startswith(".") for part in rel):
            continue                           # 不碰隐藏目录（含 .git/.clawhub 等内部）
        if not list(d.iterdir()):             # 真·空目录
            result.append(d)
    return result


def file_hash(path: Path, chunk: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(chunk), b""):
            h.update(block)
    return h.hexdigest()


def find_duplicates(root: Path):
    paths = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]  # 跳过隐藏目录
        for fn in filenames:
            if not fn.startswith("."):
                paths.append(Path(dirpath) / fn)
    hashes = {}
    for p in paths:
        try:
            hashes.setdefault(file_hash(p), []).append(p)
        except OSError:
            continue
    return {h: ps for h, ps in hashes.items() if len(ps) > 1}


def cmd_clean(args):
    root = resolve_path(args.path)
    print(f"# clean | empties={args.empties} dupes={args.dupes} | {mode_label(args.apply)}")
    print(f"# 目录: {root}\n")

    empties = find_empty_dirs(root)
    print(f"[空目录] 共 {len(empties)} 个")
    for d in empties:
        print(f"    {d}")
        if args.apply and args.empties:
            do_remove(d, True, "rmdir")

    dups = find_duplicates(root)
    print(f"\n[重复文件] 共 {len(dups)} 组")
    for h, ps in dups.items():
        ps_sorted = sorted(ps)
        keep = ps_sorted[0]
        print(f"    组 (sha256={h[:12]}…) 保留 {keep}")
        for p in ps_sorted[1:]:
            print(f"        dup  {p}")
            if args.apply and args.dupes:
                do_remove(p, True, "delete")

    if not args.apply:
        print("\n（以上为预览。加 --apply 才执行删除；"
              "建议 --empties / --dupes 明确范围。）")


def cmd_duplicates(args):
    root = resolve_path(args.path)
    print(f"# duplicates | 目录: {root}\n")
    dups = find_duplicates(root)
    if not dups:
        print("未发现重复文件。")
        return
    print(f"发现 {len(dups)} 组重复文件：")
    for h, ps in dups.items():
        print(f"\n  sha256={h}")
        for p in sorted(ps):
            print(f"    {p}")


# --------------------------------------------------------------------------- #
# flatten
# --------------------------------------------------------------------------- #
def cmd_flatten(args):
    root = resolve_path(args.path)
    print(f"# flatten | {mode_label(args.apply)}")
    print(f"# 目录: {root}\n")

    files = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]  # 跳过隐藏目录
        for fn in filenames:
            if fn.startswith("."):
                continue
            p = Path(dirpath) / fn
            if p.parent != root:
                files.append(p)
    for f in files:
        do_move(f, root, args.apply)
    print(f"\n完成。{len(files)} 个文件将被平铺到根目录。"
          if not args.apply else f"\n完成。已平铺 {len(files)} 个文件。")


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def build_parser():
    parser = argparse.ArgumentParser(
        prog="file_tidy.py",
        description="纯本地文件整理工具（零依赖 / 跨平台 / 默认预览）")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("organize", help="按类型或日期归类文件")
    p.add_argument("path")
    p.add_argument("--by", choices=["ext", "date"], default="ext")
    p.add_argument("--depth", choices=["month", "year"], default="month")
    p.add_argument("--apply", action="store_true")
    p.set_defaults(func=cmd_organize)

    p = sub.add_parser("rename", help="批量重命名")
    p.add_argument("path")
    p.add_argument("--prefix")
    p.add_argument("--suffix")
    p.add_argument("--sequence", action="store_true")
    p.add_argument("--lowercase", action="store_true")
    p.add_argument("--spaces-to-dash", action="store_true")
    p.add_argument("--recursive", action="store_true")
    p.add_argument("--apply", action="store_true")
    p.set_defaults(func=cmd_rename)

    p = sub.add_parser("clean", help="清理空目录与重复文件")
    p.add_argument("path")
    p.add_argument("--empties", action="store_true")
    p.add_argument("--dupes", action="store_true")
    p.add_argument("--apply", action="store_true")
    p.set_defaults(func=cmd_clean)

    p = sub.add_parser("flatten", help="平铺嵌套目录到一层")
    p.add_argument("path")
    p.add_argument("--apply", action="store_true")
    p.set_defaults(func=cmd_flatten)

    p = sub.add_parser("duplicates", help="仅列出重复文件")
    p.add_argument("path")
    p.set_defaults(func=cmd_duplicates)

    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
