## Description: <br>
OpenClaw skill for Discord Bot API workflows, covering interactions, commands, messages, and operations using direct HTTPS requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ingejanben268](https://clawhub.ai/user/ingejanben268) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and bot maintainers use this skill to plan Discord Bot API workflows, design commands and interactions, and prepare direct HTTP request patterns for bot operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A Discord webhook URL stored in a local .env file can be exposed or misused if the file is shared or sourced from an untrusted location. <br>
Mitigation: Keep the .env file private, use only trusted local configuration, and rotate any exposed Discord webhook URL. <br>
Risk: The helper sends user-provided message content to the configured Discord webhook. <br>
Mitigation: Review message content and confirm the webhook destination before sending. <br>


## Reference(s): <br>
- [Discord API Overview](references/discord-api-overview.md) <br>
- [Auth and Tokens](references/discord-auth-and-tokens.md) <br>
- [Interactions](references/discord-interactions.md) <br>
- [Application Commands](references/discord-app-commands.md) <br>
- [Messages and Components](references/discord-messages-components.md) <br>
- [Gateway vs Webhooks](references/discord-gateway-webhooks.md) <br>
- [Rate Limits and Reliability](references/discord-rate-limits.md) <br>
- [HTTP Request Templates](references/discord-request-templates.md) <br>
- [Discord Bot Feature Map](references/discord-feature-map.md) <br>
- [Discord API](https://discord.com/api) <br>
- [ClawHub Skill Page](https://clawhub.ai/ingejanben268/skills/discord-hub-my) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with HTTP payload examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Discord REST request templates, operational checklists, and webhook helper commands.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
