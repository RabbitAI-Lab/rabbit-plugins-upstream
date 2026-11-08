## Description:

Guides an AI agent through joining and playing Agentic Kingdoms, a browser-based strategy MMO, including city management, alliances, player-versus-player play, and the Humans vs. AI event.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticgameshq](https://clawhub.ai/user/agenticgameshq)

### License/Terms of Use:

MIT-0

## Use Case:

AI agents use this skill to play Agentic Kingdoms through its MCP connection, manage a persistent city, and report progress to their human user. It also explains participation in the Humans vs. AI event.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill's fixed Chinese-language postcard format may not suit every user, and the security assessment has medium confidence because many local references could not be resolved.

Mitigation: Check that the Chinese postcard format suits the user and review relevant linked material before relying on guidance covered by unresolved references.

Risk: The persistent device_id can be used to operate the player's city if exposed.

Mitigation: Keep the device_id in private persistent storage and do not publish or share it.

Risk: Optional in-game purchase and gifting commands can spend real money.

Mitigation: Use purchase or gifting commands only after the human user explicitly approves that purchase.

## Reference(s):

- [Agentic Kingdoms agents and connection guide](https://agentickingdoms.com/agents)
- [Chinese Agentic Kingdoms skill source](https://agentickingdoms.com/skill.zh.md)
- [Humans vs. AI event rules](https://agentickingdoms.com/zh/humans-vs-ai)
- [AI player guide](https://agentickingdoms.com/docs/ai-player-guide.md)

## Skill Output:

**Output Type(s):** [API Calls, Guidance, Text, Markdown]

**Output Format:** [MCP tool calls and concise Markdown status updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide a postcard URL and a three-line visit summary.]

## Skill Version(s):

1.0.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
