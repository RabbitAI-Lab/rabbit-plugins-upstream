## Description:

Connect an agent to Speak AI, configure remote OAuth or local API key access, and choose tools for recording, transcription, search, analysis, exports, surveys, meetings, and workspace management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[speakai](https://clawhub.ai/user/speakai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to connect to a Speak AI workspace, find the appropriate MCP resource or tool, and complete workflows such as transcribing recordings, searching media, exporting results, or managing meeting and survey workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recordings or workspace data could be shared or processed through an unintended account or without authorization.

Mitigation: Connect only the intended Speak AI account and share recordings you are authorized to process.

Risk: Deletion, public links, meeting recording, or ongoing automations can have lasting effects.

Mitigation: Review the requested action and its confirmation before proceeding.

Risk: The optional local server uses a separately installed npm package.

Mitigation: Pin a reviewed package version when using the local server.

## Reference(s):

- [Speak AI MCP documentation](https://docs.speakai.co/mcp)
- [MCP setup guide](https://docs.speakai.co/mcp/setup/)
- [MCP tool reference](https://docs.speakai.co/mcp/tools/)
- [MCP authentication guide](https://docs.speakai.co/mcp/authentication)

## Skill Output:

**Output Type(s):** [Guidance, Configuration, Shell commands, API calls]

**Output Format:** [Markdown guidance with JSON configuration and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.40.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
