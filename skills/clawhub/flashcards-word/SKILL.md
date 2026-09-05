---
name: flashcards-word
description: "Use when the user wants printable word / vocabulary flashcards for a young child (preschool / 5-year-old) as a Word (.docx) file — works for BOTH Chinese (hanzi / pinyin 认字卡) and English (simple words). e.g. '40 simple English words', '4 字 per page four corners', 'double-sided print', front = picture + big label, back = label only for recall/tracing. Builds cut-apart 2x2-grid flashcards with double-sided mirror alignment, emoji artwork, and a fully open-source ready, self-contained script set (Pillow + python-docx + Twemoji)."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [english, chinese, hanzi, vocabulary, flashcards, docx, word, printing, kids, education, preschool, flashcards-word]
    related_skills: [hanzi-flashcards-word, powerpoint, ocr-and-documents]
---

# Word / Vocabulary Flashcards as print-ready Word .docx

## Overview
Builds a print-ready `.docx` of **word / vocabulary** flashcards for a ~5-year-old. Works
for **English** (simple words) and, with a pinyin-aware variant, for **Chinese (hanzi)**.
The bundled `scripts/` ship the English path; the Chinese path follows the same recipe —
see `hanzi-flashcards-word` for the pinyin-specific variant.

- N words per page arranged in a **2×2 grid (four corners)** using a borderless table.
- **Front page** = cute illustration (emoji) + the big WORD, per card.
- **Back page** = the same WORD, large on white, for recall / tracing memorization.
- **Double-sided (long-edge flip) mirror alignment** so each back-word sits exactly
  under its front picture when the sheet is flipped — the part most people get wrong.
- The big word **auto-scales** to fit the card, so long words like "watermelon" still
  render without clipping.

This skill is intentionally **self-contained and open-source ready**: `scripts/` holds a
complete, dependency-only-on-common-packages pipeline (`Pillow`, `python-docx`, `curl`,
`rsvg-convert`). `LICENSE` (MIT) and `README.md` are included for publishing to GitHub.

Card artwork is rendered in **Pillow (PIL)** (no image model needed). Word assembly is
**python-docx**: 1 section per page, one borderless 2×2 table per page, images sized to
fill each cell.

## When to use
- "make 40 simple English words / vocabulary cards for a 5-year-old"
- "English flashcards, double-sided print, front word+picture, back word only"
- Any batch of English words → printable, cut-apart flashcards for a preschooler.

Don't use for: pinyin/Chinese cards (use `hanzi-flashcards-word`), plain vocabulary
lists, adult material, or non-printable output.

## Quickstart (scripts included, verified working)
```bash
mkdir -p /tmp/ew && cd /tmp/ew
cp <SKILL>/scripts/words100.py .            # the word list + emoji (edit this!)
cp <SKILL>/scripts/download_emoji.py .
cp <SKILL>/scripts/generate_all.py .
cp <SKILL>/scripts/build_docx.py .
python3 words100.py                          # validate: 40 unique, multiple of 4
python3 download_emoji.py                    # emoji SVG->256px PNG (needs rsvg-convert)
python3 generate_all.py                      # render 80 card PNGs (front+back)
python3 build_docx.py                        # assemble the double-sided .docx
```
Env vars: `EMOJI_OUT` (emoji PNG dir), `EN_FONT` (bold word font path), `OUT_DOCX`.

> **PIL/docx work must run in a REAL Python env (a plain terminal).** The
> `execute_code` sandbox usually does NOT have `Pillow`/`python-docx` — importing them
> there raises `ModuleNotFoundError`. Use the `terminal` tool for all card rendering,
> `build_docx.py`, and preview stitching; `execute_code` is only safe for
> dependency-free checks (regex, json, zipfile).

## Environment (check once)
```bash
python3 --version
python3 -c "import docx, PIL; print('ok')"   # python-docx + Pillow
which rsvg-convert    # if missing: apt-get install -y librsvg2-bin
fc-list | grep -iE "dejavu sans\b|liberation|noto sans\b"   # a bold sans for big words
```
Default word font: `/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf`
(falls back to `DejaVuSans.ttf` if the bold face is absent).

## The word list format
`words100.py` exports `WORDS = [(word, "", emoji_unicode_or_None), ...]`.
- `word`  — the label shown large on the card (keep it short for a 5-yr-old).
- `""`    — the unused middle slot (kept so the tuple shape matches the hanzi version;
            the English renderer ignores it).
- emoji   — a Twemoji codepoint to render as the illustration (can be a ZWJ/VS16
            sequence; the downloader strips fe0f/200d/20e3 before the CDN filename).

