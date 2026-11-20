## Description:

Connect an agent to Speak AI and orient it in the workspace. Covers the remote OAuth connection, the local stdio connection with an API key, the MCP tools and their categories, the resources, the built-in prompts, and the first workflows to run. Use this when you need to set up the Speak AI MCP server, when a Speak AI tool is missing or returning 401, or when you need to know which tool to call to transcribe a recording, read a transcript or captions, search across a media library, ask questions about recordings, create clips, export transcripts, run voice and video surveys with recorders, schedule the meeting assistant for Zoom, Google Meet or Microsoft Teams, or manage folders, custom fields, webhooks, automations, dashboards and team members.

This skill is ready for commercial/non-commercial use.

## Publisher:

[speakai](https://clawhub.ai/user/speakai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and users connecting an agent to a Speak AI workspace use this guide to configure the MCP connection, find the right media and workspace tools, and complete common transcription, search, analysis, export, recorder, and meeting workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local stdio setup uses an unpinned package version, so the installed release may change.

Mitigation: Pin @speakai/mcp-server to a reviewed version and review updates before installing them.

Risk: Connecting the MCP server gives it access to Speak AI workspace data allowed by the connected account.

Mitigation: Connect only to a Speak AI service and workspace you trust, and review the authorized account before use.

## Reference(s):

- [Speak AI MCP documentation](https://docs.speakai.co/mcp)
- [Speak AI MCP setup guide](https://docs.speakai.co/mcp/setup/)
- [Speak AI MCP tool reference](https://docs.speakai.co/mcp/tools/)
- [Speak AI MCP authentication guide](https://docs.speakai.co/mcp/authentication)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with setup steps, tables, and inline shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

2.2.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
