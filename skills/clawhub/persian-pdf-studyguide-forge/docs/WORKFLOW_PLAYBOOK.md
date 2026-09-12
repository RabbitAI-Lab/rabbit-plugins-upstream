# Persian PDF StudyGuide Forge — complete workflow playbook

This playbook records the full production method used for large Persian RTL lecture PDFs, including a 378-page bacteriology deck. It distinguishes **source reconstruction** from **educational enrichment** and requires measured QA before any completeness claim.

## 0. Authorization, security, and workspace discipline

1. Process only a PDF the operator supplied or explicitly authorized.
2. For a temporary-host landing page, inspect the page and follow its displayed download link. Do not guess private URLs or bypass controls. `download_authorized_pdf.py` accepts a direct authorized link, enforces a size cap and PDF magic, and records URL/size/SHA-256.
3. Copy the original into `uploads_backup_original/`; never mutate it.
4. Never put API keys in source, prompt files, HTML, logs, shell history, or published skills. Provider JSON names **environment variables**, not secret values. Set secret files to mode `0600`.
5. Network-assisted editing is opt-in. Extraction, rendering, normalization, build, and QA are local.
6. Keep caches so interrupted large jobs resume. Never cancel an in-flight API request; back off and retry or rotate provider after completion/failure.

## 1. Preflight and environment

Required binaries:

```bash
sudo apt-get install poppler-utils tesseract-ocr tesseract-ocr-fas tesseract-ocr-eng
python -m pip install pymupdf beautifulsoup4 pillow
python scripts/preflight.py
```

Why both Poppler and PyMuPDF: PDFs differ. PyMuPDF often gives better logical extraction; `pdftotext -layout` preserves layout clues. Poppler also renders stable page evidence. Tesseract supplies an independent OCR signal.

## 2. Intake measurements — never assume

Run `pdfinfo`, record page count, page size, encryption, PDF version, and SHA-256. Extract a first-lines-per-page diagnostic. Watch for:

- a leading blank form-feed that shifts text by one page;
- a missing final page;
- image-only or mostly diagrammatic slides;
- duplicate OCR words/lines;
- mixed Persian/Arabic letters and digits;
- English labels embedded in Persian layout;
- rotated pages, watermarks, repeated headers, and page numbers.

`extract_dual_ocr.py` verifies that extracted records equal the measured PDF page count. If whole-document form-feed splitting disagrees, it falls back to page-by-page extraction.

## 3. Dual OCR and evidence rendering

For every page retain:

- logical/raw text (PyMuPDF or Poppler);
- Tesseract `fas+eng` text from a 160–220 DPI grayscale page;
- compact display JPEG (typically 72–96 DPI, quality 55–70);
- normalized versions for search/comparison;
- page number and image path.

A practical quality/size pair used successfully:

```bash
python scripts/extract_dual_ocr.py input.pdf --out work/extraction \
  --ocr-dpi 180 --display-dpi 82 --jpeg-quality 60 --workers 4
```

The OCR render is temporary and high resolution. The display render is compact. This avoids bloating a self-contained HTML while preserving a legible source-page reference.

## 4. Persian normalization — display and search are separate

Display normalization:

- Unicode NFKC;
- Arabic `ي/ك` → Persian `ی/ک`;
- remove directional embedding controls but preserve ZWNJ (`U+200C`);
- normalize whitespace and paragraphs;
- optionally convert digits to Persian;
- remove only measured repeated watermarks/page numbers.

Search normalization uses the **same function for query and haystack**, maps both digit styles to a common form, treats ZWNJ like a space, lowercases Latin, debounces input, and caps highlights.

Do not normalize scientific names destructively. Keep Latin binomials, genes, proteins, drug names, and abbreviations where technically appropriate.

## 5. Multi-model reasoning-team reconstruction

### 5.1 Primary pass

Batch roughly 4–6 pages. Give each model:

