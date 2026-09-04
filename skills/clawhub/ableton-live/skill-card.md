## Description:

Connects an agent to the Loophole Bridge for Ableton Live so it can check prerequisites, emit MCP client configuration, and run user-approved Live editing recipes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[othmanadi](https://clawhub.ai/user/othmanadi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and music producers use this skill to connect an MCP-capable agent to a local Ableton Live bridge, verify the bridge setup, generate MCP client configuration, and apply bounded Live editing recipes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives an agent a path to a local Ableton bridge and can modify Live sets when recipes are approved.

Mitigation: Review the planned bridge tool calls, confirm mutation counts before write operations, and inspect Ableton Live undo history after changes.

Risk: The bridge bearer token is sensitive local configuration used to access the local MCP endpoint.

Mitigation: Read the token only from bridge.json, avoid exposing it beyond the MCP client configuration, and review generated config before applying it.

Risk: Some recipes depend on beta bridge limits such as MIDI-only editing, session-scoped object references, and Session-view clip creation.

Mitigation: Use current opaque references returned by read calls, re-list after structural changes, and avoid claiming Arrangement timeline writes or atomic multi-tool recipes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/othmanadi/skills/ableton-live)
- [Server-resolved GitHub import](https://github.com/OthmanAdi/loophole/tree/main/skills/ableton-live)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON configuration fragments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include prerequisite check tables, merge-safe MCP client blocks, bridge tool call sequences, mutation counts, and user confirmation prompts.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
