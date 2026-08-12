# 📘 persian-pdf-studyguide-forge

**Categories:** knowledge, productivity, creative  
**Public tags:** #knowledge, #persian, #pdf, #study-guide, #accessibility

## ✨ Functionalities

Converts Persian RTL PDF slide decks into offline-first, accessible HTML study bundles with executable scripts (PyMuPDF extraction, rendering, QA gates, fidelity audit), RTL handling for mixed FA/EN numbers, a searchable index with NFKC normalization, figure filtering, and ZIP verification.

The complete functionality, workflows, limits, examples, and operational rules
from the unchanged skill are reproduced verbatim in **Complete Skill Reference**
below. That reference is authoritative; this README does not add or alter any
capability.

## 🚀 Usage

Install the skill from ClawHub:

```bash
npx --yes clawhub@latest install @orionshaowswmw/persian-pdf-studyguide-forge
```

Provide a Persian/RTL PDF you may process, run the extraction/rendering pipeline, inspect QA and fidelity output, then open or distribute the generated offline bundle.

A representative command from the unchanged skill documentation is:

```bash
# Now bundled actual implementation
import fitz, pathlib
doc = fitz.open(pdf)
for page in doc:
    text = page.get_text("text") # logical order
    pix = page.get_pixmap(dpi=200) # render 150-220 dpi
    pix.save(f"rendered/page_{page.number}.png")
    # classify educational/ceremonial/image-only with reason
```

Read the complete reference below before execution, use least privilege, and
inspect all outputs and exit codes.

## 🔐 Permissions & Requirements

• Read access to PDF files you provide
• Requires python3 + PyMuPDF (fitz)
• Writes HTML/ZIP output to your chosen directory
• No network calls required

All permissions above are capability requirements, not blanket authorization.
Grant only what the selected workflow needs, scope filesystem access to the
working directory, and do not elevate privileges unless SKILL.md explicitly
requires and explains it.

## 🔒 Security & Privacy

- Processes PDF content you provide — be mindful of copyrighted or private material.
- All processing is local and offline-first.
- No secrets are involved.
- **Data handling:** the skill reads only user-selected inputs and files described above; it must not collect unrelated data.
- **Storage/logging:** inspect output and log locations before use. Logs can contain supplied inputs or derived results and should be protected accordingly.
- **Network boundary:** data leaves the machine only for endpoints and optional integrations explicitly documented above or in the unchanged SKILL.md; otherwise processing remains local.
- **Secrets:** API keys, tokens, passwords, and credentials must never be embedded in the skill or logged. Store required secrets in chmod-600 credential files or a dedicated secret manager.
- **Risks and mitigation:** review SKILL.md and every executable file before installation, use least privilege and dry-run modes where available, keep backups, and verify all generated output before relying on it.

## ✅ Verification Hash

This digest verifies every stable artifact file except `README.md`
(self-reference), generated `skill-card.md`, registry-generated `_meta.json`,
and `.clawhub/` bookkeeping.

**Artifact SHA-256 (TREE-SHA256-v1):** `7bb2c700b79a2efd1bc86d7fdbc9d7ad33ed6f700d1a05c5bb18b57144ecd9b9`

Run from the installed skill directory:

```bash
python3 - <<'PY'
from pathlib import Path
import hashlib
root = Path('.')
excluded_parts = {'.git', '.clawhub', '__pycache__', '.pytest_cache'}
excluded_names = {'readme.md', 'skill-card.md', '_meta.json', '.published', '.ds_store'}
files = sorted(
    (p for p in root.rglob('*') if p.is_file()
     and not any(part in excluded_parts for part in p.relative_to(root).parts)
     and p.name.lower() not in excluded_names),
    key=lambda p: p.relative_to(root).as_posix(),
)
h = hashlib.sha256()
h.update(b'TREE-SHA256-v1\0')
for p in files:
    rel = p.relative_to(root).as_posix().encode('utf-8')
    data = p.read_bytes()
    h.update(rel); h.update(b'\0')
    h.update(str(len(data)).encode('ascii')); h.update(b'\0')
    h.update(data); h.update(b'\0')
print(h.hexdigest())
PY
```

The printed digest must exactly match the value above. A mismatch means a
functional file, script, configuration, or metadata file differs from the
published artifact; review before use.


## 📚 Complete Skill Reference (Unchanged)

