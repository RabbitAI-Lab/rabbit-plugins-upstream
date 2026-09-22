#!/usr/bin/env python3
"""
run_evals.py — 触发词用例自检（Adaptability / TRACE-A 维的机器可验证证据）

为什么需要这个脚本：
    A 维（触发可辨）此前只能靠评审"读文案凭感觉"打分——本 skill 有 20 个脚本、
    23 份 references，但**没有任何一条用例**能证明"用户说了某句话就该触发我"。
    这让 A 维的自评失去依据（也因此出现过自评 A 5.0、平台实评 4.0 的落差）。

    本脚本把 `scripts/evals.json` 里的真实说法变成可复跑的断言：
      - 正例：用户会说的启动说法，必须能在证据源中找到覆盖 → 防漏触发
      - 负例：不该接管的说法，必须出现在证据源的排除区     → 防误触发
      - 冲突：正例词不得落在排除区、负例词不得落在正例区   → 防自相矛盾

    **双证据源**（`case.source` 字段，缺省 description）——方法论见条目 D-127 / 原则 DP-207：
      - `description` — 一等证据，平台召回层，受 1024 字符硬限制，只放一等口令与判定口诀
      - `router`      — 二等证据，agent 路由层，即 references/router-full.md Part 2，
                        承接 description 塞不下的长尾真实说法（槽位匹配表 + 真实语料库）
      拆两层的理由：把 60+ 种说法硬塞进 description 既撑爆上限又稀释召回精度；
      正确做法是 description 管「要不要叫我」，路由表管「这句话算不算」。

    它同时是一条**回归防线**：以后谁改 description 删掉了某个触发词，这里立刻红。

用法：
    python scripts/run_evals.py            # 人类可读报告
    python scripts/run_evals.py --json     # 机器消费
    python scripts/sd_cli.py evals         # 统一入口
"""

import argparse
import json
import re
import sys
from pathlib import Path

try:
    from errors import enable_utf8, fail
except ImportError:  # 直调时把 scripts/ 加进路径
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from errors import enable_utf8, fail


def read_description(skill_md: Path) -> str:
    """从 SKILL.md 的 YAML frontmatter 提取 description 字段值。

    同时支持两种写法：
      - 单行 / 引号包裹：description: '……'
      - **块标量**：     description: | 后接缩进块（本 skill 采用这种，多行更易读）

    为什么必须自己解析而不引 yaml：本 skill 承诺零依赖（不在用户环境装任何包），
    pyyaml 不可用是常态，正则解析足够覆盖这两种固定写法。
    """
    if not skill_md.is_file():
        return ""
    text = skill_md.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---"):
        return ""
    end = text.find("\n---", 3)
    front = text[3:end] if end != -1 else text
    m = re.search(r"^description:\s*(.+?)\s*$", front, re.M)
    if not m:
        return ""
    val = m.group(1).strip()

    # ① 引号包裹的单行
    for quote in ("'", '"'):
        if val.startswith(quote):
            inner = val[1:]
            if inner.endswith(quote):
                inner = inner[:-1]
            return inner

    # ② 块标量（| 或 >）：收集后续所有缩进更深的行
    if val in ("|", ">", "|-", ">-", "|+", ">+"):
        lines = front.split("\n")
        start = next((i for i, ln in enumerate(lines)
                      if re.match(r"^description:", ln)), None)
        if start is None:
            return ""
        # 以首个非空内容行确定缩进基准，收集所有缩进 >= 基准的行
        block = []
        for ln in lines[start + 1:]:
            if not ln.strip():
                block.append("")
                continue
            indent = len(ln) - len(ln.lstrip())
            if start + 1 == lines.index(ln) or block:
                pass
            if indent == 0:
                break
            block.append(ln.strip())
        return "\n".join(block).strip()
    return val


def split_regions(desc: str):
    """切出 Use when（正例覆盖区）与 Do NOT use for（负例排除区）。"""
    i_when = desc.find("Use when")
    i_neg = desc.find("Do NOT use for")
    when = desc[i_when:i_neg] if (i_when != -1 and i_neg > i_when) else desc
    neg = desc[i_neg:] if i_neg != -1 else ""
    return when, neg


def read_router(skill_dir: Path) -> str:
    """读取长尾意图路由表（description 的二等证据源）。"""
    for rel in ("references/router-full.md", "router-full.md"):
        p = skill_dir / rel
        if p.is_file():
            return p.read_text(encoding="utf-8", errors="replace")
    return ""


def split_router(router: str):
    """切出路由表正文（可命中区）与 Part 2.3 边界区（排除区）。"""
    i_b = router.find("### 2.3")
    body = router[:i_b] if i_b != -1 else router
    boundary = router[i_b:] if i_b != -1 else ""
    return body, boundary


