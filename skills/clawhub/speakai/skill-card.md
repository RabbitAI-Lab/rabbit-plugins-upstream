## Description:

Guides agents in connecting to Speak AI and using its workspace tools for transcription, media search, analysis, meetings, surveys, and exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[speakai](https://clawhub.ai/user/speakai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to connect to a Speak AI workspace, choose the right tools for recordings and transcripts, and manage related meeting, survey, and export workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting an agent grants access to the user's Speak AI workspace.

Mitigation: Authorize access only when needed and use OAuth where possible; avoid pasting API keys unless local connection requires them.

Risk: Deletes, bulk edits, share links, meeting recording, webhooks, automations, and exports can change or disclose workspace data.

Mitigation: Review the intended records and consequences and confirm before performing these actions.

## Reference(s):

- [Speak AI skill on ClawHub](https://clawhub.ai/speakai/skills/speakai)
- [Speak AI MCP documentation](https://docs.speakai.co/mcp)
- [Speak AI MCP setup](https://docs.speakai.co/mcp/setup/)
- [Speak AI MCP authentication](https://docs.speakai.co/mcp/authentication)
- [Speak AI MCP tool reference](https://docs.speakai.co/mcp/tools/)

## Skill Output:

**Output Type(s):** [Guidance, Configuration instructions, Shell commands]

**Output Format:** [Markdown with configuration and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides use of Speak AI workspace tools; results depend on the connected user's permissions.]

## Skill Version(s):

1.38.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
