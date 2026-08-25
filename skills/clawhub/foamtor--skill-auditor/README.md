<div align="center">

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent_Skills-compatible-blue.svg)](https://agentskills.io)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)

# skill-auditor

Checks whether a SKILL.md has the structures that keep AI agents on track — and tells you what's missing and how to fix it.

[English](README.md) · [中文](README_CN.md)

</div>

## The problem

You write a SKILL.md, give it to an AI agent, and it works — sometimes. Other times the AI skips steps, drops constraints, or rationalizes doing less work than specified. The root cause: the skill lacks patterns that force compliance.

## Quick start

```bash
npx skills add Foamtor/skill-auditor
```

```bash
python3 scripts/audit_skill.py /path/to/your-skill/SKILL.md
```

Output:

```
Type: workflow (has step-by-step process)
Applicable dimensions: 10/10

  ✅  Anti-rationalization guard
  ❌  Stage gates               — Missing. AI will run through without pausing.
  ✅  Verification scripts
  ❌  Trap checklist             — Missing. AI will repeat known mistakes.
  ✅  Progressive disclosure
  ✅  Context engineering
  ...

Score: 7 pass, 0 partial, 3 fail

Fix suggestions:
  1. [Critical] Add stage gates — force the AI to stop at key points.
     Example: see ruanzhu-from-scratch's G0-G4 gate table.
  2. [Critical] Add trap checklist — document known failure modes.
     Example: see ai-frontier-notes' "⚠️" sections with dates.
```

## What it checks

10 patterns that prevent AI from drifting off-workflow:

| Pattern | What goes wrong without it |
|---------|---------------------------|
| Anti-rationalization guard | AI invents excuses to skip steps |
| Stage gates | AI finishes without stopping for confirmation |
| Verification scripts | AI claims "done" without actually checking |
| Decision flowchart | AI gets lost in vague "then"/"if" instructions |
| Trap checklist | AI repeats mistakes others already documented |
| Progressive disclosure | Context overload — AI ignores key rules |
| Three-layer architecture | Skill tries to hold everything in one file |
| Runtime hooks | No code-level enforcement, text-only |
| Context engineering | Key rules buried, file too long |
| Scoped rules | Irrelevant rules loaded, diluting attention |

Not every skill needs all 10. The script auto-detects skill type and only checks what applies:

- **Workflow** (multi-step pipelines): all 10
- **Tool** (script wrappers): 7
- **Reference** (cheat sheets): 4
- **Pattern** (methodologies): 3

## Who uses this

**You installed a third-party skill and it's unreliable.** Run this to find out what's missing.

**You're writing a skill and want to make it robust.** Run this before publishing.

**You're a team lead rolling out shared skills.** Run this as a quality gate.

## What it does NOT do

- Check factual accuracy of skill content
- Auto-fix skills (it gives suggestions, you implement)
- Guarantee compliance (patterns reduce drift but can't eliminate it)

## Install

```bash
npx skills add Foamtor/skill-auditor
```

```bash
git clone https://github.com/Foamtor/skill-auditor.git ~/.agents/skills/skill-auditor
```

Works with any tool that supports the [Agent Skills standard](https://agentskills.io): Claude Code, Codex, Cursor, Gemini CLI, Hermes Agent, and more.

## CI integration

```bash
python3 scripts/audit_skill.py my-skill/SKILL.md || echo "Skill quality check failed"
```

Exit codes: 0 = pass, 1 = critical gaps found, 2 = bad arguments.

## License

[MIT](LICENSE)
