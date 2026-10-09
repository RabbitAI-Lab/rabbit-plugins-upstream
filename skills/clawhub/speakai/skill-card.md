## Description:

Guides agents through connecting to a Speak AI workspace and using its tools to transcribe, search, analyze, share, and manage recordings and related workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[speakai](https://clawhub.ai/user/speakai)

### License/Terms of Use:

MIT-0

## Use Case:

People connecting an agent to Speak AI use this guide to set up workspace access and choose tools for transcribing recordings, searching and analyzing media, exporting results, and managing meetings, surveys, dashboards, and automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workspace access may expose recordings and transcripts beyond what the user intends.

Mitigation: Prefer OAuth and review the workspace permissions granted before connecting.

Risk: Shareable links, exports, and meeting recordings can disclose sensitive content.

Mitigation: Confirm the audience and contents before creating links, exporting data, or recording a meeting.

Risk: Automation, webhook, group, and deletion actions may persist or change access to content.

Mitigation: Confirm the exact action and affected records before changing automations, webhooks, team groups, or deleting content.

## Reference(s):

- [Speak AI MCP documentation](https://docs.speakai.co/mcp)
- [Speak AI MCP setup](https://docs.speakai.co/mcp/setup/)
- [Speak AI MCP authentication](https://docs.speakai.co/mcp/authentication)
- [Speak AI MCP tools](https://docs.speakai.co/mcp/tools/)
- [Speak AI skill release](https://clawhub.ai/speakai/skills/speakai)

## Skill Output:

**Output Type(s):** [Guidance, Configuration instructions, Shell commands]

**Output Format:** [Markdown with JSON and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.30.0 (source: ClawHub release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