Defaults ship with 40 kid-friendly words across **animals / food / body / colors /
nature / objects**. Keep `len(WORDS)` a multiple of 4 for clean 2×2 pages
(4 → 1 sheet, 8 → 2, 100 → 25). Keep words unique.

## The 3 core recipes (details in SKILL.md / scripts)
### 1. Card artwork — aspect must match the on-page cell
A4 portrait, 10mm margins → usable 190×277mm; a 2×2 cell is 95×138.5mm. Per-card image
aspect ≈ **95:135**, so `W,H = 1150,1634` (≈0.704). `generate_all.py` renders at 2×
(2300×3268) then downscales for AA.

Each front card has 2 zones + a rounded colored frame:
- illustration (top ~35%): emoji centered, clamped inside the border.
- big WORD (lower-middle, centered): auto-fit font shrinks 24%→10% of card width until
  it fits within 72% of card width — long words just get smaller, never clipped.

Back card = white rounded card, one huge centered word (auto-fits to 80% width).

### 2. Word 2×2 grid, borderless, one table per page
- `document.add_table(rows=2, cols=2)`, `autofit=False`.
- Remove all borders (`w:tblBorders` with `w:val="none"`), zero cell margins + spacing.
- `run.add_picture(path, width=Mm(95), height=Mm(135))` on the cell's single run.
- Page 2+ uses `doc.add_section(WD_SECTION.NEW_PAGE)` — NOT a manual page-break
  (python-docx `add_break()` enum ints differ across versions and error out).
- Guard `doc.paragraphs[0]` — a fresh `Document()` may have zero paragraphs.

### 3. Double-sided mirror alignment (THE KEY TRICK)
Word's A4-portrait **default double-sided flip is "flip on long edge" = mirror left↔right**.
So the back page must have its **two columns swapped** vs the front.

Front (TL,TR,BL,BR) = `[w0, w1, w2, w3]`:
```
w0  w1
w2  w3
```
Back (long-edge flip swaps left/right, so each back-word lands under its front-picture):
```
w1  w0     <- swap row 1
w3  w2     <- swap row 2
```
i.e. back layout = `[(0,1,w0),(0,0,w1),(1,1,w2),(1,0,w3)]`.

**Verify programmatically, don't trust your eyes:**
```python
mirror={"TL":"TR","TR":"TL","BL":"BR","BR":"BL"}
for pos,w in front.items():
    assert back[mirror[pos]]==w, f"misaligned {pos}"
```

Tell the user to print with **双面打印 → 长边翻转 (long-edge flip)**, scale 实际大小/不缩放.

## Emoji artwork (fast, crisp, no art skill needed)
Download Twemoji SVG and rasterize to a high-res PNG:
```bash
# per unique codepoint (strip VS16/ZWJ/combining marks from the hex filename):
curl -sL -o cp.svg https://cdn.jsdelivr.net/gh/twitter/twemoji@latest/assets/svg/<hex>.svg
rsvg-convert -w 256 -h 256 -o cp.png cp.svg      # apt-get install -y librsvg2-bin
```
`download_emoji.py` handles all of this: race-free (one temp file + dedup by unique
codepoint before parallel download), md5 collision check, and writes `emoji/_final.json`
(word → hex). Give each codepoint its own temp path — a shared `_t.svg` under parallel
threads corrupts files.

## Emoji pitfalls (all hit — must avoid)
- **VS16 = 💥.** Codepoints with U+FE0F (VS16) or ZWJ **404** on the CDN. Strip
  `0xfe0f, 0x200d, 0x20e3` before forming the hex filename; use the base codepoint.
- **Shared temp file race = corruption.** Don't have parallel threads write to ONE shared
  `_t.svg`; it yields identical (wrong) PNGs for different emoji. Give each codepoint its
  own temp path. **De-dupe by UNIQUE codepoint BEFORE parallel download** — many words can
  share one emoji (ear/hear → 👂); a late `os.remove` on a shared path raises
  `FileNotFoundError`. Download the unique set once, then map back every word that shares it.
- **Pillow can't render color emoji** from font files (0 colored pixels). Use SVG→rsvg-convert.
- **Digit/keycap emoji 404 on the CDN.** `1⃣`–`🔟` are ZWJ/VS16 sequences. For numbers,
  render your OWN digit icons with PIL to `{EMOJI_OUT}/D{n}.png` and mark the WORDS entry's
  `emo` as `D1..D10` (not a real emoji), skipping the CDN pass in the downloader.

## Verification checklist
- [ ] `python3 words100.py` → "OK: 40 unique English words" (or N).
- [ ] `download_emoji.py` → "resolved: N / N", no "WARN unresolved", no unintended md5 dups.
- [ ] `generate_all.py` → 2N PNGs (all_front/all_back), each opens clean.
- [ ] A `vision_analyze` sample of a few cards: each front shows the matching emoji on top
      + a fully-readable word (no clipping/tofu), including the LONGEST word; backs are
      white with one large centered word.
