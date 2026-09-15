## Description:

Yuanshi yotta-logs retrieves and analyzes local historical session and memory logs across AI agents, searching JSONL, JSON, SQLite, Markdown, and limited binary records to recover prior conversations and parent-session context with original-log evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to locate, search, extract, and summarize local historical session or memory logs across supported AI agents when they need original-message evidence for previous discussions, decisions, commands, or parent-session context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill searches sensitive local conversation and memory history across supported tools.

Mitigation: Install only in environments where this local access is acceptable, and prefer explicit --dir, --source, --kind, or --format filters to narrow retrieval.

Risk: Default redaction can miss secrets embedded in URLs or other sensitive log content.

Mitigation: Treat all output as sensitive, review results before sharing, and keep --no-redact limited to trusted local workflows.

Risk: Unpinned npx installation can resolve a newer package version than the reviewed release.

Mitigation: Pin the npm package version when installing or invoking the skill for reviewed deployments.

## Reference(s):

- [Agent Formats](references/agent-formats.md)
- [CLI Protocol](references/cli.md)
- [Log and Memory Format](references/format.md)
- [Security Boundaries](references/security.md)
- [FAQ](references/faq.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples; the CLI can emit plain text timelines or JSON records.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only local retrieval; search and session outputs are redacted by default unless --no-redact is used.]

## Skill Version(s):

0.3.1 (source: SKILL.md frontmatter, package.json, CHANGELOG, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
