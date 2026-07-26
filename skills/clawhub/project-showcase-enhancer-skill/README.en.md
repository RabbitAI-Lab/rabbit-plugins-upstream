<p align="center">
  <img src="./images/logo.svg" width="120" alt="Project Showcase Enhancer" />
</p>

<h1 align="center">Project Showcase Enhancer</h1>

<p align="center">
  <b>Evolve your demo-grade personal project into a commercial-grade product, and generate a project showcase document and an interview prep guide in one pass. A script gives a deterministic map; the model does deep semantic reasoning on top of it — a four-stage loop from reading code straight to interview readiness.</b>
</p>

<p align="center">
  🌐 <a href="./README.md">Bilingual</a> &nbsp;·&nbsp; 🇨🇳 <a href="./README.zh-CN.md">中文</a>
</p>

<p align="center">
  <img alt="WorkBuddy" src="https://img.shields.io/badge/WorkBuddy-Skill-00b4d8" />
  <img alt="Stages" src="https://img.shields.io/badge/stages-4%20phases-8b5cf6" />
  <img alt="Architecture" src="https://img.shields.io/badge/architecture-hybrid-10b981" />
  <img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen" />
  <img alt="Models" src="https://img.shields.io/badge/models-Opus%204.6%20%7C%20DeepSeek%20v4%20Pro%20%7C%20GPT--5.6-ff6b35" />
</p>

---

## What is this?

> **Project Showcase Enhancer** is a WorkBuddy skill. It is not a "scan the code and emit a template" tool. It is a **human-in-the-loop workflow**: first it reads your code and your original intent, then it works with you to evolve the demo into a commercial-grade product plan, and finally it produces two ready-to-use documents — a **project showcase document** and an **interview prep guide**.

It merges two distinct sources:

- From **code-project-analyzer** — the original script and ideas for code scanning and project documentation.
- From **JD + Resume → Interview Question Predictor** — the STAR framework and structured analysis method for JD + resume → interview questions.

The real pain point: you have a working personal project or demo, but you do not know how to **explain it clearly, write it professionally, or prepare for interviews about it**. The code runs, but the project description says only "a blog built with React + Node," with no way to surface the highlights; a demo is far from shippable yet you cannot say what is missing; you freeze when an interviewer asks why a technology was chosen.

This skill handles all three in one pass: **analyze code → evolve to commercial → generate showcase doc → predict interview questions**.

## Highlights

> **The scan script provides a deterministic map; the model does deep reasoning on that map — together they are both fast and accurate.** — the core design of this skill

- **Real code comprehension:** a script does a deterministic scan, then the model reads the key source files to understand business logic, module boundaries, and data flow — not guesswork from file names.
- **Demo-to-commercial evolution:** given your product vision, it lists gaps across functionality, engineering, and operations, then gives a phased roadmap (MVP → polish → commercial).
- **Project showcase document:** fills a template with highlights, feature modules, tech-stack rationale, architecture design, and deployment steps, formatted to drop straight into a portfolio site or README.
- **Interview prep guide:** given a JD and a resume, it predicts 15 project-specific interview questions (must-ask / targeted / follow-up), each with the point being tested, an answer strategy, and a STAR framework.
- **Hybrid architecture:** a script does the fast, stable scan; the model does the deep, accurate reasoning — balancing speed and quality while saving tokens.

## Get started

### Prerequisites

```bash
# 1. WorkBuddy client installed (this is a WorkBuddy user-level skill)
# 2. Recommended to run under a "high-reasoning model" (see Configuration)
#    Recommended: Claude Opus 4.6 / DeepSeek v4 Pro / GPT-5.6

# 3. (Optional) to parse resume files, install Python dependencies
pip install pdfplumber python-docx pypdf
```

### Install the skill

```bash
# Option 1: clone into the user-level skills directory
git clone https://github.com/whishi47/project-showcase-enhancer-skill.git \
  "$HOME/.workbuddy/skills/project-showcase-enhancer"

# Option 2: extract from the zip
#   Download project-showcase-enhancer.zip, extract to $HOME/.workbuddy/skills/project-showcase-enhancer/
#   Make sure SKILL.md sits directly inside that directory

# Option 3: install from SkillHub
#   Search for project-showcase-enhancer-skill on SkillHub and install it
```

