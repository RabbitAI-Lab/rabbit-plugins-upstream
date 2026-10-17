## Description:

Enables an agent to work with macOS Calendar, Reminders, Contacts, Maps, Mail, Messages, Notes, Photos, and Music playlists through a native Swift MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Mac users and developers use this skill to let an agent find and manage local Apple app data, including calendars, messages, photos, and playlists, with permissions for sensitive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to sensitive local data, including mail, messages, contacts, notes, photos, and calendars.

Mitigation: Grant macOS permissions deliberately and enable read-only tools unless changes are needed.

Risk: Sending messages, deleting data, or changing playlists may be difficult to undo.

Mitigation: Keep confirmation mode on ask-user and review action previews before approval.

Risk: Installing an external MCP bundle requires trust in the downloaded release.

Mitigation: Verify the GitHub release before installing the .mcpb bundle.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/apple-swift-mcp)
- [Project repository linked in skill documentation](https://github.com/chrischall/apple-swift-mcp)
- [Installation releases linked in skill documentation](https://github.com/chrischall/apple-swift-mcp/releases)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Natural-language responses and structured MCP tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses can include search results, action status, and confirmation previews.]

## Skill Version(s):

2.4.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
