## Description:

Connect an agent to Speak AI and guide it through OAuth or local API-key setup, MCP tools, and common recording workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[speakai](https://clawhub.ai/user/speakai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and users connect an agent to a Speak AI workspace, find the right MCP tool, and follow guided workflows for transcribing, searching, analyzing, exporting, and managing recordings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The hosted setup connects the agent to the external Speak AI service.

Mitigation: Consider whether to connect to the service and review its privacy information before authorizing access.

Risk: The optional local setup uses an install command for an unpinned @speakai/mcp-server package.

Mitigation: Review the package and pin its version before installing.

## Reference(s):

- [Speak AI MCP documentation](https://docs.speakai.co/mcp)
- [Setup guide](https://docs.speakai.co/mcp/setup/)
- [MCP tool reference](https://docs.speakai.co/mcp/tools/)
- [Authentication guide](https://docs.speakai.co/mcp/authentication)
- [Privacy information](https://speakai.co/privacy)
- [Speak AI ClawHub page](https://clawhub.ai/speakai/skills/speakai)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Setup guidance, configuration examples, and workflows for connected Speak AI MCP tools.]

## Skill Version(s):

2.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
