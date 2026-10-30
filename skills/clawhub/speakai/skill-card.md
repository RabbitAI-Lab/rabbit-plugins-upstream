## Description:

Connect an agent to Speak AI and guide it through workspace setup and workflows for recordings, transcripts, insights, search, clips, exports, surveys, meetings, and workspace tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[speakai](https://clawhub.ai/user/speakai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workspace users use this skill to connect an agent to Speak AI, find the right tool or resource, and complete workflows for recordings, transcripts, insights, surveys, meetings, and workspace management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workspace permissions determine which recordings and related data an agent can access.

Mitigation: Review the workspace data available to the connected account before use.

Risk: Some workflows record meetings, share links or exports, delete data, or keep automations running.

Mitigation: Confirm the scope and consequence before recording, sharing, deleting, making bulk changes, or enabling persistent actions.

Risk: The local stdio connection uses an API key.

Mitigation: Prefer remote OAuth when supported; for local use, pin a reviewed package version and protect the API key.

## Reference(s):

- [Speak AI MCP overview](https://docs.speakai.co/mcp)
- [Setup guide](https://docs.speakai.co/mcp/setup/)
- [MCP tool reference](https://docs.speakai.co/mcp/tools/)
- [Authentication guide](https://docs.speakai.co/mcp/authentication)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Configuration, Shell commands]

**Output Format:** [Natural-language guidance, MCP tool calls, configuration examples, and requested transcript or insight exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Depends on the requested workflow; may include transcripts, captions, summaries, insights, clips, and media exports.]

## Skill Version(s):

1.40.1 (source: server metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
