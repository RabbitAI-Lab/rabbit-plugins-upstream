## Description:

元史 yotta-logs helps agents retrieve and analyze local historical session and memory logs across JSONL, JSON, SQLite, Markdown, and binary sources to recover prior conversations and parent-session context with original-log evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to locate prior decisions, commands, results, and context in local agent session or memory logs. The skill supports exact tracing by returning source, session ID, line number, timestamp, role, and original text snippets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose private local conversation and memory history to the agent using it.

Mitigation: Install only when local-log search is intended, keep default redaction enabled, and avoid sharing retrieved snippets outside the local review context.

Risk: A floating npx install can resolve to a package version other than the reviewed release.

Mitigation: Use a pinned package version or a reviewed local copy for controlled deployments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-logs)
- [Agent format survey](references/agent-formats.md)
- [CLI protocol](references/cli.md)
- [Log and memory format reference](references/format.md)
- [Security boundary](references/security.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell command examples; CLI output can be plain text or JSON when --json is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only local retrieval; default output redacts likely secrets unless --no-redact is used.]

## Skill Version(s):

0.2.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
