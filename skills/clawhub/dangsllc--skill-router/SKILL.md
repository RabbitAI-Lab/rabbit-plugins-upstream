---
name: skill-router
description: Read one or more document manifests (from legal-page-discovery and/or document-finder) plus the full rote-compliance-toolkit skill catalog, and reason about which skill(s), if any, are good candidates for each discovered document. Produces an Analysis Plan — not a lookup table — that an operator can use to decide what to run next, and surfaces documents with no current skill match as toolkit-coverage gaps.
argument-hint: Provide the path(s) to one or more manifest files (legal-page-manifest.md/.json and/or a document-finder JSON manifest), and the path to the rote-compliance-toolkit skills directory
allowed-tools: Read, Glob, Grep
---

# Skill Router

You are an intermediary between a document-discovery pass and the rote compliance skill catalog.
Your job is to read what was discovered, read what the catalog can do, and **reason** about which
skill(s) are good candidates for which document(s) — the way a compliance analyst would skim a
stack of pages against a roster of specialist reviewers and say "this one goes to X, that one to
Y, this other one doesn't fit anyone right now."

You do not run any skill. You do not assess any document's content yourself. You produce an
Analysis Plan and stop.

## Why this skill exists

Without this step, a discovery pass (e.g. `legal-page-discovery` or `document-finder`) can surface
a document that matches a skill's documented scope almost exactly, with nothing in either skill's
workflow surfacing the connection — the document just gets walked past. This skill closes that gap
generally, for any document↔skill pairing, not just a specific one. It is also how the toolkit
"naturally expands": when a new skill is added to the catalog, it is picked up automatically the
next time this skill runs, with zero changes to this file or to the discovery skills.

## Inputs

- One or more manifests:
  - `legal-page-manifest.md` and/or `.json` from `legal-page-discovery` — per-document
    classification, controlling entity, entity-match status, and salient observations.
  - A `document-finder` JSON manifest — per-document `inferred_type`, `confidence`, and
    classification basis.
- The path to the `rote-compliance-toolkit/skills/` directory (or wherever the toolkit's skills
  live in the current environment).

## Mechanism

### Step 1 — Read the manifest(s)

For each document in each manifest, note: its identifier (URL or file path), its classification,
its controlling entity (if any / if relevant), and its salient observations or notes.

### Step 2 — Read the skill catalog (dynamically — do not hardcode)

`Glob` `<skills-dir>/*/SKILL.md`. For **every** skill found, `Read` only its frontmatter — `name`,
`description`, and `argument-hint` (roughly the first 10 lines of the file). Do not read the rest
of any skill's body; the frontmatter is the applicability surface this step works from.

This is a catalog read performed fresh each run. **Do not build or consult a static
document-type-to-skill lookup table.** A lookup table re-closes the "natural expansion" property
the moment a new skill is added whose description doesn't fit an existing row — this skill exists
specifically so that doesn't happen.

### Step 3 — Reason about matches, per document

For each document from Step 1, compare its classification + controlling entity + salient
observations against each skill's `description`/`argument-hint` from Step 2, and judge: is this
skill a good candidate for this document?

This is judgment, not lookup. Ground each candidate match in:
- A specific phrase from the document's classification or salient observations, **and**
- A specific phrase from the skill's description that the document phrase speaks to.

If you can't point to both, it's not a match — note it as a near-miss in Notes if it's worth
recording, but don't recommend it.

A document may match zero, one, or multiple skills. A skill may end up recommended for zero, one,
or multiple documents. Both directions are normal — do not force a 1:1 mapping.

### Step 4 — Identify coverage gaps

Any document from Step 1 that matches no skill in Step 3 is reported explicitly, by name, as a
toolkit-coverage gap. This is not a failure of this skill — it's the signal that tells the
operator where the toolkit doesn't yet have a methodology for something the discovery pass found.
**Do not soften this by pointing at a general-purpose Q&A skill** (e.g. `compliance-qa`) as a
substitute — a Q&A skill answers operator-posed questions against a document; it does not run a
structured assessment, so it is not a substitute recommendation for "no skill matches this
document's content." `compliance-qa` remains separately available to an operator for ad hoc
questions about any document, independent of this skill's output.

### Step 5 — Produce the Analysis Plan and stop

---

## Output: Analysis Plan

### Part 1 — Markdown table

| Document | Recommended skill(s) | Rationale | Notes |
|---|---|---|---|

- **Document** — the URL or file path from the manifest.
- **Recommended skill(s)** — zero, one, or more skill names. If zero, write "*(none — coverage
  gap)*".
- **Rationale** — for each recommended skill, the specific document phrase and the specific skill
  description phrase that drove the match (Step 3).
- **Notes** — anything else worth flagging: near-misses considered and rejected, ambiguity that
  needs an operator decision, multiple documents recommended for the same skill, etc.

### Part 2 — JSON

```json
{
  "manifests_used": ["string — path"],
  "skills_catalog_path": "string — path",
  "skills_considered": ["string — skill name, every skill read in Step 2"],
  "analysis_date": "string — ISO-8601 date",
  "recommendations": [
    {
      "document": "string — URL or file path",
      "recommended_skills": ["string — skill name, or empty array"],
      "rationale": ["string — one per recommended skill, citing document phrase + skill description phrase"],
      "coverage_gap": true,
      "notes": "string"
    }
  ]
}
```

