## Description:

Helps agents search, read, and update Notion workspaces through an authorized connection, with optional user-approved automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams use this skill to search and read Notion pages and databases, make explicitly approved changes, or set up approved Notion automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad OAuth permissions can expose more Notion workspace content than intended.

Mitigation: Use the least-privilege connection and scopes needed for the task; obtain approval before connecting.

Risk: Writes can change or delete the wrong page, database, or block.

Mitigation: Confirm the exact target ID, connection, and proposed change with the user before each write.

Risk: Persistent triggers can continuously forward sensitive event data.

Mitigation: Require approval for automations, scope triggers to specific resources, and confirm their destinations.

Risk: Direct API-key handling can leak a long-lived credential.

Mitigation: Prefer the CLI's managed login; use a raw API key only when the CLI is unavailable, and never log or persist it.

## Reference(s):

- [ClawHub Notion skill](https://clawhub.ai/byungkyu/skills/notion-api-skill)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Notion API introduction](https://developers.notion.com/reference/intro)
- [Notion trigger reference](references/notion/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Code]

**Output Format:** [Markdown guidance with optional commands, code, or structured Notion results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may contain workspace content accessible to the authorized connection.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
