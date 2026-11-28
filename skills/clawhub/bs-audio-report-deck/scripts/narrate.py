#!/usr/bin/env python3
"""Narration tools for a deck built by any Skillry editable PPT style.

    python3 scripts/narrate.py export --deck presentation.html --lang zh --out narration.json --md narration.md
    python3 scripts/narrate.py check  --narration narration.json
    python3 scripts/narrate.py inject --deck presentation.html --audio audio/manifest.json [--embed] [--output out.html]

The narration of each page is that slide's speaker notes, so it stays editable
in the deck's own notes panel and travels into the exported PPTX. `inject`
adds a playback layer (play, seek, 0.75-2x speed, auto-advance, script view)
and is idempotent. Standard library only.
"""

import argparse
import base64
import html
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True

HERE = Path(__file__).resolve().parent
START = "<!-- narration-layer:start -->"
END = "<!-- narration-layer:end -->"
EMBED_LIMIT_BYTES = 18 * 1024 * 1024

# Per-page spoken length targets: (unit, minimum, maximum).
LENGTH_RULES = {
    "zh": ("chars", 120, 320),
    "zh-tw": ("chars", 120, 320),
    "ja": ("chars", 150, 380),
    "ko": ("chars", 130, 340),
}
WORD_RULE = ("words", 60, 190)
CJK = re.compile(r"[\u3040-\u30ff\u3400-\u9fff\uac00-\ud7af\uf900-\ufaff]")
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿←-⇿✓✕✗]")
URL = re.compile(r"https?://|www\.", re.I)
MARKUP = re.compile(r"(^|\n)\s*([-*•#>]|\d+\.)\s|\*\*|__|`")


def normalize(text):
    return re.sub(r"\s+", " ", str(text or "")).strip()


def text_hash(text):
    """FNV-1a 32 over the normalized UTF-8 text; matches narration-player.js."""
    value = 0x811C9DC5
    for byte in normalize(text).encode("utf-8"):
        value ^= byte
        value = (value * 0x01000193) & 0xFFFFFFFF
    return f"{value:08x}"


def read_deck_state(deck):
    source = deck.read_text(encoding="utf-8")
    match = re.search(r'<script id="deck-data" type="application/json">(.*?)</script>', source, re.S)
    if not match:
        raise ValueError(f"{deck} has no #deck-data block; build it with the style's build-deck.py first.")
    return source, json.loads(match.group(1))


def load_slides(args):
    if args.project:
        payload = json.loads(Path(args.project).read_text(encoding="utf-8"))
        state = payload.get("project", payload)
    else:
        _, state = read_deck_state(Path(args.deck))
    slides = state.get("slides") or []
    if not slides:
        raise ValueError("The deck has no slides.")
    return state, slides


def slide_title(slide):
    if slide.get("title"):
        return normalize(slide["title"])
    stack = [slide.get("root") or slide.get("stack") or {}]
    while stack:
        node = stack.pop(0)
        if isinstance(node, dict):
            if node.get("type") in ("heading", "subheading") and node.get("text"):
                return normalize(re.sub(r"<[^>]+>", " ", html.unescape(str(node["text"]))))[:80]
            stack.extend(node.get("children") or [])
    return slide.get("id", "")


def measure(text, lang):
    unit, low, high = LENGTH_RULES.get(lang, WORD_RULE)
    if unit == "chars":
        size = len(re.sub(r"\s", "", text))
    else:
        size = len(text.split())
    return unit, size, low, high


def cmd_export(args):
    state, slides = load_slides(args)
    lang = (args.lang or state.get("contentLocale") or "en").lower()
    pages = []
    for index, slide in enumerate(slides):
        text = (slide.get("notes") or "").strip()
        pages.append({
            "index": index + 1,
            "id": slide["id"],
            "title": slide_title(slide),
            "text": text,
            "hash": text_hash(text) if text else None,
        })
    out = {"schemaVersion": 1, "lang": lang, "slides": pages}
    Path(args.out).write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.md:
        lines = [f"# Narration ({lang})", ""]
        for page in pages:
            unit, size, _, _ = measure(page["text"], lang)
            lines += [f"## {page['index']}. {page['title']}", "", f"`{page['id']}` · {size} {unit}", "", page["text"] or "_(no narration)_", ""]
        Path(args.md).write_text("\n".join(lines), encoding="utf-8")
    missing = [page["id"] for page in pages if not page["text"]]
    print(json.dumps({"ok": not missing, "slides": len(pages), "missing": missing, "output": str(Path(args.out).resolve())}, ensure_ascii=False))
    return 0 if not missing else 2


