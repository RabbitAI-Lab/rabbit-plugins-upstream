"""沙箱与输出约束（ClawHub 版新增）。

职责边界：只管「脚本能碰什么、能吐什么」，**不改任何评分口径**。

四件事：
  1. validate_input      —— 输入文件白名单（存在 / 是文件 / 扩展名 / 体积）
  2. validate_output     —— 输出路径沙箱（只允许落在输入同级目录或当前工作目录内）
  3. clean_text / deep_clean —— 原表回显文本清洗（剥控制字符 + 截断，防间接提示注入）
  4. limit_output        —— 终端打印限量（防无界输出）

本模块不联网、不读环境变量、不起子进程、不遍历目录。
"""

from __future__ import annotations

import re
from pathlib import Path

MAX_INPUT_BYTES = 20 * 1024 * 1024          # 20 MB
ALLOWED_SUFFIX = {".xlsx", ".xlsm", ".csv", ".tsv"}
MAX_TEXT_CHARS = 1000                        # 单段文本上限（payload 深清洗）
MAX_ECHO_CHARS = 200                         # 回显原文上限（报告/Excel）
MAX_PRINT_LINES = 60                         # 终端打印行数上限

# C0/C1 控制字符与 DEL（Excel/CSV 里常见的脏字符，会被终端与 Markdown 解释）
_CTRL_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]")
_WS_RE = re.compile(r"[ \t\r\n]+")


class SandboxError(Exception):
    """违反沙箱约束。由 run.py 捕获并转为退出码 4。"""

    def __init__(self, msg: str, allowed=None):
        super().__init__(msg)
        self.msg = msg
        self.allowed = list(allowed or [])


def allowed_roots(input_path: Path) -> list[Path]:
    """允许写入的两个根：输入文件同级目录、当前工作目录。"""
    roots = []
    try:
        roots.append(input_path.resolve().parent)
    except OSError:
        pass
    try:
        roots.append(Path.cwd().resolve())
    except OSError:
        pass
    # 去重保序
    seen, uniq = set(), []
    for r in roots:
        key = str(r).lower()
        if key not in seen:
            seen.add(key)
            uniq.append(r)
    return uniq


def _within(p: Path, root: Path) -> bool:
    try:
        p.resolve().relative_to(root)
        return True
    except (ValueError, OSError):
        return False


def validate_input(raw) -> Path:
    """校验并返回解析后的输入文件路径。违规抛 SandboxError。"""
    p = Path(str(raw)).expanduser()
    if not p.exists():
        raise SandboxError(f"输入文件不存在：{p}")
    if p.is_dir():
        raise SandboxError(f"输入路径是目录，不是一个文件：{p}")
    if p.is_symlink():
        p = p.resolve()
        if not p.exists() or p.is_dir():
            raise SandboxError(f"符号链接指向的对象不可用：{p}")
    suffix = p.suffix.lower()
    if suffix not in ALLOWED_SUFFIX:
        raise SandboxError(
            f"不支持的文件类型：{suffix or '(无扩展名)'}；"
            f"仅接受 {', '.join(sorted(ALLOWED_SUFFIX))}",
            allowed=sorted(ALLOWED_SUFFIX))
    try:
        size = p.stat().st_size
    except OSError as exc:
        raise SandboxError(f"无法读取文件大小：{p}（{exc}）")
    if size > MAX_INPUT_BYTES:
        raise SandboxError(
            f"文件过大：{size / 1024 / 1024:.1f} MB，上限 {MAX_INPUT_BYTES // 1024 // 1024} MB；"
            f"请拆分或另存后再跑")
    return p.resolve()


def validate_output(raw, roots, what: str = "输出路径") -> Path:
    """校验输出路径落在 roots 内。返回解析后的路径（父目录会自动创建）。"""
    p = Path(str(raw)).expanduser()
    # 相对路径一律相对当前工作目录解析，避免歧义
    base = Path.cwd().resolve() if not p.is_absolute() else None
    resolved = (base / p).resolve() if base else p.resolve()
    for root in roots:
        if _within(resolved, root):
            return resolved
    raise SandboxError(
        f"{what}越界：{resolved}\n"
        f"本技能只允许写到以下目录（含其子目录）：\n  "
        + "\n  ".join(str(r) for r in roots)
        + "\n请改用允许范围内的路径，例如 --out-dir gongfen-out",
        allowed=[str(r) for r in roots])


def clean_text(s, maxlen: int = MAX_ECHO_CHARS) -> str:
    """清洗一段来自用户表格的文本：剥控制字符、压缩空白、截断。"""
    if s is None:
        return ""
    t = s if isinstance(s, str) else str(s)
    t = _CTRL_RE.sub(" ", t)
    t = _WS_RE.sub(" ", t).strip()
    if len(t) > maxlen:
        t = t[:maxlen] + "…(已截断)"
    return t


def deep_clean(obj, maxlen: int = MAX_TEXT_CHARS, _depth: int = 0):
    """递归清洗 payload 中的字符串（只清洗，不改结构、不改数值）。"""
    if _depth > 12:
        return obj
    if isinstance(obj, str):
        return clean_text(obj, maxlen)
    if isinstance(obj, dict):
        return {k: deep_clean(v, maxlen, _depth + 1) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        cleaned = [deep_clean(v, maxlen, _depth + 1) for v in obj]
        return type(obj)(cleaned) if isinstance(obj, tuple) else cleaned
    return obj


def limit_output(text: str, max_lines: int = MAX_PRINT_LINES) -> str:
    """终端打印限量：保留前 max_lines 行，其余提示见文件。"""
    if not text:
        return ""
    lines = text.splitlines()
    if len(lines) <= max_lines:
        return text
    head = "\n".join(lines[:max_lines])
    return (f"{head}\n\n… （终端仅显示前 {max_lines} 行，共 {len(lines)} 行；"
            f"完整报告见 .gongfen.md）")
