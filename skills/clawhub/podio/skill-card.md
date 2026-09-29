## Description:

Helps agents manage Podio workspaces, apps, items, tasks, and comments through a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams using Podio can ask an agent to find or manage workspaces, apps, items, tasks, and comments, with approval before account connections or changes. Developers can also configure scheduled or event-driven workflows using the supported trigger sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A connected account may expose Podio data or allow unintended changes or deletions.

Mitigation: Start with read-only operations, use the least access needed, and confirm the target and effect of every write or deletion.

Risk: Automated triggers can continue sending data to a destination after setup.

Mitigation: Review and approve the trigger scope and destination before enabling it; avoid broad or third-party destinations unless the ongoing data flow is understood.

Risk: Long-lived API keys can be exposed if copied into commands or logs.

Mitigation: Prefer OAuth login and avoid printing, exporting, or embedding credentials.

## Reference(s):

- [Podio skill on ClawHub](https://clawhub.ai/byungkyu/skills/podio)
- [Podio API documentation](https://developers.podio.com/doc)
- [Maton documentation](https://docs.maton.ai)
- [Maton homepage](https://maton.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Text or Markdown with commands and code when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Podio responses may contain personal data; show only fields needed for the task.]

## Skill Version(s):

1.2.5 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
