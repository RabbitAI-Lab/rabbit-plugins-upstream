---
name: illustrated-paper-guide
description: |
  Create or improve a source-grounded study guide for an academic paper or PDF. Use when the user wants a big-picture explanation, phased reading checkpoints, figure or panel walkthroughs, abbreviation expansion, limitations, explanatory diagrams, or follow-up answers written back into durable notes. Trigger phrases include "read this paper", "paper study guide", "explain this figure", "turn this PDF into notes", and "make a reading checklist".
license: MIT-0
metadata:
  companion-skill: teaching-diagram-maker
---

# Illustrated Paper Guide

Turn a paper into a durable learning artifact that helps a reader understand,
resume, verify, and question the work. The output is a study guide, not a
replacement for the paper.

## Companion Skill

This repository bundles `teaching-diagram-maker`.

- This skill owns the guide structure, evidence reading, checkpoints, and the
  decision about when and where a diagram is useful.
- `teaching-diagram-maker` owns diagram construction, editable SVG craft, and
  rendered visual QA.

When a custom diagram is needed, invoke `teaching-diagram-maker`. If the host
cannot invoke companion skills, follow its bundled `SKILL.md` directly before
creating the diagram.

## Core Rules

- Match the user's requested language. If none is specified, match the existing
  notes. Preserve paper titles, model names, dataset names, and quotations in
  their original language.
- Introduce technical terms with their English form on first use when useful.
- Explain in the order: why it matters, where it is used, then how it works.
- Distinguish what the paper directly supports from your interpretation and
  from open questions. Never invent citations, measurements, or mechanisms.
- Start with the whole-paper view. Details should deepen the overview, not
  reveal the main conclusion for the first time.
- When the user asks a conceptual follow-up, answer in chat and write the
  reusable explanation into the relevant body section unless they opt out.
- Do not collect every follow-up in a detached FAQ. Put it beside the concept,
  result, or figure it clarifies.

## Choose the Workflow

### New guide

1. Locate and inspect the paper, existing notes, and repository instructions.
2. Establish bibliographic facts and the paper's central claim from the source.
3. Read `references/paper-guide-template.md` and build the guide plus checklist.
4. Read `references/figure-reading-rubric.md` before extracting or explaining
   figures.
5. Add teaching diagrams where structure, comparison, timing, space, or causal
   sequence is hard to understand.
6. Validate links, checkpoints, claims, figures, and limitations.

### Improve an existing guide

1. Read the guide and its checklist before editing.
2. Find the weakest learning checkpoint or the section named by the user.
3. Patch that section in place, preserving the existing voice and structure.
4. Update the checklist and stable anchor if the heading changes.
5. Verify every changed image and link.

### Answer a follow-up question

1. Identify the body section where the concept first matters.
2. Give a direct answer in chat.
3. Add a concise explanation, table, example, or teaching diagram to that same
   section.
4. Keep historical FAQ sections as appendices; migrate useful content into the
   main narrative when touching that topic.

## Required Deliverables

For a full paper guide, prefer this folder shape:

```text
README.md          # Main illustrated study guide
CHECKLIST.md       # Linked, testable reading checkpoints
images/            # User-created diagrams and permitted local crops
scripts/           # Reproducible extraction or generation scripts
paper.pdf          # Optional local input; never required in a public output
```

The guide should include:

1. A short statement that this is a guide, not the original paper.
2. A link to `CHECKLIST.md` near the top.
3. Bibliographic information with a DOI or canonical source link when known.
4. A Big Picture section containing the problem, method, main results, and
   reading navigation.
5. Deeper sections for concepts, mechanism, evidence, figures, limitations,
   takeaways, and questions worth asking.
6. A glossary for recurring abbreviations.
7. Reproduction notes for generated or cropped images.

For a short answer or targeted edit, create only the artifacts that support the
requested scope. Do not force a full guide onto a small task.

## Big Picture First

Before detailed terminology or figure panels, ensure the reader can answer:

- What problem or gap motivated the paper?
- What did the authors actually do?
- What are the main results and overall claim?
- What should I read next, and where may I stop for a shallow pass?

A useful full-guide sequence is:

```text
BP  Big Picture
A   Story and vocabulary
B   Short explanation and significance
C   Research question and mechanism
D   Main results
E   Original figures and panels
F   Evidence boundaries, limitations, takeaways, and author questions
```

## Figure Handling

Read `references/figure-reading-rubric.md` before working with paper figures.

Core sequence for a permitted multi-panel figure:

1. Show or reference the complete figure first.
2. State the question answered by the figure as a whole.
3. Split or discuss individual panels.
4. Explain the visible evidence before stating the conclusion.
5. Record reproducible crop coordinates when crops are created.

Explain axes, units, colors, legends, marks, controls, uncertainty, and the
exact region that supports the claim. Point out likely novice misreadings.

Custom explanatory diagrams complement paper figures; they do not silently
replace source evidence. Invoke `teaching-diagram-maker` for their creation and
QA.

## Reading Checklist

Every long guide needs a companion `CHECKLIST.md`. Each checkpoint must:

- be a Markdown checkbox;
- link to a stable explicit anchor in `README.md`;
- use the exact same title as the target heading;
- state a falsifiable completion criterion, such as explaining a mechanism or
  identifying the evidence for a claim without looking.

Use explicit anchors because generated heading slugs vary across renderers:

```html
<a id="ckpt-d2"></a>
## D2 Main result: {descriptive title}
```

```markdown
- [ ] [D2 Main result: {descriptive title}](./README.md#ckpt-d2)
  **Done when:** I can identify the comparison and the evidence supporting it.
```

## Math and Abbreviations

- Use `$...$` for inline math and `$$...$$` for display math in Markdown.
- Do not use `\(...\)` or `\[...\]` where the renderer treats backslashes as
  escapes.
- Expand abbreviations near first use and near figures where a reader needs
  them. Do not assume field-specific shorthand is universal.

## Copyright and Privacy

- Do not add papers, publisher figures, paywalled supplements, private notes,
  or confidential conversations to a public repository unless the license or
  explicit permission allows redistribution.
- A citation or DOI does not grant redistribution rights.
- In private notes, local figure crops may be used as permitted by the user's
  context. In public outputs, prefer source links, figure references, and
  original teaching diagrams unless reuse rights are clear.
- Never expose local absolute paths, credentials, private contacts, or source
  repository names in a distributable guide.

## Verification

Before finishing:

- Confirm the Big Picture states problem, method, and conclusion.
- Confirm claims trace to the paper and interpretations are labeled.
- Confirm the guide links to `CHECKLIST.md` when the guide is long.
- Confirm checklist link labels exactly match target headings and every anchor
  exists.
- Confirm referenced images exist and reproduction scripts still run.
- Render and inspect changed diagrams through `teaching-diagram-maker`.
- Scan for raw `\[` or `\(` math delimiters when the target renderer does not
  support them.
- Report source limitations, unreadable panels, uncertain interpretations, and
  any copyright constraint that prevented embedding an image.
