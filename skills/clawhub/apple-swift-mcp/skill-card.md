## Description:

This skill should be used when the user asks about Apple app data via the native Swift MCP — Calendar, Reminders, Contacts, Maps, Mail, Messages, Notes, Photos, or Apple Music playlists on macOS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Mac users use the skill to search, read, and manage data in Apple Calendar, Reminders, Contacts, Maps, Mail, Messages, Notes, Photos, and Music playlists through native app integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The separately downloaded binary was not covered by the security review.

Mitigation: Verify the exact external release before installing.

Risk: Mail and Messages access can expose private correspondence.

Mitigation: Start with read-only tools and grant only the permissions needed for the requested tasks.

Risk: Runtime safeguards could not be confirmed.

Mitigation: Keep MCP_CONFIRM_MODE set to ask-user and review confirmation prompts before writes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/apple-swift-mcp)
- [Source repository](https://github.com/chrischall/apple-swift-mcp)
- [GitHub releases](https://github.com/chrischall/apple-swift-mcp/releases)

## Skill Output:

**Output Type(s):** [Text, Structured data, Guidance]

**Output Format:** [Natural-language responses and structured MCP results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on connected Apple apps, local account data, macOS permissions, and the requested read or write operation.]

## Skill Version(s):

2.8.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
