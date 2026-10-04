## Description:

Provides read-only shell recipes for retrieving chats, messages, teams, channels, and activity from an open, signed-in Microsoft Teams browser tab without running the MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and authorized Teams users can retrieve visible chat, channel, and activity information from a signed-in browser session for shell-based workflows and scripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commands can reveal confidential Teams content from the signed-in session.

Mitigation: Use only with permission to access that data; treat output as confidential and avoid unintended logging or sharing.

Risk: With multiple Teams tabs open, results may come from a different tab than intended.

Mitigation: Close extra Teams tabs and confirm the open conversation before relying on results.

Risk: The browser bridge retains access while its grant remains active.

Mitigation: Revoke the bridge grant when it is no longer needed.

## Reference(s):

- [Teams DOM-list recipes](artifact/references/dom-list-recipes.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/microsoft-teams-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only recipes; chat messages and channel posts are limited to the conversation open in the browser.]

## Skill Version(s):

0.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
