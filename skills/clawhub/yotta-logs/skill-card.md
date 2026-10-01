## Description:

Searches local AI-agent conversation and memory logs across JSONL, JSON, SQLite, and Markdown to recover past discussions and their original context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

People and developers using AI agents can find earlier decisions, messages, and session context in their own local conversation and memory files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search results and session excerpts may reveal private conversations or memory content.

Mitigation: Keep default redaction on, narrow searches with --dir, --source, or --kind, and avoid sharing raw results.

## Reference(s):

- [Project homepage (listed in ClawHub metadata)](https://github.com/YottaMeta/yotta-logs)
- [ClawHub skill listing](https://clawhub.ai/yottameta/skills/yotta-logs)
- [CLI reference](references/cli.md)
- [Supported agent formats](references/agent-formats.md)
- [Security boundaries](references/security.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain text or structured JSON search results and session excerpts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can include source, session, timestamp, role, and line number; likely secrets are redacted by default.]

## Skill Version(s):

0.3.2 (source: ClawHub release, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
