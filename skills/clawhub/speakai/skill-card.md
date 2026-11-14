## Description:

Connect an agent to Speak AI and find guidance for authentication, MCP tools, resources, and common workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[speakai](https://clawhub.ai/user/speakai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and users use this skill to connect an agent to Speak AI, choose the right MCP tools, and complete workflows for transcripts, media search, meeting notes, clips, exports, and workspace administration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence rates this release suspicious because an unpinned local server package command could run a changing release with local privileges; scan coverage is partial.

Mitigation: Prefer remote OAuth when supported. For local stdio use, pin and inspect the package version, and run it only with privileges and API-key access you are willing to grant.

## Reference(s):

- [Speak AI MCP documentation](https://docs.speakai.co/mcp)
- [Setup guide](https://docs.speakai.co/mcp/setup/)
- [Authentication guide](https://docs.speakai.co/mcp/authentication)
- [MCP tool reference](https://docs.speakai.co/mcp/tools/)

## Skill Output:

**Output Type(s):** [Guidance, Configuration instructions, Shell commands, API calls]

**Output Format:** [Markdown with setup steps, commands, and MCP workflow guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes connection setup, tool selection, and workflow steps; available actions depend on the connected account and permissions.]

## Skill Version(s):

1.43.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
