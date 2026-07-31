---
name: persian-pdf-studyguide-forge
version: 1.1.0
author: orionshaowswmw
license: MIT
description: Convert Persian RTL PDF slide decks into offline-first accessible HTML bundles with actual executable scripts (PyMuPDF extraction, rendering, QA gates, fidelity audit), RTL handling for mixed FA/EN numbers, searchable index with NFKC normalization, figure filtering, ZIP verification, manifest template. Fidelity-first.
permissions:
 file_read: {required: true, scope: [Read PDFs, existing HTML bundles, local assets]}
 file_write: {required: true, scope: [Create HTML guides, assets, reports, QA logs, ZIP]}
 network: {required: false, scope: [No network default, only operator-approved supplementary images/fonts]}
 shell: {required: true, scope: [Local PyMuPDF extraction, image rendering, integrity checks, archive creation workspace only]}
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
