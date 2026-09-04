# -*- coding: utf-8 -*-
"""Download emoji for every WORDS entry (SVG->256px PNG preferred, 72px fallback).
Race-free: unique temp file per codepoint. Writes a word->hex manifest
(emoji/_final.json) and md5-collision-checks that no two different words share
one image unintentionally.

Run:  python download_emoji.py   (expects words100.py with WORDS in same dir)
Deps: curl, `apt-get install -y librsvg2-bin` for rsvg-convert.
"""
import os, sys, json, subprocess, concurrent.futures as cf, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
try:
    import words100 as W; WORDS = W.WORDS
except Exception as e:
    raise SystemExit("need words100.py with WORDS list in same dir")

OUT  = os.environ.get("EMOJI_OUT", os.path.join(HERE, "emoji"))
BASE = "https://cdn.jsdelivr.net/gh/twitter/twemoji@latest/assets"
os.makedirs(OUT, exist_ok=True)
for f in os.listdir(OUT):
    p = os.path.join(OUT, f)
    if f.endswith(".png") and os.path.isfile(p):
        os.remove(p)

def hex_of(emoji_char):
    return "".join(format(ord(c), 'x') for c in emoji_char
                   if ord(c) not in (0xfe0f, 0x200d, 0x20e3))

def curl(out, url):
    return subprocess.run(["curl","-sL","-o",out,"-w","%{http_code}","--max-time","25",url],
                          capture_output=True, text=True).stdout.strip()

def get_png(cp):
    final, svg = f"{OUT}/{cp}.png", f"{OUT}/{cp}.svg"
    if curl(svg, f"{BASE}/svg/{cp}.svg") == "200" and os.path.getsize(svg) > 100:
        subprocess.run(["rsvg-convert","-w","256","-h","256","-o",final,svg], capture_output=True)
        os.remove(svg)
        if os.path.exists(final) and os.path.getsize(final) > 150:
            return "svg256"
    if os.path.exists(svg): os.remove(svg)
    if curl(final, f"{BASE}/72x72/{cp}.png") == "200" and os.path.getsize(final) > 100:
        return "png72"
    if os.path.exists(final): os.remove(final)
    return "FAIL"

# De-dupe by unique codepoint BEFORE parallel download (race-free shared files),
# then map every word that shares a codepoint to that one downloaded PNG.
final_map, report = {}, {}
unique = {}
for word, _py, emoji in WORDS:
    if emoji is None:
        report[word] = 1
        continue
    cp = hex_of(emoji)
    unique.setdefault(cp, []).append(word)

def resolve_one(cp_and_words):
    cp, words = cp_and_words
    if get_png(cp) != "FAIL" and os.path.exists(f"{OUT}/{cp}.png") and os.path.getsize(f"{OUT}/{cp}.png") > 150:
        return cp, words
    return cp, None

for cp, words in list(unique.items()):
    for w in words:
        res, reswords = resolve_one((cp, [w]))
        if reswords:
            final_map[w] = res
        else:
            report[w] = 1
if report: print("WARN unresolved:", list(report))

json.dump(final_map, open(f"{OUT}/_final.json", "w"), ensure_ascii=False, indent=1)

def md5(p): return hashlib.md5(open(p, "rb").read()).hexdigest()
seen, dups = {}, []
for w, cp in final_map.items():
    p = f"{OUT}/{cp}.png"
    if not os.path.exists(p): print("MISSING", w, cp); continue
    m = md5(p)
    if m in seen: dups.append((w, cp, seen[m]))
    seen[m] = (w, cp)
print("intentional shared images:", dups if dups else "none")
print("resolved:", len(final_map), "/", sum(1 for w in WORDS if w[2] is not None))
