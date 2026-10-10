## Description:

Guides agents in reading chats, teams, channels, activity, and the open conversation from a signed-in Microsoft Teams browser tab using the fpx CLI instead of an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other authorized users can guide an agent to extract visible Teams chats, channel posts, and activity from their signed-in browser tab for review or scripting without running the Teams MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reading a Teams account or conversation without authorization can expose sensitive communications.

Mitigation: Use only with authorization to access the account and conversations; avoid unnecessary logging or sharing of extracted content.

Risk: Multiple Teams tabs or an unexpected open conversation may yield data from the wrong conversation.

Mitigation: Close unrelated Teams tabs and confirm the selected conversation before extracting messages.

Risk: Installing a browser extension and npm CLI and granting a persistent bridge permission adds dependency and permission trust considerations.

Mitigation: Review the extension and package before installation and verify the intended scope before approving the bridge permission.

## Reference(s):

- [Teams DOM-list recipes](artifact/references/dom-list-recipes.md)
- [ContextMint Bridge extension releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, Text]

**Output Format:** [Markdown instructions and shell commands; extracted Teams rows in JSON or formatted text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; chat and channel messages are limited to the currently open conversation.]

## Skill Version(s):

0.3.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
