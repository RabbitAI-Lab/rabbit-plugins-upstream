#!/usr/bin/env python3
"""DramaLex · validate.py — 内容质量闸门（agent 生成 JSON 后的自检）

为什么要它：agent 自律不可靠。这里做硬性校验，把"看前先学 / 真实台词 / 可复习"
三件最容易翻车的事拦在 TTS 与导出之前。
  - word.line 必须真实来自字幕（防 agent 编台词）
  - cefr 合法、目标词不重复
  - 听写/精读/任务字段非空、id 连续
退出码：0 全过；1 有 error 级问题；2 输入缺失。
"""
import json, os, re, sys

CEFR_OK = {'A2', 'B1', 'B2', 'C1', 'C2'}
_TOKEN = re.compile(r"[A-Za-z]+(?:['-][A-Za-z]+)*")

def _norm(s):
    return re.sub(r"\s+", " ", (s or "").strip())

def _subtitle_tokens(subtitle_json):
    """返回字幕中所有 token 的小写集合（用于校验 line 真实性）。"""
    if not subtitle_json or not os.path.exists(subtitle_json):
        return None
    try:
        data = json.load(open(subtitle_json, encoding='utf-8'))
    except Exception:
        return None
    toks = set()
    segs = data if isinstance(data, list) else data.get('lines') or data.get('segments') or data.get('subtitles') or []
    for s in segs:
        t = s.get('text', '')
        for w in _TOKEN.findall(t):
            toks.add(w.lower())
    return toks


