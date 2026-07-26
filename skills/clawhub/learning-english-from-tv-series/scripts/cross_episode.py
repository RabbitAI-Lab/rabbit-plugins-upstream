#!/usr/bin/env python3
"""DramaLex · cross_episode.py — 跨集同词多语境复现

 spaced repetition 的「同词跨语境」补强：把上一集学的词，在新一集的真实台词里再撞见一次，
 形成「旧语境 → 新语境」对照，记忆更牢（Webb & Rodgers: 同词跨技能/跨语境复现 → 更深 retention）。

输入：
  - vocab_bank.json（build 自动维护的已学词库，建议含 term/cefr/line）
  - 新一集的 subtitle.json（已解析）
输出：
  - recall_hints.json：每个「复现词」的 {term, cefr, old_context, new_contexts[]}
    new_contexts 取自新字幕里包含该词、且与旧语境不同的真实台词（最多 3 条）。

纯标准库。
"""
import argparse, json, os, re, sys

TOKEN = re.compile(r"[a-z0-9']+")

def tokens(text):
    return TOKEN.findall((text or '').lower())

def build_recall_hints(bank, segs, episode='', max_ctx=3):
    bank_terms = {}
    for b in (bank or []):
        t = (b.get('term') or '').strip().lower()
        if t:
            bank_terms.setdefault(t, b)
    # 新字幕按词建索引：term -> [lines]
    idx = {}
    for s in segs:
        line = s.get('text', '')
        if not line:
            continue
        for tk in set(tokens(line)):
            idx.setdefault(tk, []).append(line.strip())
    hints = []
    for t, b in bank_terms.items():
        if t not in idx:
            continue
        old = (b.get('line') or '').strip().lower()
        new_ctx = []
        seen = set()
        for ln in idx[t]:
            low = ln.lower()
            if low == old:
                continue
            if low in seen:
                continue
            seen.add(low)
            new_ctx.append(ln)
            if len(new_ctx) >= max_ctx:
                break
        if new_ctx:
            hints.append({
                "term": b.get('term') or t,
                "cefr": b.get('cefr', ''),
                "old_context": b.get('line', ''),
                "new_contexts": new_ctx,
            })
    return {"episode": episode, "recalled": len(hints), "hints": hints}

def _load_subtitle(path):
    if not path or not os.path.exists(path):
        return None
    try:
        data = json.load(open(path, encoding='utf-8'))
    except Exception:
        return None
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        for k in ('lines', 'segments', 'subtitles'):
            if isinstance(data.get(k), list):
                return data[k]
    return None

def main():
    ap = argparse.ArgumentParser(description="DramaLex 跨集复现提示")
    ap.add_argument('--bank', default='vocab_bank.json', help='已学词库')
    ap.add_argument('--subtitle', required=True, help='新一集 subtitle.json')
    ap.add_argument('--episode', default='', help='新一集代号（写入输出）')
    ap.add_argument('--out', default='recall_hints.json', help='输出路径')
    args = ap.parse_args()

    bank = json.load(open(args.bank, encoding='utf-8')) if os.path.exists(args.bank) else []
    segs = _load_subtitle(args.subtitle)
    if segs is None:
        print("无法读取新字幕:", args.subtitle, file=sys.stderr); return 2
    out = build_recall_hints(bank, segs, args.episode)
    json.dump(out, open(args.out, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    if out['recalled']:
        print(f"✅ 跨集复现：在《{args.episode or '本集'}》中发现 {out['recalled']} 个已学词的新语境，已写入 {args.out}")
        for h in out['hints'][:8]:
            print(f"  · {h['term']}（{h['cefr']}）：旧「{h['old_context'][:40]}…」 → 新 {len(h['new_contexts'])} 条")
    else:
        print(f"本集无已学词复现（或词库为空）。已写入空 hints 到 {args.out}")
    return 0

if __name__ == '__main__':
    sys.exit(main())
