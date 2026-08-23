---
name: persian-pdf-studyguide-forge
version: 1.3.0
author: orionshaowswmw
license: MIT-0
description: Executable fidelity-first pipeline that converts authorized Persian RTL PDFs into accessible offline HTML study guides using dual OCR, rendered-page evidence, optional multi-model primary/reviewer correction, session-grounded maximum enrichment, self-contained images, interactive search/quizzes, measured fidelity, QA gates, and verified ZIP packaging. v1.3.0 adds robust Persian/Arabic ref-and-answer coercion, post-hoc flashcard answer verification, and stricter QA gates.
categories: [knowledge, productivity, creative]
topics: [persian, pdf, study-guide, rtl, accessibility]
permissions:
  file_read: {required: true, scope: [Operator-authorized PDFs, optional reference HTML, local templates and assets]}
  file_write: {required: true, scope: [Workspace extraction evidence, OCR cache, HTML, QA reports, manifests and ZIPs]}
  shell: {required: true, scope: [Local Poppler, Tesseract, Python, optional Node syntax check and ZIP operations]}
  network: {required: false, scope: [Disabled by default; optional operator-approved PDF download and AI provider APIs named in providers.json]}
metadata:
  openclaw:
    emoji: "📘"
    requires:
      bins: [python3, pdfinfo, pdftotext, pdftoppm, tesseract]
      optional_bins: [node]
      python: [beautifulsoup4]
      optional_python: [pymupdf, pillow]
---

# Persian PDF StudyGuide Forge v1.2.2 — complete executable pipeline

Convert an operator-authorized Persian/English RTL lecture PDF into a polished offline study guide without confusing OCR, AI reconstruction, or enrichment with source evidence.

## Capabilities included in this artifact

- authorized HTTPS download with PDF-magic, size and SHA-256 verification;
- measured `pdfinfo` intake and page-count safeguards;
- PyMuPDF or `pdftotext` logical extraction;
- independent Tesseract `fas+eng` OCR over high-resolution grayscale pages;
- compact rendered-page JPEGs for visual adjudication and HTML fidelity;
- Persian NFKC/letter/digit/whitespace normalization while preserving ZWNJ;
- resumable multi-provider reasoning-team correction with strict JSON contracts;
- primary model rotation plus independent reviewer pass;
- retry/backoff, provider failover, cache/resume, and local OCR fallback;
- session candidate detection plus mandatory boundary review;
- session-grounded tables, flashcards, mnemonics, summaries, quizzes and scenarios;
- balanced and maximum enrichment modes;
- exact duplicate rejection and page-range-constrained references;
- self-contained Base64 images or linked local-image mode;
- established RTL shell: search, session map, foldable source units, dark mode, responsive tables, print, reduced motion, quiz scoring and deep links;
- per-page fidelity metrics and manual-review queue;
- measured HTML QA gates and verified ZIP/SHA-256 packaging;
- robust Persian/Arabic coercion: «صفحهٔ ۳» references, «الف/ب/ج/د» answer labels, bare JSON arrays and partial batches are normalized instead of silently dropped (v1.3.0);
- post-hoc independent flashcard answer verification against source pages via `scripts/verify_flashcards.py` (v1.3.0);
- stricter QA gates: no bare-letter flashcard answers and no duplicated option letter prefixes (v1.3.0).

Full procedures, failure recovery, and production tricks: [`docs/WORKFLOW_PLAYBOOK.md`](docs/WORKFLOW_PLAYBOOK.md).

## Quick start

```bash
python3 scripts/preflight.py
python3 scripts/extract_dual_ocr.py authorized.pdf --out work/extraction

# Optional network-assisted correction. providers.json stores ENV NAMES only.
export GEMINI_API_KEY='set-in-your-secret-manager'
python3 scripts/reasoning_team_correct.py work/extraction/evidence.json \
  --providers providers.json --out work/corrections

python3 scripts/detect_session_candidates.py work/corrections/final.json \
  --out work/session_candidates.json
# Review candidates against rendered pages, then create work/sessions.json.

python3 scripts/reasoning_team_enrich.py work/corrections/final.json work/sessions.json \
  --providers providers.json --out work/enrichment --maximum

# Optional but recommended: independently verify flashcard answers against source pages.
python3 scripts/verify_flashcards.py work/corrections/final.json work/enrichment/all.json \
  --providers providers.json --out work/enrichment/all.verified.json

python3 scripts/build_selfcontained_html.py work/corrections/final.json work/extraction \
  work/enrichment/all.verified.json --output work/studyguide.html --title 'عنوان درس'
# (use work/enrichment/all.json if you skipped verification)

python3 scripts/fidelity_audit.py work/extraction/evidence.json \
  work/corrections/final.json --out work/fidelity.json
python3 scripts/qa_gates.py work/studyguide.html
python3 scripts/verify_zip.py work work/final-studyguide.zip
```

`run_pipeline.sh` executes through correction and then intentionally pauses for reviewed session boundaries. It prints exact continuation commands.

## Important evidence rule

Three layers remain distinct:

1. `evidence.json`: untouched/raw extraction evidence;
2. `corrections/final.json`: edited teaching/source reconstruction;
3. `enrichment/all.json`: clearly separate study aids.

Never place AI additions inside source evidence. Never claim verbatim transcription when reconstruction occurred. Rendered pages remain the final adjudication source for unreadable text and digits.

## Network and key handling

Network use is optional and requires operator approval. `providers.example.json` contains `api_key_env` names, never key values. Scripts read keys from environment variables, never print request headers, and cache response bodies without credentials. Do not commit provider configuration containing literal secrets.

## Included executable files

- `scripts/preflight.py`
- `scripts/download_authorized_pdf.py`
- `scripts/extract_dual_ocr.py`
- `scripts/reasoning_team_correct.py`
- `scripts/detect_session_candidates.py`
- `scripts/reasoning_team_enrich.py`
- `scripts/verify_flashcards.py`
- `scripts/build_selfcontained_html.py`
- `scripts/fidelity_audit.py`
- `scripts/filter_figures.py`
- `scripts/qa_gates.py`
- `scripts/verify_zip.py`
- `scripts/run_pipeline.sh`
- `scripts/common.py`
- `templates/guide.css`
- `templates/app.js`
- `templates/providers.example.json`
- `templates/sessions.example.json`
- `templates/build_manifest.json`

## Guardrails

- Process only authorized material.
- Do not bypass access controls or copy secrets into artifacts.
- Do not fabricate source text, citation, medical fact, image provenance, counts or QA results.
- Do not silently delete image-only or difficult pages.
- Do not treat automated fidelity scores as semantic proof.
- Do not publish or distribute copyrighted source pages without permission.
- Inspect and validate all generated medical education before reliance.

## Definition of done

A guide is complete only when actual source-unit/image counts match measured PDF pages, every reference resolves, every question contract passes, duplicates are removed, no forbidden external browser resources remain, fidelity exceptions were reviewed, displayed counts match measured counts, and packaging verification succeeds.