- page number;
- logical extraction;
- independent Tesseract OCR;
- strict instruction to preserve all recoverable content;
- JSON schema `page,title,text`.

Rotate providers so one model does not dominate every page. Validate exact page sets, nonempty text, and JSON before caching.

### 5.2 Independent proof pass

Batch roughly 8–12 reconstructed pages. Send the primary draft to a **different** model and request correction only: science, language, punctuation, title, residual OCR. Preserve content and page count. If review fails validation, retain the primary rather than accepting a partial response.

### 5.3 Output-size and API failure tricks

- cache every successful batch;
- exponential backoff on `429/5xx`;
- provider rotation on validated failure;
- if a large JSON response fails or truncates, split the requested sections into two smaller calls and recombine;
- accept outputs only after schema/count/reference validation;
- never log request headers or key values;
- never label raw OCR as corrected AI text.

### 5.4 Manual adjudication

Even two models can miss image-only covers, end slides, figure labels, or titles. Inspect rendered pages for:

- blank/very short corrected units;
- placeholder titles such as `سند 145`;
- residual URLs, bidi controls, replacement characters, stray comparator signs;
- unexplained Latin fragments;
- altered scientific names or digits.

Manually repair only from rendered evidence and record the change.

## 6. Session detection and source map

Do not infer session boundaries solely from page counts. Use three signals:

1. PDF table of contents;
2. candidate cover pages containing جلسه/استاد/ترم/نویسنده;
3. abrupt topic/title transitions.

`detect_session_candidates.py` produces candidates, not authoritative boundaries. Review them and create `sessions.json`. Every enrichment reference is constrained to its session’s `start..end` range.

## 7. Educational enrichment, grounded and reviewable

Keep enrichment outside source `<pre>`. For each session generate and independently review:

- comparison/diagnostic tables;
- flashcards;
- mnemonics;
- high-yield review points;
- four-option quizzes;
- clinical or laboratory scenarios.

Every item links to a source unit. Every question has exactly four options, one answer letter, explanation, and valid reference.

### Balanced mode

One table, four flashcards, one mnemonic, four review points, two quiz questions, one scenario per session.

### Maximum mode

Three tables, ten flashcards, four mnemonics, ten review points, five quiz questions, and four scenarios per session. This can yield hundreds of components while staying session-grounded.

Run:

```bash
python scripts/reasoning_team_enrich.py work/corrections/final.json work/sessions.json \
  --providers providers.json --out work/enrichment --maximum
```

After integration, deduplicate normalized captions/questions/titles/review text. More content is useful only if it is distinct and traceable.

## 8. Offline-first HTML shell

The builder creates:

1. search;
2. overview/session map;
3. teaching/source units;
4. comparison tables;
5. flashcards;
6. mnemonics;
7. review summary;
8. mini-exam;
9. scenario bank.

Each source unit is a foldable, deep-linkable article with previous/index/next navigation. Text is explicitly `dir="rtl" lang="fa"`. Page images are lazy-loaded and, by default, embedded as Base64 data URIs so the HTML is one offline file.

The shared shell includes dark mode, reduced motion, focus states, skip link, sticky navigation, responsive tables, print behavior, search normalization, fold controls, score persistence, answer explanations, and to-top control.

For very large PDFs, compact JPEGs prevent runaway HTML size. If the single file is still too large, use `--linked-images` and package the local image directory with the HTML.

## 9. Fidelity and QA

Run both kinds of audit:

```bash
python scripts/fidelity_audit.py work/extraction/evidence.json \
  work/corrections/final.json --out work/fidelity.json
python scripts/qa_gates.py work/studyguide.html --expected-pages 378
```

Fidelity metrics are diagnostic, not semantic proof. Low coverage/order pages require visual adjudication. Digit drift must be checked against the rendered page.

QA gates verify:

