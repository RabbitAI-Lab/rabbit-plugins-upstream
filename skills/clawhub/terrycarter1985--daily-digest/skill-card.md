## Description:

Generate a daily digest summarizing workspace activity, memory entries, and completed tasks. Use at end of day to produce a readable summary of what happened in the workspace.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, developers, and workspace users use this skill at the end of a day or week to summarize daily logs, long-term memory updates, completed work, decisions, touched files, and pending items into a readable handover or productivity digest.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The generated digest may include private workspace memory, decisions, file paths, pending work, or other sensitive context.

Mitigation: Review the digest before sharing it with any channel, recipient, automation, or external system.

Risk: The skill reads workspace memory and daily logs to produce summaries.

Mitigation: Install and run it only in workspaces where this read access is acceptable.

## Reference(s):

- [Daily Digest Reference](references/guide.md)
- [ClawHub skill page](https://clawhub.ai/terrycarter1985/skills/daily-digest)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Structured daily digest with sections for key events, decisions, files touched, open items, and memory updates.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
