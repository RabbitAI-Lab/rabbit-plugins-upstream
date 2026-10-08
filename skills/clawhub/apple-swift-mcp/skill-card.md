## Description:

Helps an agent read and manage local Apple app data, including calendars, reminders, contacts, mail, messages, notes, photos, and Music playlists on macOS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

macOS users and their agents use this skill to find information in Apple apps and perform requested updates, such as scheduling events, sending messages, organizing photos, and editing local playlists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to sensitive local mail, messages, contacts, notes, photos, and calendars.

Mitigation: Grant access only if needed and allow read-only tools where possible.

Risk: Sending messages or deleting and changing personal data can have irreversible effects.

Mitigation: Keep confirmation mode on ask-user and review each proposed action before approving it.

Risk: The reviewed artifact does not include the installable binary.

Mitigation: Verify the linked GitHub release before installing the binary.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/apple-swift-mcp)
- [GitHub project linked by skill documentation](https://github.com/chrischall/apple-swift-mcp)
- [GitHub releases linked by skill documentation](https://github.com/chrischall/apple-swift-mcp/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance, API Calls]

**Output Format:** [Natural-language responses and structured MCP tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can perform requested changes to local Apple app data when write tools are enabled.]

## Skill Version(s):

2.4.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
