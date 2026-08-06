---
name: iwork2md
slug: iwork2md
version: 1.0.0
displayName: iWork to Markdown
description: "Convert Apple iWork documents (Pages .pages, Numbers .numbers, Keynote .key) into Markdown. Use whenever the user wants to read, extract, or translate the content of an iWork file into text/markdown, for example 'convert this .pages file to markdown', 'extract text from a Numbers sheet', 'read a Keynote file', or 'open a .key/.numbers/.pages and turn it into markdown'. Handles the iWork '13+ format (bundle containing Index.zip with .iwa files that wrap Snappy-framed Protobuf) with no third-party dependencies."
license: MIT
summary: Convert Apple iWork (.pages/.numbers/.key) documents to Markdown with a dependency-free Python parser.
tags:
  - iwork
  - pages
  - numbers
  - keynote
  - markdown
  - conversion
---

# iwork2md — iWork (.pages / .numbers / .key) to Markdown

Convert Apple Pages / Numbers / Keynote documents to Markdown. The parser is in
`scripts/iwa.py` (pure stdlib); the converter CLI is `scripts/iwork2md.py`.

## When to use

- User provides a `.pages`, `.numbers`, or `.key` file and wants its text,
  tables, or slides as Markdown (or just to *read* the content).
- User asks to "extract text / convert / translate / open" an iWork file.
- Do NOT use for: password-protected/encrypted iWork docs (unsupported),
  or for reconstructing exact visual layout (not the goal).

## How to run

```bash
# Write a .md next to the source (auto-named)
python3 scripts/iwork2md.py path/to/Doc.pages

# Explicit output path
python3 scripts/iwork2md.py Doc.numbers out.md

# Print to stdout
python3 scripts/iwork2md.py Doc.key --stdout

# Debug: dump every recovered text fragment
python3 scripts/iwork2md.py Doc.numbers --texts

# List embedded media (images/video)
python3 scripts/iwork2md.py Doc.pages --media
```

From inside a chat, invoke with `exec` (or tell the user to run it). The script
is dependency-free (Python 3.8+, stdlib only: `zipfile`, `struct`, `io`,
`plistlib`).

## What it does

1. Opens the bundle ZIP; finds `Index.zip` (or `.iwa` files directly under
   `Index/`).
2. For each `.iwa`: removes the iWork **Snappy framing** (chunk type + 3-byte
   LE length, no stream-id, no CRC), then raw-Snappy-decompresses the body.
3. Parses the **Protobuf container** (`varint len + ArchiveInfo {identifier,
   message_infos[]}` then payloads), and generically walks every message to
   collect UTF-8 string fields — recovering ~100% of readable content without
   needing the app-specific schema map (TSPRegistry).
4. Renders Markdown: document title (from `Metadata/Properties.plist` or first
   heading), an embedded-media list, reconstructed **Numbers tables** (rows
   stored as `"a | b | c"` become proper markdown tables, deduped across
   mirrored components), a body block (largest multi-line text), and remaining
   text fragments.

## Key facts you need (so you don't re-derive them)

- iWork `.iwa` Snappy framing is **non-standard**: type byte `0x00`, 3-byte LE
  length, then a **raw** Snappy block (NOT an official framed stream). No
  stream-identifier chunk, no CRC. (`iwa.iwa_unframe`)
- Raw Snappy: uncompressed-length varint, then LZ77 (literals + copies). Copies
  have 1/2/4-byte offsets. (`iwa.snappy_decompress`)
- Payload `type` ids map to schemas inside the iWork binaries and vary by
  app/version — Protobuf is not self-describing, so we decode generically by
  string fields. See `references/FORMAT.md` for the full spec and limits.
- Numbers table rows serialize as a single `"cell | cell | cell"` string per
  row → the CLI groups consecutive such rows into a markdown table.

## Output quality & limits

- ✅ Recovers all text, Numbers table structure, slide text, media inventory.
- ❌ No exact layout/fonts/colors/merged-cell geometry/charts/shapes.
- ❌ Encrypted (password-locked) documents are not readable.
- If a user needs perfect structural fidelity, note that it requires extracting
  the TSPRegistry type map for their iWork version; the generic walker here is
  the reliable, dependency-free fallback.

## Testing / validating

`scripts/test_iwa.py` round-trips a synthetic `.iwa` (encoder + parser) to prove
the Snappy framing, raw-Snappy copy path, and Protobuf container logic. Run:
`python3 scripts/test_iwa.py`.
