---
name: docx-trackdiff
description: >
  Compare two versions of a .docx document and produce a single Word file in
  tracked-changes (revision / tracking) mode, as if a human had edited the old
  file into the new one with Track Changes turned on. Use whenever the user has
  two versions of a DOCX (e.g., successive drafts of a paper, report, or
  contract — often AI-generated or AI-assisted revisions) and wants to see the
  differences as native Word revisions (insertions/deletions) that can be
  accepted/rejected in Word. Triggers: "对比两个版本的 docx", "tracked changes",
  "tracking mode", "修订模式对比", "compare two Word documents", "diff two
  drafts", "生成修订对比文件". Do NOT use for: creating new documents from
  scratch (use docx skill), single-file editing with revisions (use docx WIR
  engine), or PDF-only comparisons.
---

# DOCX Tracked-Changes Comparison

Given an OLD and a NEW version of a `.docx`, produce ONE output `.docx` that
opens in Word with native revision marks (`<w:ins>` / `<w:del>`) showing every
change from OLD to NEW. The output uses the NEW file as the base package, so
all its styles, images, footnotes, tables, and section properties are
preserved; accepting all revisions yields exactly NEW, rejecting all yields
exactly OLD.

## Workflow

1. **Run the script** — do not reimplement the diff:

```bash
python3 scripts/compare_docx_tracked.py OLD.docx NEW.docx OUT.docx \
    --author "Reviser Name" --date "2026-08-15T00:00:00Z"
```

- Ask the user for the revision **author name** and date if not provided
  (default author "Editor", default date = today). The author is usually the
  person who made the new draft, not the assistant.
- `--threshold` (default 0.45) controls when a paragraph pair is treated as
  "modified" (word-level inline revisions) vs "deleted + inserted" (two whole
  paragraphs). Lower it if too many lightly-edited paragraphs show as whole-
  paragraph replace; raise it if heavily rewritten paragraphs produce noisy
  inline diffs.
- The script prints stats (ins/del paragraphs, word-level modified, fallbacks).
  Report these numbers to the user.

2. **Verify (mandatory)** — run the verifier; all checks must PASS:

```bash
python3 scripts/verify_tracked.py OUT.docx OLD.docx NEW.docx
```

It checks: unique revision ids, no stray `w:t` inside `w:del`, resolvable
relationship references, `w:trackChanges` present, accept-all == NEW text,
reject-all == OLD text, and that OLD-only content is fully covered by
`w:delText`.

3. **Render check** — convert with LibreOffice to confirm the package opens
   cleanly and revisions render (strikethrough deletions, marked insertions):

```bash
soffice --headless --convert-to pdf --outdir <tmpdir> OUT.docx
```

If conversion fails or the verifier fails, consult
`references/ooxml-revision-rules.md` — it catalogs the exact OOXML rules and
known failure modes (stray `w:t` in `w:del`, missing paragraph-mark deletions,
dangling r:ids, missing `w:trackChanges`).

## Output conventions

- Name the output `<oldTag>-vs-<newTag>-tracked-changes.docx` (e.g.,
  `20260810-vs-20260815-tracked-changes.docx`) and tell the user it opens in
  Word's revision ("所有标记") view.
- A few paragraphs containing images/equations/hyperlinks may legitimately
  appear as whole-paragraph delete+insert instead of inline diffs — this is a
  designed fallback, mention it if it occurs (the script reports
  `mod_fallback`).

## Scope & limits

- Both inputs must be valid `.docx` (convert `.doc` first via
  `libreoffice --headless --convert-to docx`).
- Comparison covers the main document body (including table cell paragraphs);
  comments/footnotes content is not diffed (footnotes of the NEW package are
  preserved as-is).
- Verified via LibreOffice and XML-level simulation; when the stakes are high,
  advise the user to eyeball the result in Microsoft Word's "All Markup" view.
