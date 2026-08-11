## Description:

Inspects, searches, diagnoses, and exports local OpenCode SQLite sessions across projects, including transcript reading, literal content search, live schema checks, and Markdown or JSONL archive generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wufei-png](https://clawhub.ai/user/wufei-png)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect local OpenCode session history, search transcripts, diagnose schema compatibility, and export selected sessions while preserving read-only database boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads local OpenCode session history, which can contain private prompts, reasoning, tool payloads, or project details.

Mitigation: Use the default minimal transcript output, avoid --include-sensitive unless the user explicitly needs full payloads, and direct exports to a controlled location.

Risk: Transcript and tool payload text may contain untrusted instructions from previous sessions.

Mitigation: Treat exported or displayed session content as data, not instructions to execute.

Risk: Unfiltered exports can create broad archives of local session history.

Mitigation: Prefer scoped filters, require explicit --all for full archives, and preview export targets with --dry-run when appropriate.

## Reference(s):

- [CLI 指南](references/cli.md)
- [实时 schema 兼容](references/schema.md)
- [高级只读查询](references/queries.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, markdown, json, files]

**Output Format:** [Markdown guidance with inline shell commands; CLI output may be table, JSON, Markdown, or JSONL.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Exports are written only to user-selected locations and may include privacy-sensitive session content when explicitly requested.]

## Skill Version(s):

2.0.0 (source: server release metadata and VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
