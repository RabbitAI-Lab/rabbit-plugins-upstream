# 😈 Devil's-Advocate

**A multi-agent skill that pressure-tests your decisions instead of just answering them.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Format: AgentSkill](https://img.shields.io/badge/format-AgentSkill-blueviolet)](SKILL.md)
[![Status: Battle-tested](https://img.shields.io/badge/status-battle--tested-success)](#it-actually-broke-twice-and-that's-the-point)

Most "council of AI advisors" skills are a prompt template someone wrote once and never watched run. This one isn't. It's the same core pattern — 5 independent lenses, anonymized peer review, a chairman synthesis — refined by actually running it live against a real decision, watching it fail in two specific ways, and fixing exactly those failures instead of guessing at improvements.

## What it does

Run `/devil` on any real decision with a genuine tradeoff, and it:

1. **Gathers real data first** — tries web search, then browser automation for JS-heavy pages, before ever asking you to hand-feed it facts.
2. **Spawns 5 advisors in parallel**, each arguing a distinct, uncompromising lens: Contrarian, First Principles, Expansionist, Outsider, Executor.
3. **Routes 2 of them to a different model** when you have one available — so it's not one model wearing five masks. Real architectural disagreement catches blind spots a single model shares across all its own personas.
4. **Fact-checks every claim** against the real source data, mechanically, before anyone gets to synthesize an opinion from it.
5. **Runs anonymized peer review** — the 5 responses get graded blind, by each other.
6. **Synthesizes a draft verdict**, then **mandatorily attacks its own conclusion** with a dedicated devil's-advocate pass, every single run — not just when something looks shaky.
7. **Rates its own confidence** HIGH or LOW instead of always sounding certain, and tells you outright when a verdict is closer to a coin flip than a recommendation.
8. **Optionally checks back later** — opt-in only — to log what actually happened against the original call.

## It actually broke twice, and that's the point

This skill exists because a simpler version of it got run twice, live, on the same real question with the same real data — and the majority verdict *flipped* between runs. That's not a hypothetical edge case in a spec doc; it happened, it got diagnosed, and the fix (confidence rating + mandatory devil's advocate + fact-checking) is baked into every step below, not bolted on as an afterthought.

A separate run exposed a second, sneakier bug: peer reviewers were shown a *compressed* version of the shared context and started flagging real, given facts as if an advisor had fabricated them. The fix — identical context, byte-for-byte, at every step — is now a hard rule called out explicitly in the file, because it's exactly the kind of thing that breaks silently if someone "cleans up" the prompt later.

Most skills you'll find are someone's best guess at a good process. This one is a process with a documented incident report.

## Why this over a plain 5-advisor prompt

| | Plain LLM council prompt | Devil's-Advocate |
|---|---|---|
| Model diversity | One model, five personas | Routes 2 of 5 to a second model/provider when available |
| Confidence signal | None — every answer sounds equally sure | Explicit HIGH/LOW rating, flags close calls plainly |
| Attacks its own conclusion | No | Mandatory devil's-advocate pass, every run |
| Fact-checking | Incidental, if a reviewer happens to notice | Dedicated mechanical pass before synthesis |
| Data sourcing | Assumes you hand-feed accurate context | Tries to go get it itself first |
| Outcome tracking | One-shot, nothing after | Opt-in follow-up that closes the loop |

## Requirements

Only real hard requirement: an agent harness that can spawn multiple sub-agents in parallel (Claude Code's `Agent` tool, OpenClaw, or equivalent). Everything else — a second model, web/browser access, scheduled follow-ups — is optional and degrades gracefully; see the requirements table in [`SKILL.md`](SKILL.md).

## Install

Drop [`SKILL.md`](SKILL.md) into your agent framework's skills directory (e.g. `.claude/skills/devils-advocate/SKILL.md`, or your OpenClaw `skills/` folder) and restart/reload skills. Trigger with `/devil`, or natural language: *"pressure-test this," "council this," "what would you do."*

## Origin

Core 5-lens / peer-review / chairman pattern adapted from [Andrej Karpathy's public LLM Council concept](https://github.com/karpathy). This version adds multi-model routing, mechanical fact-checking, mandatory adversarial stress-testing, confidence rating, and opt-in outcome tracking — the parts that only showed up as necessary after running the simpler version against a real decision and watching it fail.

## Contributing

Found a new way this breaks? Open an issue with the exact input and what went wrong — that's how the last two guardrails got written, and it's the only way this stays honest instead of turning into another untested spec.

## License

MIT — see [LICENSE](LICENSE). Take it, fork it, break it, tell me how.

---

If this is useful, a ⭐ helps other people find it — and follow for what gets built next.
