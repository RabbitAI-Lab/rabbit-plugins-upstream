"""统一 Message 抽象：调用方只描述"发什么"，与通道彻底解耦。

三种消息类型：
- text：纯文本
- card：统一卡片 DSL（title + color + sections）
- file：文件（邮件/Telegram 支持附件，其余通道降级为链接或文本）

统一卡片 DSL 的 section 类型：
- markdown：富文本（各通道按其 markdown 能力渲染）
- table：结构化表格（headers + rows），各通道降级渲染
- button：按钮跳转 URL
- note：脚注（弱化文本）
"""
import json
import os


def load_message(raw) -> dict:
    """从 JSON 字符串 / 文件路径 / dict 解析成标准 Message。"""
    if isinstance(raw, dict):
        m = raw
    elif isinstance(raw, str):
        s = raw.strip()
        if os.path.isfile(s):
            with open(s, "r", encoding="utf-8") as f:
                s = f.read()
        try:
            m = json.loads(s)
        except json.JSONDecodeError as e:
            raise ValueError(f"消息 JSON 解析失败：{e}") from e
    else:
        raise ValueError(f"无法解析消息类型：{type(raw)}")

    if not isinstance(m, dict):
        raise ValueError("消息必须是 JSON 对象")
    if "kind" not in m:
        raise ValueError("消息缺少 kind 字段（text/card/file）")
    if m["kind"] not in ("text", "card", "file"):
        raise ValueError(f"未知消息类型：{m['kind']}")
    return m


def table_to_markdown(headers, rows) -> str:
    """表格 → markdown 表格字符串（飞书/Telegram 等支持表格的通道用）。"""
    lines = ["| " + " | ".join(str(h) for h in headers) + " |",
             "| " + " | ".join(":---" for _ in headers) + " |"]
    for r in rows:
        lines.append("| " + " | ".join(str(c) for c in r) + " |")
    return "\n".join(lines)


def table_to_text(headers, rows, col_width: int = 12) -> str:
    """表格 → 对齐纯文本（企业微信/钉钉等不支持表格的通道降级用）。"""
    width = max(col_width, max([len(str(h)) for h in headers] + [
        len(str(c)) for r in rows for c in r] + [1]) + 1)
    lines = ["".join(str(h).ljust(width) for h in headers)]
    lines.append("-" * width * len(headers))
    for r in rows:
        lines.append("".join(str(c).ljust(width) for c in r))
    return "\n".join(lines)