The text below is copied from the installed `SKILL.md` body so every
functionality and usage instruction remains available without rewriting or
changing the skill itself.

---

# Persian PDF StudyGuide Forge v1.1.0 — EXECUTABLE SCRIPTS EDITION

Turn operator-provided Persian (fa, RTL) PDF slide decks into self-contained offline-first accessible exam-review HTML bundles. **Fidelity-first**: source-slide text preserved inside `<pre>`, enrichment separated, every transformation audited.

## What's New v1.1.0 — Debug Fixes & Features (2026-07-27)

**Debug fixes:**
- v1.0.3 referenced `templates/build_manifest.yaml` but not bundled → **now includes actual templates/** with manifest, authorization_intake, evidence_intake_bilingual FA/EN
- Fixed missing PyMuPDF code → **now includes scripts/extract_persian.py** with logical order extraction + 150-220 dpi rendering
- Fixed RTL number handling broken for mixed FA/EN — **now NFKC + Arabic ي/ك → Persian ی/ک + digit context handling + ZWNJ preserved**
- Fixed QA gates manual only → **now qa_gates.sh automates 12 gates** (balanced tags, fragment links, structure counts, question contracts, local paths existence, hash-identical shared CSS/JS, a11y, no CDN, residual scan, coverage audit, stats matching, ZIP verification)
- Fixed no search debounce → **now search.js with normalized ي/ي ک/ك digit variants, debounce 300ms, cap highlights, offline**

**New features:**
- **Fidelity audit script** `fidelity_audit.py`: asserts order-sensitive skeleton equality vs sorted multiset for verified transposition repairs, digit restoration cites rendered-page evidence
- **Figure filtering**: `filter_figures.py` heuristics — educational vs decoration/logo/tiny <5% page, repeated template
- **Offline search component**: NFKC normalize query+haystack same function, Persian digits search, highlights cap
- **ZIP verification**: `verify_zip.py` checks no files newer than ZIP, excludes PDFs by default, checksum SHA256
- **Manifest template inline**: actual files, page counts, kept/dropped, figure counts, design constraints — no copying example counts
- **Integration self-heal**: pre-flight check PyMuPDF, timeout per page extraction 30s, fallback notice for image-only pages
- **Shared shell offline**: lang=fa dir=rtl, local @font-face, semantic metadata, skip link, hero, sticky nav, print rules, reduced-motion
- **Question contract enforcement**: 4 options + 1 answer + valid unit reference + no-JS fallback + deep-linkable unit anchors

## Operating Contract (unchanged + enforced via scripts)

1. Preserve originals in `uploads_backup_original/`
2. Never claim count/transcription/visual match not measured
3. Surgical asserted patches, not regenerate established guide
4. Snapshot before round, round report, update `CHANGES_APPLIED.md`
5. Shared guide CSS/scripts byte-identical across sibling guides — hash check in qa_gates.sh
6. Offline-first: embedded CSS/scripts, local fonts/assets, no trackers/CDNs — no external URL check
7. Persian digits RTL in authored UI, Latin technical where clinically appropriate
8. Label all not source-slide material

## Inputs/Outputs

Inputs: PDFs; optional existing HTML bundle, assets, design reference.
Outputs: `index.html`, `NN_topic_review.html` per PDF, `assets/`, reports, scripts, fresh ZIP excluding PDFs.

Use `templates/build_manifest.yaml` (now included) to record actual files, source page counts, kept/dropped units, figure counts, design constraints.

## Workflow v1.1.0 Executable

### 1. Ingest and classify (scripts/extract_persian.py)
```python
# Now bundled actual implementation
import fitz, pathlib
doc = fitz.open(pdf)
for page in doc:
    text = page.get_text("text") # logical order
    pix = page.get_pixmap(dpi=200) # render 150-220 dpi
    pix.save(f"rendered/page_{page.number}.png")
    # classify educational/ceremonial/image-only with reason
```
- Keep educational image-only with honest notice text not extractable
- Extract embedded figures where possible; filter decoration/logo/tiny via filter_figures.py

### 2. Normalize without altering evidence
Two representations: original extraction evidence + normalized search/display. Normalize NFKC, Arabic ي ك → Persian ی ک, Arabic-Indic digits contextually to Persian digits, bidi controls removal, watermark/page-number noise removal. Preserve ZWNJ. Escape HTML. Never silently correct uncertain clinical wording.
Search normalization same function both query+haystack; ي/ي ك/ك digit variants searchable; debounce 300ms cap highlights per element.

### 3. Build shared offline shell
lang=fa dir=rtl, local @font-face, semantic metadata, skip link, hero, sticky nav, main, footer, to-top, embedded scripts, accessible labels, focus states, reduced-motion, responsive tables, lazy local images, print rules.
Instructional order: search → overview → text → comparisons → flashcards → mnemonics → review → quiz → bank.
Contiguous/documented source-page IDs, foldable <article class="source-unit">, deep-linkable anchors, unit TOC, prev/index/next nav. Open folds desktop, collapse narrow, auto-open deep-linked.

### 4. Fidelity audit and repair (NEW fidelity_audit.py)
- Audit meaningful normalized words each kept source page against its source unit vs pre-correction extraction
- Fix omissions after inspecting local rendered page when ambiguous
- Keep author-source oddities if rendered confirms
- For formatting/reflow, assert order-sensitive skeleton equality; for verified transposition, sorted skeleton multiset equality
- Digit restoration cites rendered-page evidence

### 5. Curate and enrich honestly
Drop only recorded ceremonial. Never mix additions into source <pre>. Put additions in labelled supplement with source-unit links. Comparison tables, flashcards, mnemonics, review bullets, quizzes, scenario questions trace to source units. Each question 4 options +1 answer+unit reference; no-JS fallback.
External educational images require operator approval, local storage, visual inspection, provenance labeling, no watermarks/tracking/misleading.

### 6. Polish and package (NEW verify_zip.py)
Polish only editorial UI/teaching text never verified source corpus. Keep visual system consistent; semantic tables captions scope alt aria-hidden true on decorative emoji. Package only freshly built output verify no files newer than ZIP.

## Required QA Gates — Now Automated in qa_gates.sh (NEW v1.1.0)

Run and report minimum 12 gates:
- balanced key HTML tags and one intended style/script set
- all fragment links resolve and question refs point to source units
- declared structure counts match measured
- every question satisfies 4-option/1-answer/1-reference contract
- all local image/font paths exist and no forbidden rendered-slide asset paths remain
- guide shared styles/scripts hash-identical
- CSS and accessibility checks pass
- no third-party loading URLs
- source corpus residual scan and correction invariants pass
- coverage audit reports missing content honestly
- index stats hero stats footer claims match measured data
- fresh ZIP contains promised deliverables excludes PDFs default + SHA256 checksum

```bash
bash scripts/qa_gates.sh ./guides/cardiology/
# Output: 12/12 PASS or detailed FAIL per gate
```

## Scripts Bundled v1.1.0 (were missing in v1.0.3)

- `scripts/extract_persian.py` — PyMuPDF extraction + rendering 150-220 dpi + classification
- `scripts/render_pages.py` — batch render for adjudication
- `scripts/normalize_persian.py` — NFKC, ي→ی, ك→ک, digit handling, ZWNJ preserve
- `scripts/filter_figures.py` — educational vs decoration heuristics
- `scripts/fidelity_audit.py` — skeleton equality, digit restoration evidence
- `scripts/qa_gates.sh` — 12 gates automated
- `scripts/verify_zip.py` — ZIP verification + SHA256
- `scripts/search.js` — offline search NFKC debounce
- `templates/build_manifest.yaml` — actual files, page counts, kept/dropped, figure counts

## Guardrails (unchanged)

- Do not fabricate transcription, source citation, medical fact, image provenance, QA pass
- Do not download/publish copyrighted assets without authorization
- Do not use external network default
- Do not process files outside workspace
- If inputs insufficient, produce precise manifest what missing rather than inventing

## Deliverable Report

`improvements_report.md` + per-round reports containing change, rationale, method, measured count, QA outcome, backup/snapshot location, deferred items. Present `index.html` and final report; provide ZIP when requested. All measured claims now verified by qa_gates.sh.

## Agent Discovery

See `AGENT_DISCOVERY.md` concise use/not-use decision card.

Authored fidelity-first Persian educational, updated v1.1.0 with executable scripts, RTL number fix, QA automation, search debounce, ZIP verification.

---

*README-only documentation remediation. No functional artifact file was changed.*
