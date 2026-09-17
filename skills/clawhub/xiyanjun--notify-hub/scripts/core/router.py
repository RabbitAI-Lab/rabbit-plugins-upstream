"""路由：解析 --to 参数，支持单发与广播。"""
from typing import Optional


def parse_targets(spec: Optional[str]) -> list:
    """解析 "feishu:群名,wecom:群名" → [("feishu", "群名"), ("wecom", "群名")]。

    - 只写通道名不带 target（如 "feishu"）→ target 为 None，用该通道默认目标。
    - 支持 "all" 广播到所有已配置通道（target 为 None）。
    """
    if not spec:
        return []
    result = []
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if ":" in part:
            ch, tgt = part.split(":", 1)
            result.append((ch.strip(), tgt.strip() or None))
        else:
            result.append((part, None))
    return result
