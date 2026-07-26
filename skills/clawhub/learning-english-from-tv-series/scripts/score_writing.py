#!/usr/bin/env python3
"""DramaLex · score_writing.py — 写作 rubric 自动化校验

把「写作反馈」从「等 agent 改」变成「先自检、再精修」：
  读取 tasks.json 中 writing[].checks（机器可校验量规），对用户作文自动打分：
    - has_word:X  必须含目标词/语块（大小写不敏感；支持带空格的语块，整体子串匹配）
    - min_words:N / max_words:N  字数上下限（按空白分词）
    - tense:past  软提示（检测是否出现常见过去式标记 -ed，仅提示不强制）
  输出逐项通过情况 + 总评 + 改进建议。agent 仍可在此基础上做深度批改。

用法：
  python score_writing.py --task 1 --text-file essay.txt --tasks tasks.json
  python score_writing.py --task 1 --text "I freaked out..." --tasks tasks.json
  python score_writing.py --all --tasks tasks.json --dir ./essays   # 批量
"""
import argparse, json, os, re, sys

def count_words(t):
    return len(re.findall(r"[A-Za-z0-9']+", t or ''))

def has_word(text, word):
    return word.lower().strip() in (text or '').lower()

def check_tense_past(text):
    # 软提示：检测是否含过去式动词（粗略：以 -ed 结尾的实词，或常见不规则过去式）
    irreg = {'went','came','saw','told','said','got','made','took','gave','found',
             'left','met','felt','thought','knew','began','began','wrote','spoke','ate','drank'}
    toks = re.findall(r"[a-z']+", (text or '').lower())
    if any(t in irreg for t in toks):
        return True
    if any(t.endswith('ed') and len(t) > 3 for t in toks):
        return True
    return False

def run_checks(checks, text):
    results = []
    for c in (checks or []):
        t = c.get('type'); v = c.get('value')
        if t == 'has_word':
            ok = has_word(text, str(v))
            results.append({"check": f"has_word:{v}", "pass": ok,
                            "msg": ("含目标词" if ok else f"缺少目标词/语块「{v}」")})
        elif t == 'min_words':
            n = count_words(text); ok = n >= int(v)
            results.append({"check": f"min_words:{v}", "pass": ok,
                            "msg": (f"字数 {n}≥{v} ✓" if ok else f"字数 {n} < {v}，再写一点")})
        elif t == 'max_words':
            n = count_words(text); ok = n <= int(v)
            results.append({"check": f"max_words:{v}", "pass": ok,
                            "msg": (f"字数 {n}≤{v} ✓" if ok else f"字数 {n} > {v}，精简到 {v} 以内")})
        elif t == 'tense':
            ok = check_tense_past(text) if str(v) == 'past' else True
            results.append({"check": f"tense:{v}", "pass": ok,
                            "msg": ("检测到过去式 ✓" if ok else "未检测到明显过去式，注意时态是否合适（仅提示）")})
        else:
            results.append({"check": f"{t}:{v}", "pass": None, "msg": f"未知量规类型 {t}（跳过）"})
    return results

def score_task(task, text):
    checks = task.get('checks') or []
    res = run_checks(checks, text)
    passed = [r for r in res if r['pass'] is True]
    failed = [r for r in res if r['pass'] is False]
    na = [r for r in res if r['pass'] is None]
    rate = (len(passed) / len(res)) if res else 1.0
    advice = []
    if failed:
        advice.append("需修改：" + "；".join(r['msg'] for r in failed))
    if not checks:
        advice.append("本条未设自动量规，仅做人工 rubric 自评 + agent 批改。")
    if task.get('require_words'):
        miss = [w for w in task['require_words'] if not has_word(text, w)]
        if miss:
            advice.append(f"目标词未全部出现：{', '.join(miss)}（recycling spine 要求复现）")
    return {"id": task.get('id'), "task_type": task.get('type'),
            "word_count": count_words(text), "pass_rate": round(rate, 2),
            "results": res, "advice": advice}

def main():
    ap = argparse.ArgumentParser(description="DramaLex 写作 rubric 自动校验")
    ap.add_argument('--tasks', default='tasks.json', help='tasks.json 路径')
    ap.add_argument('--task', type=int, help='写作条目 id（单条评分）')
    ap.add_argument('--text', help='作文文本，或')
    ap.add_argument('--text-file', help='作文文件路径')
    ap.add_argument('--all', action='store_true', help='批量评所有写作条目')
    ap.add_argument('--dir', default='.', help='批量：作文目录（<id>.txt）')
    ap.add_argument('--json', action='store_true', help='输出 JSON')
    args = ap.parse_args()

    tasks = json.load(open(args.tasks, encoding='utf-8'))
    writings = tasks.get('writing', [])

    def get_text():
        if args.text_file:
            return open(args.text_file, encoding='utf-8').read()
        if args.text is not None:
            return args.text
        return None

    if args.all:
        out = []
        for w in writings:
            p = os.path.join(args.dir, f"{w.get('id')}.txt")
            if not os.path.exists(p):
                out.append({"id": w.get('id'), "status": "no_essay"}); continue
            txt = open(p, encoding='utf-8').read()
            out.append(score_task(w, txt))
        print(json.dumps(out, ensure_ascii=False, indent=2) if args.json else _fmt_batch(out))
        return 0

    if args.task is None:
        print("请指定 --task <id> 或 --all。", file=sys.stderr); return 2
    task = next((w for w in writings if w.get('id') == args.task), None)
    if not task:
        print("tasks.json 中无 writing id =", args.task, file=sys.stderr); return 2
    text = get_text()
    if text is None:
        print("请用 --text \"...\" 或 --text-file essay.txt 提供作文。", file=sys.stderr); return 2
    r = score_task(task, text)
    if args.json:
        print(json.dumps(r, ensure_ascii=False, indent=2))
    else:
        print(f"✍️ 写作 #{r['id']}（{r['task_type']}）· 字数 {r['word_count']} · 自动量规通过率 {r['pass_rate']}")
        for res in r['results']:
            mark = "✅" if res['pass'] is True else "❌" if res['pass'] is False else "⚠️"
            print(f"  {mark} {res['check']} — {res['msg']}")
        for a in r['advice']:
            print("  💡", a)
    return 0

def _fmt_batch(out):
    s = ""
    for r in out:
        if r.get('status') == 'no_essay':
            s += f"\n写作 #{r['id']}：未找到作文文件，跳过。"; continue
        s += f"\n✍️ 写作 #{r['id']} · 字数 {r['word_count']} · 通过率 {r['pass_rate']}"
        for res in r['results']:
            mark = "✅" if res['pass'] is True else "❌" if res['pass'] is False else "⚠️"
            s += f"\n  {mark} {res['check']} — {res['msg']}"
        for a in r['advice']:
            s += f"\n  💡 {a}"
    return s

if __name__ == '__main__':
    sys.exit(main())
