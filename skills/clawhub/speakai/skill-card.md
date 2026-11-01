## Description:

Connect an agent to Speak AI and guide it through workspace setup, available tools, and common recording, transcript, search, survey, and meeting workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[speakai](https://clawhub.ai/user/speakai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Speak AI workspace users use this skill to connect an agent, choose tools for media and transcript workflows, and troubleshoot missing tools or authentication errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recordings and transcripts may contain sensitive workspace data.

Mitigation: Authorize the intended Speak AI workspace and upload only recordings the user has approved.

Risk: Deletion, sharing, access changes, and ongoing recording or webhook actions can have lasting effects.

Mitigation: Keep confirmation enabled and confirm the requested action before proceeding.

Risk: The local server connection requires an API key.

Mitigation: Prefer the documented remote OAuth connection; when using the local server, pin a reviewed package version and protect the API key.

## Reference(s):

- [Speak AI MCP documentation](https://docs.speakai.co/mcp)
- [MCP setup guide](https://docs.speakai.co/mcp/setup/)
- [MCP tool reference](https://docs.speakai.co/mcp/tools/)
- [MCP authentication guide](https://docs.speakai.co/mcp/authentication)

## Skill Output:

**Output Type(s):** [Guidance, Configuration instructions, Shell commands]

**Output Format:** [Markdown with configuration examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers remote OAuth and local API-key setup, tool selection, and workflow steps.]

## Skill Version(s):

1.41.1 (source: server-resolved release evidence; metadata server-version agrees)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
