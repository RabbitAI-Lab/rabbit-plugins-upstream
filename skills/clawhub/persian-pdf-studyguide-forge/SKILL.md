---
name: persian-pdf-studyguide-forge
version: 1.3.2
author: orionshaowswmw
license: MIT-0
description: Fidelity-first pipeline converting operator-authorized Persian/English RTL lecture PDFs into offline HTML study guides — dual OCR (PyMuPDF + Tesseract fas+eng), rendered-page evidence, optional multi-model correction, session-grounded enrichment (tables/flashcards/quizzes/mnemonics/summaries/scenarios), measured fidelity, QA gates, verified ZIP. Persian/Arabic ref-and-answer coercion, post-hoc flashcard verification, strict JSON contracts.
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

# Persian PDF StudyGuide Forge v1.3.0

Use when: converting an **operator-authorized** Persian/English RTL lecture PDF into a polished offline study guide with source evidence. Never confuse OCR output, AI reconstruction, or enrichment with source text.

**Golden example:** `examples/01_sleep_eating_review.html` — a finished, QA-passing guide (Persian RTL, sleep/eating-disorders review). After building, compare your output against it: same RTL shell (search, session map, foldable source units), embedded page images, flashcards/quizzes with «الف/ب/ج/د» labels, zero external resources. Missing these = something is wrong.

## Pipeline (run in order)

```bash
python3 scripts/preflight.py                       # env + pdfinfo intake/page-count safeguards
python3 scripts/extract_dual_ocr.py authorized.pdf --out work/extraction
# Network correction is OPTIONAL (OCR-only path works offline) and needs operator approval:
python3 scripts/reasoning_team_correct.py work/extraction/evidence.json \
  --providers providers.json --out work/corrections
python3 scripts/detect_session_candidates.py work/corrections/final.json --out work/session_candidates.json
# MANDATORY: review candidates against rendered pages, then write work/sessions.json
python3 scripts/reasoning_team_enrich.py work/corrections/final.json work/sessions.json \
  --providers providers.json --out work/enrichment --maximum   # or omit --maximum for balanced
python3 scripts/verify_flashcards.py work/corrections/final.json work/enrichment/all.json \
  --providers providers.json --out work/enrichment/all.verified.json   # independent post-hoc verification vs source pages
python3 scripts/build_selfcontained_html.py work/corrections/final.json work/extraction \
  work/enrichment/all.verified.json --output work/studyguide.html --title 'عنوان درس'
python3 scripts/fidelity_audit.py work/extraction/evidence.json \
  work/corrections/final.json --out work/fidelity.json
python3 scripts/qa_gates.py work/studyguide.html    # strict gates: no bare-letter flashcard answers, no duplicated option prefixes
python3 scripts/verify_zip.py work work/final-studyguide.zip
```

`run_pipeline.sh` automates through correction, then pauses for the mandatory session-boundary review and prints continuation commands. Built-in: retry/backoff, provider failover, cache/resume, local OCR fallback; Persian NFKC normalization preserving ZWNJ; «صفحهٔ ۳»/«الف/ب/ج/د» ref-and-answer coercion (bare JSON arrays & partial batches normalized, never dropped); RTL shell (search, session map, foldable units, dark mode, print, quiz scoring); Base64 self-contained images or linked-local mode. Full failure-recovery procedures and production tricks: `docs/WORKFLOW_PLAYBOOK.md`. File inventory: `ls scripts/ templates/`.

## Evidence layers — never mix

1. `evidence.json` — untouched extraction · 2. `corrections/final.json` — reconstruction · 3. `enrichment/all.json` — study aids.
Never place AI additions inside source evidence; never claim verbatim transcription when reconstruction occurred; rendered pages are the final adjudication source for unreadable text and digits. Enrichment references must cite page ranges; exact duplicates are rejected.

## Model routing (cost control)

Primary correction: strongest available model, rotated. Independent reviewer pass: cheaper model is fine. Bulk enrichment: cheap model (session-grounding constrains it); flashcard verification: strong model. `providers.json` stores `api_key_env` NAMES only — keys come from environment, headers are never printed, cached responses carry no credentials, and no provider config with literal secrets is ever committed.

## Guardrails

- Authorized material only; no bypassing access controls; no secrets in artifacts.
- Never fabricate source text, citations, medical facts, image provenance, counts, or QA results.
- Never silently delete image-only or difficult pages; automated fidelity scores are not semantic proof.
- Do not publish or redistribute copyrighted source pages without permission; inspect and validate generated medical education before reliance.

## Definition of done

Source-unit/image counts match measured PDF pages · every reference resolves · every question contract passes · duplicates removed · no external browser resources in the HTML · per-page fidelity exceptions reviewed · displayed counts match measured counts · QA gates and ZIP/SHA-256 verification pass.