def hit_any(text: str, matches):
    """返回第一个命中的片段，未命中返回 None。"""
    for m in matches or []:
        if m and m in text:
            return m
    return None


def run(skill_dir: Path, quiet=False):
    evals_path = skill_dir / "scripts" / "evals.json"
    skill_md = skill_dir / "SKILL.md"

    if not evals_path.is_file():
        return 1, {"error": f"缺用例文件：{evals_path}"}
    try:
        data = json.loads(evals_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return 1, {"error": f"evals.json 解析失败：{e}"}

    desc = read_description(skill_md)
    if not desc:
        return 1, {"error": f"无法从 {skill_md} 提取 description"}
    when, neg = split_regions(desc)
    router = read_router(skill_dir)
    r_body, r_boundary = split_router(router)

    cases = data.get("cases", [])
    results, n_pass = [], 0
    pos_total = pos_pass = neg_total = neg_pass = conflicts = 0

    for c in cases:
        cid, prompt = c.get("id", "?"), c.get("prompt", "")
        matches = c.get("match", [])
        want = bool(c.get("should_trigger", True))
        # 证据源：description（一等，平台召回用）｜ router（二等，长尾真实说法）
        src = str(c.get("source", "description")).lower()
        if src == "router":
            if not router:
                results.append((cid, prompt, False, "证据源 router 缺失：references/router-full.md 不存在"))
                continue
            hay, pos_zone, neg_zone = router, r_body, r_boundary
        else:
            hay, pos_zone, neg_zone = desc, when, neg

        hit = hit_any(hay, matches)

        if want:
            pos_total += 1
            if hit:
                # 冲突：正例词若同时出现在排除区，说明证据源自相矛盾
                if neg_zone and hit in neg_zone:
                    conflicts += 1
                    results.append((cid, prompt, False, f"冲突：「{hit}」同时出现在 {src} 排除区"))
                else:
                    pos_pass += 1
                    n_pass += 1
                    tag = "（路由表）" if src == "router" else ""
                    results.append((cid, prompt, True, f"命中「{hit}」{tag}"))
            else:
                results.append((cid, prompt, False, f"未覆盖：{matches} 均不在 {src} 中"))
        else:
            neg_total += 1
            hit_neg = hit_any(neg_zone, matches)
            if hit_neg:
                # 冲突：负例词若出现在正例区，说明该说法被同时"要"和"不要"
                if pos_zone and hit_neg in pos_zone:
                    conflicts += 1
                    results.append((cid, prompt, False, f"冲突：「{hit_neg}」同时出现在 {src} 正例区"))
                else:
                    neg_pass += 1
                    n_pass += 1
                    tag = "（路由表）" if src == "router" else ""
                    results.append((cid, prompt, True, f"已排除「{hit_neg}」{tag}"))
            else:
                results.append((cid, prompt, False, f"未排除：{matches} 均不在 {src} 排除区"))

    summary = {
        "total": len(cases),
        "passed": n_pass,
        "positive": f"{pos_pass}/{pos_total}",
        "negative": f"{neg_pass}/{neg_total}",
        "conflicts": conflicts,
        "results": [
            {"id": i, "prompt": p, "pass": ok, "detail": d} for i, p, ok, d in results
        ],
    }

    if not quiet:
        print("=" * 60)
        print(f"触发词用例自检: {data.get('skill', 'skill-designer')}")
        print("=" * 60)
        for cid, prompt, ok, detail in results:
            flag = "PASS" if ok else "FAIL"
            print(f"  [{flag}] {cid} {prompt[:34]:<34} — {detail}")
        print("  " + "-" * 56)
        print(f"  正例 {pos_pass}/{pos_total} · 负例 {neg_pass}/{neg_total} · 冲突 {conflicts}")
        print(f"  结果: {n_pass}/{len(cases)} 通过")

    ok = n_pass == len(cases) and conflicts == 0
    return (0 if ok else 1), summary


def main(argv=None) -> int:
    enable_utf8()
    ap = argparse.ArgumentParser(description="触发词用例自检（A 维证据）")
    ap.add_argument("target", nargs="?", default=".", help="skill 目录（默认当前目录）")
    ap.add_argument("--json", action="store_true", help="输出 JSON 而非人类可读报告")
    args = ap.parse_args(argv)

    skill_dir = Path(args.target).resolve()
    code, summary = run(skill_dir, quiet=args.json)
    if "error" in summary:
        return fail("E001", detail=summary["error"], script="run_evals")
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    return code


if __name__ == "__main__":
    sys.exit(main())
