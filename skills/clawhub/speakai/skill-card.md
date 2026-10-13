## Description:

Guides agents through connecting to Speak AI and using its workspace tools to transcribe, search, analyze, share, and manage recordings and related content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[speakai](https://clawhub.ai/user/speakai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workspace users connect an agent to Speak AI to transcribe and analyze media, search recordings, generate clips and exports, and manage meeting assistants, recorders, and workspace settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys or bearer tokens may be exposed when using the non-OAuth connection.

Mitigation: Prefer OAuth; use API keys only when needed and keep real tokens out of shared terminals, logs, screenshots, and chats.

Risk: Workspace actions can publish links, export data, schedule meeting assistants, or create persistent webhooks and automations.

Mitigation: Review the agent's access and confirm the action, audience, and affected workspace items before proceeding.

Risk: Deletion and bulk changes can remove or alter workspace content.

Mitigation: Confirm affected items and consequences before making destructive or bulk changes.

## Reference(s):

- [Speak AI MCP documentation](https://docs.speakai.co/mcp)
- [Speak AI MCP setup](https://docs.speakai.co/mcp/setup/)
- [Speak AI MCP tool reference](https://docs.speakai.co/mcp/tools/)
- [Speak AI ClawHub release](https://clawhub.ai/speakai/skills/speakai)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with command and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agent actions that access or change the connected Speak AI workspace.]

## Skill Version(s):

1.33.2 (source: ClawHub release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
