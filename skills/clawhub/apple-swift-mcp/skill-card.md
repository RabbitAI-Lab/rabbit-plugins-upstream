## Description:

This skill should be used when the user asks about Apple app data via the native Swift MCP — Calendar, Reminders, Contacts, Maps, Mail, Messages, Notes, Photos, or Apple Music playlists on macOS. Triggers on phrases like "check my calendar", "find contact", "send iMessage", "search my notes", "recent emails", "find photos of", "make a playlist", "add this song to my playlist", "sort my playlist", or any macOS-native app automation. Requires macOS 14+ on Apple Silicon; faster than the AppleScript-backed Node variant.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

macOS users and developers use this skill to read, search, organize, and update data in Apple apps through a native Swift MCP server. It covers Calendar, Reminders, Contacts, Maps, Mail, Messages, Notes, Photos, and Apple Music playlists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive data and make changes across Apple apps.

Mitigation: Grant only the app permissions and write tools needed; prefer read-only tools when possible.

Risk: Some edits and deletions do not have an additional confirmation gate.

Mitigation: Keep MCP_CONFIRM_MODE set to ask-user and review each proposed change before approving it.

Risk: The reviewed instructions do not verify the downloaded executable, and static scanner coverage was incomplete.

Mitigation: Verify the downloaded release before installing it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/apple-swift-mcp)
- [Project repository (linked in skill documentation)](https://github.com/chrischall/apple-swift-mcp)
- [GitHub Releases (linked in skill documentation)](https://github.com/chrischall/apple-swift-mcp/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance, API Calls]

**Output Format:** [Natural-language responses and Apple app operations via MCP tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the requested operation and the connected Apple app data.]

## Skill Version(s):

2.5.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
