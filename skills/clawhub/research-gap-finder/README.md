# 🔍 Research Gap Finder

**Category:** research, knowledge

## ✨ What This Skill Does

Teaches an AI agent — or a researcher — a complete, reproducible method for finding
**genuine research gaps** in the scientific literature. It distills 100 curated resources
(gap-identification frameworks, AI/citation tools, academic databases, bibliometric mining,
and advanced strategies) into one pipeline: gather evidence → map the citation landscape →
run semantic "what is unstudied?" queries → classify each gap with a six-type taxonomy →
rank importance with a five-dimension rubric → verify novelty → output a citation-backed
gap report with a candidate research question per gap.

## 🔐 Permissions & Requirements

- Runtime: `python3` and `curl` (for key-free scholarly APIs) are sufficient for the
  automated core.
- Network: outbound HTTPS to scholarly APIs (Semantic Scholar, Crossref, OpenAlex, Europe PMC,
  PubMed E-utilities, arXiv) and — interactively — to the browser-based tools listed in
  `SKILL.md` (Litmaps, ResearchRabbit, Connected Papers, Elicit, SciSpace, Consensus, Scite,
  Inciteful, Dimensions, Google Scholar, Google Patents).
- Accounts: Elicit, SciSpace, Scite, Dimensions, Consensus and most citation-mapping tools
  require user accounts (some paid). No API keys are bundled; users supply their own.
- No filesystem writes beyond the evidence-matrix/notes the user asks to create.

## 🔒 Security & Privacy

- What it reads/collects: bibliographic metadata, abstracts, and citations you query; any
  papers you ask it to analyze.
- Does data leave the machine? Queries are sent to the scholarly APIs/tools you direct it
  to. No data is uploaded to any server beyond those queries.
- No secrets are read, stored, or logged by this skill; it never asks for or persists
  passwords/API keys.
- Known risks: citation-mapping tools are largely browser-based (no public APIs) — driving
  them programmatically may violate their terms of service; use only as permitted. AI-summarised
  "gaps" can be wrong — the skill enforces confidence labels and citation verification.
- Mitigations: honesty rules (zero-invented citations, DOI/Crossref verification, confidence
  caps) are built into the workflow.
- Review before install: read `SKILL.md` and `resources.md` — they are self-contained.

## ✅ Verification Hash

Installers can verify this skill matches the published artifact by hashing the skill files
and comparing to the digests below:

- **SKILL.md SHA-256:** `21e51a107c24e730813a204c6bead588751dabbe89ca10e43b5f8a1d28d73941`
- **resources.md SHA-256:** `2561a16913934759535c896409ae8cb6de2b56a16de0df19b91bbed0337f913c`

Verify locally:

```bash
sha256sum SKILL.md resources.md
# compare the output to the SHA-256 values above.
```

---
*Authored with the repo's AI reasoning team (6 models drafting in parallel, 4 reviewing) and published under the Skill Publishing Standard — see SKILL_PUBLISHING_STANDARD.md.*
