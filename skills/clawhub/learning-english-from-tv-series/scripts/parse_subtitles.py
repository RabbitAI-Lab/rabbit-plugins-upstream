#!/usr/bin/env python3
"""DramaLex · parse_subtitles.py
解析 .srt / .vtt 字幕或粘贴文本，输出清洗后的对白 + 词频，并给出候选词（词频>=阈值）及语境例句，
供 agent 做 mine/enrich。纯标准库，agent 中立，任何能跑 python 的 agent 均可使用。
"""
import argparse, json, os, re, sys, html

# 内置停用词（功能词 + 超高频词）。可通过 references/stopwords.txt 扩展。
DEFAULT_STOPWORDS = set("""
a an the and or but if then else when while as at by for from of in on to with without about over under
i you he she it we they me him her us them my your his our their this that these those
is am are was were be been being do does did doing have has had having will would shall should can could may might must
not no nor so too very just only also even still own same such s t re ve ll m d o re y
oh yeah hey wow um uh hmm ah okay ok well now then there here what who whom which whose how why where
got get getting go going come came coming make made making take took taken see saw seen look looking know known knowing
think thought say said tell told ask asked want wanted need needed like liked love loved feel felt
one two three good bad big small time day night year man woman people thing world home work out up down off
""".split())

def load_stopwords(extra_path=None):
    sw = set(w.lower() for w in DEFAULT_STOPWORDS)
    if extra_path and os.path.exists(extra_path):
        with open(extra_path, encoding='utf-8') as f:
            for line in f:
                w = line.strip().lower()
                if w and not w.startswith('#'):
                    sw.add(w)
    return sw

def clean_text(raw):
    raw = re.sub(r'<[^>]+>', '', raw)          # 去 HTML 标签
    raw = html.unescape(raw)
    raw = re.sub(r'\{[^}]+\}', '', raw)        # 去 ass 样式花括号
    raw = re.sub(r'\[[^]]+\]', '', raw)        # 去 [music] 等
    return raw

def parse_srt(text):
    blocks = re.split(r'\n\s*\n', text.strip())
    lines = []
    for b in blocks:
        parts = b.split('\n')
        if parts and parts[0].strip().isdigit():
            parts = parts[1:]
        time, body = "", []
        for i, p in enumerate(parts):
            if re.match(r'\d{2}:\d{2}:\d{2}', p):
                time, body = p.strip(), parts[i+1:]
                break
            else:
                body.append(p)
        if not body and parts:
            body = parts
        txt = clean_text(' '.join(body))
        if txt.strip():
            lines.append({"time": time, "text": txt})
    return lines

def parse_vtt(text):
    text = re.sub(r'WEBVTT.*?(\n\n|\Z)', '', text, flags=re.S)
    blocks = re.split(r'\n\s*\n', text.strip())
    lines = []
    for b in blocks:
        parts = b.split('\n')
        time, body = "", []
        for i, p in enumerate(parts):
            if '-->' in p:
                time, body = p.strip(), parts[i+1:]
                break
            else:
                body.append(p)
        if not body and parts:
            body = parts
        txt = clean_text(' '.join(body))
        if txt.strip():
            lines.append({"time": time, "text": txt})
    return lines

def detect_speaker(text):
    m = re.match(r'\s*([A-Z][A-Za-z .\'-]{0,30}?)\s*:\s*(.*)', text)
    if m:
        return m.group(1).strip(), m.group(2).strip()
    return "", text.strip()

TOKEN_RE = re.compile(r"[a-z']+")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--input', help='字幕文件 .srt/.vtt/.txt')
    ap.add_argument('--text', help='粘贴的台词文本')
    ap.add_argument('--output', default='subtitle.json')
    ap.add_argument('--min-recurrence', type=int, default=2)
    _default_sw = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'references', 'stopwords.txt')
    ap.add_argument('--stopwords', default=_default_sw, help='额外停用词文件')
    args = ap.parse_args()

    if args.input:
        with open(args.input, encoding='utf-8', errors='ignore') as f:
            raw = f.read()
        ext = os.path.splitext(args.input)[1].lower()
        episode = os.path.splitext(os.path.basename(args.input))[0]
    elif args.text:
        raw = args.text
        ext, episode = '.txt', 'pasted'
    else:
        print("ERROR: 需提供 --input 或 --text", file=sys.stderr); sys.exit(1)

    if ext == '.srt':
        lines = parse_srt(raw)
    elif ext == '.vtt':
        lines = parse_vtt(raw)
    else:
        lines = [{"time": "", "text": clean_text(l)} for l in raw.split('\n') if l.strip()]

    for ln in lines:
        sp, tx = detect_speaker(ln['text'])
        ln['speaker'], ln['text'] = sp, tx

    stop = load_stopwords(args.stopwords)
    freq = {}
    for ln in lines:
        toks = [t.lower().strip("'") for t in TOKEN_RE.findall(ln['text'].lower())]
        for t in toks:
            if len(t) < 2 or t in stop:
                continue
            freq[t] = freq.get(t, 0) + 1

    cands = []
    for w, c in freq.items():
        if c >= args.min_recurrence:
            ex = [f"[{ln.get('speaker','')}] {ln['text']}"
                  for ln in lines if re.search(r'\b' + re.escape(w) + r'\b', ln['text'].lower())][:3]
            cands.append({"word": w, "freq": c, "examples": ex})
    cands.sort(key=lambda x: (-x['freq'], x['word']))

    out = {"episode": episode, "lines": lines, "token_freq": freq, "candidates": cands}
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print(f"Episode : {episode}")
    print(f"对白行数 : {len(lines)}")
    print(f"不同内容词 : {len(freq)}")
    print(f"候选词(词频>={args.min_recurrence}) : {len(cands)}")
    print(f"已写出 : {args.output}")

if __name__ == '__main__':
    main()
