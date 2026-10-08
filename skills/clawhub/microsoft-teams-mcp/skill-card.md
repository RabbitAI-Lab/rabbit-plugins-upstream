## Description:

Guides agents to read Microsoft Teams chats, channels, and activity from an open, signed-in browser tab using the fpx CLI instead of an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve Teams chat messages, channel posts, lists, and activity through shell commands when a signed-in Teams browser tab is available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private Teams messages and metadata may appear in terminal output, shell history, logs, or downstream tools.

Mitigation: Read only content you are authorized to access and avoid capturing sensitive output in logs or downstream tools.

Risk: An unrelated Teams tab or conversation may be read by mistake.

Mitigation: Close other Teams tabs and verify the active account and conversation before reading.

Risk: A browser bridge grant may retain access after the task ends.

Mitigation: Revoke the browser bridge grant when finished.

## Reference(s):

- [Teams DOM-list recipes](references/dom-list-recipes.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Markdown with shell commands and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only access to content rendered in an open, signed-in Teams tab; chat and channel reads are limited to the currently open conversation.]

## Skill Version(s):

0.2.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
