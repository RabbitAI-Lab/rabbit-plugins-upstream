## Description:

Yotta-logs retrieves and analyzes local historical session and memory logs across AI agents, using zero-dependency search over JSONL, JSON, SQLite, Markdown, and related local records to recover prior conversations and parent-session context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to locate, search, extract, and summarize prior local agent session logs or memory files when they need evidence for earlier decisions, commands, conclusions, or parent-session context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can search sensitive cross-agent local history and may surface private session or memory content.

Mitigation: Keep redaction enabled by default, use explicit --dir, --source, --kind, date, or session filters, and avoid pasting retrieved log output into untrusted places.

Risk: Installers can persist the skill into multiple agent environments when broad install targets are used.

Mitigation: Install only into the intended agent directory, preferably with --agent or --dir, and avoid global installation unless every target has been reviewed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-logs)
- [README](README.md)
- [CLI protocol](references/cli.md)
- [Record format](references/format.md)
- [Agent formats](references/agent-formats.md)
- [Security boundaries](references/security.md)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-logs)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text guidance with shell commands; optional structured JSON from CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include local log excerpts, source paths, session identifiers, line numbers, timestamps, roles, counts, and redacted snippets.]

## Skill Version(s):

0.2.2 (source: SKILL.md frontmatter, package.json, CHANGELOG, and evidence release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