def cmd_check(args):
    data = json.loads(Path(args.narration).read_text(encoding="utf-8"))
    lang = (args.lang or data.get("lang") or "en").lower()
    problems, warnings = [], []
    for page in data["slides"]:
        text, sid = page.get("text") or "", page["id"]
        if not text.strip():
            problems.append(f"{sid}: no narration")
            continue
        unit, size, low, high = measure(text, lang)
        if size < low:
            warnings.append(f"{sid}: {size} {unit}, short (aim {low}-{high}) — fine for cover/closing pages")
        if size > high:
            problems.append(f"{sid}: {size} {unit}, too long (max {high}); split the page or tighten the script")
        if URL.search(text):
            problems.append(f"{sid}: contains a URL; say the site name instead")
        if EMOJI.search(text):
            problems.append(f"{sid}: contains an emoji, arrow or check mark that a voice cannot read")
        if MARKUP.search(text):
            problems.append(f"{sid}: contains list or Markdown markup; write spoken sentences")
        if lang in LENGTH_RULES and not CJK.search(text):
            warnings.append(f"{sid}: no {lang} characters found; is the narration in the right language?")
    print(json.dumps({"ok": not problems, "lang": lang, "pages": len(data["slides"]), "problems": problems, "warnings": warnings}, ensure_ascii=False, indent=2))
    return 0 if not problems else 1


def cmd_inject(args):
    deck = Path(args.deck)
    source, state = read_deck_state(deck)
    manifest_path = Path(args.audio)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    output = Path(args.output) if args.output else deck
    slide_ids = [slide["id"] for slide in state.get("slides", [])]
    tracks, total_embedded = {}, 0
    for sid, track in (manifest.get("slides") or {}).items():
        audio_file = (manifest_path.parent / track["file"]).resolve()
        if not audio_file.exists():
            raise ValueError(f"Missing audio for {sid}: {audio_file}")
        if args.embed:
            data = audio_file.read_bytes()
            total_embedded += len(data)
            mime = "audio/wav" if audio_file.suffix.lower() == ".wav" else "audio/mpeg"
            src = f"data:{mime};base64," + base64.b64encode(data).decode("ascii")
        else:
            try:
                src = audio_file.relative_to(output.parent.resolve()).as_posix()
            except ValueError:
                raise ValueError(f"{audio_file} must sit inside {output.parent.resolve()} so the deck can load it; or use --embed.")
        tracks[sid] = {"src": src, "textHash": track.get("textHash"), "duration": track.get("duration")}
    if args.embed and total_embedded > EMBED_LIMIT_BYTES:
        raise ValueError(f"Embedded audio would add {total_embedded // 1024 // 1024} MB; keep the audio folder next to the deck instead of --embed.")

    notes = {slide["id"]: slide.get("notes") or "" for slide in state.get("slides", [])}
    stale = [sid for sid, track in tracks.items() if sid in notes and track.get("textHash") and track["textHash"] != text_hash(notes[sid])]
    orphans = [sid for sid in tracks if sid not in slide_ids]
    silent = [sid for sid in slide_ids if sid not in tracks]

    css = (HERE / "narration-player.css").read_text(encoding="utf-8")
    js = (HERE / "narration-player.js").read_text(encoding="utf-8")
    payload = json.dumps({"schemaVersion": 1, "slides": tracks}, ensure_ascii=False).replace("<", "\\u003c")
    block = "\n".join([
        START,
        f'<style id="narration-style">{css}</style>',
        f'<script id="narration-data" type="application/json">{payload}</script>',
        f"<script id=\"narration-runtime\">{js}</script>",
        END,
    ])
    cleaned = re.sub(re.escape(START) + r".*?" + re.escape(END) + r"\n?", "", source, flags=re.S)
    cleaned = re.sub(r'<div id="narration-bar"[^>]*>.*?</div>\s*(?=<aside id="narration-script")', "", cleaned, flags=re.S)
    cleaned = re.sub(r'<aside id="narration-script"[^>]*>.*?</aside>', "", cleaned, flags=re.S)
    if "</body>" not in cleaned:
        raise ValueError("The deck has no </body>.")
    head, tail = cleaned.rsplit("</body>", 1)
    output.write_text(head + block + "\n</body>" + tail, encoding="utf-8")
    print(json.dumps({
        "ok": not orphans and not stale,
        "output": str(output.resolve()),
        "narrated": len([sid for sid in slide_ids if sid in tracks]),
        "slides": len(slide_ids),
        "silent": silent,
        "stale": stale,
        "orphans": orphans,
        "embedded": bool(args.embed),
    }, ensure_ascii=False))
    return 0 if not orphans and not stale else 2


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    export = sub.add_parser("export", help="Write narration.json (+ Markdown) from the slides' speaker notes")
    export.add_argument("--deck", type=Path)
    export.add_argument("--project", type=Path)
    export.add_argument("--lang")
    export.add_argument("--out", required=True)
    export.add_argument("--md")
    check = sub.add_parser("check", help="Check every page has a speakable script of a sensible length")
    check.add_argument("--narration", required=True)
    check.add_argument("--lang")
    inject = sub.add_parser("inject", help="Add the narration player to a built deck")
    inject.add_argument("--deck", type=Path, required=True)
    inject.add_argument("--audio", required=True, help="audio/manifest.json written by tts.mjs")
    inject.add_argument("--embed", action="store_true", help="Inline the MP3s so the deck is one file")
    inject.add_argument("--output")
    args = parser.parse_args()
    if args.command == "export" and not (args.deck or args.project):
        parser.error("export needs --deck or --project")
    handler = {"export": cmd_export, "check": cmd_check, "inject": cmd_inject}[args.command]
    return handler(args)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as error:
        print(f"narrate.py: {error}", file=sys.stderr)
        sys.exit(1)
