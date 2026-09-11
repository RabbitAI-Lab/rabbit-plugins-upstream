## Description:

元史 yotta-logs retrieves and analyzes local historical AI-agent session and memory logs across JSONL, JSON, SQLite, Markdown, and title-only binary records so agents can trace prior conversations with original-log evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to locate, search, and extract prior session or memory records when they need evidence for earlier decisions, commands, or conversation context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad local history search can surface private session or memory content.

Mitigation: Use explicit --dir, --source, or --kind filters and review outputs before placing them into agent context.

Risk: Disabling redaction can expose secrets or credentials present in logs.

Mitigation: Keep default redaction enabled unless working in a trusted local context.

Risk: Server-resolved GitHub import provenance is unavailable for this version.

Mitigation: Prefer a pinned or locally reviewed install source before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-logs)
- [Agent formats reference](references/agent-formats.md)
- [CLI protocol](references/cli.md)
- [Record format reference](references/format.md)
- [Security boundary](references/security.md)
- [FAQ](references/faq.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Plain text or Markdown, with optional JSON for structured search results and shell commands for local execution]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default redaction masks likely secrets; --no-redact can emit raw local log content.]

## Skill Version(s):

0.3.0 (source: SKILL.md frontmatter, package.json, CHANGELOG, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