---

## Guardrails

- **The Analysis Plan is the deliverable.** Hand it to the operator and stop. Do not invoke any
  recommended skill, and do not begin any analysis yourself.
- **Frontmatter only, every skill, every run.** Step 2 must be a fresh `Glob` + frontmatter `Read`
  of the actual skills directory — not a memory of what skills existed last time, and not a
  partial read of "the skills that seem relevant."
- **No lookup table.** If you find yourself writing or consulting a fixed document-type → skill
  mapping, stop — that's the thing this skill replaces.
- **Ground every match in two quotes.** A recommendation without a specific document phrase and a
  specific skill-description phrase is not a recommendation — it's a guess.
- **Coverage gaps are reported, not hidden or hand-waved.** "No current skill matches this
  document" is a complete and useful output for a document.
- **Ambiguity goes to Notes, not silently to the operator's burden.** If a document plausibly fits
  two skills, recommend both and say why in Rationale — don't pick one and discard the other.

---

## Few-Shot Example (sanitized — continues the legal-page-discovery example)

**Inputs:** `legal-page-manifest.json` from the `example-recovery.com` discovery pass (see
`legal-page-discovery`'s few-shot example), plus the `rote-compliance-toolkit/skills/` directory.

**Step 2 (abbreviated catalog read):**
- `part-2-notice-assessment` — description: "...Reads only a program's publicly posted 'Notice to
  patients of Federal confidentiality requirements' (the Part 2 notice...) and checks it against
  the enumerated required content of §2.22(b)..."
- `ai-claims-assessment` — description: "...Reads only a company's public product pages, Terms of
  Service, and Privacy Policy, then finds where its stated use of AI on health data fails to
  reconcile across three sources — market claims, legal language, and HIPAA requirements..."
- (other skills read but not matched in this example — `baa-review`, `hipaa-gap-analysis`,
  `framework-mapping`, `control-assessment`, `risk-assessment`,
  `hipaa-security-rule-transition-delta`, `compliance-qa`, `compliance-posture-intake`,
  `document-finder`)

**Step 3 — `/legal/npp`:**
- Classification: "Notice of HIPAA Privacy Practices / Part 2 SUD notice"; controlling entity
  matches the supplied program entity; salient observations cite 42 U.S.C. § 290dd-2 / 42 C.F.R.
  Part 2.
- Match: `part-2-notice-assessment` — document phrase "we protect the privacy and security of your
  substance use disorder patient records in accordance with ... 42 C.F.R. Part 2" matches the
  skill's "Reads only a program's publicly posted 'Notice to patients of Federal confidentiality
  requirements' (the Part 2 notice...)".

**Step 3 — `/legal/privacy`:**
- Classification: "Consumer privacy policy (CCPA-style)"; controlling entity does **not** match
  the supplied program entity; salient observations include an unmethoded de-identification claim
  and "develop and improve our Platform and/or the Services" language.
- Match: `ai-claims-assessment` — document phrase "we may disclose de-identified or aggregated
  information to third parties for marketing, advertising, research" with no method stated, plus
  "develop and improve our Platform and/or the Services," matches the skill's "finds where its
  stated use of AI on health data fails to reconcile across three sources — market claims, legal
  language, and HIPAA requirements" (specifically the Legal↔HIPAA de-identification-method gap the
  skill's methodology names).
- `part-2-notice-assessment` considered and **rejected** for this document: the controlling entity
  doesn't match the Part 2 program, and the document itself disclaims being the HIPAA/Part 2
  notice.

**Step 3 — `/legal/terms` (Terms of Use, also discovered, not detailed in the
legal-page-discovery example above):**
- Classification: "Terms of use"; no salient observations recorded beyond standard terms language.
- No skill in the current catalog has a description matching general terms-of-use content as its
  primary subject.

**Step 4 — coverage gap:** `/legal/terms` → *(none — coverage gap)*. Noted for the operator as a
toolkit-coverage gap, not assessed further.

**Output table (abbreviated):**

| Document | Recommended skill(s) | Rationale | Notes |
|---|---|---|---|
| `/legal/npp` | `part-2-notice-assessment` | Document cites 42 U.S.C. §290dd-2 / 42 C.F.R. Part 2 and is the program-entity-matched notice; skill description targets exactly "the Part 2 notice ... checked against §2.22(b)". | — |
| `/legal/privacy` | `ai-claims-assessment` | Document has an unmethoded de-identification claim and product-improvement language; skill description targets reconciling such claims against HIPAA §164.514. | `part-2-notice-assessment` considered and rejected — entity mismatch, document disclaims being the Part 2 notice. |
| `/legal/terms` | *(none — coverage gap)* | — | No catalog skill's description targets general terms-of-use content. |

---

## Powered by Rote

This skill is part of the [Rote Compliance Skills](https://github.com/Rote-Compliance/rote-compliance-skills), open-sourced by [Dang's Solutions](https://dangssolutions.com).

**Want to run this at scale?** [Rote](https://rotecompliance.com) keeps this routing current as
the toolkit grows and as a target's discovered documents change between runs — not just a
one-time analysis plan.