> On Windows, `$HOME` is usually `C:\Users\your-username`. The skills directory may also be `.codebuddy\skills` depending on your client. No build step or dependency install is required; trigger the skill with plain language in a WorkBuddy conversation.

### Usage

| Trigger | Action | Result |
|---|---|---|
| 💬 Natural language | "Analyze my project" | Start skill, enter Stage 0 to collect info |
| 💬 Natural language | "Help me evolve this project to commercial grade" | Jump to Stage 2 commercial evolution |
| 💬 Natural language | "Generate a project showcase document" | Skip evolution, produce showcase doc |
| 💬 Natural language | "Prepare me for an interview on this project using my JD" | Enter Stage 4 prep |
| 📎 Resume file | Upload PDF / DOCX / TXT | Parsed to text for the interview-prep stage |

On first trigger, the skill asks four things at once (answer them together): **project path**, **use case** (resume / interview / GitHub / portfolio), **target role** (optional), **notes** (your original idea, points to emphasize).

## How it works

```
┌──────────────────────────────────────────────────────────┐
│             project-showcase-enhancer-skill                      │
│   Input: project dir + (optional) JD file + resume file    │
└───────────────────────────┬──────────────────────────────┘
                            ▼
   ┌──────────────────────────────────────────────┐
   │ ① Deep code comprehension                     │
   │   scripts/scan_project.js (dict scan → JSON)   │
   │   + model semantically reads key sources       │
   │   → code status profile (with 8-dim scoring)   │
   └──────────────────────┬───────────────────────┘
                           ▼
   ┌──────────────────────────────────────────────┐
   │ ② Commercial evolution (dialogue)             │
   │   vision → gap analysis (P0/P1/P2) → roadmap   │
   └──────────────────────┬───────────────────────┘
                           ▼
   ┌──────────────────────────────────────────────┐
   │ ③ Project showcase document                   │
   │   fill assets/showcase-template.md             │
   │   → {project}-showcase.md                      │
   └──────────────────────┬───────────────────────┘
                           ▼
   ┌──────────────────────────────────────────────┐
   │ ④ Interview perspective                        │
   │   JD + resume → 15 questions + STAR            │
   │   → {project}-interview-prep.md               │
   └──────────────────────────────────────────────┘
```

**Stage ① Deep code comprehension:** `scan_project.js` emits structured JSON in seconds (tech stack, dependencies, role-annotated directory tree, entry/config files, README text); the model then reads the key source files on top of this "map" — module boundaries, data flow, startup flow, third-party services from config, and original intent from the README; finally scores 8 dimensions (organization, type safety, security, deployability, error handling, test coverage, performance, documentation) 1–10 with file + line evidence.

**Stage ② Commercial evolution:** through dialogue, clarify target users, core selling point, business model (optional), MVP scope; list three gap types (functional / engineering / operations, each tagged P0/P1/P2); give a three-phase roadmap (MVP → polish → commercial).

**Stage ③ Deliverables:** fill `assets/showcase-template.md` with highlights, feature modules, tech-stack rationale, architecture, deployment; fill `assets/interview-prep-template.md` with 15 questions.

**Stage ④ Interview perspective:** given JD and resume, predict technical / project follow-ups an interviewer would ask; each outputs "what is tested → answer strategy → STAR framework".

## Four-stage reference

| Stage | Name | Input | Key action | Output |
|---|---|---|---|---|
| ① | Deep code comprehension | project dir | script scan + model read + 8-dim scoring | code status profile (JSON + scores) |
| ② | Commercial evolution | profile + your vision | gap analysis (P0/P1/P2) + roadmap | evolution plan |
| ③ | Project showcase doc | profile + plan | fill highlights / modules / stack / arch | {project}-showcase.md |
| ④ | Interview perspective | doc + JD + resume | 15 questions (must/targeted/follow-up) + STAR | {project}-interview-prep.md |

## Configuration

The skill requires a **high-reasoning model**. **Recommended:**

