# 📘 Persian PDF StudyGuide Forge

An executable, fidelity-first toolkit for turning **operator-authorized Persian RTL lecture PDFs** into accessible, offline-first HTML study guides. Version 1.3.0 adds robust Persian/Arabic ref-and-answer coercion, post-hoc flashcard answer verification, and stricter QA gates on top of the 1.2.2 pipeline.

## ✨ What it does

- Measures and hashes the source PDF.
- Extracts a logical text layer with PyMuPDF/Poppler.
- Runs an independent Persian–English Tesseract OCR pass.
- Renders compact page evidence for visual checking and offline HTML.
- Normalizes Persian Unicode, digits, whitespace and mixed RTL/LTR safely.
- Optionally uses multiple AI providers as a reasoning team: rotating primary correction, independent reviewer, retries, cache/resume and validated failover.
- Detects candidate session boundaries for mandatory review.
- Generates source-linked tables, flashcards, mnemonics, review points, four-option quizzes and clinical/laboratory scenarios.
- Supports a high-volume `--maximum` enrichment mode while rejecting exact duplicates.
- Coerces Persian/Arabic provider output («صفحهٔ ۳» refs, «الف/ب/ج/د» answer labels, bare arrays, partial batches) instead of silently dropping it.
- Verifies flashcard answers against their source pages with an independent model (`scripts/verify_flashcards.py`).
- Builds a self-contained HTML with embedded images, search, dark mode, folds, deep links, responsive tables, print support and interactive scoring.
- Produces fidelity reports, automated QA results, verified ZIPs and SHA-256 checksums.

See [`docs/WORKFLOW_PLAYBOOK.md`](docs/WORKFLOW_PLAYBOOK.md) for every production method, procedure, recovery trick and QA rule.

## 🚀 Minimal workflow

```bash
python3 scripts/preflight.py
python3 scripts/extract_dual_ocr.py lecture.pdf --out work/extraction
python3 scripts/reasoning_team_correct.py work/extraction/evidence.json \
  --providers providers.json --out work/corrections
python3 scripts/detect_session_candidates.py work/corrections/final.json \
  --out work/session_candidates.json
# Review and create sessions.json.
python3 scripts/reasoning_team_enrich.py work/corrections/final.json sessions.json \
  --providers providers.json --out work/enrichment --maximum
python3 scripts/verify_flashcards.py work/corrections/final.json work/enrichment/all.json \
  --providers providers.json --out work/enrichment/all.verified.json
python3 scripts/build_selfcontained_html.py work/corrections/final.json work/extraction \
  work/enrichment/all.verified.json --output work/studyguide.html --title 'عنوان درس'
python3 scripts/fidelity_audit.py work/extraction/evidence.json work/corrections/final.json \
  --out work/fidelity.json
python3 scripts/qa_gates.py work/studyguide.html
python3 scripts/verify_zip.py work work/studyguide.zip
```

## 🔐 Permissions and requirements

### Required local reads

- PDFs and optional reference HTML explicitly supplied/authorized by the operator.
- Bundled templates and locally generated extraction/OCR evidence.

### Required local writes

- Workspace-only rendered pages, OCR caches, JSON evidence, HTML, reports, manifests and ZIPs.

### Required commands

- Python 3
- Poppler: `pdfinfo`, `pdftotext`, `pdftoppm`
- Tesseract with `fas` and `eng`

Optional: PyMuPDF, Pillow, BeautifulSoup4, Node.js.

### Optional network access

Disabled by default. Network is used only when the operator explicitly requests either:

1. download of an authorized PDF URL; or
2. AI-assisted correction/enrichment through endpoints listed in a local provider configuration.

### API keys

No key is bundled. Provider configuration records only `api_key_env`, such as `GEMINI_API_KEY`. Put values in an environment/secret manager or a `0600` local file sourced outside the skill directory. Never paste keys into HTML, prompts, logs, README, Git, or ClawHub.

## 🔒 Security & Privacy

- Local extraction/build/QA sends nothing off-device.
- AI mode sends only the selected OCR/source batches to explicitly configured providers.
- The skill does not transmit files to ClawHub during normal use.
- Scripts do not print authorization headers or key values.
- Successful AI batches are cached without credentials to make long jobs resumable.
- Remote download enforces HTTPS by default, a size cap, PDF magic and SHA-256 recording.
- Source PDFs may contain private/copyrighted material. Confirm authority before processing and distribution.
- AI can introduce factual errors. Use rendered-page evidence, fidelity reports and QA; medical/academic content still requires qualified review.
- Self-contained HTML can be large because page images are embedded. Use linked-image mode when required.
- Review all bundled scripts before execution and restrict them to a dedicated workspace.

## Known risks and mitigations

| Risk | Mitigation |
|---|---|
| OCR omissions or garbled RTL | dual OCR, rendered-page evidence, primary + reviewer, manual adjudication |
| AI hallucination | source-only prompts, strict JSON, page-range references, independent review, fidelity audit |
| Partial/truncated provider output | schema/count validation, retries, provider rotation, split batches, cache/resume |
| Secret disclosure | environment variable names only; no literal keys; never log headers |
| Inflated “maximum” content | session grounding, exact duplicate rejection, source links and question contracts |
| False completeness claim | measured PDF/unit/image counts and QA gate report |
| Broken offline bundle | no external browser loads, embedded CSS/JS/images, ZIP verification |

## ✅ Verification

The published artifact includes `MANIFEST.sha256`, covering executable scripts, templates, documentation and skill metadata. Verify after installation:

```bash
cd persian-pdf-studyguide-forge
sha256sum -c MANIFEST.sha256
```

Manifest SHA-256: `fee156a1f7b271b513663f54ebbae567dffe343d1dbcaa03d801d4fd8d4987dc`

`README.md`, `MANIFEST.sha256`, and registry-managed `skill-card.md` and `_meta.json` are excluded from the file list to avoid a self-referential hash; the manifest hash above authenticates the list itself.

## License

MIT-0 — free to use, modify and redistribute without attribution.
