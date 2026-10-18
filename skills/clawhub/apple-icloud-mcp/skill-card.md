## Description:

Connects an agent to Apple Music, iCloud Calendar, Contacts and Mail, Apple Maps, WeatherKit, and iTunes search from any operating system.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents use this skill to search Apple services, check personal information, plan routes and weather, and manage music, calendars, contacts, and mail through an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad automatic triggers can route routine requests through tools with access to private iCloud data and account-changing actions.

Mitigation: Enable only needed services, limit credentials where possible, and run the healthcheck before use.

Risk: Mail, calendar, contact, or music-library changes can have unintended effects.

Mitigation: Require explicit user confirmation before sending mail or making calendar, contact, or library changes.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/apple-icloud-mcp)
- [apple-icloud-mcp npm package](https://www.npmjs.com/package/apple-icloud-mcp)

## Skill Output:

**Output Type(s):** [API Calls, Text, Guidance]

**Output Format:** [MCP tool calls and structured text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Available services depend on configured credentials.]

## Skill Version(s):

0.3.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
