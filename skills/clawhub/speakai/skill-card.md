## Description:

Guides agents through connecting to Speak AI and working with recordings, transcripts, search, meetings, and workspace tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[speakai](https://clawhub.ai/user/speakai)

### License/Terms of Use:

MIT-0

## Use Case:

Users and developers connect an agent to their Speak AI workspace to transcribe and search recordings, retrieve insights, and manage related media and workspace workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An API key may be exposed when configuring the local connection.

Mitigation: Prefer OAuth and avoid entering real API keys into shell history.

Risk: Deletes, bulk edits, public links, and persistent webhooks or automations can have lasting effects.

Mitigation: Confirm the affected items and consequences with the user before taking action.

Risk: Scheduling a meeting assistant can record a live meeting.

Mitigation: Confirm the meeting URL and start time, and tell the user explicitly that the assistant records the call.

Risk: Changes to team or group membership can affect other people's access.

Mitigation: Review and confirm the membership changes before applying them.

## Reference(s):

- [Speak AI MCP documentation](https://docs.speakai.co/mcp)
- [Speak AI MCP setup](https://docs.speakai.co/mcp/setup/)
- [Speak AI MCP authentication](https://docs.speakai.co/mcp/authentication)
- [Speak AI MCP tool reference](https://docs.speakai.co/mcp/tools/)
- [Speak AI ClawHub release](https://clawhub.ai/speakai/skills/speakai)

## Skill Output:

**Output Type(s):** [Guidance, Configuration instructions, Shell commands]

**Output Format:** [Markdown with configuration and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers connection choices, tool selection, troubleshooting, and confirmations for consequential actions.]

## Skill Version(s):

1.33.1 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
