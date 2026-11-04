## Description:

This skill should be used when the user asks about Apple app data via the native Swift MCP — Calendar, Reminders, Contacts, Maps, Mail, Messages, Notes, Photos, or Apple Music playlists on macOS. Triggers on phrases like "check my calendar", "find contact", "send iMessage", "search my notes", "recent emails", "find photos of", "make a playlist", "add this song to my playlist", "sort my playlist", or any macOS-native app automation. Requires macOS 27.2+ on Apple Silicon; faster than the AppleScript-backed Node variant.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users can ask an agent to read or manage data in macOS Calendar, Reminders, Contacts, Maps, Mail, Messages, Notes, Photos, and Music playlists. The agent can provide app data and carry out supported changes after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mail and Messages access can expose private content to the connected AI client.

Mitigation: Enable only the apps and tools needed for the task.

Risk: The external binary and enforcement of its safeguards were not verified by the supplied security review.

Mitigation: Verify the external binary before granting macOS permissions. Keep MCP_CONFIRM_MODE set to ask-user and review action previews before confirming changes.

## Reference(s):

- [Project repository](https://github.com/chrischall/apple-swift-mcp)
- [GitHub releases](https://github.com/chrischall/apple-swift-mcp/releases)

## Skill Output:

**Output Type(s):** [Text, Structured data, Guidance]

**Output Format:** [Natural-language responses and structured Apple app data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected app operation; supported changes use confirmation previews.]

## Skill Version(s):

2.9.0 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