- measured source-unit/image counts;
- unique IDs and resolving fragments;
- four-option/one-answer/reference question contracts;
- local or embedded images;
- balanced table columns;
- no external browser loads;
- no replacement/bidi artifacts;
- no exact duplicate tables/cards/mnemonics/questions/scenarios;
- JavaScript syntax when Node is available;
- displayed counters equal measured counts.

Never claim “complete,” “all pages,” or “QA pass” unless these claims were measured.

## 10. Packaging

Create a fresh ZIP only after QA. Exclude PDFs by default unless the operator explicitly requests them. Verify archive membership and CRC, then write SHA-256:

```bash
python scripts/verify_zip.py work work/final-studyguide.zip
```

Keep `extraction_manifest.json`, `reasoning_report.json`, `fidelity.json`, QA output, session manifest, and change report with the deliverable.

## 11. Practical finish checklist

- [ ] Authorized source backed up and hashed
- [ ] Page count measured
- [ ] Dual OCR evidence for every page
- [ ] Compact source image for every kept page
- [ ] Primary + independent proof pass complete
- [ ] Image-only and placeholder-title pages manually adjudicated
- [ ] Every teaching unit explicit RTL
- [ ] Sessions reviewed, not guessed
- [ ] Enrichment outside source corpus and source-linked
- [ ] Exact duplicates removed
- [ ] Question/table contracts pass
- [ ] Search, theme, folds, quiz, deep links, print tested
- [ ] Hero/section/footer counts measured and synchronized
- [ ] Fresh verified ZIP + SHA-256 produced
- [ ] Flashcard answers verified against source pages (`verify_flashcards.py`)

## 12. Robust Persian JSON contracts (v1.3.0)

Free-tier providers regularly break the strict JSON contract in ways that the
1.2.x validator treated as hard failures, silently discarding otherwise-valid
content. `scripts/common.py` now exports shared coercers used by enrichment,
the HTML builder and QA gates:

- `coerce_ref(value, start, end)` — clamps page references given as ints,
  floats, or strings like «صفحهٔ ۳» (Persian digits translated) into the
  session range; never raises.
- `coerce_answer(value)` — maps «الف/ب/ج/د», «۱–۴» and A–D to `A`–`D`.
- `is_bare_answer(value)` — flags empty/letter-only answers.
- `strip_option_prefix(text)` — removes duplicate «الف) » prefixes so the
  shell's own A–D labels do not repeat.

`reasoning_team_enrich.validate()` now accepts a bare JSON array, coerces refs
and answers, accepts well-formed subsets (no under-count failure), drops
bare-letter flashcards, and retries quiz/scenario sections with a focused pass
when the combined `--maximum` schema is truncated by a smaller provider. The
prompt contract explicitly requires integer `ref` and A–D `answer` values.

After enrichment, run the independent verification pass:

```bash
python scripts/verify_flashcards.py work/corrections/final.json work/enrichment/all.json \
  --providers providers.json --out work/enrichment/all.verified.json
```

It sends each suspicious flashcard (bare answer or «کدام…» multiple-choice
phrasing) to a different model than the generator, which confirms, corrects, or
marks it undeterminable; undeterminable cards are dropped rather than invented.
Pass the verified file to the builder. Two new QA gates
(`flash-no-bare-answer`, `quiz-options-no-letter-prefix`) fail the build if any
bare-letter answer or duplicated option prefix survives.

If a provider still returns 402/403 (payment/forbidden), that failure is not
retried by design; the caller rotates to the next provider. Treat automated
fidelity scores and answer verification as diagnostics, not semantic proof.

## 13. Running on any model, from any agent (v1.5.0)

v1.3 assumed you had a `providers.json` and a Gemini-or-OpenAI endpoint. v1.4.0
assumes nothing. The rules below are the production method for keeping results
consistent when the model or the driving agent changes.

### 13.1 Always start from `doctor`, never from assumptions

```bash
python3 scripts/forge.py doctor
```

