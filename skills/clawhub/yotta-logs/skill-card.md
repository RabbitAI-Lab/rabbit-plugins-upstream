## Description:

Searches local agent conversation and memory logs across JSONL, JSON, SQLite, and Markdown to recover earlier discussions and their sources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Agent users and developers search their local conversation and memory history to find earlier decisions, recover session context, and verify the source of past exchanges.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search results can reveal private conversation or memory content, especially when redaction is disabled.

Mitigation: Limit searches with --dir, --source, --kind, or --format; keep default redaction enabled and avoid sharing raw results or using --no-redact unless necessary.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/yottameta/skills/yotta-logs)
- [Project homepage (listed in release metadata)](https://github.com/YottaMeta/yotta-logs)
- [CLI reference](references/cli.md)
- [Security boundaries](references/security.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain text or JSON search results and session timelines]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can include source, session ID, timestamp, role, and line number; suspected secrets are redacted by default.]

## Skill Version(s):

0.3.3 (source: ClawHub release metadata, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
