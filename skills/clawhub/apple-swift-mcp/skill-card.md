## Description:

Helps an agent read and manage local Apple app data, including calendars, reminders, contacts, mail, messages, notes, photos, and Music playlists on macOS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People using an agent on macOS can look up information in Apple apps and, with suitable permissions, manage events, reminders, contacts, messages, notes, photos, and local Music playlists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to sensitive local Apple app data can expose private information.

Mitigation: Review macOS permission prompts and allow only the read-only tools needed for the task.

Risk: Write-capable tools can send messages or modify and delete personal data.

Mitigation: Keep confirmation mode at ask-user and approve each sensitive action before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/apple-swift-mcp)
- [Installation releases](https://github.com/chrischall/apple-swift-mcp/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance, API calls]

**Output Format:** [Text and structured MCP tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Access depends on macOS permissions; sensitive changes can require user confirmation.]

## Skill Version(s):

2.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
