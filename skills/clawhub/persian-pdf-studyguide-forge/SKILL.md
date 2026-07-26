---
name: persian-pdf-studyguide-forge
description: Convert Persian RTL PDF slide decks into offline-first, accessible, exam-review HTML study-guide bundles using a staged fidelity-first workflow, evidence-based corrections, and automated QA.
permissions:
  file_read:
    required: true
    scope:
      - Read operator-provided PDFs, existing HTML bundles, local assets, and local reference materials.
  file_write:
    required: true
    scope:
      - Create or patch HTML guides, local assets, reports, backups, QA logs, and a local ZIP export in the workspace.
  network:
    required: false
    scope:
      - No network is required by default. Only use operator-approved sources for optional supplementary educational images or fonts.
  shell:
    required: true
    scope:
      - Run local PyMuPDF extraction, image rendering, integrity checks, and archive creation inside the workspace only.
metadata:
  openclaw:
    audit:
      category: Creative
      permissions:
        file-read: true
        file-write: true
        network: false
        shell: true
---

# Persian PDF StudyGuide Forge

Turn operator-provided Persian (`fa`, RTL) PDF slide decks into self-contained, offline-first, accessible exam-review HTML bundles. This skill is **fidelity-first**: source-slide text is preserved inside `<pre>` blocks; editorial enrichment is clearly separated; every transformation is audited.

## Operating contract

1. Work locally and preserve original uploads in `uploads_backup_original/`.
2. Never claim a count, complete transcription, or visual match that has not been measured.
3. Apply surgical, asserted patches. Do not regenerate an established guide when a scoped change is sufficient.
4. Create a snapshot before each round, write a round report, and update `CHANGES_APPLIED.md`.
5. Keep shared guide CSS and scripts byte-identical across sibling guides.
6. Keep the bundle offline-first: embedded CSS/scripts, local fonts/assets, no trackers/CDNs.
7. Use Persian digits and RTL in authored Persian UI. Preserve Latin technical terms where clinically appropriate.
8. Clearly label all material that is not source-slide content.

## Inputs and outputs

**Inputs:** PDFs; optionally an existing HTML bundle, local assets, and a design reference.

**Outputs:** `index.html`, one `NN_topic_review.html` per PDF, `assets/`, reports, reusable scripts, and a fresh ZIP excluding input PDFs unless requested.

Use `templates/build_manifest.yaml` to record actual files, source page counts, kept/dropped units, figure counts, and design constraints. Do not copy example target counts from a reference project into a new project.

## Workflow

### 1. Ingest and classify

- Extract each page with PyMuPDF `page.get_text("text")` in logical order.
- Render each source page locally (about 150–220 dpi) for adjudication and visual QA.
- Classify pages as educational, ceremonial, or image-only. Record each decision and reason.
- Keep educational image-only pages with an honest notice that text was not extractable.
- Extract embedded educational figures where possible; filter repeated template decorations, tiny assets, and logos.

### 2. Normalize without altering evidence

Maintain two representations: original extraction for fidelity evidence and normalized text for search/display work. Normalize NFKC, Arabic `ي/ك` to Persian `ی/ک`, Arabic-Indic digits contextually to Persian digits, unwanted bidi controls, and obvious watermark/page-number noise. Preserve ZWNJ. Escape raw HTML-sensitive text. Never silently “correct” uncertain clinical or source wording.

For search, normalize both query and cached haystack with the same function; make `ی/ي`, `ک/ك`, and digit variants searchable. Debounce input and cap highlights per element.

### 3. Build a shared offline shell

Each guide uses `lang="fa" dir="rtl"`, local `@font-face`, semantic metadata, a skip link, hero, sticky navigation, main content, footer, to-top control, and embedded scripts. Use accessible labels, visible focus states, reduced-motion support, responsive tables, lazy local images, and print rules.

Build the instructional order as:
`search → overview → text → comparisons → flashcards → mnemonics → review → quiz → bank`.

The source corpus uses contiguous or documented source-page IDs, foldable `<article class="source-unit">` structures, deep-linkable unit anchors, a unit TOC, and previous/index/next navigation. Open folds on desktop, collapse them on narrow screens, and automatically open a deep-linked fold.

### 4. Fidelity audit and repair

- Audit meaningful normalized words from each kept source page against its corresponding source unit.
- Compare against the **pre-correction extraction**, not merely post-correction text.
- Fix omissions only after inspecting the local rendered page when extraction is ambiguous.
- Keep author-source oddities if the rendered source confirms them.
- For formatting/reflow changes, assert order-sensitive skeleton equality; for verified transposition repairs, assert sorted skeleton multiset equality.
- Any digit restoration must cite rendered-page evidence.

### 5. Curate and enrich honestly

Drop only recorded ceremonial material. Never mix additions into a source `<pre>`. Put educational additions in a labelled supplement with source-unit links. Ensure comparison tables, flashcards, mnemonics, review bullets, quizzes, and scenario questions trace to source units. Each question needs four options, one answer, and a valid unit reference; provide a usable no-JavaScript fallback.

Optional external educational images require operator approval, local storage, visual inspection, provenance labeling, and no watermarks, tracking, or misleading claims.

### 6. Polish and package

Polish only editorial UI and teaching text, never the verified source corpus. Keep the visual system consistent across guides; use semantic tables, captions, `scope`, image alt text, and `aria-hidden="true"` on decorative emoji spans. Package only freshly built output and verify that no files are newer than the ZIP.

## Required QA gates

Run and report, at minimum:

- balanced key HTML tags and one intended style/script set;
- all fragment links resolve and question references point to source units;
- declared structure counts match measured counts;
- every question satisfies its four-option/one-answer/one-reference contract;
- all local image/font paths exist and no forbidden rendered-slide asset paths remain;
- guide shared styles/scripts are hash-identical;
- CSS and accessibility checks pass;
- no third-party loading URLs;
- source corpus residual scan and correction invariants pass;
- coverage audit reports missing content honestly;
- index statistics, hero statistics, and footer claims match measured data;
- fresh ZIP contains the promised deliverables and excludes source PDFs by default.

## Guardrails

- Do not fabricate a transcription, source citation, medical fact, image provenance, or QA pass.
- Do not download or publish copyrighted assets without authorization.
- Do not use external network resources by default.
- Do not process files outside the operator-provided workspace.
- If inputs are insufficient, produce a precise manifest of what is missing rather than inventing content.

## Deliverable report

Write `improvements_report.md` and per-round reports containing: change, rationale, method, measured count, QA outcome, backup/snapshot location, and deferred items. Present `index.html` and the final report; provide the ZIP when requested.
## Agent discovery

See `AGENT_DISCOVERY.md` for a concise, operator-respecting use/not-use decision card. It is informational only and never authorizes autonomous installation or engagement.