def validate(work_dir, subtitle_json=None, strict=True):
    """返回 (errors, warnings) 两个 list。strict=True 时把软规则也计为 warning。"""
    errors, warns = [], []
    CORE = ['words.json', 'listening.json', 'annotated.json', 'tasks.json']

    def load(name):
        p = os.path.join(work_dir, name)
        if not os.path.exists(p):
            errors.append(f"[缺文件] {name} 不存在")
            return None
        try:
            return json.load(open(p, encoding='utf-8'))
        except Exception as e:
            errors.append(f"[JSON 解析失败] {name}: {e}")
            return None

    words = load('words.json'); listening = load('listening.json')
    annotated = load('annotated.json'); tasks = load('tasks.json')
    if None in (words, listening, annotated, tasks):
        return errors, warns

    sub_tok = _subtitle_tokens(subtitle_json) if subtitle_json else None

    # ---- words ----
    if not isinstance(words, list) or not words:
        errors.append("[words] 应为非空数组")
    else:
        seen = set()
        for i, w in enumerate(words):
            tag = f"[words#{i+1}]"
            term = (w.get('term') or '').strip()
            if not term:
                errors.append(f"{tag} 缺 term")
            else:
                key = term.lower()
                if key in seen:
                    errors.append(f"{tag} 重复目标词 '{term}'")
                seen.add(key)
            for fld in ('ipa', 'gloss', 'collocation', 'example'):
                if not w.get(fld):
                    warns.append(f"{tag} 缺 {fld}（建议补全）")
            c = w.get('cefr')
            if c not in CEFR_OK:
                errors.append(f"{tag} cefr 非法 '{c}'（应 ∈ {sorted(CEFR_OK)}）")
            line = w.get('line')
            if not line:
                errors.append(f"{tag} 缺 line（必须来自真实字幕）")
            elif sub_tok is not None:
                # line 中应至少包含一个来自字幕的词；完全对不上说明可能是编的
                lt = {t.lower() for t in _TOKEN.findall(line)}
                if lt and not (lt & sub_tok):
                    errors.append(f"{tag} line 疑似非真实台词（未在字幕中找到任何匹配词）：{line[:60]}")
            elif sub_tok is None:
                warns.append(f"{tag} 未提供 subtitle.json，无法校验 line 真实性")

    # ---- 诚实档位 & 词句一致性（软规则 → warning，不阻断） ----
    if isinstance(words, list) and words:
        c1 = [w for w in words if w.get('cefr') == 'C1']
        if c1 and len(c1) / len(words) > 0.30:
            marked = [w for w in c1 if '挑战' in ' '.join(w.get('tags', [])) or w.get('flag') == '挑战']
            if len(marked) < len(c1):
                warns.append(f"[words] C1 占比 {len(c1)/len(words):.0%} 超过 30%，部分未标 挑战★；"
                             f"低档位用户易被劝退，建议剔除或显式标注挑战项")
        for w in words:
            t = (w.get('term') or '').strip().lower()
            ln = (w.get('line') or '').lower()
            # 仅对单词检查（语块/搭配未必逐字出现在原句，避免误报）
            if t and (' ' not in t) and ln and t not in ln:
                warns.append(f"[words#{w.get('term')}] 目标词 '{w.get('term')}' 未出现在 line 中"
                             f"（建议 line 含目标词，便于语境记忆；语块例外）")

    # ---- listening ----
    comp = listening.get('comprehension', []) if isinstance(listening, dict) else []
    dic = listening.get('dictation', []) if isinstance(listening, dict) else []
    for q in comp:
        if not q.get('question') or not q.get('answer'):
            errors.append(f"[listening.comprehension#{q.get('id')}] 缺 question/answer")
        t = q.get('type')
        if t not in ('gist', 'detail'):
            errors.append(f"[listening.comprehension#{q.get('id')}] 缺/非法 type（应 ∈ {{gist, detail}}）")
        if not q.get('rationale'):
            errors.append(f"[listening.comprehension#{q.get('id')}] 缺 rationale（解析说明）")
        if not q.get('options'):
            warns.append(f"[listening.comprehension#{q.get('id')}] 无选项")
    for x in dic:
        if not x.get('line') or not x.get('answers'):
            errors.append(f"[listening.dictation#{x.get('id')}] 缺 line/answers")
        if not x.get('blanked'):
            errors.append(f"[listening.dictation#{x.get('id')}] 缺 blanked（挖空句）")

    # ---- annotated ----
    anns = annotated.get('annotations', []) if isinstance(annotated, dict) else []
    clo = annotated.get('cloze', []) if isinstance(annotated, dict) else []
    for a in anns:
        if not a.get('line') or not a.get('tip'):
            errors.append(f"[annotated.annotations#{a.get('id')}] 缺 line/tip")
    for c in clo:
        if not c.get('blanked') or not c.get('answers'):
            errors.append(f"[annotated.cloze#{c.get('id')}] 缺 blanked/answers")

    # ---- tasks ----
    spk = tasks.get('speaking', []) if isinstance(tasks, dict) else []
    wrt = tasks.get('writing', []) if isinstance(tasks, dict) else []
    for s in spk:
        if not s.get('instruction') or not s.get('use_words'):
            errors.append(f"[tasks.speaking#{s.get('id')}] 缺 instruction/use_words")
        st = s.get('type')
        if st not in ('shadow', 'roleplay', 'prompt'):
            errors.append(f"[tasks.speaking#{s.get('id')}] 缺/非法 type（应 ∈ {{shadow, roleplay, prompt}}）")
    for w in wrt:
        if not w.get('instruction') or not w.get('require_words'):
            errors.append(f"[tasks.writing#{w.get('id')}] 缺 instruction/require_words")
        wt = w.get('type')
        if wt not in ('rewrite', 'continue', 'summary'):
            errors.append(f"[tasks.writing#{w.get('id')}] 缺/非法 type（应 ∈ {{rewrite, continue, summary}}）")
        wr = w.get('register')
        if wr not in ('casual', 'formal', 'mixed'):
            errors.append(f"[tasks.writing#{w.get('id')}] 缺/非法 register（应 ∈ {{casual, formal, mixed}}）")

    # ---- id 连续性（轻量） ----
    for arr, label in ((comp, 'listening.comprehension'), (dic, 'listening.dictation'),
                        (anns, 'annotated.annotations'), (clo, 'annotated.cloze'),
                        (spk, 'tasks.speaking'), (wrt, 'tasks.writing')):
        ids = [x.get('id') for x in arr if isinstance(x, dict)]
        if ids and ids != list(range(1, len(ids) + 1)):
            warns.append(f"{label} id 不连续：{ids[:8]}")

    if not strict:
        warns = []
    return errors, warns


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--work-dir', default='.')
    ap.add_argument('--subtitle', default=None, help='subtitle.json，用于校验 line 真实性')
    ap.add_argument('--no-warn', action='store_true', help='只报 error')
    args = ap.parse_args()
    errs, warns = validate(args.work_dir, args.subtitle, strict=not args.no_warn)
    if errs:
        print("❌ 校验未通过（error）：")
        for e in errs:
            print("  -", e)
    if warns:
        print("⚠️ 警告（warning）：")
        for w in warns:
            print("  -", w)
    if not errs and not warns:
        print("✅ 校验全部通过")
    sys.exit(1 if errs else 0)


if __name__ == '__main__':
    main()
