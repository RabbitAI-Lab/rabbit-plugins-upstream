---
name: literature-deep-read-report
description: This skill should be used when a user provides an academic paper (PDF file, DOI, arXiv link, or title) and asks for a structured deep-read report or literature summary. It extracts and organizes the study into seven required components: background, variables, paradigm/method, task flow, design details, statistical analysis, and main results. Trigger on phrases such as "精读这篇论文", "做一份文献精读报告", "分析这篇文章的方法与设计", "总结这篇研究", "summarize this paper", or "deep-read report".
---

# Literature Deep-Read Report

## Overview

This skill converts a research paper into a reusable, seven-part deep-read report that a graduate student, reviewer, or researcher can file and cite. It enforces a consistent scaffold — background, variables, paradigm/method, task flow, design details, statistical analysis, main results — so nothing critical is missed and papers become comparable across a reading list. The skill reads the actual paper text; it does not invent findings.

## When to Use

Activate this skill when the user:

- Attaches or links a paper (PDF, DOI, arXiv, PubMed, or journal URL) and asks for a "精读", "文献报告", "深度总结", or "deep-read".
- Asks to extract a study's method, variables, design, or results for a literature review.
- Says "分析这篇论文的设计/统计/范式" or "帮我整理这篇文献".
- Wants a comparable one-page-per-paper note for a reading list.

Do not activate for: pure citation formatting, plagiarism checks, or non-academic documents. If the user only wants a one-line summary, still deliver the full scaffold but keep each section brief.

## Execution Logic

### Step 1 — Acquire the paper text

Resolve the input in this priority order:

1. Local PDF path → extract text (try a PDF text tool; if unavailable, ask the user to paste the text).
2. DOI or arXiv/PubMed link → fetch the abstract and, if open access, the full text.
3. Title only → search the web for the PDF/abstract and confirm with the user before proceeding.

If the full text is not obtainable, build the report from the abstract + available sections and explicitly mark missing parts as "全文未获取，以下基于摘要与公开信息".

### Step 2 — Parse the structure

Map the paper's real sections (Introduction, Methods, Results, Discussion) onto the seven required components. Do not force a mismatch — if a component is genuinely absent, say so.

### Step 3 — Extract each component

Use the scaffold in `references/deep-read-template.md` and fill:

- **背景 (Background):** the gap, research question, and why it matters.
- **变量 (Variables):** independent, dependent, moderators/mediators, control variables, and how each was measured.
- **范式方法 (Paradigm / Method):** the overarching paradigm (e.g., RL + DDM computational modeling, fMRI, survey, experiment) and the modeling or analytical approach.
- **任务流程 (Task Flow):** the participant's step-by-step experience in the experiment or the pipeline of the analysis.
- **设计细节 (Design Details):** design type (between/within), sample size, stimuli, trials, counterbalancing, software, parameters.
- **统计分析 (Statistical Analysis):** tests used, models, corrections, power, and what each test answered.
- **主要结果 (Main Results):** the key findings with effect sizes / estimates and their interpretation.

### Step 4 — Render and verify

Output the seven-section report in markdown. Quote exact numbers from the paper (with section/page if possible). Add a one-line "一句话贡献" at the top and a "局限与可复现性" note at the end. If any extracted claim is uncertain, flag it.

## Output Structure

The report must contain these seven headings (in this order), prefixed by a one-line contribution:

0. **一句话贡献 (One-line Contribution)**
1. **背景 (Background)**
2. **变量 (Variables)**
3. **范式方法 (Paradigm / Method)**
4. **任务流程 (Task Flow)**
5. **设计细节 (Design Details)**
6. **统计分析 (Statistical Analysis)**
7. **主要结果 (Main Results)**
8. **局限与可复现性 (Limitations & Reproducibility)**

A filled template and a worked computational-modeling example are in `references/deep-read-template.md`.

## Reliability Rules

- Quote the paper; never hallucinate statistics, p-values, or sample sizes.
- Mark every inferred (non-explicit) claim as "推断".
- If the text is unavailable, state it and degrade gracefully to an abstract-based report.
- Preserve the authors' original terminology for variables and methods; add Chinese glosses in parentheses.

## Resources

- `references/deep-read-template.md` — the seven-section scaffold with per-section extraction prompts and a worked example.
