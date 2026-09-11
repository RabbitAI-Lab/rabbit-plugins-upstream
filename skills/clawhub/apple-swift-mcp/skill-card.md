## Description:

This skill helps an agent use a native Swift MCP server to work with Apple app data on macOS, including Calendar, Reminders, Contacts, Maps, Mail, Messages, Notes, and Photos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent inspect, search, and update local Apple app data through a macOS MCP integration. It is suited to personal productivity workflows that involve calendars, reminders, contacts, messages, mail, notes, maps, and photos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs users to install an unpinned external binary that may receive broad access to private local Apple app data.

Mitigation: Install only from a trusted publisher source and prefer a pinned, signed, checksum-verifiable release or a locally built source version.

Risk: The MCP integration can request macOS privacy permissions and perform write-capable actions against Apple apps.

Mitigation: Grant permissions only for the specific task, avoid Full Disk Access unless Mail or Messages history access is required, and revoke the MCP entry and macOS privacy permissions when no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/apple-swift-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Configuration, Shell commands, Text]

**Output Format:** [Markdown guidance with tool names, configuration notes, and command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May lead an agent to call local MCP tools that read or modify Apple app data after user-granted macOS permissions.]

## Skill Version(s):

1.8.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
