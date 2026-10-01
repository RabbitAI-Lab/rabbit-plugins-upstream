## Description:

Helps agents manage TickTick tasks and projects through a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams using an agent to find, create, update, complete, or organize TickTick tasks and projects through their authorized account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton brokers access to the user's TickTick account.

Mitigation: Use only if the user trusts Maton, prefer OAuth login, and grant only the access needed.

Risk: Writes can change or delete tasks, projects, or connections.

Mitigation: Review the target and effect with the user and get explicit approval before each write.

Risk: Optional functions, triggers, and destinations can continue acting or forwarding event data.

Mitigation: Create them only with separate informed approval, review their scope and destination, and remove them when no longer needed.

Risk: Using a long-lived API key instead of OAuth increases credential exposure.

Mitigation: Prefer the OAuth CLI flow; use an API key only when the CLI is unavailable and never print or persist it.

## Reference(s):

- [TickTick skill on ClawHub](https://clawhub.ai/byungkyu/skills/ticktick-api-skill)
- [Maton](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [TickTick developer portal](https://developer.ticktick.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code]

**Output Format:** [Markdown guidance, commands, and structured API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authorized connection and network access; confirm writes with the user.]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