- Claude Opus 4.6
- DeepSeek v4 Pro
- GPT-5.6 (or equivalent)

A low-reasoning model still runs, but code comprehension will be shallow, commercial evolution generic, and interview predictions weak. At Stage 0 the skill prompts you to confirm the current model and suggests switching if it does not meet the bar.

> 💡 Tip: set your preferred high-reasoning model as the WorkBuddy default, or switch manually before triggering the skill, for the best results.

## Why this over alternatives?

| Aspect | This skill | Raw code-analyzer | Hand-written README | Raw interview-prep |
|---|---|---|---|---|
| Code comprehension | ✅ Script + model depth | ⚠️ File-name dict only | ❌ Manual | ❌ Not applicable |
| Demo→commercial evolution | ✅ Dialogue + roadmap | ❌ | ❌ | ❌ |
| Showcase doc quality | ✅ Tailored, evidence-based | ⚠️ Templated, generic | ⚠️ Depends on writing | ❌ |
| Interview prediction | ✅ Tied to this project's code | ❌ | ❌ | ⚠️ Generic JD only |
| Hybrid architecture (token saving) | ✅ | ❌ | — | ❌ |

**Where this fits:** you are not "replacing" code-project-analyzer or interview-prep — you are running all four steps (read code → evolve to commercial → write showcase → prep interview) in one pass. The scan script provides a deterministic map; the model does deep reasoning on it; the result is two documents you can actually show people.

## Bundled scripts

### `scripts/scan_project.js`

Scans a project with a hard-coded dictionary and emits structured JSON. It does not call a model, so it is fast and deterministic.

```bash
# Usage
node scripts/scan_project.js <project-directory>

# Example: analyze the current directory
node scripts/scan_project.js ./my-project
```

JSON fields:

| Field | Content |
|-------|---------|
| `techStack` | Tech stack grouped by runtime / framework / build / css / test / orm / deploy |
| `dependencies` | Full dependency list |
| `directoryStructure` | Directory tree with role annotations |
| `entryFiles` | Detected entry files |
| `configFiles` | Config file list |
| `readmeContent` | README text (up to 5000 chars) |
| `packageJson` | Project metadata |
| `fileStats` | File statistics |

### `scripts/parse_file.py`

Parses a resume PDF / DOCX / TXT into plain text for the interview-prep stage.

```bash
# Usage
python scripts/parse_file.py <resume-file-path>

# Example
python scripts/parse_file.py ./resume.pdf
```

Dependencies: `pdfplumber` or `pypdf` (PDF), `python-docx` (DOCX). The script prints the install command if a dependency is missing.

## Development

```bash
# Clone
git clone https://github.com/whishi47/project-showcase-enhancer-skill.git
cd project-showcase-enhancer-skill

# Adjust the workflow by editing SKILL.md and the assets templates — no build step
# To tune scanning, edit scripts/scan_project.js
# To tune resume parsing, edit scripts/parse_file.py
```

Directory layout:

```
project-showcase-enhancer/
├── SKILL.md                          # Skill definition (workflow)
├── README.md                         # Bilingual version
├── README.en.md                      # This document (English version)
├── README.zh-CN.md                   # Chinese version
├── images/
│   └── logo.svg                      # Logo used in this doc
├── scripts/
│   ├── scan_project.js               # Project scanner: dictionary match → JSON
│   └── parse_file.py                 # Resume parser: PDF/DOCX/TXT → text
└── assets/
    ├── showcase-template.md          # Project showcase document template
    └── interview-prep-template.md    # Interview prep guide template
```

## Publish

```bash
# Option 1: SkillHub web
#   Go to https://skillhub.cn , upload the packaged project-showcase-enhancer.zip
#   Slug: project-showcase-enhancer, Display name: 个人项目包装与面试备战

# Option 2: SkillHub CLI
#   After login, run: skillhub publish ./project-showcase-enhancer-skill

# Repackage (requires skill-creator's package_skill.py)
python package_skill.py ./project-showcase-enhancer-skill ./dist
```

> Bump the `version` field in SKILL.md before publishing.

## License

MIT © 2026
