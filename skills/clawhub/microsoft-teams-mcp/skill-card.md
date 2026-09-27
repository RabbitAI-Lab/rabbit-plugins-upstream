## Description:

Guides agents in reading visible Microsoft Teams chats, channels, and activity from a signed-in browser tab using the fpx CLI instead of an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized employees and developers use this skill to read visible Teams conversations, channel posts, lists, and activity from an already signed-in browser tab without running the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Extracted Teams content may contain sensitive organizational information.

Mitigation: Use only with authorization and avoid logging or sharing extracted messages unless organizational policy permits it.

Risk: A persistent browser pairing may retain access to Teams content beyond the intended task.

Mitigation: Review the fpx/Transporter pairing scope and revoke the grant when it is no longer needed.

Risk: With multiple Teams tabs open, results may come from the wrong tab.

Mitigation: Close unrelated Teams tabs and confirm the open conversation before relying on extracted rows.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/microsoft-teams-mcp)
- [Teams DOM-list recipes](references/dom-list-recipes.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON data]

**Output Format:** [Markdown guidance with shell commands; structured JSON rows from fpx]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads only content rendered in the selected Teams tab; the desired chat or channel must already be open.]

## Skill Version(s):

0.2.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
