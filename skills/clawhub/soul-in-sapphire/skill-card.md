## Description:

Continuity, durable memory, state, journal, and identity maintenance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nextaltair](https://clawhub.ai/user/nextaltair)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to maintain continuity across sessions by recording searchable long-term memory, emotional or state snapshots, journal syntheses, and identity-change evidence in Notion and local workspace files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist sensitive personal state, journals, profile facts, and long-term memories in Notion and local workspace files.

Mitigation: Use a Notion integration limited to the intended pages and databases, avoid sending secrets or intimate personal details to memory writes, and review stored data periodically.

Risk: Notion and local write helpers can create or update durable records beyond the immediate conversation.

Mitigation: Install only when durable memory is intended, pass explicit database IDs, review generated payloads before use, and prefer local-only operation when remote persistence is unnecessary.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nextaltair/skills/soul-in-sapphire)
- [Publisher profile](https://clawhub.ai/user/nextaltair)
- [Notion integrations](https://www.notion.so/my-integrations)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON and shell command examples, plus JSON output from helper scripts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and Notion credentials; writes may target Notion databases and local workspace files.]

## Skill Version(s):

1.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
