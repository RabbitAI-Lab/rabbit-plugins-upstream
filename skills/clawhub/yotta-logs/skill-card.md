## Description:

Search and analyze local AI agent session and memory logs across JSONL, JSON, SQLite, Markdown, and binary formats to retrieve past conversations and their source context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users can locate earlier conversations, decisions, commands, and results across their local session and memory files, then inspect the source, time, and speaker context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search settings can unexpectedly include private memories.

Mitigation: Limit searches with --dir or --source, and do not rely on default_scope to exclude private memories.

Risk: Retrieved text is placed in the agent context, and password masking is incomplete.

Mitigation: Treat retrieved excerpts as sensitive and review them before sharing or forwarding.

Risk: Downloaded registry packages and host permission enforcement were not verified in the security review.

Mitigation: Use the pinned installation command, choose a specific destination, and check the host's permission behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-logs)
- [Project homepage](https://github.com/YottaMeta/yotta-logs)
- [Command-line reference](artifact/references/cli.md)
- [Security guidance](artifact/references/security.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Analysis]

**Output Format:** [Readable search results and summaries, or structured JSON with source and conversation context]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Retrieved excerpts may contain sensitive local conversation content.]

## Skill Version(s):

0.3.4 (source: release metadata, SKILL.md, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
