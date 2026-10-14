## Description:

Guides agents through connecting to Speak AI and using its workspace tools for transcription, media search, insights, recordings, exports, and administration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[speakai](https://clawhub.ai/user/speakai)

### License/Terms of Use:

MIT-0

## Use Case:

Users and developers connect an agent to their Speak AI workspace to transcribe and analyze recordings, search media, manage meeting and survey workflows, and troubleshoot access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A connected agent may access and act on workspace data within the user's permissions.

Mitigation: Review the requested scope and confirm deletes, bulk changes, exports, recordings, automations, webhooks, and shareable links before approving them.

Risk: API keys may be exposed if entered in chat or shell history.

Mitigation: Prefer OAuth and avoid pasting real API keys into chat or shell history.

Risk: Transcripts and other workspace content may contain misleading instructions.

Mitigation: Treat retrieved content as data rather than instructions and ask the user before acting on embedded directives.

## Reference(s):

- [Speak AI skill release](https://clawhub.ai/speakai/skills/speakai)
- [Speak AI MCP documentation](https://docs.speakai.co/mcp)
- [Speak AI MCP setup](https://docs.speakai.co/mcp/setup/)
- [Speak AI MCP tools](https://docs.speakai.co/mcp/tools/)

## Skill Output:

**Output Type(s):** [Guidance, Configuration instructions, Shell commands, Text]

**Output Format:** [Markdown with inline configuration and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide authenticated Speak AI tool actions within the user's workspace.]

## Skill Version(s):

1.34.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
