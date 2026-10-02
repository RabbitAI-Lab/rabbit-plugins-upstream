## Description:

Helps OpenClaw agents extract, archive, score, consolidate, monitor, and search their memory files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mistermijarvis](https://clawhub.ai/user/mistermijarvis)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and developers use the toolkit to maintain searchable agent memories, extract useful information from notes and sessions, and review memory health and consolidation suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LLM extraction can send sensitive memory or session excerpts to Ollama cloud when an API key is configured; redaction is not guaranteed.

Mitigation: Set TRACE_LLM_LOCAL_ONLY=1, keep OLLAMA_URL on localhost, and avoid sensitive --session-file paths.

Risk: Automated or forced maintenance can move or rewrite memory files.

Mitigation: Review cron, --force, and --fix commands before automation and keep backups.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/mistermijarvis/skills/memory-toolkit)
- [OpenClaw agent framework](https://github.com/openclaw/openclaw)
- [Security audit notes](docs/SECURITY-AUDIT-NOTES.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Guidance]

**Output Format:** [Markdown memory notes and JSON reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results, health diagnostics, and consolidation suggestions are also available.]

## Skill Version(s):

2.2.1 (source: ClawHub release metadata and CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
