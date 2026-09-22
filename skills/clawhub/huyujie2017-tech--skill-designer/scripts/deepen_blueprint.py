#!/usr/bin/env python3
"""
deepen_blueprint.py — 四步施工流 Step ③「深化设计」批量处理引擎

②初步方案 出的是**有主张的设计稿**：AI 建议标【AI 建议】、用户必答标【需用户拍板】、
时机未到标【待回填】。③深化设计 要做的就是**逐格确认**——实测这一步若不脚本化，
用户要手工处理近百个标记，根本走不完（实跑 personal-workbench 案例验证）。

本脚本把③的三种典型动作变成一条命令：

  1. 采纳   —— 用户回「按建议」，批量去掉【AI 建议】标记（= 确认 AI 主张）
  2. 拍板   —— 给【需用户拍板】/【待回填】字段定向赋值
  3. 勾验收 —— checklist 的 ☐ 勾成 ☑（只勾用户真正确认过的）

用法：
    # 回「按建议」：批量采纳全部 AI 建议
    python scripts/deepen_blueprint.py <蓝图目录> --accept-all

    # 只采纳某几格（推翻其他格时）
    python scripts/deepen_blueprint.py <蓝图目录> --accept B01,B03,B05

    # 定向拍板 / 回填（键用中文，与蓝图字段名一致）
    python scripts/deepen_blueprint.py <蓝图目录> \
        --set "B02.正交性=与 personal-workbench 是上下游：它产数据，本 skill 消费并汇总" \
        --set "B08.验证场景=用真实一周数据跑一次，核对断签与超支是否被点名"

    # 勾验收 checklist（用户确认后）
    python scripts/deepen_blueprint.py <蓝图目录> --tick B01,B02,B06

    # 组合：采纳 + 拍板 + 勾验收，一次走完③
    python scripts/deepen_blueprint.py <蓝图目录> --accept-all \
        --set "B02.正交性=..." --tick B01,B02

    # 只看现状，不改动（默认行为，安全）
    python scripts/deepen_blueprint.py <蓝图目录>

参数：
    目标目录       蓝图 bundle 目录
    --accept-all  采纳全部格的【AI 建议】
    --accept      采纳指定格（逗号分隔，如 B01,B03）
    --set         定向赋值，格式 "B<格号>.<字段名>=<值>"，可重复
    --tick        勾验收 checklist 的指定格
    --json        结构化输出（stdout 纯净）

说明：
  · 以 `>` 开头的行是**说明块**（解释标记含义），不参与任何改动与统计——
    否则会把"标【需用户拍板】的必须由用户拍板"这句说明当成待拍板项。
  · 采纳时会顺带去掉 （AI 已判定·待复核） 后缀——用户回「按建议」即等于复核确认。
  · 不假勾：--tick 只勾你显式指定的格，B08 这类"必须真跑才算"的由用户自己判断。

退出码：0 = 成功（无论是否有改动）；1 = 参数/目录错误。
"""

import argparse
import json
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from errors import enable_utf8  # noqa: E402

enable_utf8()  # Windows GBK 控制台下保证中文（含 stderr 报错）不乱码

try:
    from blocks import BLOCKS
    from retry import read_text_robust, write_text_robust
except ImportError:  # 允许直接以脚本方式运行
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from blocks import BLOCKS
    from retry import read_text_robust, write_text_robust

AI_TAG = "【AI 建议】"
DECIDE_TAG = "【需用户拍板】"
TODO_TAG = "【待回填】"
RECHECK = "（AI 已判定·待复核）"
ALL_TAGS = (AI_TAG, DECIDE_TAG, TODO_TAG)

# 格号 → 文件名（与 export_brief.BLOCK_FILES 同口径；BLOCKS 是无 id 的 list，故由 file 反推）
BLOCK_FILES = {f"B{b['file'][:2]}": b["file"] for b in BLOCKS}

# checklist 行：以 - ☐ 或 - ☑ 开头
CHECK_RE = re.compile(r"^(\s*-\s*)☐\s*(.*)$")
MARK_LINE_RE = re.compile(r"^(?!\s*>)\s*[-*]?\s*(.+)$")

# 实证类验收项：只有 skill 真正落地跑过才成立，脚本**不得代勾**。
# 这类项由用户亲自跑完再手勾；脚本勾了就是伪造证据（E 维大忌）。
EVIDENCE_KEYWORDS = (
    "真实场景", "有 / 无 skill 对比", "有无 skill 对比", "有无对比",
    "真跑", "实测", "实际运行", "真实数据",
)


def is_note_line(line: str) -> bool:
    """说明块：以 > 开头的引用行，不参与改动与统计。"""
    return line.lstrip().startswith(">")


def tid(s: str) -> str:
    """清理标记与多余空白（保持与 render_structure.clean 同口径）。"""
    for t in ALL_TAGS + ("【草稿，待确认】", "【草稿,待确认】", "【待确认】"):
        s = s.replace(t, "")
    return re.sub(r"\s{2,}", " ", s).strip().strip("／/,，、;；")


