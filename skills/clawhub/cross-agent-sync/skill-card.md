## Description:

Reconcile recent Claude Code and Codex sessions for one project by creating local evidence packets and maintaining a curated progress ledger for cross-agent handoffs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antreasantoniou](https://clawhub.ai/user/antreasantoniou)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to resume project work across Claude Code and Codex by importing bounded local session evidence and recording verified decisions, evidence, blockers, next actions, and artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Query mode can pull sensitive local agent transcripts from unrelated projects into output or local files.

Mitigation: Use narrow project-specific queries, inspect generated .agent-sync/imports files as sensitive local data, and avoid committing raw imports.

Risk: Import packets can include sensitive user text and absolute local filesystem paths.

Mitigation: Treat packets as local evidence only, review curated summaries before sharing, and commit only the curated ledger files when repository policy permits.

## Reference(s):

- [Cross-Agent Sync README](README.md)
- [Claude Code and Codex session formats](references/session-formats.md)
- [ClawHub skill listing](https://clawhub.ai/antreasantoniou/skills/cross-agent-sync)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with shell commands and project-local JSONL/Markdown files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes curated progress to .agent-sync/events.jsonl and .agent-sync/PROGRESS.md; raw import packets are local-only under .agent-sync/imports/.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
