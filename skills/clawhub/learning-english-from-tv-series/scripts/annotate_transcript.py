#!/usr/bin/env python3
"""DramaLex · annotate_transcript.py
Validate annotated.json (pragmatic/discourse annotations + cloze) and emit
transcript_annotated.md. Pure stdlib, agent-neutral.
"""
import argparse, json, sys

def validate(d):
    errs = []
    for i, a in enumerate(d.get('annotations', []), 1):
        for f in ('id', 'line', 'focus', 'note', 'tip'):
            if f not in a:
                errs.append(f"annotations[{i}] missing '{f}'")
    for i, c in enumerate(d.get('cloze', []), 1):
        for f in ('id', 'line', 'blanked', 'answers'):
            if f not in c:
                errs.append(f"cloze[{i}] missing '{f}'")
    return errs

def md(d, deck):
    out = [f"# 📖 Transcript Literacy · {deck}\n"]
    out.append("> Subtitles are *spoken* text. This phase trains pragmatic / discourse reading:\n"
               "> turn-taking, implicature, register, humor — not academic reading.\n")
    out.append("## Annotations\n")
    for a in d.get('annotations', []):
        sp = f" ({a.get('speaker')})" if a.get('speaker') else ""
        out.append(f"**{a['id']}.** _{a.get('focus')}_ — “{a.get('line')}”{sp}\n"
                   f"  - 💡 {a.get('note')}\n  - ✅ Tip: {a.get('tip')}\n")
    out.append("## Cloze (read & fill)\n")
    for c in d.get('cloze', []):
        out.append(f"**{c['id']}.** {c.get('blanked')}\n  → {', '.join(c.get('answers', []))}\n")
    out.append("\n---\n*DramaLex · yinjianheng（殷健恒） · yinjianheng@foxmail.com · WeChat YJH-yinjianheng*")
    return "\n".join(out)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--input', required=True)
    ap.add_argument('--output', default='transcript_annotated.md')
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
    print(f"已写出: {args.output}  (annotations={len(d.get('annotations',[]))}, cloze={len(d.get('cloze',[]))})")

if __name__ == '__main__':
    main()
