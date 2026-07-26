#!/usr/bin/env python3
"""DramaLex · generate_listening.py
Validate listening.json (comprehension Qs + dictation) and emit a readable
listening.md preview. Audio for referenced lines is collected centrally by
export_hub.py. Pure stdlib, agent-neutral.
"""
import argparse, json, os, sys

def validate(d):
    errs = []
    comp = d.get('comprehension', [])
    dic = d.get('dictation', [])
    if not isinstance(comp, list) or not comp:
        errs.append("missing/empty 'comprehension'")
    for i, q in enumerate(comp, 1):
        for f in ('id', 'type', 'question', 'options', 'answer', 'rationale'):
            if f not in q:
                errs.append(f"comprehension[{i}] missing '{f}'")
        if q.get('options') and q.get('answer') not in q.get('options', []):
            errs.append(f"comprehension[{i}] answer not in options")
    for i, x in enumerate(dic, 1):
        for f in ('id', 'line', 'blanked', 'answers'):
            if f not in x:
                errs.append(f"dictation[{i}] missing '{f}'")
    return errs

def md(d, deck):
    out = [f"# 🎧 Listening · {deck}\n"]
    out.append("## Comprehension Questions (audio-only first!)\n")
    for q in d.get('comprehension', []):
        opts = "\n".join(f"  - {o}" for o in q.get('options', []))
        out.append(f"**Q{q['id']} [{q.get('type')}]** {q['question']}\n{opts}\n"
                   f"  ✅ {q.get('answer')} — {q.get('rationale','')}\n")
    out.append("## Dictation (listen, then type)\n")
    for x in d.get('dictation', []):
        sp = f" ({x.get('speaker')})" if x.get('speaker') else ""
        out.append(f"**{x['id']}.** {x.get('blanked')}{sp}\n  → {', '.join(x.get('answers', []))}\n")
    mp = d.get('minimal_pairs', [])
    if mp:
        out.append("## Minimal Pairs (phoneme ear-training)\n")
        for p in mp:
            actual = ("A" if p.get('in_episode') == 'a' else "B" if p.get('in_episode') == 'b' else "?")
            out.append(f"**{p['id']}.** A {p.get('word_a')} {p.get('ipa_a','')} | B {p.get('word_b')} {p.get('ipa_b','')}\n"
                       f"  原句：{p.get('line','')}\n  本集实际：{actual}（{p.get('word_a' if p.get('in_episode')=='a' else 'word_b','')}）"
                       + (f"\n  🔤 {p.get('hint')}" if p.get('hint') else "") + "\n")
    cs = d.get('connected_speech', [])
    if cs:
        out.append("## Connected Speech Breakdown\n")
        for c in cs:
            brk = " | ".join(f"{b.get('text','')}（{b.get('note','')}）" for b in c.get('breakdown', []))
            out.append(f"**{c['id']}.** “{c.get('line','')}”" + (f" — {c.get('gloss','')}" if c.get('gloss') else "")
                       + f"\n  自然读法：{brk}\n")
    out.append("\n---\n*DramaLex · yinjianheng（殷健恒） · yinjianheng@foxmail.com · WeChat YJH-yinjianheng*")
    return "\n".join(out)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--input', required=True)
    ap.add_argument('--output', default='listening.md')
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
    print(f"已写出: {args.output}  (comprehension={len(d.get('comprehension',[]))}, dictation={len(d.get('dictation',[]))})")

if __name__ == '__main__':
    main()
