#!/usr/bin/env python3
"""DramaLex · export_cards.py
读取 agent 萃取并 enriched 的 words.json（可选含音频路径），导出：
  - cards.tsv : Anki 可导入（Tab 分隔）。正面=音频(耳测)，背面=拼写+释义+语境。含 Audio、Tags 列。
  - cards.md  : 移动端直读的可读词表。
  - <deck>.apkg : 可选，需 genanki（pip install genanki）。
纯标准库 + 可选 genanki。Agent 中立。
"""
import argparse, json, os, sys

def back_html(w):
    p = [f"<b>{w['term']}</b>"]
    if w.get('ipa'):
        p.append(f" {w['ipa']}")
    if w.get('pos'):
        p.append(f" <i>({w['pos']})</i>")
    if w.get('cefr'):
        p.append(f" [{w['cefr']}]")
    p.append(f"<br>{w.get('gloss','')}")
    if w.get('collocation'):
        p.append(f"<br><i>搭配:</i> {w['collocation']}")
    if w.get('line'):
        sp = f" ({w['line_speaker']})" if w.get('line_speaker') else ""
        p.append(f"<br>🎬 {w['line']}{sp}")
    if w.get('example'):
        p.append(f"<br>✏️ {w['example']}")
    if w.get('tags'):
        p.append(f"<br><small>{', '.join(w['tags'])}</small>")
    return ''.join(p)

def tags_str(w):
    t = ['dramalex']
    if w.get('cefr'):
        t.append(w['cefr'].lower())
    if w.get('type'):
        t.append(w['type'])
    t += w.get('tags', [])
    return ' '.join(t)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--input', required=True)
    ap.add_argument('--out-dir', default='.')
    ap.add_argument('--deck', default='DramaLex')
    ap.add_argument('--make-apkg', action='store_true')
    args = ap.parse_args()

    with open(args.input, encoding='utf-8') as f:
        words = json.load(f)
    os.makedirs(args.out_dir, exist_ok=True)

    csv_path = os.path.join(args.out_dir, 'cards.tsv')
    with open(csv_path, 'w', encoding='utf-8') as f:
        f.write("Front\tBack\tAudio\tTags\n")
        for w in words:
            front = f"[sound:{os.path.basename(w['term_audio'])}]" if w.get('term_audio') else w['term']
            back = back_html(w)
            audio = f"[sound:{os.path.basename(w['line_audio'])}]" if w.get('line_audio') else ''
            f.write(f"{front}\t{back}\t{audio}\t{tags_str(w)}\n")

    md_path = os.path.join(args.out_dir, 'cards.md')
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(f"# DramaLex 词卡 · {args.deck}\n\n")
        for i, w in enumerate(words, 1):
            f.write(f"## {i}. {w['term']}  {w.get('ipa','')} {('('+w['type']+')') if w.get('type') else ''}\n")
            if w.get('cefr'):
                f.write(f"- CEFR: {w['cefr']}\n")
            if w.get('pos'):
                f.write(f"- 词性: {w['pos']}\n")
            f.write(f"- 释义: {w.get('gloss','')}\n")
            if w.get('collocation'):
                f.write(f"- 搭配: {w['collocation']}\n")
            if w.get('line'):
                sp = f" ({w['line_speaker']})" if w.get('line_speaker') else ""
                f.write(f"- 原句: {w['line']}{sp}\n")
            if w.get('example'):
                f.write(f"- 例句: {w['example']}\n")
            if w.get('tags'):
                f.write(f"- 标签: {', '.join(w['tags'])}\n")
            f.write("\n")
        f.write("\n---\n*DramaLex · yinjianheng（殷健恒） · yinjianheng@foxmail.com · WeChat YJH-yinjianheng*\n")

    if args.make_apkg:
        try:
            import genanki
            media_files, notes = [], []
            for w in words:
                front = f"[sound:{os.path.basename(w['term_audio'])}]" if w.get('term_audio') else w['term']
                notes.append(genanki.Note(model=genanki.BASIC_MODEL, fields=[front, back_html(w)]))
                if w.get('term_audio'):
                    media_files.append(w['term_audio'])
                if w.get('line_audio'):
                    media_files.append(w['line_audio'])
            deck = genanki.Deck(1234567890, args.deck)
            for n in notes:
                deck.add_note(n)
            apkg_path = os.path.join(args.out_dir, args.deck + '.apkg')
            genanki.Package(deck, media_files=media_files).write_to_file(apkg_path)
            print(f"已写出: {apkg_path}")
        except Exception as e:
            print(f".apkg 跳过: {e}", file=sys.stderr)

    print(f"已写出: {csv_path} 与 {md_path}")
    print(f"条目数: {len(words)}")

if __name__ == '__main__':
    main()
