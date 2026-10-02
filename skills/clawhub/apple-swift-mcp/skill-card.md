## Description:

Helps agents read and manage Apple app data and Music playlists through a native macOS Swift MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Mac users and developers use this skill to find and manage calendars, reminders, contacts, messages, mail, notes, photos, and local Music playlists through an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and modify sensitive local Apple app data.

Mitigation: Review access before installing and enable only the read tools unless writes are needed.

Risk: Notes deletion is not covered by the skill's stated extra confirmation safeguard.

Mitigation: Require client-side approval for Notes writes and deletes unless explicitly needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/apple-swift-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, API Calls]

**Output Format:** [Text and structured MCP tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires macOS 14 or later; the distributed binary targets Apple Silicon.]

## Skill Version(s):

2.4.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
