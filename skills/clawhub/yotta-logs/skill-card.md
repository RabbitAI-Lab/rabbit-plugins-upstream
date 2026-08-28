## Description:

Yuanshi yotta-logs helps agents search local historical session and memory logs across JSONL, JSON, SQLite, Markdown, and title-only binary sources to recover prior conversations and supporting context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill when they need to locate earlier decisions, commands, conclusions, or parent-session context from local AI conversation and memory files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive content from private local AI conversation and memory logs to the active agent session.

Mitigation: Limit searches with --dir, --source, or --kind, keep default redaction enabled, and review matches before sharing or acting on them.

Risk: Broad default discovery can surface more historical context than the user intended.

Mitigation: Use explicit paths or source filters for targeted investigations, and avoid broad discovery unless the user is comfortable searching across registered local sources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-logs)
- [GitHub repository](https://github.com/YottaMeta/yotta-logs)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-logs)
- [Agent formats reference](references/agent-formats.md)
- [CLI reference](references/cli.md)
- [Record format reference](references/format.md)
- [Security boundary reference](references/security.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON]

**Output Format:** [Markdown guidance with shell commands and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results are local-only and redacted by default unless the user disables redaction.]

## Skill Version(s):

0.2.1 (source: SKILL.md frontmatter, package.json, and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