def scan(text: str) -> dict:
    """统计一格里各类标记与未勾验收项（跳过说明块）。"""
    out = {"ai": 0, "decide": 0, "todo": 0, "unticked": 0, "recheck": 0}
    for line in text.splitlines():
        if is_note_line(line):
            continue
        if AI_TAG in line:
            out["ai"] += 1
        if DECIDE_TAG in line:
            out["decide"] += 1
        if TODO_TAG in line:
            out["todo"] += 1
        if CHECK_RE.match(line):
            out["unticked"] += 1
        if RECHECK in line:
            out["recheck"] += 1
    return out


def accept_text(text: str) -> tuple[str, int]:
    """采纳：去掉【AI 建议】标记 + 去掉（AI 已判定·待复核）后缀。"""
    n = 0
    lines = []
    for line in text.splitlines(keepends=True):
        if is_note_line(line):
            lines.append(line)
            continue
        if AI_TAG in line or RECHECK in line:
            # 必须先把行首项目符号摘出来再清理，否则 tid 保留的 "- " 会和
            # 重新拼上的前缀叠成 "- - "（实跑 personal-workbench 时踩到）。
            m = re.match(r"^(\s*(?:[-*]\s+)?)", line)
            prefix, body = (m.group(1), line[m.end():]) if m else ("", line)
            body = tid(body.replace(AI_TAG, "").replace(RECHECK, "").rstrip("\n"))
            if not prefix.strip():
                prefix = "- "
            lines.append(f"{prefix}{body}\n")
            n += 1
        else:
            lines.append(line)
    return "".join(lines), n


def set_field(text: str, key: str, value: str) -> tuple[str, int]:
    """定向赋值：把 `- <key>：<原值>` 整行替换为 `- <key>：<value>`，并清掉所有标记。

    匹配键名后允许全角/半角冒号。找不到返回改动数 0（调用方据此报错）。
    """
    pat = re.compile(rf"^(\s*-\s*){re.escape(key)}\s*[:：].*$")
    n = 0
    lines = []
    for line in text.splitlines():
        if not is_note_line(line) and pat.match(line):
            m = pat.match(line)
            lines.append(f"{m.group(1)}{key}：{value}")
            n += 1
        else:
            lines.append(line)
    return "\n".join(lines) + ("\n" if text.endswith("\n") else ""), n


def tick_text(text: str) -> tuple[str, int, list]:
    """勾验收：☐ → ☑，并去掉（AI 已判定·待复核）后缀。

    实证类项（真实场景 / 有·无对比 / 实测 等）**跳过不勾**，原样保留并返回到
    skipped 列表 —— 这些必须用户真跑完自己勾，脚本代勾等于伪造证据。
    """
    n = 0
    skipped = []
    lines = []
    for line in text.splitlines():
        if is_note_line(line):
            lines.append(line)
            continue
        m = CHECK_RE.match(line)
        if m:
            raw = m.group(2)
            if any(k in raw for k in EVIDENCE_KEYWORDS):
                lines.append(line)
                skipped.append(raw.strip())
                continue
            body = raw.replace(RECHECK, "")
            lines.append(f"{m.group(1)}☑ {tid(body)}".rstrip())
            n += 1
        elif RECHECK in line:
            lines.append(tid(line.replace(RECHECK, "")).rstrip())
            n += 1
        else:
            lines.append(line)
    return "\n".join(lines) + ("\n" if text.endswith("\n") else ""), n, skipped


def parse_set(expr: str) -> tuple[str, str, str]:
    """解析 "B02.正交性=值" → ("B02", "正交性", "值")。"""
    if "=" not in expr:
        raise ValueError(f"--set 缺少 '='：{expr}")
    lhs, value = expr.split("=", 1)
    if "." not in lhs:
        raise ValueError(f"--set 需用 'B<格号>.<字段名>' 定位：{expr}")
    bid, key = lhs.split(".", 1)
    bid = bid.strip().upper()
    if not re.fullmatch(r"B\d{2}", bid):
        raise ValueError(f"格号格式应为 B01–B10：{bid}")
    return bid, key.strip(), value.strip()


