## Description:

Connect an agent to Speak AI, configure OAuth or local API key access, and use its tools to manage, transcribe, analyze, search, and export workspace media.

This skill is ready for commercial/non-commercial use.

## Publisher:

[speakai](https://clawhub.ai/user/speakai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Speak AI workspace users use this skill to connect an MCP client and find workflows for recordings, transcripts, insights, meetings, surveys, exports, and workspace settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local stdio setup uses an unpinned package command, so the server package can change between runs.

Mitigation: Prefer remote OAuth where supported; for local setup, follow the version-pinning guidance and review the package before running it.

Risk: The security scan was partial because two local references could not be resolved.

Mitigation: Review the complete release artifact and its referenced materials before installation.

## Reference(s):

- [Speak AI MCP documentation](https://docs.speakai.co/mcp)
- [MCP setup guide](https://docs.speakai.co/mcp/setup/)
- [MCP authentication guide](https://docs.speakai.co/mcp/authentication)
- [MCP tool reference](https://docs.speakai.co/mcp/tools/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides connection, troubleshooting, and workflow guidance for a Speak AI workspace.]

## Skill Version(s):

1.41.4 (source: server-resolved release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
