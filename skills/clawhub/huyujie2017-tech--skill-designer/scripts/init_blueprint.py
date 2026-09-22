#!/usr/bin/env python3
"""
init_blueprint.py — 技能蓝图脚手架（skill-designer 的落盘工具）

Phase 0 三问（平台/入口/通道）确认后立即调用，把蓝图从"对话里的口头产物"
升级为"磁盘上的实体 bundle"：index.md + 01–10 十张可填积木 + 内嵌 checkpoint。

设计遵循脚本四原则：自愈性 / 结构化输出 / 幂等性 / 安全边界。
- 幂等：目标目录已存在且非空 → 报错退出（exit 1），绝不覆盖已有蓝图
- 安全：只新建文件，不删除、不移动任何已有文件

用法：
    python scripts/init_blueprint.py <目标目录> --name "<skill 名>"
    python scripts/init_blueprint.py <目标目录> --name "<skill 名>" \
        --channel full --entry improve --platform workbuddy
    python scripts/init_blueprint.py <目标目录> --name "<skill 名>" --json

参数：
    目标目录        蓝图 bundle 落盘位置（如 ./skill-blueprint）
    --name    必填  skill 名（写入 index frontmatter title）
    --channel       light（轻量 MVP，默认）| full（完整）
    --entry         create（从零创建，默认）| improve（改进已有）
    --platform      运行平台（默认 workbuddy）
    --json          结构化输出（供 AI 解析）

退出码：0 = 生成成功；1 = 参数/目录错误。

产物结构（对齐 references/blueprint-template.md）：
    <目标目录>/
    ├── index.md        # frontmatter + 快照 + checkpoint + 子积木索引
    ├── 01-条件.md … 10-复盘.md   # 每格：结构公式 + 填空字段 + checklist
"""

import argparse
import json
import sys
from pathlib import Path

from blocks import BLOCKS, CHANNELS, ENTRIES, build_index, build_block
from retry import retry, write_text_robust
sys.path.insert(0, str(Path(__file__).resolve().parent))
from errors import enable_utf8  # noqa: E402

enable_utf8()  # Windows GBK 控制台下保证中文（含 stderr 报错）不乱码


def main() -> int:
    ap = argparse.ArgumentParser(description="技能蓝图脚手架（skill-designer）")
    ap.add_argument("target", help="蓝图 bundle 落盘目录")
    ap.add_argument("--name", required=True, help="skill 名（写入 index title）")
    ap.add_argument("--channel", default="light", choices=CHANNELS, help="通道：light（默认）/ full")
    ap.add_argument("--entry", default="create", choices=ENTRIES, help="入口：create（默认）/ improve")
    ap.add_argument("--platform", default="workbuddy", help="运行平台（默认 workbuddy）")
    ap.add_argument("--json", action="store_true", help="结构化输出")
    args = ap.parse_args()

    target = Path(args.target)
    created: list[str] = []

    # 幂等：已存在且非空 → 拒绝（不覆盖）
    if target.exists() and any(target.iterdir()):
        msg = f"目标目录已存在且非空，拒绝覆盖：{target}"
        if args.json:
            print(json.dumps({"ok": False, "error": msg, "created": []}, ensure_ascii=False))
        else:
            print(f"[init_blueprint] 错误：{msg}", file=sys.stderr)
        return 1

    target.mkdir(parents=True, exist_ok=True)

    # index.md（带重试，提升 IO 抖动时的稳定性）
    write_text_robust(target / "index.md", build_index(args.name, args.channel, args.entry, args.platform))
    created.append("index.md")

    # 01–10 子积木
    for b in BLOCKS:
        write_text_robust(target / b["file"], build_block(b))
        created.append(b["file"])

    if args.json:
        print(json.dumps({
            "ok": True, "target": str(target), "name": args.name,
            "channel": args.channel, "entry": args.entry, "platform": args.platform,
            "created": created, "next": "B01 条件积木",
        }, ensure_ascii=False, indent=2))
    else:
        print(f"[init_blueprint] 已生成蓝图 bundle：{target}")
        print(f"  index.md + {' '.join(b['file'] for b in BLOCKS)}")
        print(f"  平台={args.platform} 入口={args.entry} 通道={args.channel}")
        print("  下一步：沿 B01→B10 逐格填充；每格收尾更新 index.md 的 checkpoint 表")
    return 0


if __name__ == "__main__":
    sys.exit(main())
