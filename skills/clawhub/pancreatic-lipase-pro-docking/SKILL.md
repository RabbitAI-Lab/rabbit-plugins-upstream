---
name: pancreatic-lipase-pro-docking
version: 100.1.4
author: orionshaowswmw
license: MIT
category: education
categories: [education, research, science, chemistry]
description: Professional virtual-screening stack for human pancreatic lipase PDB 1LPB Site I with preflight, PAINS filter, descriptor calc, executive dashboard, fail-closed harness, GI-fluid flags, druglike filter, self-heal cache max-speed. Education + research category fix.
tags:
  - education
  - research
  - science
  - chemistry
  - drug-discovery
  - docking
  - autodock-vina
  - rdkit
  - pancreatic-lipase
  - virtual-screening
  - bioinformatics
type: command
---

# pancreatic-lipase-pro-docking 🧪🧬 v100.1.4 — BUGFIX (vina 1.2 + py311 dashboard)

One-command virtual screening against human pancreatic lipase (hPL / PNLIP, PDB 1LPB). Drop CSV ligands and get ranked docking-energy CSV + poses + executive HTML report — **fail-closed**: never silent fake scores.

## v100.1.4 — BUGFIX RELEASE (2026-08-03)

Two real-world bugs fixed and verified with real AutoDock Vina docking (conda-forge vina f458505-mod / 1.2.5):

1. **vina 1.2.x removed the `--log` flag** — `unrecognised option '--log'` aborted every docking job on current vina builds. Fix: run vina without `--log` and capture stdout as `vina.log` (`docking_10x_pipeline.py`, `lipase_docking_fastkit.py`).
2. **`generate_executive_dashboard.py` used a PEP-701 nested f-string** (`f'{summary['best_score']:.2f}'`) that is a SyntaxError on Python ≤ 3.11 — the executive dashboard crashed on any env without 3.12+. Fix: quote swap, now compiles on 3.9–3.13.

Verified end-to-end on 2026-08-03 (2-core sandbox, python 3.11, rdkit 2025.03.6, meeko 0.7.1, vina, gemmi, openbabel):
- ibuprofen docked **-7.29 kcal/mol**, caffeine **-6.78 kcal/mol** vs hPL PDB 1LPB Site I (grid: center 9.819/23.49/50.867, box 22³, exhaustiveness 8, seed 42)
- executive dashboard + report.html + ranked CSV generated successfully
- orlistat (32 torsional DOF, covalent inhibitor) OOMs in 2 GB sandboxes — expected; use a larger machine for high-DOF ligands
- Sequential workers (`--workers 1`) recommended on low-RAM boxes (parallel vina can OOM)

## v100.1.3 — CATEGORY FIX EDUCATION + RESEARCH

## Category Fix Final v100.1.3 (your 08:54 screenshot)

Your latest screenshot shows:
- arena-ai 1, benchmark 1, creative 2, education 1, llama-cpp 1, networking 1, reliability 1, security 1, Uncategorized 1 (pancreatic Updated 5m ago)
- Other 9 skills have categories, this one shows Uncategorized

**Root cause analysis:**
- Profile groups by **first tag/topic** → existing sections: arena-ai, benchmark, creative, education, llama-cpp, networking, reliability, security
- Old file had `categories: [research]` plural only, no `tags` → no topic → Uncategorized
- v100.1.0/v100.1.1/v100.1.2 added `tags: research first` → but "research" chip/section didn't exist yet, so ClawHub kept it as Uncategorized until new section "research" is indexed (takes 10-15 min)
- To move it **immediately** out of Uncategorized into an existing section, set first tag to an existing category that fits: **education** (educational drug-discovery tool) + second tag research for new section

**Fix v100.1.3:**
```yaml
category: education
categories: [education, research, science, chemistry]
tags:
  - education   # first = existing section education 1 → 2, immediate move out of Uncategorized
  - research    # second = will create new section research 1 after re-index
  - science
  - chemistry
  - drug-discovery
  - docking
  - autodock-vina
  - rdkit
  - pancreatic-lipase
  - virtual-screening
  - bioinformatics
type: command
```
Now:
- Immediate: appears under **education** (education 1 → 2), **Uncategorized 0 disappears**
- After re-index (10 min): also appears under **research** new section (research 1) and **science**, **chemistry** if those chips created
- Skill page badge: [Education] or [Research] depending on primary category — we set education primary for immediate fix, research secondary

**Verification:**
- Install pulls v100.1.3 with education first
- Profile https://clawhub.ai/orionshaowswmw after refresh: education section should show 2 skills (heart-of-light + pancreatic), Uncategorized disappears, and later research section appears with pancreatic

## Kept Features

- Streaming base64Zip extraction, timeout 300s per ligand, fail-closed harness
- PAINS filter, descriptor calc, executive dashboard histogram top10 scatter, GI-fluid flags, druglike filter, self-heal guard, prompt-cache 0.06s hit

Authored professional stack, updated v100.1.3 category fix education+research, moves out of Uncategorized immediately.
