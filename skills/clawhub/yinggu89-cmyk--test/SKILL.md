---
name: exam-review-webapp-builder
description: Build a multi-year interactive exam-paper practice and review webapp from a single-paper HTML engine plus exam source materials (DOCX, PDF, or screenshots). Produces one self-contained HTML with a name-login entry gate, a year/paper selection grid, per-question grading and evidence, vocabulary/long-sentence analysis, teacher vs student modes, a records dashboard with CSV export, optional local Node backend, and Cloudflare Pages + D1 deployment. Use when a user wants to create or extend a "高考/考试真题互动讲评" style website, add more years to an existing one, fix missing article text, or deploy it online.
agent_created: true
---

# Exam Review Webapp Builder

## Overview

Build and extend a single-file, multi-year interactive exam review webapp. The
app lets students enter their name, pick an exam year, practice questions with
per-question feedback and evidence, and have all activity recorded; teachers get
a records dashboard and can reveal answers/analysis. Everything ships in one
HTML file, with optional Node backend and Cloudflare deployment.

Use this skill when the user wants to: create such a webapp from source exam
materials; add another year to an existing one; debug why a paper shows questions
but no article; or deploy/prepare the site for Cloudflare.

## Architecture at a glance

```
paperYYYY.json × N   (one per year: passages + sections + questions)
        │  assemble.py  (deterministic string patching)
        ▼
single-file HTML engine template  ──►  merged webapp (one HTML)
        │                                  │
   assets/app_shell.*                 assets/server.js (optional local backend)
   (login gate, paper grid,              assets/cloudflare/* (optional D1 backend)
    records panel, toolbar)
```

- `assets/engine/template.html` — the single-paper interactive engine (renders
  passages/questions, answer key, translations, vocabulary, timer, annotation,
  teacher/student toggle, print).
- `scripts/build_paper_template.py` — copy to build each year's JSON.
- `scripts/assemble.py` — merges all years + injects the shell.
- `references/data_schema.md` — every JSON field and the critical invariants.
- `references/workflow.md` — full 7-phase procedure incl. extraction and testing.
- `references/deployment.md` — Cloudflare Pages / D1 and local Node backend.

## Workflow

Follow `references/workflow.md` in full for a new build. Summary:

1. **Identify the engine** — use the bundled `assets/engine/template.html`, or
   if the user supplies their own, confirm it has the `paper-data` block and the
   JS anchors the assembler patches.
2. **Extract** each source (DOCX/PDF/long image) to plain text. For images use
   the hi-res original, slice into ~760px segments, read each with the Read tool.
3. **Build** one `paperYYYY.json` per year from `scripts/build_paper_template.py`,
   following `references/data_schema.md`. Enforce: non-empty valid `passageId`
   on every question; article text in `passage.paragraphs`; answers match the
   official key (note source typos in `qualityNotes`).
4. **Verify** each JSON: no empty/dangling `passageId`, answers checked against
   the key. (`passageId` bugs are the #1 cause of "questions but no article".)
5. **Assemble** with `scripts/assemble.py` (CLI flags — see script header).
6. **Validate** statically: JSON parses, both JS blocks pass `node --check`,
   gate/hooks/student-mode markers present.
7. **Browser-test** with agent-browser + system Chrome CDP (see workflow.md),
   then clear test records.

## Adding a year to an existing webapp

1. Extract the new year's material and build its `paperYYYY.json`.
2. Re-run `scripts/assemble.py` with the new year added to `--years` (keep all
   existing years; order oldest→newest). The entry grid is generated from the
   JSON automatically, so no UI edits are needed.
3. Re-validate and browser-test that year specifically.

## Common fixes

- **Questions show but article text is missing** → a question's `passageId` is
  empty or wrong. Backfill it per section (reading A→`ra`, B→`rb`, C→`rc`,
  D→`rd`, gap→`gap`, cloze→`cloze`, grammar→`grammar`, writing→`w1`/`w2`), then
  reassemble. See `references/data_schema.md`.
- **PDF English words run together** → restore spaces manually during extraction.
- **Source answer key contradicts its own explanation** → trust the detailed
  explanation and add a note in `qualityNotes`.
- **Cloudflare root shows 404** → the uploaded file must be `index.html` and the
  project must be Pages (not a Worker). See `references/deployment.md`.

## Teacher vs student modes

The engine toggles a `student` class on `<body>`. The shell marks the whole-paper
answer button (`answerBtn`) with `.only-teacher` so it hides in student mode;
single-question reveal/evidence/analysis buttons are hidden by the engine's own
CSS. Submit/grading, translation, vocabulary, full-text check, method tips,
annotation, timer, print, paper switch and submit are available in both modes.
The records dashboard is for the teacher.

## Resources

- `scripts/assemble.py` — parameterised merge/injection script (CLI).
- `scripts/build_paper_template.py` — starting template for a year's JSON, with
  `P`/`V`/`Q`/`W` helpers, passageId backfill, glossary aggregation and checks.
- `assets/engine/template.html` — interactive engine to patch.
- `assets/app_shell.html` / `.css` / `.js` — entry gate, paper grid, records
  panel, toolbar buttons, localStorage + `/api` logging.
- `assets/server.js` — zero-dependency local Node backend.
- `assets/cloudflare/` — `log.js`, `records.js`, `schema.sql`, `wrangler.toml`.
- `references/data_schema.md`, `workflow.md`, `deployment.md`.
