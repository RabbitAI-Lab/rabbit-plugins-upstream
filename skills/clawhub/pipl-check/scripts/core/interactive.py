"""交互式问答 — 支持审计自查和影响评估两种模式"""

import sys
from .audit_items import AUDIT_ITEMS, AUDIT_STATUS_CHOICES, IMPACT_ITEMS


def _ask_choice(prompt: str, options: list[str], allow_skip: bool = True) -> str:
    """通用选择题：显示选项编号，返回选择的文本"""
    labels = {str(i + 1): opt for i, opt in enumerate(options)}
    prompt_text = f"  {prompt} ({'/'.join(f'{k}={v}' for k, v in labels.items())}"
    if allow_skip:
        prompt_text += ", 空=跳过"
    prompt_text += "): "
    while True:
        try:
            inp = input(prompt_text).strip()
            if inp == "" and allow_skip:
                return "跳过"
            if inp in labels:
                return labels[inp]
            print(f"  请输入 {', '.join(labels.keys())} 之一")
        except (EOFError, KeyboardInterrupt):
            print()
            return "跳过"


def run_interactive() -> list[dict]:
    """附件1：19项合规审计自查 — 逐项问答"""
    print()
    print("=" * 60)
    print("  附件1：个人信息保护合规审计自查表")
    print("  依据：《小型个人信息处理者个人信息保护简化措施规定》")
    print("=" * 60)
    print("  请逐项判断合规情况：")
    print()

    results = []
    for item in AUDIT_ITEMS:
        print(f"── [{item['id']:2d}/19] {item['name']} ──")
        print(f"  {item['description'][:100]}...")
        print(f"  依据: {item['pipl_articles']}")
        status = _ask_choice("合规情况", AUDIT_STATUS_CHOICES)
        note = ""
        if status == "不合规":
            note = input("  整改说明（可空）: ").strip()
        results.append({"id": item["id"], "status": status, "note": note})
        print()

    return results


def run_impact_interactive() -> list[dict]:
    """附件2：个人信息保护影响评估表 — 逐项问答"""
    print()
    print("=" * 60)
    print("  附件2：个人信息保护影响评估表")
    print("  依据：《小型个人信息处理者个人信息保护简化措施规定》")
    print("=" * 60)
    print()

    results = []
    for scenario in IMPACT_ITEMS:
        print(f"── [{scenario['id']}/5] {scenario['name']} ──")
        answers = []
        for criterion in scenario["criteria"]:
            ans = _ask_choice(criterion["q"], criterion["choices"])
            answers.append({"question": criterion["q"], "answer": ans})
        note = input("  备注（可空）: ").strip()
        results.append({"id": scenario["id"], "answers": answers, "note": note})
        print()

    return results
