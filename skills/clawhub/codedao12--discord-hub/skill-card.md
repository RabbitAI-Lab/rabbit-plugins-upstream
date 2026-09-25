## Description:

OpenClaw skill for Discord Bot API workflows, covering interactions, commands, messages, and operations using direct HTTPS requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[codedao12](https://clawhub.ai/user/codedao12)

### License/Terms of Use:


## Use Case:

Developers and engineers use this skill to design Discord bot workflows, command UX, interaction flows, and direct HTTPS request patterns without relying on an SDK.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated Discord API requests may post, edit, delete, or moderate Discord content if used without review.

Mitigation: Review generated HTTP requests before execution and test bot behavior in a limited guild first.

Risk: Discord bot tokens and interaction secrets can grant unauthorized access if exposed.

Mitigation: Treat bot tokens as secrets, avoid logging them, rotate compromised tokens, and use minimal OAuth scopes and gateway intents.

## Reference(s):

- [Discord API Overview](references/discord-api-overview.md)
- [Application Commands](references/discord-app-commands.md)
- [Auth and Tokens](references/discord-auth-and-tokens.md)
- [Interactions](references/discord-interactions.md)
- [Messages and Components](references/discord-messages-components.md)
- [Gateway vs Webhooks](references/discord-gateway-webhooks.md)
- [Rate Limits and Reliability](references/discord-rate-limits.md)
- [HTTP Request Templates](references/discord-request-templates.md)
- [Discord Bot Feature Map](references/discord-feature-map.md)
- [Discord API Base URL](https://discord.com/api)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, API Calls, Configuration instructions]

**Output Format:** [Markdown with JSON and HTTP request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces bot workflow plans, command designs, request templates, and operational checklists for review before use.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
