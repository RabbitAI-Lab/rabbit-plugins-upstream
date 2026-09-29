## Description:

Guides agents using an unofficial MCP server to access Apple Music, iCloud Calendar, Contacts and Mail, Apple Maps, WeatherKit, and iTunes search from any OS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Users and developers can ask an agent to search Apple media and places, check weather, and manage their configured Apple Music and iCloud data through the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The unofficial server can access sensitive Apple account data and credentials across multiple services.

Mitigation: Enable only needed services and credentials; prefer revocable app-specific credentials where possible.

Risk: Mail, contact, calendar, and music-library changes could affect personal data or other people.

Mitigation: Require explicit user confirmation before sending mail or changing contacts, calendar events, or library contents.

Risk: An unpinned npm installation may pull a different package version on later runs.

Mitigation: Review the package before installation and pin an approved version for repeatable deployments.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/apple-icloud-mcp)
- [apple-icloud-mcp npm package](https://www.npmjs.com/package/apple-icloud-mcp)

## Skill Output:

**Output Type(s):** [Text, Configuration, Guidance]

**Output Format:** [Markdown with JSON configuration examples and tool-use guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool results may include paginated data; changes to mail, contacts, calendars, or playlists can require explicit confirmation.]

## Skill Version(s):

0.2.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
