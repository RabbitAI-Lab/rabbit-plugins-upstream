#!/usr/bin/env python3
"""
pipl-check — 个人信息保护合规审计自查工具

支持两种模式:
  audit (默认)   — 附件1：个人信息保护合规审计自查表（19项）
  impact         — 附件2：个人信息保护影响评估表（5场景×3评估项）

输出 Markdown + PDF 报告，含官方样式 □复选框。

使用:
  python3 check.py                                  # 交互式审计自查 → PDF
  python3 check.py --mode impact                    # 影响评估 → PDF
  python3 check.py --mode all                       # 两个都做
  python3 check.py --json data.json                 # JSON批量导入审计自查
  python3 check.py --json impact.json --mode impact # JSON导入影响评估
  python3 check.py --format md                      # 仅输出Markdown
"""

import sys, os, json, argparse
sys.path.insert(0, os.path.dirname(__file__))

from core.audit_items import AUDIT_ITEMS, IMPACT_ITEMS
from core.interactive import run_interactive, run_impact_interactive
from core.report import generate_audit, generate_impact


def load_from_json(path: str) -> list[dict]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, list):
        return data
    if isinstance(data, dict) and "results" in data:
        return data["results"]
    raise ValueError("JSON 格式错误，需要 list[dict] 或 {results: [...]}")


def main():
    parser = argparse.ArgumentParser(
        description="pipl-check — 个人信息保护合规审计自查工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "示例:\n"
            "  python3 check.py                           # 审计自查 → PDF\n"
            "  python3 check.py --mode impact             # 影响评估 → PDF\n"
            "  python3 check.py --mode all                # 两者都做\n"
            "  python3 check.py --org \"某科技有限公司\"     # 指定企业\n"
            "  python3 check.py --json data.json          # 批量导入\n"
            "  python3 check.py --format md               # 仅Markdown\n"
        )
    )
    parser.add_argument("--mode", choices=["audit", "impact", "all"],
        default="audit", help="模式: audit(自查表), impact(影响评估), all(两者)")
    parser.add_argument("--json", type=str, default=None,
        help="从JSON文件加载数据")
    parser.add_argument("--format", choices=["pdf", "md"], default="pdf",
        help="输出格式")
    parser.add_argument("--output", "-o", type=str, default="",
        help="输出路径前缀（不含扩展名）")
    parser.add_argument("--org", type=str, default="",
        help="企业/组织名称")
    parser.add_argument("--list-items", action="store_true",
        help="列出19项审计事项")

    args = parser.parse_args()

    if args.list_items:
        print("\n《小型个人信息处理者个人信息保护简化措施规定》（国家互联网信息办公室、公安部令第25号）附件1 审计事项\n")
        for item in AUDIT_ITEMS:
            print(f"  [{item['id']:2d}] {item['name']}")
            print(f"       依据: {item['pipl_articles']}")
        print()
        return

    base_name = args.output or "pipl-check-report"
    if base_name.endswith((".pdf", ".md")):
        base_name = os.path.splitext(base_name)[0]

    # ── 审计自查 ──
    if args.mode in ("audit", "all"):
        if args.json and args.mode != "all":
            results = load_from_json(args.json)
            print(f"📂 加载 {len(results)} 项审计自查数据")
        else:
            results = run_interactive()
        if results:
            generate_audit(results, base_name, args.org, args.format)

    # ── 影响评估 ──
    if args.mode in ("impact", "all"):
        if args.json and args.mode == "impact":
            results = load_from_json(args.json)
            print(f"📂 加载 {len(results)} 项影响评估数据")
        elif args.mode == "impact":
            results = run_impact_interactive()
        elif args.mode == "all":
            # 在all模式下，如果是从JSON加载，复用audit的数据不适用
            print("\n⚠️  --mode all 交互模式会跳过影响评估。请分别运行。")
            return

        if args.mode == "impact" and results:
            generate_impact(results, base_name, args.org, args.format)

    print("✅ 完成")


if __name__ == "__main__":
    main()