def normalize_bids(raw: str) -> list[str]:
    out = []
    for part in raw.replace("，", ",").split(","):
        p = part.strip().upper()
        if not p:
            continue
        if not re.fullmatch(r"B?\d{1,2}", p):
            raise ValueError(f"格号无法识别：{part}")
        out.append(p if p.startswith("B") else f"B{int(p):02d}")
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description="③深化设计：批量采纳 AI 建议 / 定向拍板 / 勾验收 checklist",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("target", help="蓝图目录")
    ap.add_argument("--accept-all", action="store_true", help="采纳全部格的【AI 建议】")
    ap.add_argument("--accept", help="采纳指定格（逗号分隔，如 B01,B03）")
    ap.add_argument("--set", action="append", default=[], metavar="B02.字段=值",
                    help="定向赋值，可重复")
    ap.add_argument("--tick", help="勾验收 checklist 的指定格（逗号分隔）")
    ap.add_argument("--json", action="store_true", help="JSON 输出（stdout 纯净）")
    args = ap.parse_args(argv)

    bp = Path(args.target)
    if not bp.is_dir():
        msg = f"蓝图目录不存在：{bp}"
        if args.json:
            print(json.dumps({"ok": False, "error": msg}, ensure_ascii=False))
        else:
            print(f"❌ {msg}", file=sys.stderr)
        return 1

    # 解析动作
    try:
        accept_bids = normalize_bids(args.accept) if args.accept else []
        tick_bids = normalize_bids(args.tick) if args.tick else []
        sets = [parse_set(s) for s in args.set]
    except ValueError as e:
        msg = str(e)
        if args.json:
            print(json.dumps({"ok": False, "error": msg}, ensure_ascii=False))
        else:
            print(f"❌ {msg}", file=sys.stderr)
        return 1

    if args.accept_all:
        accept_bids = list(BLOCK_FILES)

    write_mode = bool(accept_bids or sets or tick_bids)

    # 1) 扫描现状
    before = {}
    for bid in BLOCK_FILES:
        f = bp / BLOCK_FILES[bid]
        before[bid] = scan(read_text_robust(f)) if f.exists() else None

    if not write_mode:
        payload = {
            "ok": True,
            "dir": str(bp),
            "mode": "scan",
            "blocks": before,
            "totals": {
                k: sum((v or {}).get(k, 0) for v in before.values())
                for k in ("ai", "decide", "todo", "unticked", "recheck")
            },
        }
        if args.json:
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            print(f"[deepen] 蓝图：{bp}（只读扫描，未改动）\n")
            print(f"{'格':<5}{'AI建议':>7}{'待拍板':>7}{'待回填':>7}{'未勾':>6}")
            print("-" * 34)
            for bid in BLOCK_FILES:
                v = before[bid]
                if v is None:
                    print(f"{bid:<5}{'—':>7}")
                    continue
                print(f"{bid:<5}{v['ai']:>7}{v['decide']:>7}{v['todo']:>7}{v['unticked']:>6}")
            t = payload["totals"]
            print("-" * 34)
            print(f"{'合计':<5}{t['ai']:>7}{t['decide']:>7}{t['todo']:>7}{t['unticked']:>6}")
            print("\n→ 采纳：--accept-all 或 --accept B01,B03")
            print("  拍板：--set \"B02.正交性=...\"")
            print("  勾验收：--tick B01,B02")
        return 0

    # 2) 执行改动
    changed, errors, evidence_skipped = [], [], []
    for bid in BLOCK_FILES:
        f = bp / BLOCK_FILES[bid]
        if not f.exists():
            continue
        text = read_text_robust(f)
        orig = text
        counts = {"accepted": 0, "set": 0, "ticked": 0}

        if bid in accept_bids:
            text, counts["accepted"] = accept_text(text)
        for sbid, key, value in sets:
            if sbid == bid:
                text, n = set_field(text, key, value)
                counts["set"] += n
                if n == 0:
                    errors.append(f"{bid} 未找到字段「{key}」")
        if bid in tick_bids:
            text, counts["ticked"], skipped = tick_text(text)
            if skipped:
                counts["skipped"] = skipped
                evidence_skipped.extend(f"{bid}：{s}" for s in skipped)

        if text != orig:
            write_text_robust(f, text)
            changed.append({"block": bid, "file": BLOCK_FILES[bid], **counts})

    # 3) 扫描改后
    after = {}
    for bid in BLOCK_FILES:
        f = bp / BLOCK_FILES[bid]
        after[bid] = scan(read_text_robust(f)) if f.exists() else None

    def tot(d, k):
        return sum((v or {}).get(k, 0) for v in d.values())

    payload = {
        "ok": True,
        "dir": str(bp),
        "mode": "apply",
        "changed": changed,
        "errors": errors,
        "evidence_skipped": evidence_skipped,
        "before": {k: tot(before, k) for k in ("ai", "decide", "todo", "unticked")},
        "after": {k: tot(after, k) for k in ("ai", "decide", "todo", "unticked")},
    }

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0

    print(f"[deepen] 蓝图：{bp}")
    for c in changed:
        bits = [f"采纳 {c['accepted']}" if c['accepted'] else "",
                f"赋值 {c['set']}" if c['set'] else "",
                f"勾验收 {c['ticked']}" if c['ticked'] else ""]
        print(f"  ✅ {c['block']} {c['file']} — {' / '.join(b for b in bits if b)}")
    for e in errors:
        print(f"  ⚠️ {e}")
    for s in evidence_skipped:
        print(f"  ⛔ 实证项不代勾（须用户真跑后手勾）：{s}")
    print()
    b, a = payload["before"], payload["after"]
    print(f"  剩余标记：AI建议 {b['ai']}→{a['ai']} ｜ 待拍板 {b['decide']}→{a['decide']} "
          f"｜ 待回填 {b['todo']}→{a['todo']} ｜ 未勾 {b['unticked']}→{a['unticked']}")
    print("→ 下一步：跑 `sd_cli check <目录>` 看 IQS；剩下【待回填】项多为④施工蓝图后才填得出。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