- [ ] `build_docx.py` → `.docx` with `len(doc.tables) == 2*(N/4)`; mirror alignment
      asserted for ALL pairs (not a sample).
- [ ] Send the file (MEDIA:path) + a front/back preview image; remind: 双面/长边翻转,
      实际大小, 157g+ 卡纸 for sturdiness.

## Verification (structure vs content)
- **Structure** (deterministic, always do this): `len(doc.tables) == 2*(N/4)`; each table
  `rows=2, cols=2`; page count = 2*(N/4) sections; total image parts ≈ 2*N.
- **Content** (do a vision check): sample 4–8 front cards + a couple backs; confirm emoji
  matches word, word fully readable (longest word in your list, e.g. "watermelon"), backs
  centered. python-docx renames all inserted images to `media/imageN.png`, so you cannot
  map a cell back to its source PNG by name — verify structure by count, content by eye.

## Extending to a new word set
- Keep `len(WORDS)` a multiple of 4 and words unique. 100 → 25 sheets.
- For a FOLLOW-UP batch ("more 40, no repeats"), first recover the previous `WORDS`,
  keep them as a `USED` set, then `assert not (set(new) & USED)` AND
  `assert len(set(new))==len(new)==N`. Use a FRESH work dir (e.g. `/tmp/ew2`) and a
  distinct `OUT_DOCX` so files never collide with the prior batch.
- A few intentional shared illustrations across words are fine and expected (e.g. two
  body-part words both use ✋/👂 variants).

## Publishing to the internet (open-source)
This skill is laid out to be dropped into a public repo — it works for **both English
and Chinese/hanzi** word flashcards. The working scripts live in `scripts/` (English
path; the Chinese path reuses the same pipeline with pinyin in the middle slot — see
`hanzi-flashcards-word`). The repo-root scaffolding (README, LICENSE, Makefile,
requirements, env example) lives in `templates/open-source/` because the skill's
file-organizer only accepts `scripts/ templates/ references/ assets/` subtrees —
**copy `templates/open-source/*` to the repo root** when publishing, alongside `SKILL.md`.
`references/word-sets.md` holds copy-paste-ready example `WORDS` lists (colours,
animals, verbs, feelings, …) to feed straight into the README's examples or a user's
`words100.py`.

```
flashcards-word/                          (repo root after publishing)
├── SKILL.md                            # this file (spec, recipes, pitfalls, checklists)
├── README.md                           # <- templates/open-source/README.md   (English, has examples)
├── README.zh.md                        # <- templates/open-source/README.zh.md (中文, has examples)
├── LICENSE                             # <- templates/open-source/LICENSE (MIT)
├── Makefile                            # <- templates/open-source/Makefile (make cards)
├── requirements.txt                    # <- templates/open-source/requirements.txt
├── .env.example                        # <- templates/open-source/.env.example
├── references/
│   └── word-sets.md                    # copy-paste-ready example WORDS sets
└── scripts/
    ├── words100.py          # the word list + emoji (edit me)
    ├── download_emoji.py    # Twemoji SVG->PNG downloader (race-free)
    ├── generate_all.py      # renders front+back card PNGs (auto-fit big word)
    └── build_docx.py        # double-sided 2x2 borderless .docx assembler
```
Publish checklist:
- [ ] `scripts/*.py` import `words100.py` from the SAME dir (via `sys.path.insert(0, HERE)`),
      no hardcoded machine paths — works from any clone location.
- [ ] Copy `templates/open-source/*` → repo root → `git add`.
- [ ] `requirements.txt` loosely pinned (`Pillow>=9`, `python-docx>=0.8`); README notes the
      system deps (`rsvg-convert`, a bold sans font, `curl`).
- [ ] `SKILL.md` frontmatter parseable (`name: flashcards-word`); description covers
      BOTH English and Chinese flashcard use cases.
- [ ] `LICENSE` (MIT) + `README.md` (English) + `README.zh.md` (中文) present at root; both
      have **Examples / 示例** sections, cross-linked between them.
- [ ] `make cards` runs the 4 commands in order; optionally add a GitHub Actions workflow
      that builds + attaches the `.docx` as an artifact for folks who just want the file.
- [ ] `git init` → commit → push to a public repo. The `.docx` title is already set to
      "English Words · N · double-sided".

## Related
- `hanzi-flashcards-word` — same layout pipeline for Chinese characters (pinyin).
- `powerpoint` — if the user later wants a .pptx deck instead of print cards.
- `ocr-and-documents` — text/PDF extraction if the user has source vocab to import.