It reports binaries, python modules, tesseract languages, every provider it
discovered and where each came from. `extraction_ready` and `model_ready` are
independent: you can extract with no model, and you can run the model stages on
a machine without Poppler. Act on what it says rather than guessing.

### 13.2 Provider resolution — let the environment win

Order: `--providers` file → environment keys → local runtimes
(`OLLAMA_HOST`, `LOCAL_OPENAI_BASE_URL`) → `FORGE_MOCK=1`.

In practice: **do not ship a `providers.json` with a job.** The host agent
already has a key; auto-discovery finds it, and the job stays portable. Use a
config file only to pin a specific model, force an ordering, or reach a private
endpoint.

Confirm what will actually be used, cheaply:

```bash
python3 scripts/model_adapters.py --list
```

### 13.3 Probe before a long job

A 378-page deck is a bad place to discover that a model was retired last week.

```bash
python3 scripts/forge.py compat --out compat.json
```

One cheap round-trip per provider records reachability, JSON discipline,
Persian round-trip, latency and learned quirks. `verdict: READY` means at least
one provider can satisfy the contract. Real findings from this exact command
during development: Gemini had retired `gemini-2.5-flash` (the replacement was
adopted automatically), Mistral rejects `seed` with HTTP 422, and three
providers were out of credit — all before a single page was processed.

### 13.4 Choose a determinism level deliberately

| Need | Command | Cost |
|---|---|---|
| Fast draft | `enrich --maximum` | 1 call/session |
| Reproducible structure | default (temp 0, seed, canonical JSON) | 1 call/session |
| Cross-model agreement | `enrich --maximum --consensus 3` | 3 calls/session |
| Hallucination-resistant | `enrich --maximum --consensus 3 --min-votes 2` | 3 calls/session, fewer items kept |
| No network at all | `FORGE_MOCK=1` | 0 calls, placeholder content |

`--min-votes 2` is the important one for medical or exam material: an item
survives only if two independent model families produced it from the same page.
Expect it to reduce volume; that is the point.

### 13.5 Reading `finish_reason: length`

Truncation is surfaced, not hidden. When you see
`[forge] truncated response provider=… chars=…`:

1. the valid prefix has already been salvaged (brackets auto-closed);
2. missing quiz/scenario sections are automatically re-asked in a focused pass;
3. if it recurs on the same provider, that model's output ceiling is too low
   for `--maximum` on your session size — shorten sessions or drop that
   provider with `--only`.

### 13.6 Cache hygiene

`~/.cache/persian-pdf-studyguide-forge/` (override with `FORGE_CACHE_DIR`)
holds two things:

- `responses/` — completions keyed by a hash of dialect+model+prompt+params.
  This is what makes re-runs free and byte-identical.
- `capabilities.json` — learned provider quirks and model renames.

Neither contains credentials. **Delete `responses/` when you change the source
PDF or want genuinely fresh generations**; deleting `capabilities.json` merely
costs one retry per quirk to relearn.

### 13.7 Driving it from another agent

Whatever the runtime, the contract is the same: `python3 scripts/forge.py
<command>`, one JSON document on stdout, logs on stderr, stable exit codes.

- **Parse stdout only.** Never scrape stderr or log lines.
- **Branch on the exit code**, not on message text.
- **Honour the pause.** `run` without `--auto-sessions` returns
  `status: PAUSED_FOR_SESSION_REVIEW` with exit 0. That is a request for human
  review of session boundaries, not a failure. Auto-accepting marks the guide
  unreviewed and that mark must survive into whatever you publish.
- **Re-invocation is safe** — every stage caches.

MCP hosts mount `integrations/mcp_server.py`; tool-calling models use
`integrations/tool-spec.json`; Python frameworks import
`integrations/adapters.py`. See `integrations/README.md`.

### 13.8 CI

```bash
FORGE_MOCK=1 python3 scripts/forge.py selftest
```

Eight checks, full unit suite, no keys, no network, about a second. Run it on
every change to the skill and before every publish.
