#!/usr/bin/env python3
"""把评分 JSON 注入模板,生成独立的评分报告 HTML。

用法:
  python build_report.py            # 读 data/scores.json
  python build_report.py --check    # 只校验 scores.json,不生成

Claude 打完分写 data/scores.json,这个脚本负责组装。
输出 data/score-report.html,自包含,可以直接双击打开。
"""

import argparse
import json
import os
import re
import sys
import time

import console  # noqa: F401  — 修 Windows GBK 控制台

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT, "data")
SESSION_PATH = os.path.join(DATA_DIR, "session.json")
SCORES_PATH = os.path.join(DATA_DIR, "scores.json")
TEMPLATE_PATH = os.path.join(ROOT, "web", "score-report.template.html")
OUT_PATH = os.path.join(DATA_DIR, "score-report.html")

PLACEHOLDER = "__SCORE_DATA__"
DIMS = ("substance", "structure", "relevance", "credibility", "differentiation")
DIM_LABELS = {
    "substance": "实质",
    "structure": "结构",
    "relevance": "相关性",
    "credibility": "可信度",
    "differentiation": "差异化",
}


def load(path, what):
    if not os.path.exists(path):
        raise SystemExit(f"找不到 {what}: {os.path.relpath(path, ROOT)}")
    with open(path, encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError as e:
            raise SystemExit(f"{what} 不是合法 JSON:{e}")


def validate(scores):
    """把错误一次全列出来,别让 Claude 改一个跑一次。"""
    errs = []

    overall = scores.get("overall")
    if not isinstance(overall, dict):
        errs.append("缺少 overall 对象")
    else:
        for d in DIMS:
            v = overall.get(d)
            if not isinstance(v, (int, float)):
                errs.append(f"overall.{d} 缺失或不是数字")
            elif not 1 <= v <= 5:
                errs.append(f"overall.{d} = {v},超出 1-5")

    pq = scores.get("per_question")
    if not isinstance(pq, list) or not pq:
        errs.append("per_question 缺失或为空")
    else:
        for i, item in enumerate(pq):
            tag = item.get("qid", f"#{i}")
            sc = item.get("scores")
            if not isinstance(sc, dict):
                errs.append(f"{tag}: 缺少 scores")
                continue
            for d in DIMS:
                v = sc.get(d)
                if not isinstance(v, int):
                    errs.append(f"{tag}.scores.{d} 必须是整数")
                elif not 1 <= v <= 5:
                    errs.append(f"{tag}.scores.{d} = {v},超出 1-5")

            errs.extend(_validate_strengths(item, tag))
            errs.extend(_validate_weaknesses(item, tag))
            errs.extend(_validate_rewrite(item, tag))

            fix = (item.get("fix") or "").strip()
            if not fix:
                errs.append(f"{tag}: fix 为空")
            elif len(fix) < 40:
                errs.append(f"{tag}: fix 太短({len(fix)} 字),要求 2-3 句可执行动作")

    return errs + _validate_summary_and_bottleneck(scores)


def _validate_strengths(item, tag):
    errs = []
    st = item.get("strengths")
    if not isinstance(st, list) or not st:
        return [f"{tag}: strengths 缺失或为空(每题至少一条,哪怕整题很差)"]
    for j, s in enumerate(st):
        if not isinstance(s, dict):
            errs.append(f"{tag}.strengths[{j}] 必须是对象")
            continue
        if not (s.get("quote") or "").strip():
            errs.append(f"{tag}.strengths[{j}].quote 为空")
        why = (s.get("why") or "").strip()
        if not why:
            errs.append(f"{tag}.strengths[{j}].why 为空")
        elif len(why) < 25:
            errs.append(f"{tag}.strengths[{j}].why 太短,要说清这句为什么值钱")
    return errs


def _validate_weaknesses(item, tag):
    errs = []
    wk = item.get("weaknesses")
    if not isinstance(wk, list) or not wk:
        return [f"{tag}: weaknesses 缺失或为空"]
    for j, w in enumerate(wk):
        if not isinstance(w, dict):
            errs.append(f"{tag}.weaknesses[{j}] 必须是对象")
            continue
        if not (w.get("quote") or "").strip():
            errs.append(f"{tag}.weaknesses[{j}].quote 为空")
        prob = (w.get("problem") or "").strip()
        if not prob:
            errs.append(f"{tag}.weaknesses[{j}].problem 为空")
        elif len(prob) < 30:
            errs.append(f"{tag}.weaknesses[{j}].problem 太短,要说清会导致什么后果")
        if w.get("dimension") not in DIMS:
            errs.append(f"{tag}.weaknesses[{j}].dimension 必须是 {DIMS} 之一")
    return errs


def _validate_rewrite(item, tag):
    rw = item.get("rewrite")
    if not isinstance(rw, dict):
        return [f"{tag}: rewrite 缺失(改写示范是点评里最有用的一块,不能省)"]
    errs = []
    for field in ("before", "after"):
        if not (rw.get(field) or "").strip():
            errs.append(f"{tag}.rewrite.{field} 为空")
    wc = (rw.get("what_changed") or "").strip()
    if not wc:
        errs.append(f"{tag}.rewrite.what_changed 为空")
    elif len(wc) < 30:
        errs.append(f"{tag}.rewrite.what_changed 太短,要说清改了什么、为什么")
    return errs


def _validate_summary_and_bottleneck(scores):
    errs = []

    summary = (scores.get("summary") or "").strip()
    if not summary:
        errs.append("缺少 summary(顶层全局总结,3-5 句)")
    elif len(summary) < 80:
        errs.append(f"summary 太短({len(summary)} 字),要有跨题观察")

    bn = scores.get("bottleneck")
    if not isinstance(bn, dict):
        return errs + ["缺少 bottleneck"]

    if bn.get("dimension") not in DIMS:
        errs.append(f"bottleneck.dimension 必须是 {DIMS} 之一")

    rc = (bn.get("root_cause") or "").strip()
    if not rc:
        errs.append("bottleneck.root_cause 为空")
    elif len(rc) < 50:
        errs.append(f"bottleneck.root_cause 太短({len(rc)} 字)")

    ev = bn.get("evidence_across_questions")
    if not isinstance(ev, list) or len(ev) < 2:
        errs.append("bottleneck.evidence_across_questions 至少两条(证明不是偶然)")
    else:
        for j, e in enumerate(ev):
            if not isinstance(e, dict):
                errs.append(f"bottleneck.evidence_across_questions[{j}] 必须是对象")
                continue
            for field in ("qid", "quote", "note"):
                if not (e.get(field) or "").strip():
                    errs.append(f"bottleneck.evidence_across_questions[{j}].{field} 为空")

    plan = bn.get("improvement_plan")
    if not isinstance(plan, list) or len(plan) != 3:
        errs.append("bottleneck.improvement_plan 必须是 3 步")
    else:
        for j, step in enumerate(plan):
            s = (step or "").strip() if isinstance(step, str) else ""
            if not s:
                errs.append(f"bottleneck.improvement_plan[{j}] 为空")
            elif len(s) < 25:
                errs.append(f"bottleneck.improvement_plan[{j}] 太短,要给具体动作")

    return errs

    bn = scores.get("bottleneck")
    if not isinstance(bn, dict):
        errs.append("缺少 bottleneck")
    else:
        if bn.get("dimension") not in DIMS:
            errs.append(f"bottleneck.dimension 必须是 {DIMS} 之一")
        for field in ("root_cause", "next_drill"):
            if not (bn.get(field) or "").strip():
                errs.append(f"bottleneck.{field} 为空")

    return errs


def check_quotes_grounded(scores, session):
    """所有 quote 必须能在用户实际回答里搜到 —— 防模型替用户编话。"""
    warns = []
    answers = {a["qid"]: a.get("text", "") for a in session.get("answers", [])}

    def norm(s):
        # 中英标点和空白差异很常见,别为这个报错
        return re.sub(r"[\s,,。.、;;::""''\"'!!??()()]+", "", s or "")

    for item in scores.get("per_question", []):
        qid = item.get("qid")
        src = norm(answers.get(qid, ""))
        if not src:
            continue
        quotes = [(s.get("quote"), "strengths") for s in item.get("strengths") or []]
        quotes += [(w.get("quote"), "weaknesses") for w in item.get("weaknesses") or []]
        rw = item.get("rewrite") or {}
        if rw.get("before"):
            quotes.append((rw["before"], "rewrite.before"))
        for q, where in quotes:
            if q and norm(q) not in src:
                warns.append(f"{qid}.{where} 的引用在原回答里找不到:{q[:30]!r}")

    for e in (scores.get("bottleneck") or {}).get("evidence_across_questions") or []:
        src = norm(answers.get(e.get("qid"), ""))
        if src and e.get("quote") and norm(e["quote"]) not in src:
            warns.append(
                f"bottleneck 引用在 {e.get('qid')} 原回答里找不到:{e['quote'][:30]!r}"
            )
    return warns


def synthesize_legacy_fields(scores):
    """从结构化字段合成旧的 evidence 字符串。

    前端当前把 evidence / fix 当纯字符串渲染。新 schema 用 strengths /
    weaknesses / rewrite 承载细节,这里合成一份 evidence,让现有页面不改也能
    显示更丰富的内容。前端升级成读结构化字段后,这个函数可以删。
    """
    for item in scores.get("per_question", []):
        if (item.get("evidence") or "").strip():
            continue  # 模型自己给了就不覆盖

        parts = []
        for s in item.get("strengths") or []:
            parts.append(f"✓ 你说「{s['quote']}」—— {s['why']}")
        for w in item.get("weaknesses") or []:
            parts.append(f"✗ 「{w['quote']}」—— {w['problem']}")
        rw = item.get("rewrite") or {}
        if rw.get("after"):
            parts.append(
                f"改写示范:把「{rw.get('before', '')}」换成「{rw['after']}」。"
                f"{rw.get('what_changed', '')}"
            )
        if parts:
            item["evidence"] = "\n\n".join(parts)

    bn = scores.get("bottleneck") or {}
    if bn and not (bn.get("next_drill") or "").strip():
        plan = bn.get("improvement_plan") or []
        if plan:
            bn["next_drill"] = "\n".join(f"{i}. {s}" for i, s in enumerate(plan, 1))


def check_consistency(scores):
    """算术和逻辑对不上时给警告,不阻断。"""
    warns = []
    pq = scores.get("per_question") or []
    overall = scores.get("overall") or {}

    for d in DIMS:
        vals = [q["scores"][d] for q in pq
                if isinstance(q.get("scores"), dict) and isinstance(q["scores"].get(d), int)]
        if not vals:
            continue
        want = round(sum(vals) / len(vals), 1)
        got = overall.get(d)
        if isinstance(got, (int, float)) and abs(got - want) > 0.05:
            warns.append(f"overall.{d} = {got},但逐题均值是 {want}")

    bn = scores.get("bottleneck") or {}
    if isinstance(overall, dict) and all(isinstance(overall.get(d), (int, float)) for d in DIMS):
        lowest = min(DIMS, key=lambda d: overall[d])
        if bn.get("dimension") and bn["dimension"] != lowest:
            warns.append(
                f"bottleneck 指向 {bn['dimension']},但最低分维度是 {lowest} "
                f"({overall[lowest]})"
            )
    return warns


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="只校验,不生成")
    args = ap.parse_args()

    scores = load(SCORES_PATH, "评分文件")

    errs = validate(scores)
    if errs:
        print("✗ scores.json 校验不通过:\n")
        for e in errs:
            print(f"  - {e}")
        return 1

    for w in check_consistency(scores):
        print(f"⚠ {w}")

    # 引用落地检查要读 session,--check 时也做(这是防编造的主要闸门)
    if os.path.exists(SESSION_PATH):
        for w in check_quotes_grounded(scores, load(SESSION_PATH, "session")):
            print(f"⚠ {w}")

    if args.check:
        print("✓ scores.json 校验通过。")
        return 0

    session = load(SESSION_PATH, "session")
    synthesize_legacy_fields(scores)
    answers = {a["qid"]: a for a in session.get("answers", [])}
    questions = {q["id"]: q for q in session.get("questions", [])}

    # 把 session 里的题干和回答补进报告,让前端不用同时读两个文件
    for item in scores.get("per_question", []):
        qid = item.get("qid")
        q, a = questions.get(qid, {}), answers.get(qid, {})
        item.setdefault("question", q.get("text", ""))
        item.setdefault("competency", q.get("competency", ""))
        if "answer_excerpt" not in item:
            text = a.get("text", "")
            item["answer_excerpt"] = text[:200] + ("…" if len(text) > 200 else "")
        item.setdefault("input_mode", a.get("input_mode"))
        item.setdefault("duration_sec", a.get("duration_sec"))

    n_answered = len(answers)
    n_total = len(questions)
    scores.setdefault("session_id", session.get("session_id"))
    scores.setdefault("context", session.get("context", {}))
    scores.setdefault("generated_at", time.strftime("%Y-%m-%d %H:%M"))
    scores.setdefault("answered_count", n_answered)
    scores.setdefault("partial", n_answered < n_total)

    bn = scores["bottleneck"]
    bn.setdefault("label", DIM_LABELS.get(bn["dimension"], bn["dimension"]))
    bn.setdefault("score", scores["overall"].get(bn["dimension"]))

    if not os.path.exists(TEMPLATE_PATH):
        raise SystemExit(
            f"找不到模板 web/score-report.template.html\n"
            f"这个文件由前端同事提供,里面要有占位符 {PLACEHOLDER}\n"
            f"格式见 api-contract.md 的「评分报告模板」一节。"
        )

    with open(TEMPLATE_PATH, encoding="utf-8") as f:
        html = f.read()

    n_found = html.count(PLACEHOLDER)
    if n_found == 0:
        raise SystemExit(f"模板里没有占位符 {PLACEHOLDER},无法注入。")

    payload = json.dumps(scores, ensure_ascii=False, indent=2)
    # </script> 会提前闭合宿主 script 标签
    payload = payload.replace("</", "<\\/")

    # 只替换真正的 script 标签那一处。
    # 模板注释里通常也会提到占位符名字(说明用途),全局 replace 会把几 KB 的
    # JSON 灌进注释,而且 JSON 里的 "--" 会提前闭合 HTML 注释、把页面弄坏。
    m = re.search(
        r'(<script\b[^>]*\bid=["\']score-data["\'][^>]*>)\s*'
        + re.escape(PLACEHOLDER) + r'\s*(</script>)',
        html,
    )
    if m:
        out = html[:m.start()] + m.group(1) + payload + m.group(2) + html[m.end():]
    else:
        # 没有标准 script 标签时退回替换最后一处 —— 注释一般在文件靠前
        head, _, tail = html.rpartition(PLACEHOLDER)
        out = head + payload + tail
        if n_found > 1:
            print(f"⚠ 模板里有 {n_found} 处 {PLACEHOLDER},且找不到 "
                  f'id="score-data" 的 script 标签 —— 只替换了最后一处。')

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(out)

    print(f"✓ 报告已生成:{os.path.relpath(OUT_PATH, ROOT)}")
    if scores["partial"]:
        print(f"  注意:只有 {n_answered}/{n_total} 题,报告里已标为低置信度。")
    print(f"  瓶颈维度:{bn['label']} ({bn.get('score')})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
