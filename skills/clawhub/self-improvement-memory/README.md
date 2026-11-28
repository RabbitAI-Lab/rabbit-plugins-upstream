<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Ricardodpalmeida/self-improvement-memory/main/.github/assets/banner-dark.jpg">
  <img alt="self-improvement memory: remember what you tried, why, and whether it worked. A memory card for problem P-003, a silent Telegram bot, lists three attempts: a restart rejected, a hand dead-letter that fixed it, and a patch still waiting for proof." src="https://raw.githubusercontent.com/Ricardodpalmeida/self-improvement-memory/main/.github/assets/banner-light.jpg">
</picture>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT-0" src="https://img.shields.io/badge/license-MIT--0-1F5AA6?style=flat-square"></a>
  <img alt="Agent Skill" src="https://img.shields.io/badge/Agent%20Skill-SKILL.md-18191B?style=flat-square">
  <a href="https://clawhub.ai/ricardodpalmeida/skills/self-improvement-memory"><img alt="On ClawHub" src="https://img.shields.io/badge/ClawHub-self--improvement--memory-6B7280?style=flat-square"></a>
  <img alt="Plain Markdown, no database" src="https://img.shields.io/badge/storage-plain%20Markdown-6B7280?style=flat-square">
</p>

Agents and the people who maintain them fix the same problems more than once. The fix lands in a config file, a prompt or a skill, and the reason behind it is gone by the next session. **Self-Improvement Memory (SIM)** is an Agent Skill that keeps that reason. Each recurring problem gets one Markdown note with every attempt: what changed, why, what it was expected to fix, written before the test, and what actually happened. An index lists every note, so the next session reads one file, searches with `grep` and skips the directions that already failed.

This trace comes from a real test turn on OpenClaw, where an agent was asked what had already been tried for a silent Telegram bot. The skill list was not in its prompt, so it had to find the skill by itself:

```
skills.search  "Telegram bot silent not responding troubleshooting"  ->  self-improvement-memory (1st of 5)
skills.read    self-improvement-memory
read           sim/index.md
grep -ril      telegram|silent|inbound  ->  P-003-telegram-stuck-inbound.md
read           P-003-telegram-stuck-inbound.md
answer         cites P-003: a restart does not clear it (rejected), dead-lettering the stuck
               inbound row fixed it, the local patch still waits for a real case
```

## Where the idea comes from

This skill is an independent implementation of the idea in *Self-Improvement Memory Enables Continual Recursive Self-Improvement* ([Yu et al., 2026, arXiv:2611.18856](https://arxiv.org/abs/2611.18856)). It is not affiliated with or endorsed by the authors or their employers. In the paper, harness optimizers that carried a record of each problem, the edits tried and their predicted and observed outcomes finished higher than optimizers that kept only the evolved harness, in all ten benchmark and model transitions the authors tested, and by 2.36 points on average across ten paired coding runs (p = 0.003). Keeping only the diagnosis, without the attempts and outcomes, gave mixed results: the evidence is what helps.

This skill applies that record to everyday agent maintenance and stores it the simple way: append-only plain text, read on demand with search, never loaded whole into the prompt ([GrepMem, Yang et al., 2026](https://arxiv.org/abs/2611.25123)).

## How it works

1. **Before a change** the agent reads `index.md` and searches the notes for the symptom. If a note fits, it reads the attempts and checks which agent, model and version they ran on before reusing one.
2. **Before the test** it appends the attempt with what it changes, why and what it predicts.
3. **After validation** it fills in what was fixed, what was missed and the evidence, and updates the note's line in the index in the same change.

Notes are append only. A replaced fix stays in the note, so the next reader sees what was tried and why it went.

```markdown
## Attempt 2026-11-20 dead-letter the two stuck rows
- **Who:** maintenance session; OpenClaw 2026.11.5
- **What:** marked the two stuck inbound rows as dead-lettered, with the Gateway stopped
- **Why:** no native command handles items that are not yet dead
- **Predicted:** both bots answer the next direct message
- **Observed:** fixed; both answered within the hour, no conflict lines
- **Kept:** yes
```

## Install

OpenClaw is the primary target:

```bash
openclaw skills install @ricardodpalmeida/self-improvement-memory            # this workspace
openclaw skills install @ricardodpalmeida/self-improvement-memory --global   # all agents
```

On OpenClaw the memory lives in `~/.openclaw/sim/`, shared by every agent on the machine. Name another folder in your agents' instructions to move it.

The folder is a standard Agent Skill, so other agents that read `SKILL.md` can use it too. Clone it into the agent's skills folder under the skill's name, for example:

```bash
git clone https://github.com/Ricardodpalmeida/self-improvement-memory ~/.claude/skills/self-improvement-memory
```

Use `~/.codex/skills/self-improvement-memory` for Codex or `~/.copilot/skills/self-improvement-memory` for GitHub Copilot. Outside OpenClaw the memory defaults to `.sim/` at the project root.

## What is inside

```
SKILL.md       when to use the memory, the before and after steps, note and index templates
CHANGELOG.md   release notes
```

The memory holds descriptions of changes and links to evidence, never logs, secrets or personal data.

## License

[MIT-0](LICENSE). Use, share, modify and redistribute it, including commercially, without an attribution requirement. The same license applies on ClawHub.

## Author

**Ricardo Pacheco Almeida**, Senior AI Tech Lead and Architect and PhD student researching enterprise and solution architectures for generative AI, including multi-agent structures.

[Website](https://me.ricbits.cc/en/) · [LinkedIn](https://www.linkedin.com/in/ricardodpa/) · [GitHub](https://github.com/Ricardodpalmeida) · [ClawHub](https://clawhub.ai/ricardodpalmeida)

More skills by the same author:

| Skill | What it does |
|---|---|
| [data-storycraft](https://github.com/Ricardodpalmeida/data-storycraft-skill) | Turn analysis into charts, slides and reports that make the point |
| [Whetstone](https://github.com/Ricardodpalmeida/whetstone) | Scale your coding agent's engineering care to the risk of each change |
| [Excalidraw Diagrams](https://github.com/Ricardodpalmeida/openclaw-excalidraw-diagrams) | Draw clean, hand-drawn Excalidraw diagrams for Obsidian or excalidraw.com |
| [Book Capture for Obsidian](https://github.com/Ricardodpalmeida/book-capture-obsidian-skill) | Turn photos, ISBNs or Goodreads exports into Obsidian book notes |
| [Microsoft Learn MCP](https://github.com/Ricardodpalmeida/openclaw-mslearn-mcp) | Ground Microsoft answers in current Learn docs and code samples |
| [Multi-cloud Docs](https://github.com/Ricardodpalmeida/multicloud-docs) | Ground cloud and AI platform answers in each vendor's own current docs |
| [LadybugDB openCypher](https://clawhub.ai/ricardodpalmeida/skills/ladybug-opencypher-updated) | Work with LadybugDB property graphs using openCypher and Python |
