#!/usr/bin/env python3
"""DramaLex · generate_tasks.py
Validate tasks.json (speaking + writing prompts) and emit tasks.md preview.
Speaking audio (model_line) is collected centrally by export_hub.py.
Pure stdlib, agent-neutral.
"""
import argparse, json, sys

def validate(d):
    errs = []
    for i, s in enumerate(d.get('speaking', []), 1):
        for f in ('id', 'type', 'instruction', 'use_words', 'checklist'):
            if f not in s:
                errs.append(f"speaking[{i}] missing '{f}'")
    for i, w in enumerate(d.get('writing', []), 1):
        for f in ('id', 'type', 'instruction', 'register', 'require_words', 'rubric'):
            if f not in w:
                errs.append(f"writing[{i}] missing '{f}'")
    return errs

def md(d, deck):
    out = [f"# 🗣️ Speak & ✍️ Write · {deck}\n"]
    out.append("## Speaking (reuse the target lexicon!)\n")
    for s in d.get('speaking', []):
        ch = f" as {s.get('character')}" if s.get('character') else ""
        ml = f"\n  🎧 Model: “{s.get('model_line')}”" if s.get('model_line') else ""
        out.append(f"**{s['id']}.** [{s.get('type')}]{ch} {s.get('instruction')}{ml}\n"
                   f"  - Use: {', '.join(s.get('use_words', []))}\n"
                   f"  - Checklist: {', '.join(s.get('checklist', []))}\n")
        if s.get('focus_sounds'):
            out.append(f"  - 🔤 重点发音：{', '.join(s['focus_sounds'])}\n")
        if s.get('asr_target'):
            out.append(f"  - 🎤 可评分：录下你说的话，运行 `score_speaking.py --audio 录音 --target \"{s['asr_target']}\"`\n")
    out.append("## Writing (with feedback — paste your text for agent correction)\n")
    for w in d.get('writing', []):
        out.append(f"**{w['id']}.** [{w.get('type')} / {w.get('register')}] {w.get('instruction')}\n"
                   f"  - Must use: {', '.join(w.get('require_words', []))}\n"
                   f"  - Rubric: {', '.join(w.get('rubric', []))}\n")
        if w.get('checks'):
            chk = '; '.join(f"{c.get('type')}:{c.get('value')}" for c in w['checks'])
            out.append(f"  - 🤖 自动量规：{chk}（运行 `score_writing.py --task {w.get('id')} --text essay.txt --tasks tasks.json`）\n")
        if w.get('model'):
            out.append(f"  - 📝 Model: {w.get('model')}\n")
    out.append("\n---\n*DramaLex · yinjianheng（殷健恒） · yinjianheng@foxmail.com · WeChat YJH-yinjianheng*")
    return "\n".join(out)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--input', required=True)
    ap.add_argument('--output', default='tasks.md')
    ap.add_argument('--deck', default='DramaLex')
    args = ap.parse_args()
    d = json.load(open(args.input, encoding='utf-8'))
    errs = validate(d)
    if errs:
        print("VALIDATION WARNINGS:", file=sys.stderr)
        for e in errs:
            print(" -", e, file=sys.stderr)
    txt = md(d, args.deck)
    open(args.output, 'w', encoding='utf-8').write(txt)
    print(f"已写出: {args.output}  (speaking={len(d.get('speaking',[]))}, writing={len(d.get('writing',[]))})")

if __name__ == '__main__':
    main()
