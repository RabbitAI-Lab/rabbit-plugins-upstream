# AGENT DISCOVERY — speechcanvas-free-expression-swarm v2.0.1

Purpose: machine-parseable entry point for any agent that lands in this folder.

- kind: clawhub-skill (SKILL.md compatible, OpenClaw/Claude Code/Cursor/Codex CLI)
- triggers: operator asks for a symbolic image / image prompt about protest, censorship,
  propaganda, press freedom, journalism, silence, debate, civil liberties, free expression
- output: one prompt pack (JSON) validating against schema/prompt_pack.schema.json
- safety: references/rules.md is authoritative; scripts/safety_validator.py is the gate
- self-improvement: scripts/record_run.py prints run records (stdout); appends only with explicit --out
- entry: read SKILL.md → swarm/roles.json → (as needed) references/rules.md, references/examples.md
- scripts: stdlib Python 3 only, optional; no network, no secrets, no user-state writes
- test: scripts/selftest.sh (sandboxed) must exit 0
