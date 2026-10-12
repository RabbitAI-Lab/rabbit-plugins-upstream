## Description:

Guides an agent in accessing and automating local Apple app data through a native Swift MCP server on macOS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

macOS users and developers use this skill to let an agent find information in Calendar, Reminders, Contacts, Maps, Mail, Messages, Notes, Photos, and Music, and perform requested app actions such as creating events, sending messages, or editing playlists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to local Apple app data can expose sensitive personal information.

Mitigation: Enable read-only tools first and grant macOS permissions only for the apps you intend to use.

Risk: Sends, deletes, playlist rewrites, and exports can disclose data or make unwanted changes.

Mitigation: Review action previews and destinations carefully before approving sends, deletes, playlist rewrites, or exports.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/apple-swift-mcp)
- [Apple Swift MCP project](https://github.com/chrischall/apple-swift-mcp)
- [Apple Swift MCP releases](https://github.com/chrischall/apple-swift-mcp/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text or Markdown with app-specific results and action guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include previews for actions requiring confirmation.]

## Skill Version(s):

2.4.4 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
