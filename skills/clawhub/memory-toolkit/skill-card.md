## Description:

Openclaw Memory Toolkit provides a local-first Python pipeline for OpenClaw agent memory extraction, archiving, temporal scoring, consolidation, health checks, and hybrid search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mistermijarvis](https://clawhub.ai/user/mistermijarvis)

### License/Terms of Use:

MIT-0

## Use Case:

Developers running local-first OpenClaw agents use this skill to maintain and search agent memory over time with standalone scripts, scheduled checks, and optional local LLM assistance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search indexing can recursively ingest broad or sensitive directories and persist their contents in a local search database.

Mitigation: Keep indexing scoped to the intended memory workspace, avoid hybrid_search.py index --dir on broad or sensitive paths, and review generated databases before retaining them.

Risk: Memory management commands can move or rewrite memory files, and --force or --yes can bypass interactive prompts.

Mitigation: Run dry-run or read-only modes first, keep backups, and reserve --force or --yes for tightly controlled automation.

Risk: LLM and embedding features send memory text to an Ollama HTTP endpoint.

Mitigation: Keep Ollama bound to localhost and do not configure remote endpoints for private memory workloads.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mistermijarvis/skills/memory-toolkit)
- [OpenClaw project](https://github.com/openclaw/openclaw)
- [Artifact README](artifact/README.md)
- [Artifact changelog](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, code, files]

**Output Format:** [Markdown guidance with shell command examples and optional JSON, SQLite, SVG, and Markdown file outputs from the bundled scripts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally against an OpenClaw workspace; some commands write memory, report, archive, or index files, while memory-health.py is read-only unless output or fix flags are used.]

## Skill Version(s):

2.1.1 (source: server release evidence and CHANGELOG.md, released 2026-08-22)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
