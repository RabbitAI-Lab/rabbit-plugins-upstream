## Description:

Guides agents through connecting to Speak AI and choosing workflows for recordings, transcripts, search, clips, surveys, meetings, and workspace tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[speakai](https://clawhub.ai/user/speakai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Speak AI workspace users use this skill to connect an agent through OAuth or a local API-key setup, troubleshoot access, and choose the right workflow for media and workspace tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The integration can access sensitive recordings and transcript content in the connected workspace.

Mitigation: Connect an account with only the workspace access needed and prefer OAuth over handling an API key.

Risk: Some workflows can permanently delete data, create public links, record meetings, or keep automations running.

Mitigation: Review each confirmation and verify the intended action and scope before proceeding.

## Reference(s):

- [Speak AI MCP documentation](https://docs.speakai.co/mcp)
- [MCP setup guide](https://docs.speakai.co/mcp/setup/)
- [MCP authentication guide](https://docs.speakai.co/mcp/authentication)
- [MCP tool reference](https://docs.speakai.co/mcp/tools/)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Workflow instructions and troubleshooting guidance]

## Skill Version(s):

1.39.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
