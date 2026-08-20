#!/usr/bin/env python3
"""从会议文本中抽取行动项：owner(@/称呼)、截止时间、动作 三元组（启发式初稿）。"""
import argparse, json, re


AT_RE = re.compile(r"@([\w一-龥]{1,12})")
DATE_RE = re.compile(r"(\d{1,2}月\d{1,2}日|\d{4}-\d{1,2}-\d{1,2}|本周\w*|下?\w*底|明天|下周\w*)")
ACTION_KW = re.compile(r"(需要|应当|负责|跟进|完成|提交|输出|安排|确认|准备|修复|上线|评审)")


def extract(text):
    actions = []
    for ln in text.splitlines():
        if not ACTION_KW.search(ln):
            continue
        owners = AT_RE.findall(ln)
        dates = DATE_RE.findall(ln)
        if owners or dates:
            actions.append({
                "owner": owners[0] if owners else "（待确认）",
                "deadline": dates[0] if dates else "（待确认）",
                "action": ln.strip()[:200],
            })
    return actions


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    text = open(args.path, encoding="utf-8", errors="replace").read()
    acts = extract(text)
    if args.json:
        print(json.dumps(acts, ensure_ascii=False, indent=2))
    else:
        print(f"抽取到行动项：{len(acts)}")
        for a in acts:
            print(f"  @{a['owner']} 截止{a['deadline']} :: {a['action'][:80]}")


if __name__ == "__main__":
    main()
